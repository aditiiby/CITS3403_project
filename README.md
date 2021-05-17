# Elements Lab!

A web flask app with lessons and quizzes helping people learn about the basic elements of a periodic table.

## Sections
[Project Overview](#project-overview)
[To get started](#to-get-started)

## Project Overview 
The aim of this project is to create a web app where people can learn about the basic elements in a periodic table. Users have lessons on six main elements which all have a quiz at then end of the lesson. The progress is tracked by users completing their quizzes. 

### As outlined by the project guidelines we have included these features: 
* A main webpage explaining the theme of the website
* A signup/signin feature for new and returning users
* A few pages on the lessons regarding the elements 
* Quizzes on each of the lesson pages with 3 multiple choice questions each 
* A profile page with feedback and results 
* An about page with authors information.
* A progress bar to track all aggregate results of all quizzes. 


## To get started

Activate the python virtual environment:
`$source virtual-environment/bin/activate`

To run the app:
`$flask run`

To stop the app:
`$^C`

To exit the environment:
`$deactivate`

### Prerequisites

Requires python3, flask, venv, and sqlite

Also requires: 

appdirs==1.4.4
asgiref==3.3.4
click==8.0.0
distlib==0.3.1
Django==3.2.3
dominate==2.6.0
filelock==3.0.12
Flask==2.0.0
Flask-Bootstrap==3.3.7.1
Flask-WTF==0.14.3
itsdangerous==2.0.0
Jinja2==3.0.0
MarkupSafe==2.0.0
pytz==2021.1
six==1.16.0
sqlparse==0.4.1
virtualenv==20.4.6
visitor==0.1.3
Werkzeug==2.0.0
WTForms==2.3.3


### Installing

Install python3, sqlite3

1. Set up a virtual environment:
 - use pip or another package manager to install virtualenv package `pip install virtualenv`
 - start the provided virtual environment
   `source virtual-environment/bin/activate`
 - This should include flask and all the required packages
2. Install sqlite
 - [Windows instructions](http://www.sqlitetutorial.net/download-install-sqlite/)
 - In \*nix, `sudo apt-get install sqlite`
3. Build the database: `flask db init`
4. `flask run`

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000/index](http://localhost:5000/index)

## Running the tests

We have implemented unit tests with test.py
* Tests whether database stored the correct information
* If results stored in database changed 
* If its updated the changes will be recorded

To run unit tests
`python3 test.py`

## Deployment

via localhost

## Built With

Visual Studio Code and git

## Development: 

The project was done using agile methodology whereby we managed to split the project in different phases. 
We cycled through planning, executing, and evaluating.
Continously going back and forth to make sure each component worked.
We split each part of the project to different people, worked on it independently and came back to collaborate and evaluate our work. 
We met face to face for many sessions as well as contacted each other through facebook messenger and git. 


## Authors

* **Victor Wojcieski** - [vwojcieski](https://github.com/vwojcieski) 22987825
* **Joshua Symons** - [jws1998](https://github.com/jws1998) 22996948
* **Aditi Malu** - [aditiiby](https://github.com/aditiiby) 22526301


## References:

Periodic Table. (2020, June 15). In _GitHub_ https://github.com/project-gemmi/periodic-table/blob/master/index.html

Clip Art: Elements: Oxygen B&W. (n.d.). _Oxygen_[Photograph]. abcteach. https://www.abcteach.com/documents/clip-art-elements-oxygen-bw-i-abcteachcom-42742

Clip Art: Elements: Carbon B&W. (n.d.). _Carbon_[Photograph]. abcteach. https://www.abcteach.com/documents/clip-art-elements-carbon-bw-i-abcteachcom-42735 

Clip Art: Elements: Hydrogen B&W. (n.d.). _Hydrogen_[Photograph]. abcteach. https://www.abcteach.com/documents/clip-art-elements-hydrogen-bw-i-abcteachcom-42738

Clip Art: Elements: Helium B&W. (n.d.). _Helium_[Photograph]. abcteach. https://www.abcteach.com/documents/clip-art-elements-helium-bw-i-abcteachcom-42737

Clip Art: Elements: Iron B&W. (n.d.). _Iron_[Photograph]. abcteach. https://www.abcteach.com/documents/clip-art-elements-iron-bw-i-abcteachcom-42863

Clip Art: Elements: Nitrogen B&W. (n.d.). _Nitrogen_[Photograph]. abcteach. https://www.abcteach.com/documents/clip-art-elements-nitrogen-bw-i-abcteachcom-42741

Bootstrap (n.d.). In _Bootstrap_. https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"

jQuery Library (n.d.). In _jQuery_ https://code.jquery.com/jquery-1.10.2.js

HTML (n.d.). In _Html_ https://www.w3schools.com/

FLASK (n.d.).https://prettyprinted.com/flasksql

