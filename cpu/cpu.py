import random
import psutil
import threading
import time
from flask import Flask, render_template
from turbo_flask import Turbo

app = Flask(__name__)
turbo = Turbo(app)

def get_bar(percent):
    progress = round(percent * 0.1 + 0.5)
    return '|' + '██' * progress + '__' * (10 - progress) + '|'

def get_CPU_report():
    return 'cpu {} {}%'.format(
        get_bar(psutil.cpu_percent(interval=1)),
        psutil.cpu_percent(interval=1)
    )

def get_RAM_report():
    return 'ram {} {}%'.format(
        get_bar(psutil.virtual_memory().percent),
        psutil.virtual_memory().percent
    )

@app.context_processor
def inject_load():
    load = [int(random.random() * 100) / 100 for _ in range(3)]
    return {'cpu': get_CPU_report(), 'ram': get_RAM_report()}

@app.route('/report')
def index():
    return render_template('index.html')

def update_load():
    with app.app_context():
        while True:
            time.sleep(1)
            turbo.push(turbo.replace(render_template('index.html'), 'load'))
            inject_load()

th = threading.Thread(target=update_load)
th.daemon = True
th.start()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port= 5000, debug=True)