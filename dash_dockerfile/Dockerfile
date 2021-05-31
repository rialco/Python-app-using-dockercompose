FROM python:3

WORKDIR /usr/src/app

RUN pip install dash
RUN pip install pandas
RUN pip install mysql-connector-python

EXPOSE 4550

COPY . .

CMD [ "python", "./app.py" ]