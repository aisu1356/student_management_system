from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','username', 'email', 'age', 'course','password']
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18 or age > 30:
            raise forms.ValidationError('Age must be between 18 and 30.')
        return age
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Please enter a valid email address.')
        return email
