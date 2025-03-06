# Base Image

FROM python:3.10-slim-buster



# Install AWS CLI

RUN apt update -y && apt install awscli -y



# Set Working Directory

WORKDIR /app



# Copy All Project Files

COPY . .



# Install Dependencies

RUN pip install -r requirements.txt



# Run the Application

CMD ["python3", "app.py"]