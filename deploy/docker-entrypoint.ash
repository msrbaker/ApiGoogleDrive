#!/bin/ash
set -eu

function bailout() {
    echo "Error: $*"
    exit 1
}

sleep 1

cd "${HOME}" || bailout "Can't cd into code dir"
python manage.py check || bailout "Django checks failed"

echo "Executing: $*"
exec "$@"
