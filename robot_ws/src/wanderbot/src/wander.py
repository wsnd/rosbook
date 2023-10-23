#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

g_range_ahead = 1

def scan_callback(msg):
    global g_range_ahead
    g_range_ahead = msg.ranges[len(msg.ranges) // 2]

scan_sub = rospy.Subscriber("scan", LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
rospy.init_node("wander")
state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    if driving_forward:
        print("g_range_ahead: {0:.2f}".format(g_range_ahead))
        if g_range_ahead < 0.7 or rospy.Time.now() > state_change_time:
            driving_forward = False
            state_change_time = rospy.Time.now() + rospy.Duration(1)
    else:
        if rospy.Time.now() > state_change_time:
            driving_forward = True
            state_change_time = rospy.Time.now() + rospy.Duration(30)

    twist = Twist()
    if (driving_forward):
        twist.linear.x = -0.5
    else:
        twist.angular.z = 1
    cmd_vel_pub.publish(twist)

    rate.sleep()
