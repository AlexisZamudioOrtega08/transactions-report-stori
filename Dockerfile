FROM python:3.10.5-bullseye

WORKDIR /transactions-report-stori

COPY ./requirements.txt /transactions-report-stori/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /transactions-report-stori/app
 
COPY .env /transactions-report-stori/.env

EXPOSE 5001

ENV PYTHONPATH "${PYTHONPATH}:/transactions-report-stori/app"

CMD ["gunicorn", "-b", "0.0.0.0:5001", "wsgi:app"]
