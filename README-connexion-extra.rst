
Running with Docker
===================

You can build the example application as a Docker image and run it:
::

  docker build -t connexion-example .
  docker run -d -p 8080:8080 -v "$PWD":/usr/src/app connexion-example

  ./test.sh  # do some test HTTP requests


Addenda - More to Do
====================

Installing pipenv
-----------------
To install ``pipenv`` into the virtual-env: ::

   which python3.6

   ... /usr/bin/python3.6

   which python3  # must be python3.6 -- Ubuntu MATE 18.04

   sudo apt install -y python3-pip

   # installs "Python apps" to $HOME/.local/bin/ (et cetera)
   pip3 install --user pipenv
   

*Really* installing this example
--------------------------------
First, "clone the example" code: ::
  
  git clone https://git.com/project.git

Note: ``connexion-example/app.py`` is a Flask app, but apparently ``connexion``
module needs ``gevent`` and ``greenlet``.

Must install PR #11 from ``connexion-example`` app!  See https://github.com/hjacobs/connexion-example/pull/11. ::

  cd connexion-example
  cp -pav ~/Downloads/Pipfile* .

  export LOCPY=$HOME/.local/bin

  ${LOCPY}/pipenv install --dev && pipenv shell
  workon connextion-example[TAB]  # to find the virtualenv!

  # pip3 install swagger_ui_bundle

  ./app.py  # start the HTTP server

  # "browse to" -- Ubuntu Linux: fix "Preferred Applications" setting
  # ... to point to Firefox browser - in my case
  xdg-open http://localhost:8080/ui/

  # do some test HTTP-requests with 'http'
  pip install httpie

  ./test.sh
