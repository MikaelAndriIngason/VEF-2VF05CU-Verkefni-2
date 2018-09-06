#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import run, route, static_file, error, request, default_app, get, response

bottle.debug(True)

@route('/')
def index():
    return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Hello world!</title>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="static/styles.css">
                </head>
                <body>
                    <h1>Halló heimur</h1>
                    <a href="/forum/wiki?page=1"><img src="static/img1.png" alt="Bottle logo"></a>
                    <a href="/forum/wiki?page=2"><img src="static/img3.jpeg" alt="Bottle logo"></a>
                    <a href="/forum/wiki?page=3"><img src="static/img2.jpeg" alt="Bottle logo"></a>
                </body>
            </html>
            '''

@route('/forum/<subforum>')
def display_forum(subforum="wiki"):
    forum_page = request.query.page
    return "Forum, ", subforum, ", page ", forum_page

@route('/static/<skra>')
def static_skrar(skra):
    return static_file(skra, root='./public/')

@error(404)
def error404(error):
    return '''
            <link rel="stylesheet" href="static/styles.css">
            <img src="static/img4.jpg" alt="Bottle logo" class="error">
            <h3>Nothing here, sorry</h3>
    '''

bottle.run(host='0.0.0.0', port=argv[1])
