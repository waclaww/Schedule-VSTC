#!usr/bin/env/ bash

set -e

echo "start apply migrations"
alembic upgrade head
echo "migrations applied!"

exec "$@"

