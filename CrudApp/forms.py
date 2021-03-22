from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','mobile','roll_no','course')
        labels = {
            'fullname':'Full Name',
            'roll_no':'Roll No'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['course'].empty_label = "Select"
        self.fields['roll_no'].required = False
