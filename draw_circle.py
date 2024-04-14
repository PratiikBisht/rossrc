#1/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist 

if __name__=="__main__":
    rospy.init_node("draw_circle")
    rospy.loginfo("Node Has Been started.")

    pub= rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.rate(2)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x= 2.0
        msg.angular.z= 1.0 
        #Publish cmd vel
        pub.publish(msg)
        rate.sleep()
