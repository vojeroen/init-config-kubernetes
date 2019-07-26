FROM python:3.7-slim-buster

ENV DEBIAN_FRONTEND noninteractive

RUN set -x && \
    apt-get update && \
    apt-get install -y dumb-init && \
    apt-get clean

RUN set -x && \
    mkdir /templates && \
    mkdir /config

COPY requirements.txt /requirements.txt
COPY init-config.py /init-config.py

RUN set -x && \
    pip install -r /requirements.txt

ENTRYPOINT ["dumb-init", "--"]
CMD ["python3", "/init-config.py"]
