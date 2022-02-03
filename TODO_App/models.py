from django.db import models


class User(models.Model):
    autor = False
    username = models.CharField("Имя", max_length=30)
    email = models.EmailField("Почта", max_length=100)
    password = models.CharField("Пароль", max_length=100)

    def __str__(self):
        return self.username




class Task(models.Model):
    headline = models.CharField(max_length=150, null=True, blank=True)
    name_user_articles = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.headline == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.headline
