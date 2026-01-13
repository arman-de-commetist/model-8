from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # маршруты ToDo
    path('', lambda request: redirect('task_list')),  # редирект с корня на список задач
]
