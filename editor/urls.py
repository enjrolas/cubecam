from django.conf.urls import url
from editor import views

urlpatterns = [
    url(r'^$', views.edit, name='edit'),
    url(r'^compile/', views.compile, name='compile'),
    url(r'^flash/', views.flash, name='flash'),
]


