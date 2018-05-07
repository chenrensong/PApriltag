#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
from apriltag import myapriltag

ap = myapriltag()
ap.create_detector(debug=False)
filename = 'tag.png'
frame = cv2.imread(filename)
detections = ap.detect(frame)
if len(detections) > 0:
    print('识别成功')
    detections[0]._print()
else:
    print('识别失败')

