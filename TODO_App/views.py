import re

import bcrypt

from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .models import User, Task
from django.contrib import messages
from django.http import HttpResponseRedirect


class EditTask(View):

    def post(self, request):
        id_task = request.POST.get('id_name')
        edit_headline = request.POST.get('tasks')
        task = Task.objects.get(id=id_task)
        task.headline = edit_headline
        task.save()
        return HttpResponseRedirect(reverse('todo'))


class DeleteTask(View):

    def post(self, request):
        id_task = request.POST.get('id_name')
        Task.objects.get(id=id_task).delete()
        return HttpResponseRedirect(reverse('todo'))


class TODO(View):

    def get(self, request):
        username = request.session['username']
        user_for_tasks_model = User.objects.get(username=username)
        user_for_page = User.objects.filter(username=username)
        tasks = Task.objects.all().filter(name_user_articles=user_for_tasks_model)
        context = {
            'user':user_for_page,
            'username': username,
            'Task': tasks[::-1],
        }
        return render(request, 'todo.html', context)

    def post(self, request):
        task = request.POST.get('task')
        user = User.objects.get(username=request.session['username'])
        Task_todo = Task.objects.create(headline=task, name_user_articles=user)
        Task_todo.save()
        return HttpResponseRedirect(reverse('todo'))


class Logout(View):
    def get(self, request):
        username = request.session['username']
        user_for_page = User.objects.filter(username=username)
        user_for_page.model.autor = False
        print(user_for_page)
        print(f"from login {user_for_page.model.autor}")
        return render(request, 'registration/login.html')


class Register(View):

    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        errors = []
        context = {'data': request.POST}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password').encode("utf-8")
        password2 = request.POST.get('password2').encode("utf-8")

        if not username:
            errors.append(messages.add_message(request, messages.ERROR,
                                               'Username is required'))

        if User.objects.filter(username=username).exists():
            errors.append(messages.add_message(request, messages.ERROR, "Данный логин уже существует"))

        if User.objects.filter(email=email).exists():
            errors.append(messages.add_message(request, messages.ERROR, "Данный email уже существует"))

        if len(password1) < 8:
            errors.append(
                messages.add_message(request, messages.ERROR, "Длина пароля должна быть больше чем 6 символов"))

        if password1 != password2:
            errors.append(messages.add_message(request, messages.WARNING, "Пароли не совпадают"))

        if len(errors) > 0:
            return render(request, 'registration/register.html', context)
        password = bcrypt.hashpw(password1, bcrypt.gensalt())
        user = User.objects.create(username=username, email=email, password=bytes(password))
        user.save()
        return HttpResponseRedirect(reverse('login'))


class Login(View):

    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        errors = []
        login_email = request.POST.get('email')
        login_password = request.POST.get('password').encode('utf-8')
        user_from_model = User.objects.filter(email=login_email)
        try:
            hash_password_from_model = "".join(
                re.findall(r"[^']", user_from_model.values()[0]['password'])[1:]).encode(
                "utf-8")  # converting hashed password
        except IndexError:
            errors.append(messages.add_message(request, messages.ERROR, "Неверный пароль"))

        if not user_from_model:
            errors.append(messages.add_message(request, messages.ERROR, "Указанный email невереный"))
        if len(errors) > 0:
            return render(request, 'registration/login.html', )
        else:
            if bcrypt.checkpw(login_password, hash_password_from_model) and user_from_model:
                request.session['username'] = user_from_model.get().username
                user_from_model.model.autor = True
                print(user_from_model)
                print(f"from login {user_from_model.model.autor}")
                return HttpResponseRedirect(reverse('todo'))
            else:
                errors.append(messages.add_message(request, messages.ERROR, "Неверный логин или пароль"))

        return render(request, 'registration/login.html')
