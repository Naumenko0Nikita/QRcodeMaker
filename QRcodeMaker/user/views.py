from django.shortcuts import render, redirect  # Импорт функций для рендеринга страниц и редиректа
from django.contrib.auth import authenticate, login, logout  # Импорт методов аутентификации и управления сессией
from django.contrib.auth.decorators import login_required  # Импорт декоратора для защиты страниц
from django.contrib import messages  # Импорт системы сообщений Django
from .models import CustomUser as User  # Импорт кастомной модели пользователя



def render_registation(request):  # Определение функции обработки регистрации
    context = {
        "name": [],  # Контейнер для возможных ошибок имени пользователя
        "email": [],  # Контейнер для возможных ошибок email
        "password": []  # Контейнер для возможных ошибок пароля
    }
    if request.method == 'POST':  # Проверяем, что запрос выполнен методом POST
        username = request.POST.get('username')  # Получаем введенное имя пользователя
        email = request.POST.get('email')  # Получаем введенный email
        password = request.POST.get('password')  # Получаем введенный пароль
        password_confirm = request.POST.get("passwordConfirm")  # Получаем подтверждение пароля
        
        if User.objects.filter(username=username).exists():  # Проверяем, существует ли пользователь с таким именем
            context["name"].append("Користувач з таким ім'ям вже існує.")  # Добавляем сообщение об ошибке

        elif User.objects.filter(email=email).exists():
            # messages.error(request, 'Користувач з таким email вже існує.')
            # return redirect('reg')
            context["email"].append("Користувач з таким email вже існує.")
        
        elif User.objects.filter(email=email).exists():  # Проверяем, существует ли пользователь с таким email
            context["email"].append("Користувач з таким email вже існує.")  # Добавляем сообщение об ошибке

        else:
            user = User.objects.create_user(username=username, email=email, password=password)  # Создаем нового пользователя
            user.save()  # Сохраняем пользователя в базе данных
            return redirect('login')  # Перенаправляем на страницу входа после успешной регистрации

    return render(request=request, template_name="registration/registration.html", context=context)  # Рендерим страницу регистрации с контекстом


def render_login(request):  # Определение функции обработки входа
    context = {
        "error": []  # Контейнер для возможных ошибок входа
    }
    if request.method == 'POST':  # Проверяем, что запрос выполнен методом POST
        username = request.POST.get('username')  # Получаем введенное имя пользователя
        password = request.POST.get('password')  # Получаем введенный пароль
        user = authenticate(request, username=username, password=password)  # Аутентифицируем пользователя
        
        if user is not None:  # Проверяем, найден ли пользователь
            login(request, user)  # Авторизуем пользователя
            return redirect('/')  # Перенаправляем на главную страницу
        
        else:
            context["error"].append("Неправильне ім'я користувача або пароль.")  # Добавляем сообщение об ошибке

    return render(request=request, template_name="login/login.html", context=context)  # Рендерим страницу входа с контекстом

def render_logout(request):  # Определение функции выхода из системы
    logout(request)  # Выполняем выход из системы
    messages.success(request, 'Ви вийшли із системи.')  # Добавляем сообщение об успешном выходе
    return redirect('login')  # Перенаправляем на страницу входа

def render_account(request):  # Определение функции обработки страницы аккаунта
    if request.user.is_authenticated:  # Проверяем, авторизован ли пользователь
        return render(request=request, template_name="account/account.html")  # Рендерим страницу аккаунта
    return redirect("reg")  # Если пользователь не авторизован, перенаправляем его на регистрацию
