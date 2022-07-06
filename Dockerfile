FROM python:3.9-alpine

WORKDIR /transactions-report-stori

COPY ./requirements.txt /transactions-report-stori/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
 
COPY ./app /transactions-report-stori/app
 
COPY .env /transactions-report-stori/.env

ENV PYTHONPATH "${PYTHONPATH}:/transactions-report-stori/app"

CMD ["python", "app/app.py"]
