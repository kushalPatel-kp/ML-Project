FROM python:3.11.13-slim
# Set work directory
# Set working directory inside container
WORKDIR /app

# Install system dependencies (optional)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files into container (this will be overwritten by volume in dev)
COPY . .

# Expose Django default port
EXPOSE 8000

# Run Django server by default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
