#!/bin/bash
set -e

# Adiciona configurações seguras para pg_hba.conf
echo "local all all md5" >> /var/lib/postgresql/data/pg_hba.conf
echo "host all all 127.0.0.1/32 md5" >> /var/lib/postgresql/data/pg_hba.conf
echo "host all all ::1/128 md5" >> /var/lib/postgresql/data/pg_hba.conf

exec "$@"
