from flask import Flask, render_template, jsonify

import datetime, random


# Create the instance of our web application server
app = Flask(__name__)



@app.route('/')
def landing_page():
    ''' Render the index html file to the client '''
    return render_template('index.html')


@app.route('/chart_example_data')
def chart_example_data():
    ''' Return data for a chart as JSON '''

    # You might notice that the measurements and dataPoints variables have the same structure (list of dicts)
    # In this example this is the case
    # However depending on how you query your measurement data they might differer slightly. 
    # So you have to make sure it is in the right format when parsing it to datapoints list.
    # Which is why we recreate the list of data points

    # A list of dicts containing the measurements
    # This is what you should replace by your database query
    # The result of the query should follow the same data format
    measurements = [
        {'x': getDateTime1(), 'y': getRandomDataPoint()},
        {'x': getDateTime2(), 'y': getRandomDataPoint()},
        {'x': getDateTime3(), 'y': getRandomDataPoint()},
        {'x': getDateTime4(), 'y': getRandomDataPoint()}
    ]

    # Create an empty list
    dataPoints = []

    # Loop through all the measurements
    for measurement in measurements:

        # Create an empty dict
        dataPoint = {}

        # Add the x and y values to the datapoint
        dataPoint['x'] = measurement['x']
        dataPoint['y'] = measurement['y']

        # Add the datapoint to datapoints list
        dataPoints.append(dataPoint)

    # Create a list of a dict in the format that Apexcharts expect
    # Name is the name of the data
    # Data are the data points in the graph
    data = [{
        'name': 'testData',
        'data': measurements
        }]

    # Convert the python list to a Response object with the application/json mimetype, so it can be send to the client over HTTP
    jsonData = jsonify(data)

    return jsonData




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

# Get a randomvalue between 1 and 10
def getRandomDataPoint():
    return random.randint(1, 10)



if __name__ == "__main__":
    ''' Start the server '''
    app.run(debug=True)