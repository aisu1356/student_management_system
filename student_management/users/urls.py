
from django.contrib import admin
from django.urls import path
from .import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('register/',views.register),
    # path('register_post/',views.register_post),
    path('user_login/',views.user_login),
    path('login_post/',views.login_post),
    path('stud_list/', views.stud_list, name='stud_list'),
    path('api/', include(router.urls)),
    # path('student-api/', views.StudentDetailAPIView.as_view(), name='student-api'),

]



