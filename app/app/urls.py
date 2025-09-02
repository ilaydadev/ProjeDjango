"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
>>>>>>> 053c74df2c30cc2feccea9dd9c2f9dffaed6b0ae
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
from todo import views

<<<<<<< HEAD
#register
#login
#todo
=======
#login
#todo
#register
>>>>>>> 053c74df2c30cc2feccea9dd9c2f9dffaed6b0ae
#home
#logout

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('todos/', views.todo_list, name='todo_list'),
    path('todo/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/<int:id>/update-status/', views.todo_update_status, name='todo_update_status'),
]
=======
    path('todo/', views.home, name='home'),
    path('', views.home, name='home'),
    path('login', views.login,name='login'),
    path('todo/<int:id>', views.todo_list,name='todo_list'),
    path('register/', views.register,name='register'),
    path('home/', views.home,name='home'),
]

>>>>>>> 053c74df2c30cc2feccea9dd9c2f9dffaed6b0ae
