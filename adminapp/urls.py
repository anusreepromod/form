from django.urls.conf import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('logins/', views.fnlogin, name="fnlogin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('getdata/', views.getdata, name="getdata"),
    path('deldata/', views.deldata, name="deldata"),
    path('masters/', views.masters, name="masters"),
    path('logout/', views.logout, name="logout"),

]
