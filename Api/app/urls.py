from app.views import home, getData, showResult
from django.urls import   path
urlpatterns = [
    path('', home),
    path('getData', getData),
    path('showResult', showResult),
]