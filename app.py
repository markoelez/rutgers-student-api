import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return 'nothing to see here'

@app.route('/name', methods=['GET'])
def get_name():
    res, _ = login(request.headers['username'], request.headers['password'])
    soup = BeautifulSoup(res.text, 'lxml')
    tags = soup.find_all('b', class_='name')
    return tags[0].string


@app.route('/login', methods=['POST'])
def authenticate():
    res, cookies = login(request.headers['username'], request.headers['password'])
    if 'CASTGC' in cookies.keys():
        return 'Login Successful'
    else:
        return 'Login Failed'

def login(user, pw):
    session = requests.session()
    base_url = 'https://cas.rutgers.edu/login?'
    params = {'service': 'https://my.rutgers.edu/portal/Login'}
    login = session.get(base_url, params=params)
    login_html = BeautifulSoup(login.text, 'lxml')
    hidden_elements = login_html.find_all('input', type='hidden')
    form = {tag['name']: tag['value'] for tag in hidden_elements}
    form['username'] = user
    form['password'] = pw
    res = session.post(base_url, data=form, params=params)
    cookies = session.cookies.get_dict()
    return (res, cookies)
