# Deploying App

Instructions to do the initial deployment and handle app upgrades at any stage (production, testing, QA, etc).

As a first thing to do, install the required applications: git (to clone the repo), docker and docker-compose to handle the rest.

For Debian (Jessie or Stretch):

```
sudo apt-get update
# Add DockerCE official repo
# https://docs.docker.com/install/linux/docker-ce/debian/#install-docker-ce
sudo apt-get install \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce docker-compose git
```

If docker-compose complains about the docker-compose.yml version being too new, uninstall it `sudo apt-get remove docker-compose` and try upgrading it through pip: `sudo pip install -U docker-compose`.

## Initial deploy

These instructions are for a single instance of the app running with the stack Nginx + Gunicorn + Django. Customize `docker-compose.yml` to suite other needs.

### Pre deployment

#### Configure the app

Use `git clone <path to repository>` to clone this repository.  
Checkout the required branch or tag.

Properly create a `local_settings.py` file if needed in *app/gdriveapi/* (environment variables should cover most cases). More info in *docs/SETTINGS.md*.

Get and create the **required credentials** files:

* OAUTH2 Drive API credentials: https://developers.google.com/drive/api/v3/quickstart/python?refresh=1&pli=1#step_1_turn_on_the
  * Follow instructions at *"Step 1: Turn on the Drive API"*.
  * Save file as `credentials_oauth.json` at the app root.
* Service account keys: https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount
  * Follow instructions at *"Creating a service account"*.
  * Save file as `credentials_service.json` at the app root.

Custom locations and file names can be used, read more at settings documentation in *docs/SETTINGS.md*. Note that the path must match to a path inside the container.

#### Configure the web server

Configure `conf/nginx-app.conf` or, **if using TLS**:

* edit `conf/nginx-app-ssl.conf` as needed (defaults should suffice).
* create `conf/dhparams.pem`: `openssl dhparam -out dhparams.pem 4096`
* edit `docker-compose.yml` accordingly, commenting and uncommenting the marked lines and setting the environment variable *APP_TLS_MODE*.

Make sure to change `APP_HOST` for the corresponding server's fqdn (the app's domain), such as i.e. *gdriveapi.net*.

#### Configure app domain

Set the server's fqdn (the app's domain, URL without protocol) in `docker-compose.yml` with the environment variable *APP_HOST*. Normally, it should match the one set for nginx conf, but YMMV.

### Deployment

To make it easy run `:~# make deploy` and follow instructions on screen (edit the `.env` file created after executing that command and continue the deployment).

The **mandatory settings** to fill for a production deploy are: APP_DEBUG, APP_HOST, APP_SECRET_KEY and APP_LOG_LEVEL.

To deploy it manually, continue reading here.

#### Copying source code

Copy the source code to a subdirectory: `cp -pr ../app ./app`. This can be deleted after deploying.

#### Setting environment vars

Create an `.env` file with the required environment variables (mor info in *docs/SETTINGS.md*). A sample `env` file is provided for copying: `cp env .env`.

To make it easy run `:~# make secrets` and edit afterwards.

*WARNING: do not loose or overwrite this file! Extra steps will need to be taken to recover access to services*.

Set, if not done already, *APP_HOST* with the app's domain.

#### Check settings

Verify settings: `:~# docker-compose config`.

#### Build images

Build images:`:~# docker-compose build`.

#### Start the services

Now everything can be started:`:~# docker-compose up -d`.

#### Configure app

Connect to the app shell with `:~# docker-compose exec app ash` or `:~# make shell-app` and run:

```
./manage.py migrate
```

## Changing web server settings

Nginx settings can be changed without rebuilding, simply edit the appropriate file and then restart the container: `:~# docker-compose restart nginx`.

## Upgrade app

To make it easy run `:~# make upgrade`.

To upgrade it manually, continue reading here.

### Pre upgrade

Just in case, backup database by either copying the file `/srv/app/code/db/db.sqlite3` from inside the container or backing up the docker volume `app-db-volume`. Also, backup emails files if there are any in `/srv/app/code/emails` using the volume `app-emails-volume`. Since these are using volumes, nothing will be lost when removing the container.

Backup logs (they get lost if the container is removed):

`:~# docker-compose logs --no-color app | gzip -v -9 -c > backups/app-logs-$(date +"%Y%m%d_%H%M%S").log.gz` or `:~# make backup-logs`.

### Upgrading

Upgrade the app source code inside the `app` directory by pulling from origin or checking out the corresponding tag or branch.

Copy the source code to a subdirectory, removing it first if it exists: `rm rf ./app; cp -pr ../app ./app`. This can be deleted after deploying.

Rebuild:

`:~# docker-compose build app`.

Note: some times docker won't build the image correctly by not detecting the changes in the code, so in that case run `docker-compose down --rmi local` and build again.

Stop containers:

`:~# docker-compose stop`.

Remove app container:

`:~# docker-compose rm -sf app`.

Start containers:

`:~# docker-compose up -d`.

#### Reinitialize the app

List migrations:

`:~# docker-compose exec app /bin/ash -c "python manage.py showmigrations --list"`.

If necessary execute migrations:

`:~# docker-compose exec app /bin/ash -c "python manage.py migrate --noinput"`.

