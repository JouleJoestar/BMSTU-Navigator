# Инструкция по развёртыванию 
## Подготовка IDE
1. Скачиваем все файлы или клонируем репозиторий
2. Открываем директорию, в которую склонировались\скачались исходники, в терминале
3. Устанавливаем зависимости 

``` pip install -r requirements.txt ```

4. Активируем виртуальное окружение 

``` venv/Scripts/Activate.ps1 ```

5. Создаём ```.env``` файл в той же директории 
6. Внутри ```.env``` файла создаём следующие переменные окружения ()
```
HOST_NAME=postgres  #при запуске вне контейнера localhost, при запуске в контейнере postgres
DATABASE_NAME=BMSTU_Navigator
USER_NAME=postgres
PASSWORD_POSTGRES=postgres
BACKEND_PORT_POSTGRES=5432 #по умолчанию 5432
PG_ADMIN_PORT=15432
FLASK_EXTERNAL_PORT=5000 #по умолчанию 5000
PGADMIN_LISTEN_PORT_ENV=80
```
## Работа с Docker
7. Запускаем все сервисы, описанные в файле docker-compose.yml 
``` docker-compose up -d ```

Опция "-d" (или "--detach") означает, что контейнеры запускаются в фоновом режиме, без вывода их логов в консоль
В результате должно получиться 3 сервиса-контейнера 
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/f7b67d0e-8859-46d1-831f-de182de0f305)

## Работа в PGAdmin
8. Переходим по ссылке http://localhost:15432/browser/

Данные для входа 
```
admin@pgadmin.com
password
```
9. Создаём сервер

![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/cb876462-1c92-4099-ac41-152ba2d5c9d0)
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/2ed24a7b-ee34-4d5a-a6fe-8b8ef3f67676)

10. Создаём БД 

![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/245bc8fc-2b7d-455f-ad6d-12b305c7b02e)

11. Восстанавливаем базу данных из backup файла

![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/a839c835-c747-470e-b8b0-b5108a517b30)
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/ea510283-a0cc-4c05-b4ae-0783cfb6271d)
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/cf8b4ee5-eb82-4385-8b82-bbeacaf75ad7)
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/8c54e349-0d44-4589-95af-b943152db282)
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/c4bcc636-5a3d-4a6e-91ef-f48153fe82c5)
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/f8ec031a-fb56-4768-80c6-5107ed5bc989)

12. Радуемся тому, что всё работает 
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/31835ffd-4b62-43d8-9b06-c90db9b082ef)

# Развёртывание на локальной машине (не в контейнере) 

1. Открываем файл ``` util.py ``` 
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/822de145-3974-4348-a729-f42928227d92)
2. Комментируем часть кода под цифрой 1 и раскомментируем часть кода по цифрой 2
![image](https://github.com/VorchukOleg/BMSTU-Navigator/assets/55689955/d6b387b0-4fae-436b-a395-337ceff45eb9)
3. Запускаем сервер с помощью команды ```python -m flask --app flask_api\app.py run --host=0.0.0.0```
















