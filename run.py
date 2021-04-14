from flask import Flask, render_template, jsonify

import datetime, random


# Create the instance of our web application
app = Flask(__name__)



@app.route('/')
def landing_page():
    ''' Render the index html file to the client '''
    return render_template('index.html')


@app.route('/chart_example_data')
def chart_example_data():
    ''' Return data for a chart as JSON '''

    # A list of dicts
    measurementsData = [
        {'x': getDateTime1(), 'y': getRandomDataPoint()},
        {'x': getDateTime2(), 'y': getRandomDataPoint()},
        {'x': getDateTime3(), 'y': getRandomDataPoint()},
        {'x': getDateTime4(), 'y': getRandomDataPoint()}
    ]

    measurements = []

    for measurement in measurementsData:
        info = {}
        info['x'] = measurement['x']
        info['y'] = measurement['y']
        measurements.append(info)

    data = [{
        'name': 'testData',
        'data': measurements
        }]

    #print(data)

    return jsonify(data)




# Util functions

# For ApexCharts to understand datetime we need to send it as epochtime.
def getDateTime1():
    return 1327359600000

def getDateTime2():
    return 1327446000000

def getDateTime3():
    return 1327532400000

def getDateTime4():
    return 1327618800000


def getRandomDataPoint():
    return random.randint(1, 10)


if __name__ == "__main__":
    app.run(debug=True)