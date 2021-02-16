from django.urls import path
from App2 import views
urlpatterns = [
    path('homeurl/',views.home,name="home"),
    # path('index/',views.index,name="index"),
    # path('studenturl/',views.student,name='student'),
    # path('valueurl/<int:val>',views.value,name='value'),
    # path("tableurl/<int:v>",views.table,name='table'),
    path("sampleurl/",views.sample,name='sample'),
    path('registerurl/',views.register,name='register'),
    path('displayurl/',views.display_details,name='details'),
    path('updateurl/<int:id>',views.update_details,name='update'),
    path('deleteurl/<int:id>',views.delete,name='delete'),
    path('signupurl/',views.signup,name='signup'),
]