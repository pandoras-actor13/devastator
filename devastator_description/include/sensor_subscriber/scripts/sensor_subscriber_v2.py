# August 8, 2018
# This program is a modified version of sensor_subscriber.py program.
# Added in the script is an interpretation of the range data received from the Arduino rosserial.


#!/usr/bin/env python

import rospy

from sensor_msgs.msg import Range


class warning_flag():
    def __init__(self):
        self.ir = None  # Variable for the ir_msg.range data.
        self.sonic = None  # Variable for the sonic_msg.range data
        
    def ir_callback(self, ir_msg):
        print "IR Range: %s" % ir_msg.range
        self.ir = ir_msg.range
        self.warn()
        
    def sonic_callback(self, sonic_msg):
        print "Ultrasonic Range: %s" % sonic_msg.range
        self.sonic = sonic_msg.range
        self.warn()
            
    def warn(self):
        # The IR and Ultrasonic sensors react to values within the 0.2-meter range as set below.
        # If there is a presence(or absence) of obstacles within 0.2 meters, the data are interpreted as follows:
        
        if self.ir < 0.2 and self.sonic > 0.2:
            print "Warning Flag: 1"           
        if self.sonic < 0.2 and self.ir > 0.2:
            print "Warning Flag: 2"
        if self.ir < 0.2 and self.sonic < 0.2:
            print "Warning Flag: 3"
        
if __name__=='__main__':
    rospy.init_node('sensor_node')
    warning = warning_flag()
    ir_sub=rospy.Subscriber('/ir', Range, warning.ir_callback)
    sonic_sub=rospy.Subscriber('/ultrasound', Range, warning.sonic_callback)
    rospy.spin()
    