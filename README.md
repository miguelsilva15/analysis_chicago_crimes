# analysis_chicago_crimes

The original dataset is [here](https://we.tl/t-ez8zUugHBQ), this analysis is based on the criminal reports of the city of Chicago in USA.
In the file "CHICAGO_ANALYSIS_MIGUEL_SILVA.ipynb" are the answers to both questions
The main.py file include an API.
The model is uploaded [here](https://we.tl/t-h9ufmHkTUJ) because this normally could have been in an S3 bucket.
The Dockerfile is an attempt to dockerize the API for production use (kubernetes)
There are a lot of things missing, like logs and ETL process, that could not be done because of time constraints.
An example of the JSON for the API is the following:

```
curl --location 'localhost:8008/predict' \
--header 'Content-Type: application/json' \
--data '{
    "Domestic": 0,
    "Beat": 833,
    "Ward": 13,
    "Community_Area": 65,
    "Year": 2023,
    "dow": 1,
    "month": 6,
    "day": 5,
    "season": 2,
    "Location_Description_encoded": 111
}'
```

Miguel
