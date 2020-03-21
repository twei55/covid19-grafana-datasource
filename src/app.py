from flask import Flask, jsonify, request, Response
from datasource.covid19 import Covid19

app = Flask(__name__)

# should return 200 ok. Used for "Test connection" on the datasource config page.
@app.route('/', methods=['GET'])
def index():
    return Response(status=200)

# Used by the find metric options on the query tab in panels
@app.route('/search', methods=['GET'])
def search():
    covid19 = Covid19()
    return jsonify(covid19.metrics())

# Return metrics based on input
#
# Example timeserie request
# {
#   "panelId": 1,
#   "range": {
#     "from": "2016-10-31T06:33:44.866Z",
#     "to": "2016-10-31T12:33:44.866Z",
#     "raw": {
#       "from": "now-6h",
#       "to": "now"
#     }
#   },
#   "rangeRaw": {
#     "from": "now-6h",
#     "to": "now"
#   },
#   "interval": "30s",
#   "intervalMs": 30000,
#   "targets": [
#      { "target": "upper_50", "refId": "A", "type": "timeserie" },
#      { "target": "upper_75", "refId": "B", "type": "timeserie" }
#   ],
#   "adhocFilters": [{
#     "key": "City",
#     "operator": "=",
#     "value": "Berlin"
#   }],
#   "format": "json",
#   "maxDataPoints": 550
# }
@app.route('/query', methods=['POST'])
def query():
    covid19 = Covid19()
    series = []
    from_date = request.json["range"]["from"]
    to_date = request.json["range"]["to"]
    for target in request.json["targets"]:
        series.append({
            "target": target,
            "datapoints": covid19.timeseries(target["target"], from_date, to_date)
        })
    return jsonify(series)

# Returns annotations
@app.route('/annotations')
def annotations():
    return True
