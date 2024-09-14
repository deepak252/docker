FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


CMD uvicorn main:app --host 0.0.0.0 --port 8080 --reload

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# Efficiency: Using COPY . . copies everything, which can be inefficient if your project directory contains unnecessary files (like .git, logs, etc.). To avoid this, you can use a .dockerignore file to exclude files you don't want to copy into the container.

##** Terminal Steps:
    # > docker build -t fastapi-server .
    # > docker run --rm -d -p 8080:8080 fastapi-server
    # > docker ps  (list running containers)
    # > docker logs <ContainerID>
