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

1. Install [docker](https://docs.docker.com/install/) on your machine.

2. Create a .env file in the root directory:

```
# .env
DB_NAME=your_dbname
DB_USER=your_mysql_username
DB_PASSWORD=your_password
DB_HOST=localhost
```

3. Build and run the Docker containers. This might take a while.

```
docker compose up --build
```


## License
This project is licensed under the MIT License - see the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) file for details.