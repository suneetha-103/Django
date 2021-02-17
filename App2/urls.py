from django.urls import path
from App2 import views
from django.contrib.auth import views as as_views
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
    path('userregistration/',views.registration,name='registration'),
    path('showdataurl/',views.showdata,name='showdata'),
    path('signupform/',views.signupform,name='signupform'),
    path('loginurl/', as_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logouturl/',as_views.LogoutView.as_view(),name='logout'),
    path('profile/',views.profile,name='profile')
]