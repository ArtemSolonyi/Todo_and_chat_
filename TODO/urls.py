from django.contrib import admin
from django.urls import path, include

import TODO_App
from TODO_App import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(TODO_App.urls))
]
