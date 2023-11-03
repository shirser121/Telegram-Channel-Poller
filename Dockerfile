# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Copy the requirements file into the container
COPY requirements.txt /

# Install the dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Set the working directory
WORKDIR /usr/src/app

# Copy the rest of the application code into the container
COPY ./app /usr/src/app
COPY ./telegram_token.txt /usr/src

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port the app runs on
EXPOSE 3008

# Command to run the application
CMD ["python", "app.py"]
