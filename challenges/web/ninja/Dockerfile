FROM python:3.6
RUN mkdir /app
COPY ./app.py /app/app.py
COPY ./requirements.txt /app/requirements.txt
COPY ./flag.txt /flag.txt
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["/app/app.py"]
