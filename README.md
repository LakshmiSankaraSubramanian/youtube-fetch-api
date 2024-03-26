# youtube-fetch-api

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

<img width="1124" alt="Screenshot 2024-03-27 at 12 00 01 AM" src="https://github.com/LakshmiSankaraSubramanian/youtube-fetch-api/assets/72433278/30745743-f005-4d63-a74e-160f429c851b">

### API's exposed 
`/videos` - list all the videos stored in the postgres database 

`/search?q=` - search endpoint allows you to fetch all partial or completely matched details based on the query parameter passed


