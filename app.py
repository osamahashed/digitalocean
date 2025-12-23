#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DigitalOcean Practical Research Web Application
Title: Practical Research on DigitalOcean Platform
Author: Osama Hashed
Description:
A professional academic web application presenting a practical research
about DigitalOcean and its usage with AI Agents.
"""

from flask import Flask, render_template

app = Flask(__name__)

# Configuration
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    """
    Main page – research content
    """
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors
    """
    return render_template('500.html'), 500
