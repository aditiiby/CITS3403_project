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
* Quizzes on each of the lesson pages 
* A profile page with feedback and results
* An about page with authors information.


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

```
Give examples
```

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

A few tests now:

To run unit tests
`python -m tests.unittest`

To run selenium tests, make sure that you have the 
appropriate web driver installed. In this case it should be geckodriver for Firefox, 
and it assumes that it is installed in the test directory.
Then start the webserver in TestingConfig, and run
`python -m tests.systemtest`

## Deployment

via localhost

## Built With

Visual Studio Code and git


## Authors

* **Victor Woj** - [vwojcieski](https://github.com/vwojcieski)
* **Joshua Symons** - [jws1998](https://github.com/jws1998)
* **Aditi Malu** - [aditiiby](https://github.com/aditiiby)


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

https://www.w3schools.com/
https://prettyprinted.com/flasksql
https://getbootstrap.com/
https://www.youtube.com/watch?v=At4B7A4GOPg&t=638s&ab_channel=WebDevSimplified