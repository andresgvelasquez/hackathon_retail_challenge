FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Copy project
COPY . /code/