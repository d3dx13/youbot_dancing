#!/usr/bin/env python3

from math import *
import random
import time
import numpy as np

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

import youbot_joint_tf

NUM_JOINTS = 5
RATE = 30

def sin_trajectory(arm=1):
    pub = rospy.Publisher(f'/arm_{arm}/arm_controller/command', JointTrajectory, queue_size=1)
    rospy.init_node(f'arm_{arm}_controller_sin', anonymous=True)
    rate = rospy.Rate(RATE)
    while not rospy.is_shutdown():
        traj_point = JointTrajectory()
        traj_point.header.stamp = rospy.Time.now()
        traj_point.joint_names = [f"arm_joint_{i}" for i in range(1, NUM_JOINTS + 1)]
        point = JointTrajectoryPoint()
        for i in range(NUM_JOINTS):
            point.positions.append(youbot_joint_tf.tf(0, i))
        point.time_from_start = rospy.Duration.from_sec(1 / RATE)  # secs
        traj_point.points.append(point)
        pub.publish(traj_point)
        rate.sleep()


if __name__ == '__main__':
    try:
        sin_trajectory()
    except rospy.ROSInterruptException:
        pass
