from app import app
from flask import render_template, redirect, request, url_for, flash
from htmlmin.minify import html_minify
from .findStuff import findStuff

from .forms import CreateBook

@app.route('/', methods=['GET', 'POST'])
def index(): 
  # Do something 
  form = CreateBook()
  if form.validate_on_submit():
    if not(form.vent.data):
      flash("Oh no you didn't fill out the single field :( ")
      return redirect(url_for('index'))
    else: 
      flash(findStuff(form.vent.data))
      return redirect(url_for('index'))
  return html_minify(render_template('index.html', form = form))	
