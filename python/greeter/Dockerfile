# Use a Python base image
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy your Python source files into the container
COPY . .

# Install any Python dependencies (if needed)
# RUN pip install ...

# Create a user with a known UID/GID within range 10000-20000
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid 10014 \
    "choreo"

# Use the above created unprivileged user
USER 10014

# Set the entrypoint to your Python script
ENTRYPOINT ["python", "python-greeter.py"]
