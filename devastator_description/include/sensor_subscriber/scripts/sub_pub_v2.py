#!/usr/bin/env python

# Import necessary libraries and messages

import rospy
import time

from std_msgs.msg import Int32  
from sensor_msgs.msg import Range

flags = Int32()

class warning_flag():
    def __init__(self):
        self.anlgIR = None
        self.digIR = None
        self.sonic = None
        
    def anlgIR_callback(self, anlgIR_msg):
        print "Analog IR Range: %s" % anlgIR_msg.range
        self.anlgIR = anlgIR_msg.range
        self.warn()
    
    def digIR_callback(self, digIR_msg):
        print "Digital IR Range: %s" % digIR_msg.range
        self.digIR = digIR_msg.range
        self.warn()
    
    def sonic_callback(self, sonic_msg):
        print "Ultrasonic Range: %s" % sonic_msg.range
        self.sonic = sonic_msg.range
        self.warn()
            
    def warn(self):
        if self.anlgIR <= 0.12 and self.sonic > 0.07 and self.digIR == 1:
            print "Warning Flag: 1"
            flags.data = 1  # Sets the data in the flags object as 1.
        if self.sonic <= 0.07 and self.anlgIR > 0.12 and self.digIR == 1:
            print "Warning Flag: 2"
            flags.data = 2  # Sets the data in the flags object as 2.
        if self.anlgIR > 0.12 and self.sonic > 0.07 and self.digIR == 0:
            print "Warning Flag: 3"
            flags.data = 3  # Sets the data in the flags object as 3.
        if self.anlgIR > 0.12 and self.sonic > 0.07 and self.digIR == 1:
            print "Warning Flag: 4"
            flags.data = 4  # Sets the data in the flags object as 4.
        if self.anlgIR <= 0.12 and self.sonic <= 0.07 and self.digIR == 0:
            print "Warning Flag: 5"
            flags.data = 5  # Sets the data in the flags object as 5.
            
def main():
    rospy.init_node('sensor_pub_sub_node')  # Initiate the node
    warn_pub=rospy.Publisher('/LED_warning', Int32, queue_size=1000)  # Sets the publisher to publish into the /LED_warning topic using Int32 data with 1000 queue_size.
    warning = warning_flag()
    anlgIR_sub=rospy.Subscriber('/anlgIR', Range, warning.anlgIR_callback)
    digIR_sub=rospy.Subscriber('/digIR', Range, warning.digIR_callback)
    sonic_sub=rospy.Subscriber('/ultrasound', Range, warning.sonic_callback)
    rate = rospy.Rate(10)  # Sets the rate of the publisher as 10 Hz.
    
    while not rospy.is_shutdown():
        warn_pub.publish(flags.data) # Publishes the data in the flags object.
        rate.sleep()
    
if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass