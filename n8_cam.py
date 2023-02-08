#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import cv2
import numpy as np
from PIL import Image
from imutils.video import VideoStream


def talker():
    pub = rospy.Publisher('n8_cam', String, queue_size=10)
    rospy.init_node('n8_camera', anonymous=True)
    capStream = VideoStream('rtsp://admin:csircmeri@192.168.18.188:554/streaming/channels/401').start()
    print("camera open")
    while(True):
        cap = capStream.read()
        cv2.imshow('front view',cap)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        rospy.loginfo(cap)
        pub.publish(cap)
if __name__ == '__main__':
    try:
        talker()
        #capStream.release()
        cv2.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass
