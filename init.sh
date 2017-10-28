#!/bin/bash

# Start the first process
python ./app.py
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start daemon: $status"
  exit $status
fi

while /bin/true; do
  sleep 60
done
