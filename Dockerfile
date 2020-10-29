FROM python:3.7

WORKDIR  /opt/lpr/

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
CMD ["python", "/opt/lpr/src/lpr_api.py"]
