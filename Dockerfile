# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r mysite/requirements.txt

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Открываем порт
EXPOSE 8000

# Запуск миграций и старт сервера
CMD ["sh", "-c", "python mysite/manage.py migrate && python mysite/manage.py runserver 0.0.0.0:8000"]
