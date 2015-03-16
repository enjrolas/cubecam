from django.conf.urls import url
from javascript import views

urlpatterns = [
    url(r'^browser/', views.browser, name='browser'),
]


