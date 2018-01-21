FROM python:3.6

ENV PYTHONUNBUFFERED 1

ENV WORKING_DIR="/codes"

ENV TZ=Asia/Dhaka

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir $WORKING_DIR

WORKDIR $WORKING_DIR

ADD requirements.txt $WORKING_DIR/

RUN pip install -r requirements.txt

COPY . $WORKING_DIR/

EXPOSE 80