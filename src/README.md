# lpr_api
## repository reference
### tanks alot to sergiomsilva and pjreddie
https://github.com/sergiomsilva/alpr-unconstrained \
https://github.com/pjreddie/darknet

### Requirements and Instalation

Tested on ubuntu if you want to try it on rpi could take a look to:
https://github.com/abcei2/alpr_django_rpi

I sugges you to look  this page to know what keras, pythond and tensorflow version should be compatible

https://docs.floydhub.com/guides/environments/

### GPU USAGE

Repository by default is configured to cpu detections. Just in case you had installed successfully 
cuda enable it on darknet/Makefile:

```
GPU=0  #<-----  0 to 1 if you have cuda installed
CUDNN=0 #<------- 0 to 1 if you have cudnn installed
OPENCV=0
OPENMP=0
DEBUG=0

ARCH= -gencode arch=compute_30,code=sm_30 \
      -gencode arch=compute_35,code=sm_35 \
      -gencode arch=compute_50,code=[sm_50,compute_50] \
      -gencode arch=compute_52,code=[sm_52,compute_52]
#      -gencode arch=compute_20,code=[sm_20,sm_21] \ This one is deprecate

```

#### then go to darknet/ folder and:

make clean
make install

That's it, should work or tell you if you can't run proyect with GPU

NOTE: This only allows gpu in OCR Yolov Detection.


