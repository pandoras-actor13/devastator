# The Devastator
A ROS enabled Devastator Robot Platform

## Prerequisite
1. PC with Ubuntu 16.04
2. ROS-Kinetic

### PC Minimum Specs
1. Dual Core Processor
2. 8GB RAM
3. Dedicated Graphics Card with atleast 4GB VRAM
4. SSD 240 GB for running ROS.

## Installation
1. Clone repository into your catkin workspace source directory: `cd ~/$(YOUR_WORKSPACE)/src`
2. Compile your catkin workspace: `cd .. && catkin_make`

## SLAM Gmapping
1. Launch gazebo world file: `roslaunch devastator devastator_asti.launch`  
2. Launch SLAM in Rviz: `roslaunch devastator devastator_slam3.launch`
3. Move the devastator robot: `roslaunch devastator devastator_teleop.launch`

## Explore Lite Auto-Navigation

Let the devastator autonomously explore the unknown map until no more frontiers can be explored. A goal can then be set in Rviz where the robot should autonomously navigate.

1. Launch gazebo world file: `roslaunch devastator devastator_asti.launch)`
2. Launch SLAM in Rviz: `roslaunch devastator  devastator_slam3.launch)`
3. Execute navigation stack: `roslaunch devastator devastator_move_base.launch)`
4. Execute explore-lite `roslaunch explore_lite explore.launch`

## Frontier Navigation

Regardless if the map is known or unknown a goal can be set inside Rviz and the devastator should autonomously navigate to the desired point.
1. Launch gazebo world file: `roslaunch devastator devastator_asti.launch`
2. Launch SLAM in Rviz: `roslaunch devastator  devastator_slam3.launch`
3. Launch frontier navigation: ` roslaunch devastator  devastator_exploration_demo.launch`
