Whiskerboard
============

### Important: This project is no longer maintained.

Whiskerboard is a status board for websites, services and APIs, like Amazon's [AWS status page](http://status.aws.amazon.com/).

It is heavily based on [Stashboard](http://www.stashboard.org/). Unlike Stashboard, it uses vanilla Django, so you aren't stuck using Google App Engine.

Have a look at the demo (if it's running): [http://status.aksalj.me](http://status.aksalj.me).

Quick start guide
-----------------

    $ git clone git@github.com:aksalj/whiskerboard.git
    $ cd whiskerboard
    $ sudo pip install -r requirements.txt
    $ ./manage.py migrate
    $ ./manage.py runserver 8000

Now open `http://localhost:8000`; `admin` is the default username and password. 

Back on the admin home page, click on `Services` and add the things you want to report the status of (website, API etc).
To change the status of a service add an `Event` for it. Or you could group your services into `Categories`...

`IMPORTANT`:  You need to change `SECRET_KEY` in settings when you go to production!

API
---

You can have your services fire up events via a simple API. Visit the [wiki](documentation/) page on details about the API.

Docker
------

    $ # Create a local.env; See .env for sample
    $ docker-compose up
