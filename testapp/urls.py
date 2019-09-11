from django.contrib import admin
from django.urls import path, include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name = 'home'),
    path('staff form', views.staff_form, name = 'staffform'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout')
]
