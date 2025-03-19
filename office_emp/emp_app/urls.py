# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('view_all_emp/',views.all_emp,name='view_ll_emp'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('remove_emp/',views.remove_emp,name='remove_emp'),
    path('filter_emp/',views.filter_emp,name='filter_emp'),
]
