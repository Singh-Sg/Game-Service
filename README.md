# Game-Service


Getting Started

	To work on the sample code, you'll need to clone project's repository to your local computer. If you haven't, do that first.

	bitbucket repo :

	git clone

	1)Install and Create a Python virtual environment for your Django project. This virtual environment allows you to isolate this project and install any packages you need without affecting the system Python installation. At the terminal, type the following command:

		$ pip install virtualenv
		$ virtualenv venv

	2)Activate the virtual environment:

		$ source venv/bin/activate

	3)Install Python dependencies for this project:

		$ pip install -r requirements.txt

	4)For Database schema:

		$ python manage.py migrate

	5)Create Super User

		$ python manage.py createsupersuer

	6)Start the Django development server:

		$ python manage.py runserver

	7)Running the Tests:

		$ python3 manage.py test

	8)Running Tests Coverage

		* Run `$ cd scheduling-service` command for jump into the project directory
		* Run `$ coverage run --source='.' manage.py test` for run test cases with coverage
		* Run `$ coverage html`  to see the result.
		* Run `$ coverage report`  to see the report in HTML format.

