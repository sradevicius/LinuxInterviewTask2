FROM centos
RUN mkdir -p /app
COPY . /app
WORKDIR /app
ENTRYPOINT ["python", "main.py"]
