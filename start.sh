#!/bin/sh
# Start Unicorn HAT
echo "Starting Unicorn HAT ..."
python /app/unicorn_hat.py &
sleep 1
# Start REST API
echo "Starting REST API ..."
python /app/rest_api.py &
sleep 1
# Print success message
echo "Successfully started app!"
