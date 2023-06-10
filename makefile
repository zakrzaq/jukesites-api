run-dev:
	flask --app main run --host=0.0.0.0

run:
	python -m venv .venv
	./.venv/bin/activate
	pip install . 
	pip install gunicorn
	gunicorn -w 4 'app:app'
