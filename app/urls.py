from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'bug', views.BugAPI, 'bug')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('', login_required(views.Home.as_view())),
    path('record-bug/', login_required(views.RecordBug.as_view()))
]