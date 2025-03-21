from django.shortcuts import redirect, render

from .forms import StudentForm

from .serializers import StudentSerializer
from .models import Student
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework import viewsets


# def register(req):
#     return render(req,'student/register.html')

# def register_post(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         age = request.POST.get('age')
#         course = request.POST.get('course')
#         password = request.POST.get('password')
#         created_at = request.POST.get('created_at')

#         obj = Student.objects.create(
#             username=username,
#             name=name,
#             email=email,
#             age=age,
#             course=course,
#             created_at=created_at,
#         )

#         obj.set_password(password)  
#         obj.save() 

#         return render(request, 'login.html')

#     return render(request, 'register.html')

from django.contrib.auth import get_user_model

def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
           
            student = form.save(commit=False)
            student.set_password(request.POST.get('password'))  
            student.save()
            return render(request, 'login.html')
        return render(request, 'student/register.html', {'form': form})

    form = StudentForm()
    return render(request, 'student/register.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'stud_list.html', {'students': students})

def user_login(request):
    if request.user.is_authenticated:
        return render(request,"student/stud_list.html")
    return render(request,"login.html")

def login_post(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login successful")
            return redirect('stud_list')
        else:
            return render(request, 'login.html', {'error': 'You are not authorized as a student.'})
        
    return render(request, 'login.html')


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "hasError": False,
                "errorCode": -1,
                "message": "Student created successfully",
                "debugMessage": "",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "hasError": True,
                "errorCode": 400,
                "message": "Validation error",
                "debugMessage": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "hasError": False,
                "errorCode": -1,
                "message": "Student updated successfully",
                "debugMessage": "",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "hasError": True,
                "errorCode": 400,
                "message": "Validation error",
                "debugMessage": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        student.delete()
        return Response({
            "hasError": False,
            "errorCode": -1,
            "message": "Student deleted successfully",
            "debugMessage": "",
            "data": {}
        }, status=status.HTTP_204_NO_CONTENT)

    def custom_retrieve(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response({
            "hasError": False,
            "errorCode": -1,
            "message": "Student retrieved successfully",
            "debugMessage": "",
            "data": serializer.data
        }, status=status.HTTP_200_OK) 


def stud_list(request):
     return render(request,'student/stud_list.html')





