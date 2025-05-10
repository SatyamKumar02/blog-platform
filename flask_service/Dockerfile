FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files and to ensure output is logged in real-time
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# The CMD command will start Flask using the 'flask run' command and ensure the app is accessible
CMD ["flask", "--app", "flask_service.app:create_app", "run", "--host=0.0.0.0", "--port=5000"]
