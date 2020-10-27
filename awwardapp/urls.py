from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    url('^$',views.index,name = 'home'),
]