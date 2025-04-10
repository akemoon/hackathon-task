from flask import Flask, render_template, jsonify, Response
import psutil
import time
import datetime
import threading

def get_bar(percent):
    progress = round(percent * 0.1 + 0.5)
    return '|' + '█' * progress + '_' * (10 - progress) + '|'

def get_CPU_report():
    return 'cpu {} {}%'.format(
        get_bar(psutil.cpu_percent()),
        psutil.cpu_percent()
    )

def get_RAM_report():
    return 'ram {} {}%'.format(
        get_bar(psutil.virtual_memory().percent),
        psutil.virtual_memory().percent
    )

app = Flask(__name__)

@app.route('/report', methods=['GET','POST'])
def report():
    return render_template(
        'index.html', 
        cpu_report= get_CPU_report(), 
        ram_report= get_RAM_report(), 
        date = str(datetime.datetime.now())
    )

if __name__ == '__main__':
    app.run(host='localhost', port= 5000, debug=True)
