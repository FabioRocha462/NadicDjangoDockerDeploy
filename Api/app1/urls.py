from app1.views import capture_get, postdata, showPost
from django.urls import   path
urlpatterns = [
    #path('v1/', capture_get),
    path('', postdata),
    path('showPost', showPost),
]