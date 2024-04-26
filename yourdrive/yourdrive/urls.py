"""
URL configuration for yourdrive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', views.customer_signin, name='customer_signin'),
    path('cars/', views.car_listing, name='car_listing'),
    path("about",views.about,name = 'about'),
    #path('signout/', views.signout, name='signout'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('make-rental-agreement/', views.make_rental_agreement, name='make_rental_agreement'),
    path('do-rental-assignment/', views.do_rental_assignment, name='do_rental_assignment'),
    # Define URL patterns for other views similarly
]
