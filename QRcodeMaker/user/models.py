from django.db import models  # Импортируем модуль для работы с моделями Django
from django.contrib.auth.models import AbstractUser  # Импортируем абстрактную модель пользователя Django
from datetime import datetime  # Импортируем модуль работы с датой и временем
from dateutil.relativedelta import relativedelta  # Импортируем функцию для работы с относительными датами
# Create your models here.


class CustomUser(AbstractUser):  # Создаем кастомную модель пользователя, наследуясь от AbstractUser
    licence = models.CharField(max_length=255, blank=True, null=True)  # Поле для хранения лицензии, может быть пустым
    licence_date = models.DateTimeField(default=datetime.now() + relativedelta(months=1))  # Поле даты лицензии, по умолчанию +1 месяц от текущей даты
    
    def __str__(self):  # Определяем строковое представление объекта
        return self.username  # Возвращаем имя пользователя
