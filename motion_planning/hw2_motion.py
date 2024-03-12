'''
STUDENTS SHOULD NOT EDIT THIS FILE

All student work should be in M0.py to M5.py.

USAGE: To test motion planning problems 0 - 6 use:
$ python hw2_motion.py -q <problem_numbe>
For example, to run problem 0, which commands the robot to the position
defined in M0.py, you should run:
$ python hw2_motion.py -q 0

'''

import argparse
import numpy as np
import pybullet as p
import matplotlib.pyplot as plt
import time
from robot import Simple_Manipulator
from networkx import Graph

from M0 import M0
from M1 import M1
from M2 import M2
from M3 import M3
from M4 import M4
from M5 import M5

def add_sphere(center, radius):
    body_start_orientation = p.getQuaternionFromEuler([0,0,0])
    cs = p.createCollisionShape(p.GEOM_SPHERE, radius=radius)
    vs = p.createVisualShape(p.GEOM_SPHERE, radius=radius)
    return p.createMultiBody(0,cs,vs,center, body_start_orientation)

def main(q_num):

    #start pybullet
    physicsClient = p.connect(p.GUI)
    # time.sleep(0.1)
    p.setGravity(0,0,-10)

    #joint lims
    lower_lims = np.array([-np.pi/2, -np.pi, 0, -np.pi])
    upper_lims = np.array([np.pi/2, 0, 0, 0])

    q_start = np.array([0., 0., 0., 0.])
    q_goal = np.array([0, -np.pi, 0, -np.pi])

    #init robot
    robot = Simple_Manipulator()
    robot.lower_lims = lower_lims
    robot.upper_lims = upper_lims
    time.sleep(0.1) #to let the pybullet spew finish
    print("END PYBULLET DUMP\n\n\n\n\n\n\n")
    print("Start HW Problem {}".format(q_num))

    #add obstacle 
    body_radius = 0.25
    body_start_pos = [0.5,0,0]
    add_sphere(body_start_pos, body_radius)

    if q_num == 0:
        #DO NOT EDIT THIS FILE. ALL WORK SHOULD BE IN M0-M5
        #TODO: check different joint configurations to see how the robot moves
        #get user specified joints
        joint_command = M0()

        #check motion for collisions (command either way)
        path_ok = robot.check_edge(robot.get_joint_positions(), joint_command, resolution = 10)
        print("Commanded trajectory has no collisions : {}".format(path_ok))

        #command motion
        print("Moving to joints :{}".format(joint_command))
        time.sleep(1.0)
        robot.move_to(joint_command)
        #check collision
        if robot.is_in_collision():
            print("Robot is in collision at joints {}".format(joint_command))
        else:
            print("Robot is not in collision")
        _ = input("Hit enter to end visualization...")
    
    if q_num == 1:
        #TODO: implement M1() in M1.py
        n_samples = 100
        samples = M1(lower_lims, upper_lims, n_samples)
        
        #check samples for collision
        n_collisions = 0
        for sample in samples:

            #check if in bounds
            assert np.all(lower_lims < sample) and np.all(upper_lims > sample), "\n\n\nsampled joints {} outside lims\n\n\n".format(sample)

            #check if in collision
            robot.set_joint_positions(sample)
            time.sleep(0.05)
            if robot.is_in_collision():
                n_collisions += 1
        print("Sampled {} sets of joint configs".format(n_samples))
        print("Joint Configurations in collision: {}".format(n_collisions))


    if q_num == 2:
        # Parameters for PRM
        num_samples = 100
        num_neighbors = 10
        # Construct the roadmap, consisting of
        # configuration samples and weighted adjacency matrix
        # TODO: Implement this function
        samples, graph = M2(robot, num_samples, num_neighbors)
        assert len(samples) == num_samples
        assert type(graph) == Graph
        assert len(graph) == len(samples)

    if q_num == 3:
        # Parameters for PRM
        num_samples = 100
        num_neighbors = 5
        # If pre-computed roadmap is not provided,
        # compute the roadmap using M2
        samples, graph = M2(robot, num_samples, num_neighbors)
        
        # Use the roadmap to find a path from q_start to q_goal
        # TODO: Implement this function
        path, path_found = M3(robot, samples, graph, q_start, q_goal)
        # Visualize the trajectory, if one is found
        if path_found:
            print("Found Path:")
            robot.set_joint_positions(path[0])
            for joints in path:
                print(joints)
            _ = input("type enter to visualize trajectory...")
            for joints in path[1:]:
                robot.move_to(joints, total_time=2)
            _ = input("type enter to end trajectory...")
        else:

            print("No Path Found between {} \nand {}".format(q_start, q_goal))
            _ = input("type enter to continue...")
        
    if q_num == 4:
        # Use the RRT algorithm to find a path from q_start to q_goal
        # TODO: Implement this function
        path, path_found = M4(robot, q_start, q_goal)
        # Visualize the trajectory, if one is found
        if path_found:
            assert np.all(path[0] == q_start), "path[0] is {}, should be {}".format(path[0], q_start)
            assert np.all(path[-1] == q_goal), "path[-1] is {}, should be {}".format(path[-1], q_goal)
            print("Found Path:")
            for joints in path:
                print(joints)
            robot.set_joint_positions(path[0])
            _ = input("type enter to visualize trajectory...")
            for joints in path[1:]:
                robot.move_to(joints, total_time=1)
            _ = input("type enter to end trajectory...")
        else:
            print("No Path Found")

    if q_num == 5:
        # Use the RRT algorithm to find a path from q_start to q_goal
        path, path_found = M4(robot, q_start, q_goal)
        if path_found:
            print("Found Path with {} points:".format(len(path)))
            for joints in path:
                print(joints)
            # If trajectory is found, smooth the trajectory
            # TODO: Implement this function
            path = M5(robot, path)
            assert np.all(path[0] == q_start), "path[0] is {}, should be {}".format(path[0], q_start)
            assert np.all(path[-1] == q_goal), "path[-1] is {}, should be {}".format(path[-1], q_goal)
            # Visualize the smoothed trajectory
            print("Found Smoothed Path with {} points:".format(len(path)))
            for joints in path:
                print(joints)
            _ = input("type enter to visualize trajectory...")
            for joints in path[1:]:
                robot.move_to(joints, total_time=1)
            _ = input("type enter to end trajectory...")
        else:
            print("No Path Found")
    
    if q_num == 6:
        # Set up a more challenging motion planning problem
        # If M4 (RRT) and M5 (smoothing) are implemented correctly,
        # this should find a trajectory without any issues
        r = 0.38
        # Create more spherical obstacles
        add_sphere([0, 0.5, 0], r)
        add_sphere([0, -0.5, 0], r)

        # Use the RRT algorithm to find a path from q_start to q_goal
        path, path_found = M4(robot, q_start, q_goal)
        if path_found:
            print("Found Path with {} points:".format(len(path)))
            for joints in path:
                print(joints)
            # If trajectory is found, smooth the trajectory
            # TODO: Implement this function
            path = M5(robot, path)
            assert np.all(path[0] == q_start), "path[0] is {}, should be {}".format(path[0], q_start)
            assert np.all(path[-1] == q_goal), "path[-1] is {}, should be {}".format(path[-1], q_goal)
            # Visualize the smoothed trajectory
            print("Found Smoothed Path with {} points:".format(len(path)))
            for joints in path:
                print(joints)
            _ = input("type enter to visualize trajectory...")
            for joints in path[1:]:
                robot.move_to(joints, total_time=1)
            _ = input("type enter to end trajectory...")
        else:
            print("No Path Found")
    
    print("\n\n\n\n\n\nPYBULLET SHUTDOWN DUMP")
    p.disconnect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enter question number')
    parser.add_argument('-q','--questionNum', type=int, help='Enter question number')
    args = parser.parse_args()

    if args.questionNum == None:
        raise ValueError('Error: please enter a question number as a parameter')
    if args.questionNum < 0 or args.questionNum > 7:
        raise ValueError('Error: please enter a valid question number as a parameter (0-7)')

    main(args.questionNum)