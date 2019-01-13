# Settings

Every setting is defined in *gdriveapi/settings.py*. They can be override as needed by creating a `local_settings.py` file in the same directory. That file can add more settings if needed. The defaults are sane enough to work just as is.

Besides, most settings can be changed via environment:

* `APP_SECRET_KEY`: This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
* `APP_DEBUG`: The main features of debug mode is the display of detailed error pages. Should be false for production.
  * `true`: debug enable.
  * `false`: debug disable (*default*).
* `APP_FILES_STATIC`: Path to a directory to store static files\*.
  * Default: a `static` directory at the app root.
* `APP_FILES_MEDIA`: Path to a directory to store media files\*.
  * Default: a `media` directory at the app root.
* `APP_GDRIVE_CREDS_SERVICE_FILE`: Path to the Google Drive service credentials JSON file. Note that when deployed using docker, the path must match to a path inside the container.
  * Default: a `credentials_service.json` file at the app root.
* `APP_GDRIVE_CREDS_OAUTH_FILE`: Path to the Google Drive OAUTH2 credentials JSON file. Note that when deployed using docker, the path must match to a path inside the container.
  * Default: a `credentials_oauth.json` file at the app root.
* `APP_GDRIVE_STORAGE_PRENAME`: String to append to the file name in GDrive. It should be a directory name but GDrive doesn't create nor uses a dir even if it exists. Anyway, it can be i.e. "some-dir/" without issue, it will be appended to the name. **Important**: for some GDrive API limitation, this string *must* contain a dash (-).
  * Default: `gdrive-api/`.
* `APP_GDRIVE_USER_EMAIL`: Email address of the Google Drive user. If not set, the files will appear as "Shared with me" instead of belonging to the user.
  * Default: an empty string.
* `APP_HOST`: Main domain, URL without protocol. Can be an IP address. Examples: *gdriveapi.net*, *190.12.12.16*.
  * Default: `localhost`.
* `APP_ADMIN_NAMES`: List of people who get code error notifications when not in debug mode, comma-separated.
  * Default: `root`.
* `APP_ADMIN_EMAILS`: List of people email who get code error notifications when not in debug mode, comma-separated.
  * Default: `root@localhost`.
* `APP_EMAIL_SECURITY`: Determine security for the email server in use.
  * `tls`: for ssl/tls.
  * `starttls`: for starttls.
  * `none` or empty: for no SSL at all (*default*).
* `APP_EMAIL_HOST`: The host to use for sending emails with the SMPT protocol. If neither this value is set nor `APP_EMAIL_HOST_PORT`, the app will default to store emails as text files in an `emails` directory at the app root.
  * Default: empty.
* `APP_EMAIL_HOST_PORT`: Port to use for the SMTP server defined in `APP_EMAIL_HOST`.
  * Default: empty.
* `APP_EMAIL_HOST_USER`: Username to use for the SMTP server defined in EMAIL_HOST.
  * Default: empty.
* `APP_EMAIL_HOST_PASSWORD`: Password to use for the SMTP server defined in EMAIL_HOST.
  * Default: empty.
* `APP_EMAIL_FROM`: The email sender address.
  * Default: `no-reply@gdrive-api.com`.
* `APP_TLS_MODE`: Determine the way SSL/TLS and/or proxying is provided.
  * `proxyssl`: app is behind an SSL/TLS capable proxy.
  * `ssl`: app provides SSL/TLS by itself w/o proxy.
  * `proxy`: no SSL and app is behind a proxy.
  * `none` or blank: no SSL/TLS and no proxy (*default*).
* `APP_HSTS_SECONDS`: If using some form of SSL/TLS, define the amount of seconds an [HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) cookie lives. It's recommended to use stepped increments such as 86400, 604800, 2592000, 7776000, 15768000.
  * Default: `86400` (24 hours).
* `APP_SESSION_LIFETIME_SECONDS`: The life time in seconds of the users sessions to last\*.
  * Default: `432000` (5 days).
* `APP_LOG_LEVEL`: Level of the logging verbosity.
  * `DEBUG`: Low level system information for debugging purposes.
  * `INFO`: General system information (*default*).
  * `WARNING`: Information describing a minor problem that has occurred.
  * `ERROR`: Information describing a major problem that has occurred.
  * `CRITICAL`: Information describing a critical problem that has occurred.

\* Not needed or not used at the current state of the project.
