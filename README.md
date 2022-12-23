# vehicle-insurance-management-
A vehicle management system that predicts the risk and allots policy for customer.

Clone the repo and follow the instructions.

I suggest to create a virtual environment for this.

Use the below command to create venv :
```conda activate --name venv-name```

To start the env :
```conda activate env-name```

To run:
```
pip install -r requirements.txt
```

Start the mysql server in a separate tab:
```
mysql -u root
```

Create DB as:
```
create schema insurance_db;
use insurance_db;
```


Django Server part:

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



