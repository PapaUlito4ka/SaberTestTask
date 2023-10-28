# SaberTestTask

Тестовое задания для компании "Saber".

Запуск проекта через Docker:

1. Собираем проект
```
docker-compose build
```

2. Запускаем контейнеры
```
docker-compose up -d
```

3. Optional. Остановить контейнеры
```
docker-compose down
```

После этого проект будет запущен на http://127.0.0.1:8008/

Swagger для просмотра API: http://127.0.0.1:8008/docs/

API для получения задач по названию билда: http://127.0.0.1:8000/api/v1/tasks/
