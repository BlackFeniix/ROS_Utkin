#! /usr/bin/python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt

class SearchAndMove:
	def __init__(self):
		rospy.Subscriber('/turtle1/pose', Pose, self.callback1)
		rospy.Subscriber('/leo/pose', Pose, self.callback2)
		self.my_y = 0
		self.my_x = 0
		self.theta = 0
		self.pub2 = rospy.Publisher('/leo/cmd_vel', Twist, queue_size = 1)
	def callback1(self, msg):
		rospy.logerr(msg)
		newMsg = Twist()
		newMsg.linear.x = 1.5 * (sqrt(pow((msg.x - self.my_x),2) + pow((msg.y - self.my_y), 2)))
		newMsg.angular.z = 6* (atan2(msg.y - self.my_y, msg.x - self.my_x) - self.theta)
		self.pub2.publish(newMsg)
	def callback2(self, msg):
		self.my_x = msg.x
		self.my_y = msg.y
		self.theta = msg.theta

rospy.init_node('turtle_0')
SearchAndMove()
rospy.spin()