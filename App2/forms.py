from App2.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        # fields='__all__'
        fields=['FullName','RollNo','EmailId','MobileNo','Gender']
        widgets={
            "FullName":forms.TextInput(attrs={'placeholder':'Enter your Name'}),
            "RollNo":forms.TextInput(attrs={'placeholder':"Enter your PIN"}),
            "EmailId":forms.EmailInput(attrs={'placeholder':'Enter your MailId'}),
            "MobileNo":forms.TextInput(attrs={'placeholder':'Enter your PhoneNumber'}),
        }
        
