# Djongo Based REST Api Development for Ayucare Management.

<img src="https://img.shields.io/github/issues/SubramanyaKS/AyuCareManagement"/>
<img src="https://img.shields.io/github/forks/SubramanyaKS/AyuCareManagement?color=yellow&logoColor=black"/>

![GitHub language count](https://img.shields.io/github/languages/count/SubramanyaKS/AyuCareManagement?style=for-the-badge)

### Django
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It is free and open source, has a thriving and active community, great documentation, and many options for free and paid-for support.

### Djongo
Djongo is a SQL to mongodb query transpiler. It translates a SQL query string into a mongoDB query document. As a result, all Django features, models etc work as is

### REST API
A REST API (also known as RESTful API) is an application programming interface (API or web API) that conforms to the constraints of REST architectural style and allows for interaction with RESTful web services. REST stands for representational state transfer and was created by computer scientist Roy Fielding<br><br>
<b>Ayucare Management:</b> This is management system where we can get the details of products from Ayucare.and sell the products.<br><br>

---

### Technologies used.<br><br>
* Framework :  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
* Database : 	![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
* Programming language: ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* Hosted/ Deployed : ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
<br>
<b>This is the project is done for my internship at <a href="https://www.ekathvainnovations.com">Ekathva Innovation Pvt.Ltd.</a></b><br>
<br>

#### Project is hosted on the heroku app. Click the [Link](https://ayucare.herokuapp.com/) to view.
---

### Project Structure.
```
📦 
├─ .gitignore
├─ Ayucare
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-38.pyc
│  │  ├─ settings.cpython-38.pyc
│  │  ├─ urls.cpython-38.pyc
│  │  └─ wsgi.cpython-38.pyc
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ AyucareApp
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-38.pyc
│  │  ├─ admin.cpython-38.pyc
│  │  ├─ apps.cpython-38.pyc
│  │  ├─ models.cpython-38.pyc
│  │  ├─ serializers.cpython-38.pyc
│  │  └─ views.cpython-38.pyc
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_auto_20210926_1136.py
│  │  ├─ 0003_auto_20210926_1145.py
│  │  ├─ 0004_purchased_user.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ 0001_initial.cpython-38.pyc
│  │     ├─ 0002_auto_20210926_1136.cpython-38.pyc
│  │     ├─ 0003_auto_20210926_1145.cpython-38.pyc
│  │     ├─ 0004_purchased_user.cpython-38.pyc
│  │     └─ __init__.cpython-38.pyc
│  ├─ models.py
│  ├─ serializers.py
│  ├─ static
│  │  └─ site.css
│  ├─ templates
│  │  ├─ home.html
│  │  └─ layout.html
│  ├─ tests.py
│  └─ views.py
├─ README.md
├─ db.sqlite3
├─ manage.py
└─ requirements.txt
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

---

### Prerequisite.

1. Python
2. Git

### How to install and run the Application.

1. Install Python from the [python website](https://www.python.org/).

2. Install Virtual environment globally
```
$ pip install virtualenv
```

3. To Get Started, Fork the repository to your github account:

4. Clone this repository:
```
git clone https://github.com/SubramanyaKS/AyuCareManagement.git
```

5. Then install python django and all requirements:
```
pip install -r requirements.txt
```

6. Create the DB tables first, connect to it and migrate:
```
python manage.py makemigrations
python manage.py migrate
```
7. Create a Super User:
```
python manage.py createsuperuser 
```
8. Run the development web server:
```
python manage.py runserver
```
Open the URL http://localhost:8080/ to access the application.

---
### API Endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | `/users` | To get the user list |
| POST | `/users` | To post/add the user data |
| DELETE | `/users/:userid` | to delete the record of particular user id |
| PUT | `/users/:userid` | To update the record of particular user id |
| GET | `/ayucare` | To get the ayucare product list |
| POST | `/ayucare` | To post/add the ayucare product data |
| DELETE | `/ayucare/:ayucareid` | to delete the record of particular ayucare product id |
| PUT | `/ayucare/:ayucareid` | To update the record of particular ayucare product id |
| GET | `/purchased` | To get the ayucare purchased list |
| POST | `/purchased` | To post/add the ayucare purchased  data |
| DELETE | `/purchased/:purchasedid` | to delete the record of particular ayucare product purchased  id |
| PUT | `/purchased/:purchasedid` | To update the record of particular ayucare product purchased id |




---
If you like the work 🌟 the repository.

Thank you
with ❤ Subramanya KS
