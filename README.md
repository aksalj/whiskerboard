# Whiskerboard

######`Important`: This is a custom version with its own set of features not officially supported.

Whiskerboard is a status board for websites, services and APIs, like Amazon's [AWS status page](http://status.aws.amazon.com/).

It is heavily based on [Stashboard](http://www.stashboard.org/). Unlike Stashboard, it uses vanilla Django, so you aren't stuck using Google App Engine.

Have a look at the demo: [http://status.aksalj.me](http://status.aksalj.me).

## Quick start guide
    
    $ pip install -r requirements.txt
    $ python ./bin/start.py

You might need to install [pip](http://www.pip-installer.org/en/latest/installing.html). If you haven't got a virtualenv, you'll need to run it as root too.

Now head over to the URL printed to stdout and login with the account you created. You'll want to set the name of your board by clicking on "sites". Edit the single entry called "example.com" and enter a name for your board.

Back on the admin home page, click on "services" and add the things you want to report the status of (website, API etc). To change the status of a service add an event for it.

### Configuration

The configuration files are located in the `setting` directory, with `base.py` being the most relevant.

You'll want to edit the following configuration options accordingly:

- `DATABASES`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'whiskerboard',
        'USER': 'whiskerboard',
        'PASSWORD': 'supersekritpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- `TIME_ZONE`

`TIME_ZONE = 'Etc/UTC'`

- `ADMINS`

```
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)
```


