from django import forms
from .models import Resume


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

JOB_CITY_CHOICES = [
    ('Rawalpindi','Rawalpindi'),
    ('Islamabad','Islamabad'),
    ('Peshawar','Peshawar'),
    ('Karachi','Karachi'),
    ('Lahore','Lahore'),
    ('Quetta','Quetta'),
]



class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    job_city = forms.MultipleChoiceField(choices=JOB_CITY_CHOICES , label='Preferred Job Location', widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {'name': 'Full Name', 'dob':'Date of Birth', 'pinCode': 'Pin Code',
                  'mobile':'Mobile No.', 'profile_image':'Profile Image', 'my_file':'Document'}
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pinCode': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }