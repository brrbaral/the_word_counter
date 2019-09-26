
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='countagain'),
    path('apps/',include('words.urls')),
    path('count/',views.count,name='countit'),
    path('about/',views.about,name='about'),
]
