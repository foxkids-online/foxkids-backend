
![alt text](./source/readme-promo.jpg)

# Project FOX KIDS ONLINE 4
The fourth version of the refactoring of the platform for broadcasting American animated series Fox Kids Online

## About the project
Platform code of the site foxkids-online.ru
Swagger documentation is located in the /docs path

## Description of the project tree

html - папка фронтенда  
--static  
----css  
----js  
----sources  
------promos - images for promo  
------series - images of series cards   
------site - site styling    
----favicon.ico  
src - folder with backend main project    
tests - autotests  


## Useful scripts (run from the project directory root)

Running the autotests:
`python -m pytest -s`

Starting the code documentation server:
`poetry run pdoc --http 0.0.0.0:8000`

Launching the project:
`poetry run python -m foxkids`

Loading the poetry-dotenv plugin to read .env:
`poetry self add poetry-dotenv-plugin`

Checking test coverage:
`pytest --cov=foxkids tests/ --cov-report html`

## Environment variables
| Variable name | Value | Comment |
| --- | --- | --- |
| ENV_FOR_DYNACONF | production, development, test | variable to indicate the environment of the stand |

## Application configurations

The application scripts are located in the settings folder. Inside config-files, there are the configuration files themselves:  
* dev-settings.yaml — development environment  
* test-settings.yaml — testing environment, autotests are launched from it  
* prod-settings.yaml — production  

Dockerfile — production environment  
Dockerfile-dev — development environment  

| Variable name       | Value                           | Example of filling                                                     |
| ------------------- | ------------------------------- | ---------------------------------------------------------------------- |
| COUNT_COMMERTIALS   | Number of commercials between blocks | 2                                                                 |
| TIME_START          | Start time of the broadcast       | 07:00                                                                |
| STREAM_URL          | Stream address                   | rtmp://server_rtmp:1935/stream/test                                   |
| MAIN_FOLDER         | Main folder of the broadcasting cloud | dev_mnt_sample/foxkids                                           |
| FILE_PROGRAM        | Program file                     | dev_mnt_sample/program.json                                           |
| FILE_SERIES         | File with TV series | dev_mnt_sample/series.json                                                         |
| FILE_STREAM         | Streaming script   | dev_mnt_sample/stream.sh                                                            |
| PROMO_FOLDER        | Folder with promos of TV series inside the main folder of the cloud | reklama                            |
| BLOCK_PROMO_FOLDER  | Folder with promo blocks inside the main folder of the cloud | reklama_block                             |
| COMMERTIALS_FOLDER  | Folder with random commercials inside the main folder of the cloud | reklama_random                      |
| PLAY_SCRIPT         | Mask of the ffmpeg launch script line       | ffmpeg -re -i {file address} -f flv {broadcast address}    |
| CURL_SCRIPT         | Address for setting up the promo of the next episode | Variable to indicate the environment of the stand |
| PORT                | Port of the broadcast server                  | Variable to indicate the environment of the stand.       |

**Full script mask template:**

`ffmpeg -re -i {file} -c:a aac -c:v libx264 -b:v 200k -b:a 64K -r 25 -s 320x240 -f flv {broadcast address}`

**Full address of the script for setting up the promo of the next episode:**

`curl -X POST https://reqbin.com/echo/post/json -H "Content-Type: application/json" -d '{{"current_series": "{}"", "next_series": "{}"}}'`

## Linters

`isort isort --settings-path pyproject.toml .` — sorts and makes beautiful imports in all files

`black -l 79 --preview .` or `black --config pyproject.toml .` — formats the code

`flake8 .` — checks the code style

`mypy . --ignore-missing-imports` or `mypy --config pyproject.toml .` — checks typing

## Installing pre-commit

- Install pre-commit via `poetry add pre-commit`

- Install pre-commit hooks via `pre-commit install`

- When creating a commit, hooks from the `.pre-commit-config.yaml` file will be triggered  

REAMDE.md — это, вероятно, название файла или репозитория. Если вам нужно перевести его содержимое на английский язык, я могу помочь с этим. Пожалуйста, уточните запрос.

Перевод содержимого файла REAMDE.md с русского на английский:

## Setting up a remote machine for deployment

**Prerequisites:**
- Docker is installed
- Docker Compose is installed

Creating a separate user $SSH_USER on the remote machine:  
`useradd $SSH_USER`  

Granting ownership of the user's folder  
`sudo chown -R $SSH_USER: /home/$SSH_USER/*`  

Generating a key (run as the user responsible for deployment):  
`ssh-keygen -t rsa -b 4096`  

Adding the key to the file:  
`cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`  

Checking the key, it will also be needed in the $SSH_KEY variable:  
`cat ~/.ssh/id_rsa`  

On the machine itself, add Docker permissions to the user:  
`sudo chown $SSH_USER /var/run/docker.sock`  

Inside the `/home/$SSH_USER/` folder, create a $WORKDIR folder where the project will be installed.
