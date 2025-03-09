from django.urls import path  # Импортируем функцию path для определения маршрутов
from .views import render_registation, render_login, render_logout, render_account  # Импортируем представления из views.py


urlpatterns = [
    path('registration/', render_registation, name="reg"),  # URL для страницы регистрации
    path('login/', render_login, name="login"),  # URL для страницы входа
    path('logout/', render_logout, name='logout'),  # URL для выхода из системы
    path('account/', render_account, name="account")  # URL для страницы аккаунта
]
