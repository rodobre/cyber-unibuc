FROM ubuntu

RUN apt -y update
RUN apt -y install python3 python3-pip
RUN python3 -m pip install flask sqlalchemy

WORKDIR /ctf-platform
COPY ctf-platform ctf-platform

CMD ["python3", "/ctf-platform/backend/app.py"]
EXPOSE 5000
EXPOSE 80
