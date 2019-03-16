# projectt3

<h1>Hello. Thanks for reading !</h1>

<h2>This project for SI507 requires that you have python 3.7, a python framework called Flask that provides opportunity to interact with our python code in browser. In order for this project to work properly, please refer to the required list of dependencies in requirements.txt</h2>

<h4>The csv file you'll need is provided with in this repository as well as all other code. The movies_tools code essentially sets us up for success with the app that we wrote funtionality for in it's code like instances of the movies class and defining movie titles, movie title numbers as well as the rankings per movie with variables. </h3>

<h4>The Project 2 code is where the Flask app is defined. The Flask app takes the information that is built and coded into movies_tools to get an output when it's run locally on your computer via the terminal and browser. </h3>

<p>Additionally in this file, you're going to see a database sketch that was required for this assignment. You can see that I created the database based on the cleaned CSV data provided, there are three tables for the data - MOVIES, FISCAL(for money, and earnings data), as well as PERCEPTION (ratings by companies like IMDB, or Rotten Tomatoes). <p>

<p>Unlike in project 1, this code is completely defined within the file. You cannot input other attributes to the Flask path like we did previously to personalize or alter the outcome. The outputs for the paths are based on the CSV file and the structured items inside of it. </p>

<h3>In order for this code to run, you must clone my repository to your local machine, Start off and place it right onto your mac desktop.</h3>

- Open up your terminal window and type $ cd desktop (navigate to the location).
- Now in the command prompt window, type $ python SI507_project2.py ( this runs the flask application)
- You should be able to see something going on in your terminal window. (terminal is displaying the URL calls directed to your local host port)
- Now, open another tab and go to: http://localhost:5000/ - you'll get a hompage greeting and a count of movies!
- Now alter the URL to write http://localhost:5000/movies/ratings - you'll recieve a set list of 5 movie titles and their corresponding movie ratings that can be found in the CSV data.
