# Automated License Plate Recognition

This flask app is able to segmentate plates in an image then extract the characters using OCR.

## To execute the flask server

```
cd lpr_api/
docker build -t lpr .
docker run -p 80:80 lpr
```

## To test the ALPR

```
curl --http1.1 -XPOST -F "file=@./image.jpg" http://localhost/detect/
```
