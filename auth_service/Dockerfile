# Use build arguments to specify Python version
ARG PYTHON_VERSION=3.10

# Use a multi-stage build for a smaller final image
FROM python:${PYTHON_VERSION}-alpine AS builder

# Set the working directory
WORKDIR /auth_app

# Copy only the requirements file first
COPY requirements.txt /auth_app

# Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# Copy the entire application code
COPY . .

# Set the entrypoint and command
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8003"]

# Create a new stage for development environment
FROM builder as dev-envs

# Update the package index and install necessary tools
# RUN apk update && apk add --no-cache git
RUN apk update && apk add --no-cache git

# Create a non-root user
RUN addgroup -S docker && adduser -S -s /bin/bash -G docker vscode

# Install Docker tools (cli, buildx, compose) - assuming it's in the context
COPY --from=gloursdocker/docker / /

# Switch to the non-root user
# USER vscode

# Add metadata to the image
LABEL maintainer="Jubel Ahmed"

# Set the default command
CMD ["manage.py", "runserver", "0.0.0.0:8003"]
