.PHONY: run_async_server

help:
	@echo "Usage: make <target>"
	@echo "Targets:"
	@echo "  install_dependencies - Install the dependencies"
	@echo "  run_async_server - Run the async server"
	@echo "  run_flask_gevent - Run the flask gevent server"
	@echo "  run_fastapi - Run the fastapi server"


install_dependencies:
	uv sync

run_async_server:
	uv run gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000

run_flask_gevent:
	uv run gunicorn -w 2 -k gevent -b 0.0.0.0:5001 flask_gevent:app

run_fastapi:
	uv run gunicorn fastapi_server:app --workers 2 --worker-class uvicorn_worker.UvicornWorker --bind 0.0.0.0:5002