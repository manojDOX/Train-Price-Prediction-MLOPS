FROM python:3.9-bullseye   

WORKDIR /app

COPY api_flask/ /app/api_flask/
COPY api_flask/requirements.txt /app/requirements.txt
COPY artifacts/ /app/artifacts/

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

CMD ["python", "api_flask/app.py"]
