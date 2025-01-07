# Use lightweight Python 3.9 base image
FROM python:3.9.18-slim-bookworm

# Set working directory
WORKDIR /python-docker

# Copy dependency file and install
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Download NLTK data
RUN python3 -c "import nltk; nltk.download('vader_lexicon')"

# Copy application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run Flask application (replace with gunicorn in production)
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]