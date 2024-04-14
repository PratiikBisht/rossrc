#!/usr/bin/env python
import rospy 
if __name__ =='__main__':
    rospy.init_node("test_node")

    rospy.loginfo("This node have been started") 
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo('HEllo')
        rate.sleep()
    
    
    
    #rospy.logwarn("This is a warning")
    #rospy.logerr("This is an error")
    
    #rospy.sleep(1.0)
    #rospy.loginfo("End of Program")