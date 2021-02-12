"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include 
from Workshop import views
from App2 import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('staticurl/',views.static,name="static"),
    path('dynamic1/<str:name>',views.dynamicstr,name="dynamicstr"),
    path('dynamic2/<int:id>',views.dynamicint,name="dynamicint"),
    path('dynamic3/<str:name>/<int:id>',views.dynamicstrint,name="dynamicstrint"),
    path('staturl/',v.stat,name="stat"),
    path('App2/',include('App2.urls')),
]