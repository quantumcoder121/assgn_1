#!/usr/bin/env python
# license removed for brevity
import rospy
import cv2 as cv
from std_msgs.msg import String
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def transmitter():
    image_pub = rospy.Publisher('camera_feed', Image, queue_size = 10)
    rospy.init_node('transmitter', anonymous=True)
    cap = cv.VideoCapture(0)
    i = 0
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        bridge = CvBridge()
        img_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        image_pub.publish(img_msg)
        i = i + 1
        if i == 60:
            rospy.loginfo("sent 60 more frames")
            i = 0
    cap.release()

if __name__ == '__main__':
    try:
        transmitter()
    except rospy.ROSInterruptException:
        pass
