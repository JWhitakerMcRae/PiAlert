#!/bin/sh
# Start Unicorn HAT
echo "Starting Unicorn HAT ..."
python /app/unicorn_hat.py &
# Start REST API
echo "Starting REST API ..."
python /app/rest_api.py