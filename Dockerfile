FROM alpine
COPY . /url_short
WORKDIR /url_short
RUN apk --update add python3 python3-pip
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]