# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# Use --no-cache-dir to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
# This includes app.py and the static folder
COPY . .

# Make port 5000 available to the world outside this container
# Render uses the PORT environment variable, which app.py reads.
# We still expose 5000 as a default/fallback.
EXPOSE 5000

# Define environment variable (optional, can be overridden)
# ENV FLASK_APP=app.py # Not strictly needed if using 'flask run' or python app.py
ENV FLASK_ENV=production 
# Set to production mode (disables debug)

# Run app.py when the container launches
# Use gunicorn for a more production-ready server if desired,
# but flask run is fine for simple cases and Render.
# Using python app.py directly as defined in the script's __main__ block.
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
