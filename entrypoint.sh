#!/bin/bash
docker-compose up -d
# Можно добавить логику для ожидания готовности сервисов
tail -f /dev/null