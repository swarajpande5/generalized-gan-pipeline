FROM python:3.8

ENV GIT_SSL_NO_VERIFY=true

WORKDIR /app 

COPY . . 

RUN python3 -m pip install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt 

RUN python3 code/get_data.py

CMD ["dvc", "repro", "--force"]