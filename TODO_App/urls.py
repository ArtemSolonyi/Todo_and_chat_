from django.urls import path

from TODO_App.views import Register, Login, Logout, TODO, DeleteTask, EditTask

urlpatterns = [

    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('', TODO.as_view(), name='todo'),
    path('delete_task', DeleteTask.as_view(), name='delete'),
    path('edit_task', EditTask.as_view(), name='edit'),

]
