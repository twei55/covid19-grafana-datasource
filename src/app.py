from flask import Flask, jsonify, render_template, request
from datasource.covid19 import Covid19

app = Flask(__name__)

# Returns 200 ok. Used for "Test connection" on the datasource config page.
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Used by the find metric options on the query tab in panels
@app.route('/search', methods=['GET', 'POST'])
def search():
    covid19 = Covid19()
    return jsonify(covid19.metrics())

# Return metrics based on input
@app.route('/query', methods=['POST'])
def query():
    covid19 = Covid19()
    series = []
    from_date = request.json["range"]["from"]
    to_date = request.json["range"]["to"]
    for target in request.json["targets"]:
        series.append({
            "target": target["target"],
            "datapoints": covid19.timeseries(target["target"], from_date, to_date)
        })
    return jsonify(series)

# Returns annotations
@app.route('/annotations')
def annotations():
    return jsonify([])
