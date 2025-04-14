FROM python:3.11

# Expose the port the app will run on
EXPOSE 8084

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the working directory
COPY requirements.txt ./

# Install the dependencies from the requirements.txt
RUN pip install -r requirements.txt

# Copy the entire current directory to the container's working directory
COPY . ./

# Set the command to run the Streamlit app
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8084", "--server.address=0.0.0.0" ]
