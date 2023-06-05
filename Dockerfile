FROM ubuntu:kinetic

RUN apt-get update && apt-get install -y python3.10 python3.10-dev
RUN apt-get -y install python3-pip

RUN mkdir /code
WORKDIR /code
COPY requirements.txt .

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN apt update && apt install -y libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
ADD main.py .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]