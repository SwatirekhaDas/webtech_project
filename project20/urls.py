"""
URL configuration for project20 project.

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('one/',one,name='one'),
    path('two/',two,name='two'),
    path('three/',three,name='three'),
    path('four/',four,name='four'),
    path('five/',five,name='five'),
    path('six/',six,name='six'),
    path('seven/',seven,name='seven'),
    path('eight/',eight,name='eight'),
    path('nine/',nine,name='nine'),
    path('ten/',ten,name='ten'),
    path('eleven/',eleven,name='eleven'),
    path('twelve/',twelve,name='twelve'),
    path('thirteen/',thirteen,name='thirteen'),
    path('fourteen/',fourteen,name='fourteen'),
    path('fifteen/',fifteen,name='fifteen'),
    path('sixteen/',sixteen,name='sixteen'),
    path('seventeen/',seventeen,name='seventeen'),
    path('eighteen/',eighteen,name='eighteen'),
    path('nineteen/',nineteen,name='nineteen')
]
