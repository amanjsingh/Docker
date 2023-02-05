FROM python:3.11.1

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python", "./md5-checksum.py"]