# Вопросы по практике на экзамен 

## 1. **Команды для подключения к серверу по SSH, клонирования git-репозитория, создания и активации venv и установки зависимостей:**
  ```bash
  ssh user@host
  git clone https://github.com/username/repository.git
  cd repository
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

## 2. **Скрипт для инициализации git репозитория, добавления всех файлов, коммита и пуша:**
  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  git remote add origin https://github.com/username/repository.git
  git push -u origin master
  ```

## 3. **Структура типового проекта Data Science и README.md:**
  - README.md включает структуру.
  ```markdown
  # Data Science Project

  ## Описание проекта

  Этот проект представляет собой типовой пример проекта Data Science. Он включает в себя все необходимые компоненты для работы с данными, их обработки, моделирования и оценки результатов.

  ## Структура проекта

  `project/`: Корневая папка проекта.
  ├── `data/`: Данные проекта.
  │   ├── `raw/`: Сырые данные, которые были получены из внешних источников и не подвергались никакой обработке.
  │   ├── `processed/`: Обработанные данные, которые были очищены и подготовлены для анализа и моделирования.
  ├── `notebooks/`: Jupyter ноутбуки, используемые для исследования данных, визуализации и разработки моделей.
  ├── `src/`: Исходный код проекта, включая скрипты для обработки данных, обучения моделей и их оценки.
  ├── `models/`: Сохраненные модели машинного обучения, которые были обучены на данных.
  ├── `reports/`: Отчеты и визуализации, созданные в ходе анализа данных и оценки моделей.
  ├── `README.md`: Описание проекта, его структуры и инструкции по использованию.
  ├── `requirements.txt`: Файл с зависимостями проекта, необходимыми для его работы.
  ├── `.gitignore`: Файл, содержащий список файлов и папок, которые должны быть проигнорированы системой контроля версий Git.
  ├── `LICENSE`: Файл с лицензией проекта.

  ## Установка и настройка

  1. Клонируйте репозиторий
  2. Создайте и активируйте виртуальное окружение
  3. Установите зависимости

  ## Использование

  ### Предобработка данных
  
  Для предобработки данных используйте скрипт preprocess.py:
  
  ### Обучение модели

  Для обучения модели используйте скрипт train.py

  ### Оценка модели

  Для оценки модели используйте скрипт evaluate.py

  ## Вклад
  
  Если вы хотите внести свой вклад в проект, пожалуйста, создайте pull request или откройте issue для обсуждения изменений.
  
  ## Лицензия
  
  Этот проект лицензирован. Подробности см. в файле LICENSE.
  ```

## 4. **Фреймворк Flask:**
  - Flask — это микрофреймворк для создания веб-приложений на Python.
  ```python
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def hello_world():
     return 'Hello, World!'

  if __name__ == '__main__':
     app.run()
  ```

## 5. **Расширения Flask-CORS и Flask-HTTPAuth:**
  - Flask-CORS: Управление CORS (Cross-Origin Resource Sharing).
  ```python
  from flask import Flask
  from flask_cors import CORS

  app = Flask(__name__)
  CORS(app)
  ```

  - Flask-HTTPAuth: HTTP аутентификация.
  ```python
  from flask import Flask
  from flask_httpauth import HTTPBasicAuth

  app = Flask(__name__)
  auth = HTTPBasicAuth()

  @auth.verify_password
  def verify_password(username, password):
    if username == 'admin' and password == 'secret':
        return True
    return False

  @app.route('/')
  @auth.login_required
  def index():
    return "Hello, {}!".format(auth.username())

  if __name__ == '__main__':
    app.run()
  ```

## 6. **Библиотека Boto3:**
  - Boto3 — это библиотека для взаимодействия с AWS сервисами.
  ```python
  import boto3

  s3 = boto3.client('s3')
  s3.upload_file('local_file.txt', 'bucket_name', 's3_file.txt')
  ```

## 7. **Библиотека python-dotenv:**
  - Python-dotenv используется для загрузки переменных окружения из файла `.env`.
  ```python
  from dotenv import load_dotenv
  import os

  load_dotenv()
  secret_key = os.getenv('SECRET_KEY')
  ```

## 8. **Фреймворк DVC:**
  - DVC (Data Version Control) используется для управления версиями данных и моделей.
  ```bash
  dvc init
  dvc add data/raw/dataset.csv
  dvc remote add -d myremote s3://mybucket/path
  dvc push
  ```

## 9. **Сервер Gunicorn:**
  - Gunicorn — это WSGI HTTP сервер для Python веб-приложений.
  ```bash
  gunicorn --workers 2 --threads 2 --preload app:app
  ```

## 10. **Скрипт предварительной обработки CSV файла:**
   ```python
   import pandas as pd

   df = pd.read_csv(args.input_file)
   df_filtered = df[df['X'] > 0]
   df_filtered.to_csv(args.output_file, index=False)
   ```

## 11. **Скрипт обучения модели линейной регрессии:**
   ```python
   import pandas as pd
   from sklearn.linear_model import LinearRegression

   df = pd.read_csv(args.input_file)
   X = df[['X']]
   y = df['Y']

   model = LinearRegression()
   model.fit(X, y)
   ```

## 12. **Скрипт тестирования модели линейной регрессии:**
   ```python
   import pandas as pd
   from sklearn.metrics import mean_squared_error

   df = pd.read_csv(args.data_file)
   X = df[['X']]
   y = df['Y']

   model = joblib.load(args.model_file)
   predictions = model.predict(X)
   mse = mean_squared_error(y, predictions)
   ```

## 13. **Пайплайн DVC:**
   ```yaml
   stages:
    preprocess:
      cmd: python preprocess.py data/raw/dataset.csv data/processed/dataset.csv
      deps:
       - preprocess.py
       - data/raw/dataset.csv
      outs:
       - data/processed/dataset.csv
    train:
      cmd: python train.py data/processed/dataset.csv model.pkl
      deps:
       - train.py
       - data/processed/dataset.csv
      outs:
       - model.pkl
    evaluate:
      cmd: python evaluate.py data/processed/dataset.csv model.pkl report.txt
      deps:
       - evaluate.py
       - data/processed/dataset.csv
       - model.pkl
      outs:
       - report.txt
   ```

## 14. **Dockerfile для предиктивного сервиса:**
   ```dockerfile
   # Используем официальный образ Python
   FROM python:3.9-slim

   # Устанавливаем рабочую директорию
   WORKDIR /app

   # Копируем файлы проекта в контейнер
   COPY . /app

   # Устанавливаем зависимости
   RUN pip install --no-cache-dir -r requirements.txt

   # Открываем порт для приложения
   EXPOSE 5000

   # Команда для запуска приложения
   CMD ["gunicorn", "--workers", "2", "--threads", "2", "--preload", "app:app"]
   ```

