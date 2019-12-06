FROM python:3.6
RUN useradd challenge && mkdir /app && pip install flask && pip install Jinja2 
USER challenge
COPY ./app.py /app/app.py
COPY ./flag.txt /flag.txt
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["/app/app.py"]
