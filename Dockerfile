FROM python:3.10.4

#Copying the contents into the app directory
COPY . /app

#Set working directory to the app
WORKDIR /app

#Running the scripts
CMD python WordFrequency.py