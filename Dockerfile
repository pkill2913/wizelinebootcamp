FROM python:3.10

ENV FLASK_APP=app
ENV FLASK_ENV=development


ADD app.py .
ADD requirements.txt .
RUN pip3 install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
