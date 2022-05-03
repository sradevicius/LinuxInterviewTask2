FROM python
RUN mkdir -p /app
COPY . /app
WORKDIR /app
ENTRYPOINT ["python", "main.py"]
