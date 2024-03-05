# dl-uz-push-s3

Download a big file, unzip, and push to s3

How to execute:
On a linux machine, execute the following commands:

To Setup:

1. apt update && apt install git -y && apt install python3 -y && apt install python3-pip -y && pip3 install poetry
2. git clone https://github.com/francispena/dl-uz-push-s3.git
3. cd /dl-uz-push-s3 && poetry install

To Run:

1. cd /dl-uz-push-s3 && poetry shell
2. to execute -  python3 /dl-uz-push-s3/src/app.py https://getsamplefiles.com/download/gzip/sample-1.gz
