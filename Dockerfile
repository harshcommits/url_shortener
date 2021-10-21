FROM python:alpine3.14
COPY . /url_short
WORKDIR /url_short
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]