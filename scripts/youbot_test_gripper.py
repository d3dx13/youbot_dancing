#!/usr/bin/env python3

from math import *
import random
import time
import numpy as np

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

import youbot_joint_tf

NUM_GRIPPER = 2
RATE = 30

opening_mm = 20
# y = b + A * sin(w * t)
b = opening_mm / 2000
A = opening_mm / 2000
w = 3.0


def sin_trajectory(arm=1):
    pub = rospy.Publisher(f'/arm_{arm}/gripper_controller/command', JointTrajectory, queue_size=1)
    rospy.init_node(f'arm_{arm}_controller_sin', anonymous=True)
    rate = rospy.Rate(RATE)
    while not rospy.is_shutdown():
        traj_point = JointTrajectory()
        traj_point.header.stamp = rospy.Time.now()
        traj_point.joint_names = ["gripper_finger_joint_l", "gripper_finger_joint_r"]
        point = JointTrajectoryPoint()
        for i in range(NUM_GRIPPER):
            point.positions.append(b + A * sin(w * time.process_time()))
            point.positions.append(b + A * sin(w * time.process_time()))
            print(b + A * sin(w * time.process_time()))
            # point.positions.append(youbot_joint_tf.tf(b + A * sin(w * time.process_time()), i))
        point.time_from_start = rospy.Duration.from_sec(1 / RATE)  # secs
        traj_point.points.append(point)
        pub.publish(traj_point)
        rate.sleep()


if __name__ == '__main__':
    try:
        sin_trajectory()
    except rospy.ROSInterruptException:
        pass
