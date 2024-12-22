
![alt text](./source/readme-promo.jpg)

# Проект FOX KIDS ONLINE 4
Четвертая версия рефакторинга платформы трансляции американских мультсериалов Fox Kids Online

🌎 [Веб-сайт проекта](https://foxkids-online.ru/)  
💼 [Страница организации](https://github.com/foxkids-online)  

## О проекте
Код платформы сайта foxkids-online.ru  
Документация Swagger по пути /docs

## Описание дерева проекта

html - папка фронтенда  
--static  
----css  
----js  
----sources  
------promos - изображения для промо  
------series - избражения для карточек сериалов  
------site - оформление сайта  
----favicon.ico  
src - папка с проектом бекенда  
tests - автотесты  


## Полезные скрипты (производятся из корня директории проекта)

Запуск автотестов

`python -m pytest -s`

Запуск сервера документации к коду

`poetry run pdoc --http 0.0.0.0:8000`

Запуск проекта

`poetry run python -m foxkids`

Загрузка плагина poetry-dotenv для чтения .env

`poetry self add poetry-dotenv-plugin`

Проверка покрытия тестами

`pytest --cov=foxkids tests/ --cov-report html`

## Переменные окружения

| Название переменной | Значение | Комментарий |
| --- | --- | --- |
| ENV_FOR_DYNACONF | production, development,   test | переменная для указания среды стенда |

## Конфигурации приложения

Скрипты приложения находятся в папке settings.  
Внутри config-files находятся сами файлы конфигурации:  

dev-setttings.yaml - дев среда  
test-settings.yaml - среда тестирования, с нее запускаются автотесты  
prod-settings.yaml - прод  

Dockerfile - прод среда
Dockerfile-dev - дев среда

| Название переменной | Значение | Пример заполнения                                                                       |
| ------------------- | ------------------------------- | ---------------------------------------------------------------- |
| COUNT_COMMERTIALS   | количество реклам между блоками | 2                                                                |
| TIME_START          | время пересчета серий | 06:55                                                                      |
| STREAM_URL          | адрес стрима | rtmp://server_rtmp:1935/stream/test                                                 |
| MAIN_FOLDER         | главная папка облака трансляции | dev_mnt_sample/foxkids                                           |
| FILE_PROGRAM        | файл программы передач | dev_mnt_sample/program.json                                               |
| FILE_SERIES         | файл с сериалами | dev_mnt_sample/series.json                                                      |
| FILE_STREAM         | скрипт трансляции | dev_mnt_sample/stream.sh                                                       |
| PROMO_FOLDER        | папка с промо сериалов внутри основной папки облака | reklama                                      |
| BLOCK_PROMO_FOLDER  | папка с промо блоков внутри основной папки облака | reklama_block                                  |
| COMMERTIALS_FOLDER  | папка рандомных реклам внутри основной папки облака | reklama_random                               |
| PLAY_SCRIPT         | маска строки скрипта запуска ffmpeg       | ffmpeg  -re -i {адрес файла} -f flv {адрес трансляции} |
| CURL_SCRIPT         | адрес для установки промо следующей серии | переменная для указания среды стенда                   |
| PORT                | порт сервера трансляции                   | переменная для указания среды стенда                   |

полный шаблон маски скрипта: 

`ffmpeg  -re -i {файл} -c:a aac -c:v libx264 -b:v 200k -b:a 64K -r 25 -s 320x240 -f flv {адрес трансляции}`

полный адрес скрипта для установки промо следующей серии

`curl -X POST https://reqbin.com/echo/post/json -H \"Content-Type: application/json\" -d '{{\"current_series\": \"{}\", \"next_series\": \"{}\"}}'`

## Линтеры

`isort isort --settings-path pyproject.toml .`  - отсортирует и сделает красивые импорты во всех файлах  
`black -l 79 --preview .` или `black --config pyproject.toml .`  - отформатирует код  
`flake8 .`  - проверит кодстайл  
`mypy . --ignore-missing-imports` или `mypy --config pyproject.toml .`  - проверит типизацию  

## Установка pre-commit

- Установить pre-commit через `poetry add pre-commit`  
- Установить pre-commit хуки через `pre-commit install`  
- При создании коммита будут срабатывать хуки из файла `.pre-commit-config.yaml`  

## Настройка удаленной машины для деплоя 

Условия:
- установлен docker
- установлен docker-compose

Создание отдельно пользователя $SSH_USER на удаленной машине:  
`useradd $SSH_USER`  

Выдача прав владельца на папку пользователя  
`sudo chown -R $SSH_USER: /home/$SSH_USER/*`  

Создание ключа  (выполнять от лица пользователя, который ответственен за деплой)
`ssh-keygen -t rsa -b 4096`  

Запись ключа в файл  
`cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`  

Проверка ключа, он же понадобится в переменной $SSH_KEY*
`cat ~/.ssh/id_rsa`  

На самой машине добавить пользователю права на докер  
`sudo chown $SSH_USER /var/run/docker.sock`  

Внутри папки `/home/$SSH_USER/` , создать папку $WORKDIR куда будет производиться установка проекта




                    