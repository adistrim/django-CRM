# Django-CRM
Django-CRM is a basic customer relationship management (CRM) project built using Django framework. It provides a simple interface for managing customer records and interactions.

## Features
- MySQL Database: Django-CRM uses a MySQL database to store customer data.
- Bootstrap UI: The user interface is designed using Bootstrap framework, providing a clean and responsive layout.
- Multi-user Login: Supports multiple user accounts with different levels of access.
- Record Management: Users can create, update, and delete customer records.
- Admin Interface: Django admin is also available for managing records and user accounts.
- Environment Variables: Database credentials are stored securely in a .env file.

## Getting Started

1. Install dependencies:
```pip install -r requirements.txt```

2. Create a .env file in the root directory:

```
# .env
DB_NAME=your_dbname
DB_USER=your_mysql_username
DB_PASSWORD=your_password
DB_HOST=localhost
```

3. Apply database migrations:
```python manage.py migrate```

4. Create a superuser: 
```python manage.py createsuperuser```

5. Run the mydb.py file: 
```python mydb.py```

6. Run the dev server:
```python manage.py runserver```

## License
This project is licensed under the MIT License - see the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) file for details.