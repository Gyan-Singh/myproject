 echo "BUILD START"
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 python3.9 manage.py makemigrations
 python3.9 manage.py migrate
 vim var/task/django/db/backends/sqlite3/base.py
 # from sqlite3 import dbapi2 as Database # annotation
 from pysqlite3 import dbapi2 as Database # import pysqlite3
 echo "BUILD END"