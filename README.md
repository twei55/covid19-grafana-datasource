![](https://travis-ci.com/twei55/covid19-grafana-datasource.svg?branch=master)

## Covid-19 JSON API

Visualize Covid-19 data in [Grafana](https://grafana.com/grafana/) using the [JSON Datasource plugin](https://grafana.com/grafana/plugins/simpod-json-datasource).

### API Endpoint

This API is running at [https://covid19-grafana.herokuapp.com/](https://covid19-grafana.herokuapp.com/). Just add the API Endpoint to the URL field of your datasource to visualize the data in Grafana.

### Data

The API endpoint uses data provided by [https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19) and transformed to JSON by [https://github.com/pomber/covid19](https://github.com/pomber/covid19).

### Develop and run locally

#### Install dependencies

```
pipenv install --dev
```

#### Run application

```
ENVIRONMENT=development FLASK_DEBUG=true FLASK_APP=src/app pipenv run flask run
```

#### Test application

```
PYTHONPATH=src ENVIRONMENT=test pipenv run mamba src/tests
```
