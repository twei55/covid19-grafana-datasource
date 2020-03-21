## Covid-19 JSON API

Visualize Covid-19 data in [Grafana](https://grafana.com/grafana/) using a the [JSON Datasource plugin](https://grafana.com/grafana/plugins/simpod-json-datasource).

### API Endpoint

This API is running at [https://covid19-grafana.herokuapp.com/](https://covid19-grafana.herokuapp.com/). Just add the API Endpoint to the URL field of your datasource to visualize the data in Grafana.

### Data

The API endpoint uses data provided by [https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19) and transformed to JSON by [https://pomber.github.io/covid19/timeseries.json](https://github.com/CSSEGISandData/COVID-19).

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
