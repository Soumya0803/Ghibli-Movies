# Ghibli-Movies
- Create a virtual environment

`python3 -m venv ghibli`  

- Activate the virtual environment 

`source ghibli/bin/activate`

- Installation

`git clone git@github.com:Soumya0803/Ghibli-Movies.git`

`cd Ghibli-Movies`

- Install dependencies:

`pip install -r requirements.txt`

- Apply migrations:

`python manage.py migrate`

- Run the development server:

`python manage.py runserver`

- Movies API endpoint: http://127.0.0.1:8000/movies


- Install httpie
https://httpie.io/docs/cli/universal

- Get ghiblikey for authentication

`http post http://127.0.0.1:8000/api-token-auth/ username=test password=test`                       

- Get movies list with authors:

`http http://127.0.0.1:8000/movie/ 'Authorization: ghiblikey GHIBLI_KEY'`

- Run tests

`python manage.py test movies.tests`
