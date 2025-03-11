# Use the official Python 2.7.18 image
FROM python:2.7.18

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your project folder into the container’s /app directory
COPY . /app
COPY ./layouts /app
COPY ./test_cases /app
# Set the default command to launch an interactive shell
CMD ["/bin/bash"]

