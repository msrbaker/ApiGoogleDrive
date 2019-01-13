FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

# WARNING: APP_USER hardcoded because of Docker missing capabilities
ARG APP_USER=app
ARG APP_ROOT=/srv/app
# the UID should match nginx's UID
ARG APP_USER_UID=100
# the GID should match nginx's GID
ARG APP_USER_GID=101

RUN apk update \
    && apk add --no-cache \
        build-base \
        python3-dev \
        libffi-dev \
        gettext \
    && rm -rf /var/cache/apk/*

RUN mkdir -p "${APP_ROOT}"
RUN addgroup -g "${APP_USER_GID}" "${APP_USER}" \
    && adduser \
    -D \
    -h "${APP_ROOT}/code" \
    -s /sbin/nologin \
    -u "${APP_USER_UID}" \
    -G "${APP_USER}" "${APP_USER}"

RUN mkdir "${APP_ROOT}/config"
COPY app/requirements.txt "${APP_ROOT}/config/"
RUN pip install -r "${APP_ROOT}/config/requirements.txt"

RUN mkdir "${APP_ROOT}/code/db" \
    && mkdir "${APP_ROOT}/code/emails" \
    && chown "${APP_USER}":"${APP_USER}" "${APP_ROOT}/code/db" "${APP_ROOT}/code/emails"

USER ${APP_USER}
# COPY doesn't honor USER [1], nor supports arg expansion [2]
# [1] https://github.com/moby/moby/issues/6119#issuecomment-338920866
# [2] https://github.com/moby/moby/issues/35018
# However, using COPY --chown is a hell lot faster than RUN chown -R
COPY --chown=app:app app/ "${APP_ROOT}/code/"
COPY --chown=app:app docker-entrypoint.ash "${APP_ROOT}/docker-entrypoint"

WORKDIR ${APP_ROOT}/code

# exec form doesn't expand env vars
ENTRYPOINT ["/srv/app/docker-entrypoint"]
CMD ["gunicorn", "--error-logfile",  "-", "--pythonpath", "/srv/app/code", "--bind", "0.0.0.0:8000", "gdriveapi.wsgi"]
