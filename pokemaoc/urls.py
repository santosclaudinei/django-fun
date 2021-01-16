from django.urls import path
from . import views

urlpatterns = [
    path('simple', views.simple, name="A page with api request"),
    path('package', views.package, name="A page with package"),

]
