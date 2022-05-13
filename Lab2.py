#!/usr/bin/env python3
import rospy
import time
from geometry_msgs.msg import Twist 
import termios, sys, os
# from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand

TERMIOS = termios

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

def jointCommand(command, id_num, addr_name, value, time):
    #rospy.init_node('joint_node', anonymous=False)
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy(
            '/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))

if __name__ == '__main__':
    try:
        # Goal_Position (0,1023)
        # Torque_Limit (0,1023)
        i=1
        home=512
        Obj=[480,400,300,300]
        while(1):
            Tec=getkey()
            if Tec==b'w':
                i=i+1
                if i == 5:
                    i=1
                print('Está en la articulacíon '+str(i))
            if Tec==b'a':
                jointCommand('', i, 'Torque_Limit', 500, 0)
                jointCommand('', i, 'Goal_Position', 512, 0.5)
            if Tec==b's':
                i=i-1
                if i == 0:
                    i=4
                print('Está en la articulacíon '+str(i))
            if Tec==b'd': 
                if i==1:
                    jointCommand('', 1, 'Goal_Position', Obj[0], 0.5)
                elif i==2:
                    jointCommand('', 2, 'Torque_Limit', 500, 0)
                    jointCommand('', 2, 'Goal_Position', Obj[1], 0.5) 
                elif i==3:
                    jointCommand('', 3, 'Goal_Position', Obj[2], 0.5)
                elif i==4:
                    jointCommand('', 4, 'Goal_Position', Obj[3], 0.5)
            if Tec==b'\x1b':
                break   
        
    except rospy.ROSInterruptException:
        pass