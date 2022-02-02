from django.contrib import admin
from .models import question
from .models import quiz
from .models import result
from .models import userSignup

# Register your models here.

admin.site.register(quiz)
admin.site.register(question)
admin.site.register(result)
admin.site.register(userSignup)





