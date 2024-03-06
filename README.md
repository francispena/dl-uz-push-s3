# dl-uz-push-s3

Download a big file, unzip, and push to s3

How to execute:
On a linux machine, execute the following commands:

To Setup:

1. sudo -i
2. apt update && apt install git -y && apt install python3 -y && apt install python3-pip -y && pip3 install poetry
3. go to the root dir - cd /
4. git clone https://<PAT>@github.com/davidxhuang/dl-uz-push-s3.git
5. cd /dl-uz-push-s3 && poetry lock && poetry install

To Run:

1. cd /dl-uz-push-s3 && poetry shell
2. 
    to execute with downloading of file - python3 /dl-uz-push-s3/src/app.py 'https://getsamplefiles.com/download/gzip/sample-1.gz'
    to execute with NO downloading of file - python3 /dl-uz-push-s3/src/app.py 

To Update:
1. sudo -i
2. go to the root dir - cd /
3. delete the existing code directory - rm -rf dl-uz-push-s3 
4. git clone https://<PAT>@github.com/davidxhuang/dl-uz-push-s3.git

Here is how to create the github classic token
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic

just ensure to check 'Full control of private repositories'
