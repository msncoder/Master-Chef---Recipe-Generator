 echo "BUILD START"
 python3.13.1 -m pip install -r requirements.txt
 python3.13.1 manage.py collectstatic --noinput --clear
 echo "BUILD END"