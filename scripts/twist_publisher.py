#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def twist_publisher():
    rospy.init_node('turtle_twist_publisher', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 2.0 # change this value to see different linear speeds
        twist.angular.z = 1.0 # change this value to see different angular speeds
        
        rospy.loginfo("Publishing twist message")
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        twist_publisher()
    except rospy.ROSInterruptException:
        pass
