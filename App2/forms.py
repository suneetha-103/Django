from App2.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        # fields='__all__'
        fields=['FullName','RollNo','EmailId','MobileNo','Gender']
