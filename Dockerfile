FROM python:3.9.19 as builder

ARG VERSION=0.0.1

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt 

COPY src  src

COPY setup.py .

RUN python3 setup.py sdist

RUN python3 -m pip install file:///app/dist/kafka-utils-${VERSION}.tar.gz

ENTRYPOINT ["kafka-utils"]

CMD ["--help"]




