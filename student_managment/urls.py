"""
URL configuration for student_managment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import students_list,add_student,delete_student,edit_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s/',students_list,name='student_list' ),
    path('a/',add_student ,name='add_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
    path('edit/<int:id>/', edit_student, name='edit_student'),


]


