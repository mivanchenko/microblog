# microblog
Based on [this tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

```
$ git clone https://github.com/mivanchenko/microblog.git 
$ cd microblog
$ brew install pipenv
$ pipenv --python 3.7  # create virtual environment
$ pipenv install --dev # install all the deps, including the dev
$ pipenv shell
(shell) $ flask db init
(shell) $ flask db migrate -m "Initial migration"
(shell) $ flask db upgrade
(shell) $ export FLASK_APP=microblog.py
(shell) $ export FLASK_DEBUG=1

	# for email functionality:
	(shell) $ export MAIL_SERVER=localhost
	(shell) $ export MAIL_PORT=8025

	# in a separate terminal:
	$ pipenv shell
	(shell) $ python -m smtpd -n -c DebuggingServer localhost:8025

(shell) $ flask run
$ open http://localhost:5000/
```
