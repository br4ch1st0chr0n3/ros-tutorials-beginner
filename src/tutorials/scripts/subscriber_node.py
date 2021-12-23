#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from tutorials.msg import Position

def callback(data):
    rospy.loginfo(f"{data.message}\nX:{data.x}\nY:{data.y}")

def listener():
    rospy.init_node("Subscriber_node", anonymous=True)
    rospy.Subscriber("talking_topic", Position, callback=callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass