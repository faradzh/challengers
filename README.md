# CHALLENGERS

## Установить mysql

### Mac OS
  brew install mysql
  
  mysql.server start (это придется делать каждый раз при перезагружке компьютера. Есть возможность сделать автозагрузку сервера, надо погуглить)
  
  
  Создаем базу данных:
  CREATE DATABASE `challengers_db` CHARACTER SET utf8 COLLATE utf8_general_ci;
  
  
## Разворачиваем проект

  git clone git@github.com:faradzh/challengers.git
  
  brew install python3
  
  sudo pip3 install virtualenv
  
  virtualenv -p /usr/bin/python3 venv
  
  source venv/bin/activate
  
  устанавливаем зависимости pip install -r requirements.txt
  
  python manage.py migrate
  
  python manage.py createsuperuser
  
  python manage.py runserver
  

