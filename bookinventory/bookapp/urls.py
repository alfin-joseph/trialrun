"""bookinventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('index',views.Home,name="index"),
    path('signup',views.SignUp,name="signup"),
    path('',views.Login,name="login"),
    path('bksearch',views.Booksearch,name="bksearch"),
    path('showbook',views.Showbook,name="showbook"),
    path('cr',views.CreateStore,name="createstore"),
    path('stre',views.Bookstore,name="strbook"),
    path("str",views.ShowStore,name="showstore"),
    path('up',views.UpdateCopies,name="updatecopies"),
    path('dlt',views.DeleteBook,name="deletebook"),
    path('dl',views.DeleteStore,name="deletestore"),
    path('logout',views.Logout,name="logout")

]
