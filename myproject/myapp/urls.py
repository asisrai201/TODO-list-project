from django.urls import path, include
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/complete/', views.task_complete, name='task_complete'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/confirmation/', TemplateView.as_view(template_name='registration/logout_confirmation.html'), name='logout_confirmation'),
]
