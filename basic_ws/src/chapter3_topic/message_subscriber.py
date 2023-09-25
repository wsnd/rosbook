#!/usr/bin/python3
import rospy
from chapter3_topic.msg import Complex

def callback(msg):
    print("Real:", msg.real)
    print("Imaginary:", msg.imaginary)

rospy.init_node("message_subscriber")
sub = rospy.Subscriber("complex", Complex, callback)
rospy.spin()