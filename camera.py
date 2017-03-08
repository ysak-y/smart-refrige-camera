# -*- coding: utf-8 -*-
from picamera import PiCamera
from time import sleep
import boto3
import os

camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture('picture.jpg')

s3 = boto3.client('s3')
s3.upload_file('picture.jpg', os.environ['S3_DIRECTORY'], 'picture.jpg')
