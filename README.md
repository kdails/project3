# projectt3

<h1>Hello. Thanks for reading !</h1>

<h2>This project for SI507 requires that you have python 3.7, a python framework called Flask that provides opportunity to interact with our python code in browser. In order for this project to work properly, please refer to the required list of dependencies in requirements.txt and pip-install all dependencies to a virtual environment within the project folder for this application to run.</h2>

<h4>The csv file you'll need is provided with in this repository as well as all other code. There are two different types of files in this program, the SI507_project3.py code where a SQL database is created with SQLAlchemy, and 3 tables are additionally created for Movies, Directors and Ratings. </h3>

<h4>The Flask application is additionally defined within the Project 3 code. The Flask app puts information into the database that is created. a database will be created within the project folder when the project_3 code is run locally on your computer via the terminal and browser. </h3>

<p>Additionally in this file, you're going to see a database sketch that was required for this assignment. You can see that I created the database based off my drawing from projejct 2, but altered the information so that it wasn't extreneous and is just enough to get the job done. You can see that there are three tables for the data - MOVIES, RATINGS, as well as DIRECTORS. <p>

<p>Unlike in my Project 2 code, you're able to input the movie titles, genre, director, and rating for one specific film within one Flask path like we did previously in the first project to personalize or alter the outcome. The outputs for the paths are based on the code written in the project_3 file. You're able to add as many movies to the database as you want. You'll then be able to see in different tables different informations according to you input like directors, titles of films, and your personal rating. </p>

<h3>In order for this code to run, you must clone my repository to your local machine. Start off and place it right onto your mac desktop.</h3>

- make sure all dependencies are installed within the project folder as a virtual environment. see this for more information on virtual environments and how to create and use one intelligently: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/ 

- Open up your terminal window and type $ cd desktop (navigate to the location).
- Now in the command prompt window, type $ python SI507_project3.py ( this runs the flask application and creates an empty database)
- You should be able to see something going on in your terminal window. (terminal is displaying the URL calls directed to your local host port)
<h3> Flask Path #1 </h3>
- Now, open another tab and go to: http://localhost:5000/ - you'll get a hompage greeting and a count of movies! (Nothing yet in your database, don't worry... let's add some movies!!!
<h3> Flask Path #2 </h3>
<h4> Now alter the URL to write "http://localhost:5000/movie/new/<title>/<director>/<genre>/<rating>" </h4>
    - you're going to input a title of a film where "<title>" is.
    - you're going to input a director of the film where "<director>" is.
    - you're going to input a genre for the film where "<genre>" is.
    - you're going to input your own rating of the film (of type string) where "<rating>" is.
- You should do this more than once so the next paths show more and pull more data from the items you added to your database!
<h3> Flask Path #3 </h3>
- Now if you alter the URL to write http://localhost:5000/all_movies you'll see all the films you inputted in the last step! If you added none of them, It will tell you that too. 

<h3> Flask Path #4 </h3>
- Now if you alter the URL to write http://localhost:5000/all_directors you'lll see all the film directors and their movie count! If you haven't added anything yet, it will let you know! 

