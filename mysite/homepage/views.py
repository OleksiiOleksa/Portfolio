from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'homepage/index.html')

def send_feedback(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')  # Почта пользователя
        user_message = request.POST.get('message')  # Сообщение пользователя

        if user_email and user_message:
            try:
                # Формируем тело письма
                email_body = f"Message from: {user_email}\n\n{user_message}"

                # Отправляем письмо
                send_mail(
                    subject="New Hire Me Request",  # Тема письма
                    message=email_body,  # Тело письма
                    from_email='baginski.oleksii@gmail.com',  # Ваша почта-отправитель
                    recipient_list=['baginski.oleksii@gmail.com'],  # Ваша почта-получатель
                    fail_silently=False,
                )
                # Добавляем сообщение об успешной отправке
                messages.success(request, "Message sent! I will reply to you as soon as possible.")
            except Exception as e:
                # Добавляем сообщение об ошибке
                messages.error(request, f"An error occurred: {e}")
        else:
            # Если пользователь не заполнил все поля
            messages.error(request, "Please fill in all fields.")

        return redirect('home')  # Замените 'home' на ваш URL

    return redirect('home')