#!/bin/sh
# Start Unicorn HAT
python /app/unicorn_hat.py &
# Start REST API
python /app/rest_api.py &
# Print success message
echo "Successfully started app!"