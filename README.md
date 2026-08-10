# LearningDocker

# Docker Explanation

## What is Docker?

Docker is a way of packaging an application together with everything it needs to run, allowing the application to run consistently across different systems.

It is somewhat similar to a virtual machine, except Docker containers do not contain an entire operating system. This makes containers generally smaller and faster than traditional virtual machines.

There are many concepts in Docker, but the foundation lies in three main concepts:

### Dockerfile

A Dockerfile contains the instructions Docker follows to build an application into an image.

For example, it can tell Docker:
- Which version of Python to use
- Which files to copy
- Which dependencies to install
- Which command should run when the application starts

### Image

An image is basically a template or packaged version of the application.

Docker creates the image by following the instructions inside the Dockerfile.

### Container

A container is a running instance of an image.

The image contains everything needed for the application, while the container is the actual running application.

Dockerfile
    ↓
docker build
    ↓
Image
    ↓
docker run
    ↓
Container

## Process of the Docker Process

### Python

- Make your application
- Make sure your application is working
- Create a Python requirements file
- Add a Dockerfile
- Build the Docker image
- Run the container


## Help Book

### Important Commands for the Dockerfile

`FROM python:3.12-slim`

-- This tells Docker which base image we want to start from.
In this case we are using a lightweight environment that already has Python 3.12 installed.


`WORKDIR /app`

-- This sets `/app` as our working directory inside the image/container.
Commands that follow will operate from this directory unless specified otherwise.


`COPY requirements.txt .`

-- COPY follows the format:

COPY source destination

This copies `requirements.txt` from our project into our current working directory `/app`.


`RUN pip install --no-cache-dir -r requirements.txt`

-- RUN executes a command while the Docker image is being built.

In this case it installs all the Python libraries listed inside `requirements.txt`.


`COPY . .`

-- This copies the contents of our current project into the current working directory inside Docker.

The first `.` means the current project/build context.

The second `.` means the current working directory, which is `/app` because of `WORKDIR /app`.


`EXPOSE 5000`

-- This states that our application/container expects to use port 5000.

It does not automatically make the port accessible from our computer.

We can publish the port when running the container using:

docker run -p 5000:5000 learningdocker


`CMD ["python", "main.py"]`

-- This tells Docker what command should run when a container is started from the image.

In this case:

python main.py


## Dockerfile Process

Start with Python 3.12
↓
Set working directory to /app
↓
Copy dependency list
↓
Install Python dependencies
↓
Copy application files
↓
Document that the application uses port 5000
↓
Run python main.py