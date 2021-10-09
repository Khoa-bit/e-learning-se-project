# e-learning-se-project

Admin login: admin@admin.com pass: admin

To sync database when you clone the project onto your remote, follow this steps:
1. Run the command python manage.py flush and choose y.

2. Run the command python manage.py loaddata (file_name) for all these files in the order given below (can be run in one command line):

user_data.json 

lecturer_data.json 

major_data.json 

schedule_data.json 

course_data.json 

class_data.json 

student_data.json

------------------------
After this step is finished, run this command python manage.py runserver.

Access the URL localhost:8000/admin.

Log in using the admin log in info given above.

Choose your account in Users directory and change your password.

--------------------------------
Go to the URL localhost:8000/login and log into your account using the given email and the password you've just set.

