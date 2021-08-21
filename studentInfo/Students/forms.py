from django import forms
from .models import Student,StudentAcademics


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','cls','mobile','address']


class StudentAcaForm(forms.ModelForm):
    class Meta:
        model = StudentAcademics
        fields = ['math','physics','bio','chemistry']
