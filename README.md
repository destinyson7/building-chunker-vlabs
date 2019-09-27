
## Project Title

Building Chunker Experiment

## Installing and Prerequisites

```bash
sudo apt-get update
sudo apt-get install python3.6
sudo apt install python3-pip
pip3 install Flask
pip3 install flask_sqlalchemy
pip3 install Markups
pip3 install requests
```

## Running the Experiment

Step1 - -> Run the run.py file using command: -
```python
    $ python3 run.py
```

Step2 - -> Open the browser and open the following link

    "localhost:5000/"


## Testings

Step1 - -> Run the Experiment.
(Testing is to be done on a new terminal)

Testing is done as follows: -
Test for all the links to pages. Ensure that server is running before running the tests.
Run the unitTests.py file using command
```python
    $ python3 unitTests.py
```

## Folder Structure

├── building-chunker
│   ├── Documentation.py
│   ├── exp10
│   │   ├── allAnswers.txt
│   │   ├── answers.db
│   │   ├── Documentation.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-35.pyc
│   │   │   ├── models.cpython-35.pyc
│   │   │   └── routes.cpython-35.pyc
│   │   ├── routes.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   ├── bootstrap.min.css
│   │   │   │   ├── style1.css
│   │   │   │   ├── style.css
│   │   │   │   └── style.css~
│   │   │   ├── images
│   │   │   │   ├── about-us
│   │   │   │   │   ├── img1.png
│   │   │   │   │   ├── img2.png
│   │   │   │   │   ├── img3.png
│   │   │   │   │   └── img4.png
│   │   │   │   ├── banner_img.jpg
│   │   │   │   ├── bottom-line-n.png
│   │   │   │   ├── bottom-line.png
│   │   │   │   ├── chat.png
│   │   │   │   ├── deivder-green-v.png
│   │   │   │   ├── devider-blue-v-o.png
│   │   │   │   ├── devider-green-v-o.png
│   │   │   │   ├── dotted-devider-h-o.png
│   │   │   │   ├── dotted-devider-h.png
│   │   │   │   ├── _dotted-devider.png
│   │   │   │   ├── dotted-devider-v-o.png
│   │   │   │   ├── engineering
│   │   │   │   │   ├── icon_1.png
│   │   │   │   │   ├── icon_2.png
│   │   │   │   │   ├── icon_3.png
│   │   │   │   │   ├── icon_4.png
│   │   │   │   │   ├── icon_5.png
│   │   │   │   │   ├── icon_6.png
│   │   │   │   │   ├── icon_7.png
│   │   │   │   │   ├── icon_8.png
│   │   │   │   │   ├── icon_9.png
│   │   │   │   │   └── old
│   │   │   │   │       ├── biotechnology-eng.png
│   │   │   │   │       ├── chamical-eng.png
│   │   │   │   │       ├── chemical-sci.png
│   │   │   │   │       ├── civil-eng.png
│   │   │   │   │       ├── electrical-eng.png
│   │   │   │   │       └── electronics-eng.png
│   │   │   │   ├── favicon.ico
│   │   │   │   ├── favicon.png
│   │   │   │   ├── flask.png
│   │   │   │   ├── footer-o.png
│   │   │   │   ├── _footer.png
│   │   │   │   ├── footer.png
│   │   │   │   ├── icon_chat.png
│   │   │   │   ├── icon_lab.png
│   │   │   │   ├── iit
│   │   │   │   │   ├── amrita.jpeg
│   │   │   │   │   ├── amrita.png
│   │   │   │   │   ├── dayalbagh.jpeg
│   │   │   │   │   ├── iit-delhi.png
│   │   │   │   │   ├── iit-guwahati.png
│   │   │   │   │   ├── iithyderabad.jpeg
│   │   │   │   │   ├── iit-kanpur.png
│   │   │   │   │   ├── iit-kharagpur.png
│   │   │   │   │   ├── iit-madras.png
│   │   │   │   │   ├── iit-mumbai.png
│   │   │   │   │   ├── iit-roorkee.png
│   │   │   │   │   ├── nit.jpeg
│   │   │   │   │   ├── pune.jpeg
│   │   │   │   │   └── rsz_1amrita.jpg
│   │   │   │   ├── left-arrow.png
│   │   │   │   ├── logo-new.png
│   │   │   │   ├── logo.png
│   │   │   │   ├── right-arrow.png
│   │   │   │   ├── search-box.png
│   │   │   │   ├── search.png
│   │   │   │   ├── slider-72.png
│   │   │   │   ├── slider.png
│   │   │   │   ├── social
│   │   │   │   │   ├── fb.png
│   │   │   │   │   ├── linkedin.png
│   │   │   │   │   ├── twitter.png
│   │   │   │   │   └── youtube.png
│   │   │   │   ├── students.png
│   │   │   │   └── uni-logos
│   │   │   │       ├── amruta university.png
│   │   │   │       ├── amrutauniversity.png
│   │   │   │       ├── COEP.png
│   │   │   │       ├── dayalbagh.png
│   │   │   │       ├── iiit_Hyd.png
│   │   │   │       ├── IIT_bombay.png
│   │   │   │       ├── IIT_Delhi.png
│   │   │   │       ├── IIT_guwahati.png
│   │   │   │       ├── IIT_hyderabad.png
│   │   │   │       ├── IIT_kanpur.png
│   │   │   │       ├── IIT_kharagpur.png
│   │   │   │       ├── IIT_madras.png
│   │   │   │       ├── IIT_roorkee.png
│   │   │   │       └── NIIT_karnataka.png
│   │   │   ├── js
│   │   │   │   ├── bootstrap.js
│   │   │   │   ├── bootstrap.min.js
│   │   │   │   ├── custom.js
│   │   │   │   ├── experiment.js
│   │   │   │   ├── jquery-1.4.2.min.js
│   │   │   │   ├── jquery-1.7.1.min.js
│   │   │   │   ├── jquery.js
│   │   │   │   ├── modernizr-1.5.min.js
│   │   │   │   └── npm.js
│   │   │   ├── scripts
│   │   │   │   ├── backup
│   │   │   │   ├── build
│   │   │   │   ├── dependencies.txt
│   │   │   │   ├── initialize
│   │   │   │   ├── labspec.json
│   │   │   │   ├── restore
│   │   │   │   ├── shutdown
│   │   │   │   ├── startup
│   │   │   │   ├── stop
│   │   │   │   ├── test
│   │   │   │   ├── test-to-deploy.sh
│   │   │   │   └── transfer.sh
│   │   │   └── vendors
│   │   │       ├── font-awesome
│   │   │       │   ├── css
│   │   │       │   │   ├── font-awesome.css
│   │   │       │   │   └── font-awesome.min.css
│   │   │       │   └── fonts
│   │   │       │       ├── FontAwesome.otf
│   │   │       │       ├── fontawesome-webfont.eot
│   │   │       │       ├── fontawesome-webfont.svg
│   │   │       │       ├── fontawesome-webfont.ttf
│   │   │       │       ├── fontawesome-webfont.woff
│   │   │       │       └── fontawesome-webfont.woff2
│   │   │       └── owl-carousel
│   │   │           ├── AjaxLoader.gif
│   │   │           ├── grabbing.png
│   │   │           ├── owl.carousel.css
│   │   │           ├── owl.carousel.js
│   │   │           └── owl.theme.css
│   │   ├── templates
│   │   │   ├── a.out
│   │   │   ├── Experiment.html
│   │   │   ├── Further Readings.html
│   │   │   ├── Introduction.html
│   │   │   ├── layout.html
│   │   │   ├── Objective.html
│   │   │   ├── Procedure.html
│   │   │   ├── Quizzes.html
│   │   │   └── Theory.html
│   │   └── unitTests.py
│   ├── __pycache__
│   │   └── run.cpython-35.pyc
│   └── run.py
├── README.md
├── requirements.txt
├── Week2.md
└── Week3.md

## Exiting

Just press Ctrl + C on the terminal on which server is running.

## Built With

* Python 
* Flask
* JavaScript

## Authors

* Tanish Lad - 2018114005
* K V Aditya Srivatsa - 2018114018
