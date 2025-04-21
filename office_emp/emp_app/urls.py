from django.urls import path
from . import views
 
app_name = 'emp_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('all_emp/',views.all_emp,name='all_emp'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('remove_emp/',views.remove_emp,name='remove_emp'),
    # path('filter_emp/',views.filter_emp,name='filter_emp'),
    # path('register/',views.register, name='register'),
    # path('login/',views.user_login,name='login'),  
]
