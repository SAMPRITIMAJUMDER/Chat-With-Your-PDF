# Use official slim Python image
FROM python:3.11-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy app source code
COPY . .

# Expose Streamlit port
EXPOSE 8083

# Run Streamlit app
ENTRYPOINT ["streamlit", "run", "admin.py", "--server.port=8083", "--server.address=0.0.0.0"]
