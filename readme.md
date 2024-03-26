### Pre-Requisites

- **Python**: Ensure you have Python installed on your system. You can download it from the official Python website.
- **YouTube Data API**: You'll need to set up a project in the Google Developers Console and enable the YouTube Data API v3. Obtain an API key for making requests to the API.

### Set Up Your Development Environment with docker
- Use docker commands to set the required database and packages for the changes 
```
docker build -t youtube-project .
docker run -p 8000:8000 my-django-app
docker-compose run web python manage.py migrate
docker-compose up
```

### Set Up Your Development Environment without docker
- Install all the packages in requirement.txt using `pip install`
- Install postgres and add it's credentials in settings.py
- Use `python manage.py migrate` to apply migration to your database.
- Use `python manage.py runserver` to start the django server

### Technical flow
![Alt text](image.png)


### API's exposed 
`/videos` - list all the videos stored in the postgres database 
`/search?q=` - search endpoint allows you to fetch all partial or completely matched details based on the query parameter passed


