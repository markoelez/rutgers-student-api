### API for querying Rutgers student information

Currently handles only basic authentication to CAS for use in a mobile app but further scraping is simple and more features will be added later.

# API Reference:

| URL | Method | Description | Parameters |
|:-------------------------------:|:------:|:---------------------------------------:|:-----------------------------------:|
| /login | POST | Login to Rutgers CAS | netid & password |
| /name \ GET | Returns student's full name | netid & password |
