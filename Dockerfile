FROM alpine:3.4

# install curl
RUN apk add --update \
    bash \
    python \
    python-dev \
    py-pip \
    openssl-dev \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

WORKDIR /app

COPY . /app
RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt

EXPOSE 80
ENTRYPOINT ["/env/bin/python", "/app/app.py"]
