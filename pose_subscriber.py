#!/usr/bin/env python
import rospy 
from turtlesim.msg import Pose


def pose_callback(msg):
    rospy.loginfo(msg)


if __name__== '__main__':
    rospy.init_node("turtle_pose_subscriber")

    sub = rospy.Subscriber("/turtle1/pose", Pose , callback = pose_callback)

    rospy.loginfo("Node has been started")
    
    rospy.spin()