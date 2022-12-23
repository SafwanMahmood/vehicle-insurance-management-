# vehicle-insurance-management-
A vehicle management system that predicts the risk and allots policy for customer.


I suggest to create a virtual environment for this.

To run:
```
pip install -r requirements.txt
```

Start the mysql server in a separate tab:
```
mysql -u root
```

Run database migrations:
```
python3 manage.py makemigrations risk_app

python3 manage.py migrate  
```

Then start the Django server:
```
python3 manage.py runserver
```

Go to:
 ```
 http://127.0.0.1:8000/
 ``` 

 You can check database and tables at:
 ```
 http://127.0.0.1:8000/admin/
 ```
 use credentials:
 ```
 user: admin  password:admin123
 ``` 



