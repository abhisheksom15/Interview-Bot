from django import forms
from django.contrib.auth.models import User
from Front.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields=( 'username','email','password','first_name','last_name' )
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields=('phone_number', 'date_of_birth','Address','school_10th','percentage_10th','school_12th','percentage_12th','graduation','branch_graduation','technical_skills_and_language','Other_skills','Main_Hobbies','Other_Hobbies','achievement','Project_Done','profile_picture')
