from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('platform/',views.platform,name='platform'),
    path('locked/',views.locked,name='locked'),
    path('unlock/',views.unlock,name='unlock')

]
