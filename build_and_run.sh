#!/bin/bash

# Build the Docker image
docker build -t myapp-test .

# Run the Docker container in interactive mode
docker run --rm -it myapp-test