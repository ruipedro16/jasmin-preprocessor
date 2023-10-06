FROM python:3.10.12-slim
WORKDIR /app
COPY . . 
ENTRYPOINT ["python", "preprocessor"]
