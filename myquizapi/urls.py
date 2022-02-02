from django.urls import include, path
from rest_framework import routers
from .views import questionViewset, quizViewset, resultViewset, userSignupViewset
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'question', questionViewset)
router.register(r'quiz', quizViewset)
router.register(r'result', resultViewset)
router.register(r'userSignup', userSignupViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('My_Quiz_web_app_login', views.web_view, name="web_Login"),
    path('My_Quiz_web_app_ListQuiz', views.web_List_Quiz, name="web_ListQuiz"),
    path('My_Quiz_web_app_signup', views.userSignup, name="web_Signup"),
    path('My_Quiz_web_app_profile', views.web_profile, name="web_profile"),
    path('My_Quiz_web_app_att_quiz', views.web_Attend_quiz, name="web_AttendQuiz"),
    path('My_Quiz_web_app_create_quiz', views.web_Create_quiz, name="web_CreateQuiz"),
    path('My_Quiz_web_app_create_question', views.web_Create_question, name="web_CreateQuestion"),
    path('My_Quiz_web_app_admin', views.admin_page, name="web_admin"),
    path('My_Quiz_web_app_home', views.web_home, name="web_home"),



]
urlpatterns += staticfiles_urlpatterns()
