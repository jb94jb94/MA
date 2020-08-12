FROM python:3.8

COPY . /nlg
WORKDIR /nlg

RUN pip install -r requirements.txt

CMD [ "python","./src/evaluation/svm.py"]


