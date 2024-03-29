# project_3 file

import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./my_movies.db' # TODO: MYMOVIES AS DB NAME
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


#########
######### Everything above this line is important/useful setup, not problem-solving.
#########


##### Set up Models #####

# Set up association Table between artists and albums
collections = db.Table('collections',db.Column('rating_id',db.Integer, db.ForeignKey('ratings.id')),db.Column('director_id',db.Integer, db.ForeignKey('directors.id')))

class Ratings(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.String(64))
    directors = db.relationship('Director',secondary=collections,backref=db.backref('ratings',lazy='dynamic'),lazy='dynamic')
    movies = db.relationship('Movie',backref='Rating')


class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Director')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64),unique=True) # Only unique title songs can exist in this data model
    rating_id = db.Column(db.Integer, db.ForeignKey("ratings.id")) #ok to be null for now
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id")) # ok to be null for now
    genre = db.Column(db.String(64)) # ok to be null
    # keeping genre as atomic element here even though in a more complex database it could be its own table and be referenced here

    def __repr__(self):
        return "{} by {} | {}".format(self.title,self.director_id, self.genre)




##### Helper functions #####

### For database additions
### Relying on global session variable above existing

def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director

def get_or_create_rating(rating_score):
    rating = Ratings.query.filter_by(score=rating_score).first()
    if rating:
        return rating
    else:
        rating = Ratings(score=rating_score)
        session.add(rating)
        session.commit()
        return rating



##### Set up Controllers (route functions) #####

## Main route
@app.route('/')
def index():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('index.html', num_movies=num_movies)

@app.route('/movie/new/<title>/<director>/<genre>/<rating>')
def new_movie(title, director, genre, rating):
    if Movie.query.filter_by(title=title).first(): # if there is a song by that title
        return "That film already exists! Go back to the main app!"
    else:
        director = get_or_create_director(director)
        rating = get_or_create_rating(rating)
        movie = Movie(title=title, director_id=director.id,genre=genre, rating_id=rating.id)
        session.add(movie)
        session.commit()
        return "New movie: {} directed by {} is of the {} genre. You rated this as: {} Check out the URL for ALL movies to see the whole list.".format(movie.title, director.name, movie.genre, rating.score)

@app.route('/all_movies')
def see_all():
    all_movies = [] # Will be be tuple list of title, genre
    movies = Movie.query.all()
    for m in movies:
        director = Director.query.filter_by(id=m.director_id).first() # get just one artist instance
        all_movies.append((m.title,director.name, m.genre)) # get list of songs with info to easily access [not the only way to do this]
    return render_template('all_movies.html',all_movies=all_movies) # check out template to see what it's doing with what we're sending!

@app.route('/all_directors')
def see_all_directors():
    directors = Director.query.all()
    names = []
    for d in directors:
        num_movies = len(Movie.query.filter_by(director_id=d.id).all())
        newtup = (d.name,num_movies)
        names.append(newtup) # names will be a list of tuples
    return render_template('all_directors.html',director_names=names)


if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver
