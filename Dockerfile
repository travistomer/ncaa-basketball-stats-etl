FROM python:3.9

WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /app

CMD ["Python", "/app/main.py"]