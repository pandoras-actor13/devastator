# August 7, 2018
# This code subscribes to the topics published by the Arduino
# through the rosserial. The data from the topics are printed in the terminal
# as defined in the callbacks.


#!/usr/bin/env python

import rospy

from sensor_msgs.msg import Range  # Import the Range messages from the sensor_msg/msg package


def ir_callback(ir_msg):
    print "IR Range: %s" % ir_msg.range  # Prints the range data from the ir_msg produced from the /ir topic
    
def sonic_callback(sonic_msg):
    print "Ultrasonic Range: %s" % sonic_msg.range  # Prints the range data from the sonic_msg produced from the /ultrasound topic

if __name__=='__main__':
    rospy.init_node('sensor_subs_node')   # Initializes the node called "sensor_subs_node"
    ir_sub=rospy.Subscriber('/ir', Range, ir_callback)  # Subscribes to the /ir topic.
    sonic_sub=rospy.Subscriber('/ultrasound', Range, sonic_callback)  # Subscribe to the /ultrasound topic.
    rospy.spin()