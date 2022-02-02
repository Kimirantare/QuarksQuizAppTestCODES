from rest_framework import serializers

from .models import question, quiz, result, userSignup


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = question
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz
        fields = "__all__"




class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = result
        fields = "__all__"

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSignup
        fields = "__all__"
