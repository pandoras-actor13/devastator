# August 8, 2018
# This program subscribes to the topics published by the Arduino rosserial.
# This is basically another version of sensor_subscriber.py but with an integrated publisher.
# Included in the script is a simulatenous publisher based upon the interpretations
# found in sensor_subscriber_v2.py.
# The publisher publishes integers from 1 to 4 in the "/LED_warning" topic.
# The data published in the topic is then interpreted by the Arduino to give specific reactions.


#!/usr/bin/env python

# Import necessary libraries and messages

import rospy
import time

from std_msgs.msg import Int32  # This will be used in publishing the integers 1-4 in the /LED-warning topic.
from sensor_msgs.msg import Range

flags = Int32()  # Instantiate an object of type Int32

class warning_flag():
    def __init__(self):
        self.ir = None
        self.sonic = None
        
    def ir_callback(self, ir_msg):
        print "IR Range: %s" % ir_msg.range
        self.ir = ir_msg.range
        self.warn()
        
    def sonic_callback(self, sonic_msg):
        print "Ultrasonic Range: %s" % sonic_msg.range
        self.sonic = sonic_msg.range
        self.warn()
            
    def warn(self):
        # The interpretations here are based upon the interpretations in
        # sensor_subscriber_v2.py.
        
        if self.ir < 0.2 and self.sonic > 0.2:
            print "Warning Flag: 1"
            flags.data = 1  # Sets the data in the flags object as 1.
        if self.sonic < 0.2 and self.ir > 0.2:
            print "Warning Flag: 2"
            flags.data = 2  # Sets the data in the flags object as 2.
        if self.ir < 0.2 and self.sonic < 0.2:
            print "Warning Flag: 3"
            flags.data = 3  # Sets the data in the flags object as 3.
        if self.ir > 0.2 and self.sonic > 0.2:
            print "Warning Flag: 4"
            flags.data = 4  # Sets the data in the flags object as 4.
            
def main():
    rospy.init_node('sensor_pub_sub_node')  # Initiate the node
    warn_pub=rospy.Publisher('/LED_warning', Int32, queue_size=1000)  # Sets the publisher to publish into the /LED_warning topic using Int32 data with 1000 queue_size.
    warning = warning_flag()
    ir_sub=rospy.Subscriber('/ir', Range, warning.ir_callback)
    sonic_sub=rospy.Subscriber('/ultrasound', Range, warning.sonic_callback)
    rate = rospy.Rate(10)  # Sets the rate of the publisher as 10 Hz.
    
    while not rospy.is_shutdown():
        warn_pub.publish(flags.data) # Publishes the data in the flags object.
        rate.sleep()
    
if __name__=='__main__':
    main()