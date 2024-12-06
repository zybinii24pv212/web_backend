# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт для Gunicorn/Django
EXPOSE 8000

# Запускаем сервер
CMD ["gunicorn", "project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
