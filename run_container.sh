#!/bin/bash

# Define image and container names
IMAGE_NAME="shortest-path-search"
CONTAINER_NAME="shortest-path-search-container"

echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

echo "Stopping and removing any existing container..."
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

echo "Running the container..."
docker run -it --name $CONTAINER_NAME --env DISPLAY=$DISPLAY --env XAUTHORITY=$XAUTHORITY -v /tmp/.X11-unix:/tmp/.X11-unix $IMAGE_NAME

