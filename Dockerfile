# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /model

# Копируем необходимые файлы в контейнер
COPY app.py model.pkl requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для приложения (например, Flask)
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]