# megawatt

1. Create a virtualenv. - `virtualenv -p /usr/bin/python3 megawatt_venv`
2. Install all the required dependencies. `pip install -r requirements.txt`
3. Perform migrate. - `python manage.py migrate`
4. Create super user. - `python manage.py createsuperuser`
5. Log into admin site and add the sites with `A value` and `B value` => `http://127.0.0.1:8000/admin`
6. Now load the page => `http://127.0.0.1:8000/`. This should give desired result.
8. Under summary page,
    if a param called type is added, based on the type, the function to calculate average and sum is done.
    
    Eg : `http://127.0.0.0.1:8000/sites/summary/?type=django` => this will calculate the Sum based on Django's api's 
         `http://127.0.0.0.1:8000/sites/summary/?type=python` => this will calculate the Sum based using built in python functions.
         
 9. Similar thing works for Average as well.
 
 10. You can view this from my personal heroku hosted website : https://shashank-megawatt.herokuapp.com/ (Login credentials in the email)
