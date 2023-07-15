 echo "BUILD START"
 python3.7 -m pip install -r requirements.txt
 python3.7 manage.py collectstatic --noinput --clear
 python3.7 manage.py makemigrations
 python3.7 manage.py migrate
 echo "BUILD END"