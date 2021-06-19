from flask import render_template, session, url_for, request, g, jsonify
from app import app
from datetime import datetime
from app import app, db, lm, oid
#from .forms import LoginForm, EditForm
from .models import Task


@app.route('/')
@app.route('/index')
def index():
	activities  = Task.query.all()
	count 		= Task.query.count()
	return render_template('index.html', activities=activities, count=count)

@app.route('/activity')
def activity():
	count = Task.query.count()
	return render_template('activity.html', count=count)

@app.route('/add')
def add():
	act = request.args.get('activity', 0, type=str)
	dat = request.args.get('date', 0, type=str)
	if act != '' and dat != '':
		task = Task(activity=act, date=dat)
		db.session.add(task)
		db.session.commit()
		return jsonify(result='Activity added successfully!')
	else:
		return jsonify(result='All fields are required!')

@app.route('/view/<id>')
def view(id):
	count = Task.query.count()
	return True

@app.route('/editpage/<id>')
def editpage(id):
	task  = Task.query.get(id)
	count = Task.query.count()
	return render_template('edit.html', task=task, id=id, count=count)

@app.route('/edittask')
def edittask():
	act = request.args.get('activity', 0, type=str)
	dat = request.args.get('date', 0, type=str)
	key = request.args.get('id', 0, type=str)
	if act != '' and dat != '':
		details          = Task.query.get(key)
		details.activity = act
		details.date     = dat
		db.session.add(details)
		db.session.commit()
		return jsonify(result='Activity edited successfully!')
	else:
		return jsonify(result='All fields are required!')

@app.route('/delete/<id>')
def delete(id):
	task = Task.query.get(id)
	db.session.delete(task)
	db.session.commit()

	activities  = Task.query.all()
	count 		= Task.query.count()
	return render_template('index.html', activities=activities, count=count)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500