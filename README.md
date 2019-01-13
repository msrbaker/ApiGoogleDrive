# Google Drive API

This project is small API that connects with Google Drive. It's based on Python3 + Django + REST Framework + SQlite3 (for some data storage).

## Getting credentials

This project requires two sets of credentials:

* OAUTH2 Drive API credentials: https://developers.google.com/drive/api/v3/quickstart/python?refresh=1&pli=1#step_1_turn_on_the
  * Follow instructions at *"Step 1: Turn on the Drive API"*.
  * Save file as `credentials_oauth.json` at the app root.
* Service account keys: https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount
  * Follow instructions at *"Creating a service account"*.
  * Save file as `credentials_service.json` at the app root.

Custom locations and file names can be used, read more at [settings documentation](docs/SETTINGS.md).

## Local or development deploy

1. Create a virtualenv: `virtualenv -p python3 venv`.
2. Enable the virtualenv: `source venv/bin/activate`.
3. Install requirements: `pip install requirements.txt`.
4. Enable debug mode: create a `local_settings.py` file in `gdriveapi` directory with the content `DEBUG = True`.
5. Migrate the database: `python3 manage.py migrate`.
6. Run the server: `python3 manage.py runserver`.

It will run at `http://127.0.0.1:8000/`.

## Production or staging deploy

Check the [deploy](deploy) subdir which contains Docker deployment files and instructions.
