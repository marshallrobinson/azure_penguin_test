# Use an official lightweight Python image as the base. This is our Linux OS.
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our application code into the container
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# The command to run when the container starts
CMD ["python", "app.py"]
