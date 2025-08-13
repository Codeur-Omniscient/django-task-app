from django.urls import path

from tasks.api.views import TaskCreateView, TaskDetailView, UserTaskView



urlpatterns = [
    path('list/', UserTaskView.as_view(), name="task-list"),
    path('create/', TaskCreateView.as_view(), name="task-create"),
    path('<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
]
