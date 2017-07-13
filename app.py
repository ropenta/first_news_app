import csv
from flask import Flask 
from flask import render_template
app = Flask(__name__)


def get_csv():
    csv_path = './static/la-riots-deaths.csv'  #path to file
    csv_file = open(csv_path, 'rb')            #open the csv
    csv_obj = csv.DictReader(csv_file)         #parse as dict
    csv_list = list(csv_obj)                   #keeps csv object permanently
    return csv_list


@app.route('/')
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list = object_list)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
