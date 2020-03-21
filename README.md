## Covid-19 JSON API

### Install dependencies

```
pipenv install --dev
```

### Run application locally

```
ENVIRONMENT=development FLASK_DEBUG=true FLASK_APP=src/app pipenv run flask run
```

### Test application

```
PYTHONPATH=src ENVIRONMENT=test pipenv run mamba src/tests
```
