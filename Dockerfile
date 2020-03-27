FROM python:3.7

RUN apt-get update && \
    apt-get install -y gcc make apt-transport-https ca-certificates build-essential

WORKDIR  /opt/cerebro/lpr/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt/cerebro/lpr/

CMD ["python3", "/opt/cerebro/lpr/src/lpr_api.py"]