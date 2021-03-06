# AlcoDB
[![PyTest](https://github.com/ArtemD/flask-demo-2021/actions/workflows/pytest.yml/badge.svg)](https://github.com/ArtemD/flask-demo-2021/actions/workflows/pytest.yml)

Simple project powered by Flask/Python/SQLAlchemy for displaying alchohol licensed locations in Finland. Based on [avoindata.fi](https://www.avoindata.fi/data/fi/dataset/alkoholielinkeinorekisteri/resource/2ce47026-377f-4837-b26f-610626be0ac1) data.

## Installation

Make sure you have Python 3.X installed as well as pipenv. Make sure to create .env file in your project directory (check .env_example for example content).

```bash
  pipenv install
  pipenv shell
  python app.py
```

## Running tests

You can run unit tests found in test_app.py using following commands:

```bash
  pipenv install
  pipenv shell
  pytest
```


## Deployment

Application has support for Heroku deployment (gunicorn).
  
## Authors

- [@artemd](https://www.github.com/artemd)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  