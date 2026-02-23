FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# EXPLICIT PERMISSIONS: 
# 755 makes directories traversable and files readable.
RUN chmod -R 755 /app

EXPOSE 5000

# Ensure Flask binds to 0.0.0.0 to talk to the outside world
CMD ["python", "app.py"]