from django.db import models
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Student , StudentAcademics
from django.views.generic import ListView
from .forms import StudentAcaForm,StudentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

class home(ListView):
    template_name = 'Students/home.html'
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        self.object = Student.objects.all()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context
    
    def get_queryset(self):
        return self.object.all()

class search(ListView):
    template_name = 'Students/search.html'

    def get_queryset(self,*args,**kwargs):
        query=self.request.GET.get('q',None)
        qs=Student.objects.none()
        if query is not None:
            lookup=Q(name__icontains=query)
            qs=Student.objects.filter(lookup).distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super(search,self).get_context_data(**kwargs)
        context["students"] = self.get_queryset()
        return context 

@login_required
def create(request,*args, **kwargs):
    if(request.method == 'POST'):
        roll_no     = request.POST.get('roll_no')
        name        = request.POST.get('name')
        cls         = request.POST.get('cls')
        mobile      = request.POST.get('mobile')
        address     = request.POST.get('address')
        math        = request.POST.get('math')
        physics     = request.POST.get('physics')
        bio         = request.POST.get('bio')
        chemistry   = request.POST.get('chemistry')
        obj1        = Student.objects.create(roll_no=roll_no,name=name,cls=cls,mobile=mobile,address=address)
        obj2        = StudentAcademics.objects.create(student=obj1,math=math,physics=physics,bio=bio,chemistry=chemistry)
        
        # for i in range(2,15):
        #     temp = Student.objects.create(roll_no=roll_no+str(i),name=name+str(i),cls=cls,mobile=mobile,address=address)
        #     StudentAcademics.objects.create(student=temp,math=math+str(i),physics=physics+str(i),bio=bio+str(i),chemistry=chemistry+str(i))

        if obj1 is None and obj2 is not None:
            obj2.delete()
        if obj2 is None and obj1 is not None:
            obj1.delete()
    return render(request,'Students/add.html',{})

def detail(request,roll,*args, **kwargs):   
    object = Student.objects.get(roll_no=roll)
    object2 = StudentAcademics.objects.get(student=object)
    data = {
        'student': "not found",
    }
    if object and object2:
        data = {
            'student': object,
            'student1':object2
       }
    return render(request=request, template_name='Students/detail.html', context=data)

@login_required
def delete(request,roll,*args, **kwargs):
    if request.method == 'POST':
        object  = Student.objects.get(roll_no=roll)
        object2 = StudentAcademics.objects.get(student=object)
        object.delete()
        object2.delete()
        return redirect('/')  
    return redirect('/')    
      

@login_required
def edit(request, roll, *args, **kwargs):
    object  = Student.objects.get(roll_no=roll)
    object2 = StudentAcademics.objects.get(student=object)
    form1 = StudentForm(instance=object)
    form2 = StudentAcaForm(instance=object2)
    data = {
        'roll_no':roll,
        'form1': form1,
        'form2': form2,
    }
    if object is None:
        return Http404
    if request.method == "POST":
        form1=StudentForm(request.POST)
        form2=StudentAcaForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            object = form1.save(commit=False)
            object.roll_no = roll
            object.save()
            object2.delete()
            object2 = form2.save(commit=False)
            object2.student = object
            object2.save()
        return redirect(f'/detail/{roll}')
    return render(request=request, template_name='Students/edit.html', context=data)
