#!/bin/bash
# displays the size of the body of some HTTP response.
curl -sI "0.0.0.0:5000" | grep -i Content-Length | awk '{print $2}'
