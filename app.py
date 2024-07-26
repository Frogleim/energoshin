from flask import Flask, request, render_template, redirect
from flask_babel import Babel, _
import os, requests


app = Flask(__name__)

# Configuration
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

# Supported languages
LANGUAGES = {
    'en': 'English',
    'hy': 'Armenian',
    'ru': 'Russian'

}


def get_locale():
    return request.cookies.get('language') or request.accept_languages.best_match(LANGUAGES.keys())


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/change_language/<language>')
def change_language(language=None):
    print(language)
    response = redirect(request.referrer)
    if language not in LANGUAGES.keys():
        language = 'hy'
    response.set_cookie('language', language)
    return response


def get_ipv4_address():
    try:
        eth0_ip = os.getenv('IP_ETH0')
        print(eth0_ip)
        ip = '192.168.18.110'
        return ip
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    ip = get_ipv4_address()
    app.run(host=ip, debug=True)
