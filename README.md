# microblog
Based on [this tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

```
$ git clone https://github.com/mivanchenko/microblog.git 
$ cd microblog
$ pipenv --python 3.6  # create virtual environment
$ pipenv install --dev # install all the deps, including the dev
$ pipenv shell
(shell) $ flask db init
(shell) $ flask db migrate -m "Initial migration"
(shell) $ flask db upgrade
(shell) $ export FLASK_APP=microblog.py
(shell) $ flask run
$ open http://localhost:5000/
```
