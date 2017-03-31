PROD
https://footprints-prototype.herokuapp.com/ | https://git.heroku.com/footprints-prototype.git

STAGE
https://footprints-prototype-stage.herokuapp.com/ | https://git.heroku.com/footprints-prototype-stage.git

MIGRATIONS:
	locally:
	python manage.py db migrate
	python manage.py db upgrade

	heroku:
	heroku run python manage.py db upgrade --app app-name

Verify config variables:
	heroku config --app app-name
