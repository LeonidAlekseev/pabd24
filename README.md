# Предиктивная аналитика больших данных

Учебный проект для демонстрации основных этапов жизненного цикла проекта предиктивной аналитики.  

## Installation 

Клонируйте репозиторий, создайте виртуальное окружение, активируйте и установите зависимости:  

```sh
git clone https://github.com/LeonidAlekseev/pabd24
cd pabd24
python3 -m venv venv

source venv/bin/activate  # mac or linux
.\venv\Scripts\activate   # windows

pip install -r requirements.txt
```

## Usage

### 1. Сбор данных о ценах на недвижимость
```sh
python src/parse_cian.py 
```  
Параметры для парсинга можно изменить в скрипте.  
Подробности см. в [репозитории](https://github.com/lenarsaitov/cianparser)  

### 2. Выгрузка данных в хранилище S3
Для доступа к хранилищу скопируйте файл `.env` в корень проекта.  

```sh
python src/upload_to_s3.py -i data/raw/file.csv 
```  
Аргумент -i или --input указывает пути до локального файла, по умолчанию переменная CSV_PATH в исполняемом файле

### 3. Загрузка данных из S3 на локальную машину
Для доступа к хранилищу скопируйте файл `.env` в корень проекта.  

```sh
python src/download_from_s3.py -i data/raw/file.csv 
```  
Аргумент -i или --input указывает пути до удаленного файла, по умолчанию переменная CSV_PATH в исполняемом файле

### 4. Предварительная обработка данных

```sh
python src/preprocess_data.py -s 0.9 -i data/raw/file.csv 
```  
Аргумент -s или --split указывает относительный размер обучающей выборки, по умолчанию переменная TRAIN_SIZE в исполняемом файле
Аргумент -i или --input указывает пути до удаленного файла, по умолчанию переменная CSV_PATH в исполняемом файле

### 5. Обучение модели 

```sh
python src/train_model.py -m models/ridge_regression_v01.joblib
```  
Аргумент -m или --model указывает путь сохранения модели, по умолчанию переменная MODEL_SAVE_PATH в исполняемом файле
Модель обучается предсказывать цену (price) по площади (total_meters)

```sh
python src/test_model.py -m models/ridge_regression_v01.joblib
```  
Аргумент -m или --model указывает путь сохранения модели, по умолчанию переменная MODEL_SAVE_PATH в исполняемом файле
Модель обучается предсказывать цену (price) по площади (total_meters)

### 6. Запуск приложения flask 

```sh
python src/predict_app.py
```  

### 7. Запуск приложения gunicorn 

```sh
gunicorn -b 0.0.0.0:8000 -w 1 src.predict_app:app --daemon
```  

### 8. Тестирование приложения 

```sh
python src/test_api.py 
```  
Api Endpoint 'http://31.129.100.203:8000' в исполняемом файле указывает на личный сервер

```sh
python src/test_parallel.py 
```  
Api Endpoint 'http://31.129.100.203:8000' в исполняемом файле указывает на личный сервер

### 9. Сборка Docker образа проекта

```sh
docker build --platform="linux/amd64" -t leonidalekseev/pabd24:dev -f Dockerfile.dev . 
```  
Development версия с запуском приложения через flask
Аргумент --platform указывает платформу для сборки образа

```sh
docker build --platform="linux/amd64" -t leonidalekseev/pabd24:latest -f Dockerfile .
```  
Production версия с запуском приложения через gunicorn
Аргумент --platform указывает платформу для сборки образа

### 10. Запуск Docker контейнера проекта

```sh
docker pull leonidalekseev/pabd24:dev
docker run --log-driver json-file --name=pabd24dev -d -p 8000:8000 leonidalekseev/pabd24:dev
```  
Development версия с запуском приложения через flask
Аргумент --log-driver указывает формат записи логов контейнера
Аргумент --name указывает название для запуска контейнера
Аргумент -d указывает на то что нужно отсоединиться после запуска (detach)
Аргумент -p указывает на открытие и соединение портов приложения к внешнему

```sh
docker pull leonidalekseev/pabd24:latest
docker run --log-driver json-file --log-opt max-size=32m --log-opt max-file=1 --name=pabd24 -d -p 8000:8000 leonidalekseev/pabd24:latest
```  
Production версия с запуском приложения через gunicorn
Аргумент --log-driver указывает формат записи логов контейнера
Аргумент --log-opt указывает на ограничения размера логов контейнера
Аргумент --name указывает название для запуска контейнера
Аргумент -d указывает на то что нужно отсоединиться после запуска (detach)
Аргумент -p указывает на открытие и соединение портов приложения к внешнему

### 11. Использование сервиса через веб интерфейс 
Для доступа к сервису используйте следующий адрес: 
`http://31.129.100.203:8000/`

Для использования сервиса используйте файл `web/index.html`.  




# Предиктивная аналитика больших данных

Учебный проект для демонстрации процесса разработки сервиса предиктивной аналитики. 
Мы будем шаг за шагом разрабатывать сервис, предсказывающий цены на недвижимость.  
В качестве IDE рекомендуется использовать PyCharm Community. Вы можете использовать другую IDE, если лучше ее знаете.  


### Балльно-рейтинговая система:  

**Экзамен** - 60 баллов  
В билете будет два теоретических вопроса и один практический (20, 20, 20).  
Ответы только на листочках, компьютеры не включать, интернетом не пользоваться.  
Вопросы по [теории](docs/theory.md) и [практике](docs/practice.md)  

**Текущая успеваемость** - 40 баллов, вкл:  
4 лаб работы по 8 баллов = 32  
Активность на занятиях (тесты) = 8  

[Тест 1](https://campus.fa.ru/mod/quiz/view.php?id=536912)  
[Тест 2](https://campus.fa.ru/mod/quiz/view.php?id=536914)  
[Тест 3](https://campus.fa.ru/mod/quiz/view.php?id=536916)  
[Тест 4](https://campus.fa.ru/mod/quiz/view.php?id=536918)  

Лекции и литература находятся на [Google Drive](https://drive.google.com/drive/folders/1cUry7oySkAJ5OB5lMGQcMceTO2nWxUHT?usp=drive_link)  

Текущая успеваемость студентов выставляется в таблице, которую можно найти в [файле](docs/results.csv)

Ссылки на свои репозитории и решения практических задач экзамена присылайте на почту ailabintsev@fa.ru   
Тесты проходить в классе на занятиях, в присутствии преподавателя.  

## План семинаров

### 1. Настройка окружения. Основы работы с bash, git, pycharm
Основные команды bash и git. 
Создание проекта с именем **pabd24** и публикация на github.  
Внесение первых правок через pull request.  

**Результат:**  
1. Cсылка на проект у меня на почте - 2 балла. 
2. Ветка master - защищена от прямых коммитов - 1 балл. 
3. Ветка tmp - содержит в README.md строчку о том, что это другая ветка - 1 балл. 

### 2. Сбор данных. Предобработка с помощью скриптов.  
Парсинг циан.  
Работа с переменными окружения .env  
Работа с хранилищем S3.  
Первичный анализ данных и скрипт предобработки данных.  

Файл .env находится в [Google Drive](https://drive.google.com/drive/folders/1cUry7oySkAJ5OB5lMGQcMceTO2nWxUHT?usp=drive_link)    
Посмотреть содержимое бакета можно по ссылке https://storage.yandexcloud.net/pabd24  

**Результат:**  
1. 3 CSV файла результатами парсинга для 1, 2, 3 комнатных квартир (по 50 на каждую) размещены на S3 бакете в папке с Вашим ID - 4 балла.  
2. Реализованы скрипты для загрузки Ваших данных из хранилища S3 и препроцессингу - 2 балла.   
3. В README.md Вашего проекта (шаблон - [здесь](docs/README.template.md)) есть описание использования для скриптов - 2 балла. 

ШТРАФ!!! ЗА .env и / или данные в папке data на гитхабе - минус 2 балла.  


P.S. Файлы данных можно скачать отсюда [1](https://storage.yandexcloud.net/pabd24/data/raw/cian_flat_sale_1_50_moskva_26_Apr_2024_14_08_32_338904.csv), 
[2](https://storage.yandexcloud.net/pabd24/data/raw/cian_flat_sale_1_50_moskva_26_Apr_2024_14_15_43_988750.csv), 
[3](https://storage.yandexcloud.net/pabd24/data/raw/cian_flat_sale_1_50_moskva_26_Apr_2024_14_22_17_675082.csv)

### 3. Обучение модели. Оценка метрик. Деплой на сервер.  
Решить проблему с перемешиванием данных в `preprocess_data.py`  
Выделить логику валидации из файла `train_model.py` в отдельный скрипт `test_model.py`  
Добавить  предсказание модели в `predict_app.py`   
Добавить тест для сервиса с помощью библиотеки `requests`  
Добавить  аутентификацию по токену в `predict_app.py`      

Создать виртуальную машину и подключиться по SSH.  

Создание пары публичный-приватный ключ 
```shell
ssh-keygen
```
Подключение по ssh к виртуальной машине
```shell
ssh user1@192.144.12.4 
```
Запустить оболочку bash
```shell
bash
```
Обновить индексы пакетов системы и  установить модуль `venv` для pyton3  
```shell
sudo apt update
sudo apt install python3-venv
```
Клонировать свой репозиторий:
```shell
git clone https://github.com/labintsev/pabd24
```
Открыть второе окно PowerShell в директории проекта `pabd24`, там где есть файл `.env`.  
Копирование файла .env из локальный машины на сервер выполняется командой:  
```shell
scp .\.env user1@192.144.12.4:/home/user1/pabd24
```
Дальше устанавливаем зависимости, скачиваем данные и обучаем модель по инструкции в Вашем README.  

Не забудьте настроить группы безопасности для открытия портов 5000 и 8000!  

#### Gunicorn сервер
Установка и запуск: 
```shell
pip install gunicorn
gunicorn -b 0.0.0.0 -w 1 src.predict_app:app --daemon
```
Для исследований следует опустить флажок `--daemon`, тогда можно легко остановить сервер нажатем `Ctr-C`. 
Остановить запущенный в фоне процесс можно командой 
```shell
pkill gunicorn
```

#### Результат: 
1. В Вашем README указан адрес, на котором запущен Ваш сервис предсказания цен, (gunicorn на порт 8000) - 4 балла.  
2. В папке docs краткое описание разницы в работе development и production (gunicorn) серверов - 4 балла.  
Шаблон отчета - [здесь](docs/report_3.md). 

### 4. Версионирование данных и экспериментов. 
Инициализация DVC и базовые операции - [Get started](https://dvc.org/doc/start?tab=Windows-Cmd-)  
Гайд по [credentials](https://yandex.cloud/ru/docs/storage/tools/aws-cli#config-files)  
В качестве `endpointurl` в настройках dvc указать `https://storage.yandexcloud.net`.  
Подробнее [здесь](https://dvc.org/doc/user-guide/data-management/remote-storage/amazon-s3#s3-compatible-servers-non-amazon)    
Опционально: Настройка собственного S3 хранилища на [cloud.ru](https://cloud.ru/ru/docs/s3e/ug/topics/tools__sdk-python.html)  

Настройка пайплайна по официальной [инструкции](https://dvc.org/doc/start/data-pipelines/data-pipelines). 
Их проект скачивать не нужно, stages добавлять командой 
```
dvc stage add -n preprocess python src/preprocess_data.py
```
Всего четыре стадии: 
1. подготовка данных для обучения,
2. подготовка данных для тестирования
3. обучение модели
4. тестирование модели
   
Подробнее см. в файле [dvc.yaml](dvc.yaml).  

Обучение лучшей модели - это поиск наиболее информативных признаков, архитектуры модели и гиперпараметров обучения. 
Каждый вариант с разными признаками или моделью должен быть в отдельной git-ветке. 
Как минимум еще один.  

Ваша лучшая модель должна работать в gunicorn-сервисе на том адресе, который указан у Вас в README.  
Тестирование сервиса будет происходить с помощью синхронных запросов, скрипт [здесь](grads/service_test.py).  
В запросе будут все поля, что и в исходных csv-файлах.  
Пример запроса: 
```
{'author': 'Verges of estate', 'author_type': 'real_estate_agent', 'url': 'https://www.cian.ru/sale/flat/294966171/', 'location': 'Москва', 'deal_type': 'sale', 'accommodation_type': 'flat', 'floor': 4, 'floors_count': 30, 'rooms_count': 3, 'total_meters': 115.6, 'district': 'Южнопортовый', 'street': ' 1-я Машиностроения', 'house_number': '10', 'underground': 'Дубровка', 'residential_complex': 'Дубровская Слобода', 'url_id': 294966171, 'first_floor': False, 'last_floor': False, 'area': 115.6}
```
Метрика - средняя ошибка на 100 случайных объектах недвижимости.  


[Docker tutorial](https://docs.docker.com/guides/workshop/)  

Установка docker на [ubuntu](https://docs.docker.com/engine/install/ubuntu/)  

**Результат:**
1. Подключение dvc к проекту, настройка пайплайна и версионирование экспериментов  - 4 балла
2. Обучение лучшей модели и деплой на сервер - 4 балла   
3. Контейнеризация Docker и публикация образа на DockerHub - 4 балла.

Ваш образ должен использовать gunicorn и порт 8000.   
В README.md Вашего git-репозитория должна содержаться инструкция по запуску приложения в docker, например:  

Для запуска приложения используйте docker:
```shell
docker run ailabintsev/pabd24:latest
```

#### P.S. cron and airflow
Для автоматического выполнения задачи (например, парсинга данных) целесообразно написать скрипт. 
В нашем случае это [task](tasks/task.sh) - запуск парсинга Циан. 
Сделать скрипт исполняемым нужно с помощью команды 

```shell
chmod +x tasks/task.sh
```
Проверьте возможность выплнения скрипта перед его добавлением в cron!  

```shell
./tasks/task.sh
```

Для создания периодических заданий нужно редактировать таблицу cron с помощью команды:  
```shell
crontab -e
```
Для выполнения скрипта `task.sh` каждую минуту нужно добавить следующую строку:  
`* * * * * cd /home/user1/pabd24 && ./tasks/task.sh`  

Журнал событий сервиса cron можно посмотреть командой 
```shell
sudo journalctl -u cron -f
```

Для более продвинутых заданий нужно использовать более мощный инструмент, например, airflow. 
Самый простой способ запуска - через [docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)  
