from django import forms
from django.forms import ModelForm
from .models import question, quiz, userSignup
from django.forms import  Form


# create quiz form

class questionForm(ModelForm):
    class Meta:
        model = question
        fields = ['question_title', 'marks', 'expected_answer']

        widgets = {

            'question_title': forms.TextInput(attrs={'class': 'w3-input'}),
            'marks': forms.TextInput(attrs={'class': 'w3-input'}),
            'expected_answer': forms.TextInput(attrs={'class': 'w3-input'}),
        }
class quizForm(ModelForm):


    class Meta:
       model = quiz
       fields = ['title', 'quiz_description', 'choices']

       widgets = {

           'title': forms.TextInput(attrs={'class': 'w3-input'}),
           'quiz_description': forms.TextInput(attrs={'class': 'w3-input'}),

       }

class userSignupForm(ModelForm):

    class Meta:
        model = userSignup
        fields = '__all__'

        widgets = {

            'First_Name': forms.TextInput(attrs={'class': 'w3-input'}),
            'Last_Name': forms.TextInput(attrs={'class': 'w3-input'}),
            'Username': forms.TextInput(attrs={'class': 'w3-input'}),
            'Email': forms.EmailInput(attrs={'class': 'w3-input'}),
            'Password': forms.PasswordInput(attrs={'class': 'w3-input'}),
        }



