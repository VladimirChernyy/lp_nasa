# Landig page

## Фото 

![photo2](https://github.com/VladimirChernyy/Web-app-validate-form/assets/116533449/ac4a39b4-b0d0-4b04-8f50-eac1ffe65aa8)
![photo](https://github.com/VladimirChernyy/Web-app-validate-form/assets/116533449/6762f73d-28bd-44a7-a70c-390ffc4d3adc)


## В проекте были использованы технологии:
Django 4.1
Python 3.9
MySQL

## Как запустить проект:


Клонируйте с GitHub проект и перейдите в директорию проекта.
``` 
git@github.com:VladimirChernyy/lp_nasa.git

cd lp_nasa
``` 

Создаем файл .env по примеру .env.example

``` 
sudo nano .env
```

Настройте и активируйте виртуальную среду  
```
python3.9 -m venv venv

source venv/bin/activate
```

Установите зависимости
```
pip install -r req.pip
```
Примените миграции
```
python3 manage.py migrate
```

Создайте пользователя для доступа к админ панели 
```
python3 manage.py createsuperuser
```

## Над проектом работал:
[Vladimir Chernyy](https://github.com/VladimirChernyy)
