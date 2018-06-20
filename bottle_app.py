
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template, post, request, get

#import sqlite to be able to use for db
import sqlite3

#establish a connection with db
db = sqlite3.connect('/home/P10er101/mysite/views/admeon/admeonsql.db')
c = db.cursor()



@route('/')
def dsiplayCurrentpage():
    #Display the Search and Book page when website is loaded
    return template("admeon/newUser.html", db = db, c = c)

@post('/searchAndBook')
def dsiplaySearchAndBookPost():
    #Display the Search and Book page when website is loaded
    return template("admeon/searchAndBook.html", db = db, c = c)

@get('/login')
def displayLogin():
    #Display the login form
    return template("admeon/login.html")


@get('/newUser')
def displayLogin():
    #Display the newUser form
    return template("admeon/newUser.html")


application = default_app()

