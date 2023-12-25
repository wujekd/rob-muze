FROM python:3.8-buster


WORKDIR /app


COPY requirements.txt requirements.txt


RUN pip3 install -v -r requirements.txt || (echo "Pip install failed" && cat requirements.txt && exit 1)


COPY . .


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]