from django.urls import path
from App2 import views
urlpatterns = [
    path('homeurl/',views.home,name="home"),
    path('index/',views.index,name="index"),
    path('studenturl/',views.student,name='student'),
    path('valueurl/<int:val>',views.value,name='value'),
    path("tableurl/<int:v>",views.table,name='table')
]