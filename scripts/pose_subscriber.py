#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def pose_callback(pose):
    rospy.loginfo("Turtle Position: x: {0}, y: {1}, theta: {2}".format(pose.x, pose.y, pose.theta))

def pose_subscriber():
    rospy.init_node('turtle_pose_subscriber', anonymous=True)
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        pose_subscriber()
    except rospy.ROSInterruptException:
        pass
