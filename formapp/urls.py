from django.urls.conf import path
from . import views


urlpatterns = [
    path('forms/', views.fnforms, name="forms"),
    path('datatransfer/', views.datatransfer, name="datatransfer"),
]
