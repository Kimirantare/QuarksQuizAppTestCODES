from django.db import models
from django import forms
from django.forms import forms
from multiselectfield import MultiSelectField


class question(models.Model):

    question_title = models.CharField(max_length=100)
    marks = models.CharField(max_length=50)
    expected_answer = models.CharField(max_length=100)

    quest_dict = {'question.id': 'question.question_title',}
# akabazo = []
#
# for i in quest_dict:
#     akabazo.append(i)

class quiz(models.Model):
    for i in question.quest_dict:
        my_choices = ((question.quest_dict.values()))
    MY_CHOICES =(
        (my_choices, my_choices),

            )

    title = models.CharField(max_length=100)
    quiz_description = models.CharField(max_length=100)
    choices = MultiSelectField(default=MY_CHOICES,choices = MY_CHOICES)
#
#
class result(models.Model):
    initial_marks = 0
    answer = models.CharField(max_length=100)
    if answer == question.expected_answer:
        initial_marks = initial_marks + question.marks
    else:
        initial_marks = initial_marks

    ikibazo = models.ForeignKey(question, on_delete=models.CASCADE)
    marks = models.CharField(default=initial_marks, max_length=50)



class userSignup(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)