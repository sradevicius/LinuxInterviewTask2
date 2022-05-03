FROM python
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install requests
ENTRYPOINT ["python", "main.py"]
