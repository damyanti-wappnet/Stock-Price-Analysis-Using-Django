from django.urls import path
from MSFTAnalysis import views

urlpatterns = [
    path('', views.index,name = 'hello'),

]