# Используем базовый образ Python 3.7 slim
FROM python:3.7-slim

# Создаем директорию для HTTP-сервера
RUN mkdir -p /usr/local/http-server

# Создаем пользователя runner с домашней директорией
RUN useradd runner -d /home/runner -m -s /bin/bash

# Устанавливаем рабочую директорию
WORKDIR /usr/local/http-server

# Копируем файлы приложения в контейнер
ADD ./application.py /usr/local/http-server/application.py
ADD ./index.html /usr/local/http-server/index.html

# Изменяем владельца файлов на пользователя runner
RUN chown -R runner:runner /usr/local/http-server/

# Открываем порт 8000
EXPOSE 8000

# Устанавливаем пользователя для выполнения команд
USER runner

# Указываем команду по умолчанию для запуска приложения
CMD ["python3", "-u", "/usr/local/http-server/application.py"]
