#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -vH "X-School-User-Id: 98" "$1"

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Failed to send GET request."
    exit 1
fi
