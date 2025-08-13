from django.urls import path

from tasks.api.views import TaskCreateView, TaskDetailView, UserTaskView



urlpatterns = [
    path('list/', UserTaskView.as_view()),
    path('create/', TaskCreateView.as_view()),
    path('<int:pk>/', TaskDetailView.as_view()),
]
