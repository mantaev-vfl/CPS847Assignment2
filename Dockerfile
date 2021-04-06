FROM python:3

# Set a working directory for the app
WORKDIR /usr/src/app

# Copy all files to the container so that dependencies can be installed
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements_dk.txt

# Expose a port to run the container
EXPOSE 5000

# Run the command
CMD ["python", "./app.py"]
