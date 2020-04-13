


from flask import render_template
from application import app
import request


@app.route('/')
def home():
    return render_template('home.html', title='Home')
@app.route('/get/animal', methods=['get', 'post'])
def animal():
    animal=requests.get('http://spplication2:5001/animal/name')
    noise=requests.post('http://application2:5001/animal/noise', data=animal.text)
    return render_template('animal.html', title='animal', animal=animal.text, noise=noise.text)
    
    



