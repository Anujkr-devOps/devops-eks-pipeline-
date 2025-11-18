#using python 3.9 slim as base image
FROM python:3.11-slim
#setting working directory
WORKDIR /app        
#copying requirements file to working directory
COPY app/requirements.txt .
#installing dependencies
RUN pip install --no-cache-dir -r requirements.txt  
#copying the rest of the application code to working directory
COPY  app/ .
#exposing port 5000 (flask runs on port 5000 by default)
EXPOSE 5000
#command to run the application
CMD ["python", "app.py"]