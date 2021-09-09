from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'bug', views.BugAPI, 'bug')
router.register(r"bug-nested", views.BugNestedAPI, 'bug-nested')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('', login_required(views.Home.as_view())),
    path('record-bug/', login_required(views.RecordBug.as_view())),
    path('set-duplicate/', login_required(views.SetDuplicate.as_view())),
    path('set-resolved/<int:pk>/', login_required(views.SetResolved.as_view()))
]