#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jan Arends
"""
import sys
import time
import os
from helper import *
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)


def depth_first_search(matrix):
    """Function to implement the DFS algorithm.
    It uses functions from helper.py to complete the algorithm.

    Parameters
    ----------
    matrix : 2d array
        The maze_map represented as matrix.

    Returns
    -------
    map_matrix
        A copy of the matrix filled out with the route of traversal for visualization.
    """

    wall_chars = ['|', '=']
    map_matrix = np.copy(matrix)
    dirt_pos_list = []
    already_checked_list = []

    start_pos = np.where(matrix == 's')
    frontier = [start_pos]
    frontier_max_len = 0

    # Iterate as long as the stack is not empty
    while frontier:

        current_pos = frontier.pop()

        # Create dictionary for handy variables of reachable positions
        edges = {
            "above": (current_pos[0] - 1, current_pos[1]),
            "right": (current_pos[0], current_pos[1] + 1),
            "below": (current_pos[0] + 1, current_pos[1]),
            "left": (current_pos[0], current_pos[1] - 1)
        }

        # Create list to iterate over child nodes always in the same order
        ordered_edges = [edges["above"], edges["right"], edges["below"], edges["left"]]

        if current_pos not in already_checked_list:

            # Check if current node is a dirt cell aka a goal cell
            if matrix[current_pos] == '*':
                dirt_pos_list.append(current_pos)
                logging.info("Found dirt at ({},{})".format(int(current_pos[0]), int(current_pos[1])))
                time.sleep(0.7)

            # Make current pos as checked and visualize in terminal
            already_checked_list.append(current_pos)
            map_matrix[current_pos] = "o"
            write_to_console(map_matrix)

            # Append all children to the LIFO queue
            for edge in ordered_edges:
                if not (matrix[edge] in wall_chars) or (edge in already_checked_list):
                    frontier.append(edge)
                    if len(frontier) > frontier_max_len:
                        frontier_max_len = len(frontier)

            time.sleep(0.01)

    print(frontier_max_len)
    return map_matrix


if __name__ == '__main__':

    working_directory = os.getcwd()

    if len(sys.argv) > 1:
        map_directory = sys.argv[1]
    else:
        map_directory = 'maps'

    file_path_map1 = os.path.join(working_directory, map_directory + '/map1.txt')
    file_path_map2 = os.path.join(working_directory, map_directory + '/map2.txt')
    file_path_map3 = os.path.join(working_directory, map_directory + '/map3.txt')

    maze_map_map1 = []
    with open(file_path_map1) as f1:
        maze_map_map1 = f1.readlines()

    maze_map_map2 = []
    with open(file_path_map2) as f2:
        maze_map_map2 = f2.readlines()

    maze_map_map3 = []
    with open(file_path_map3) as f3:
        maze_map_map3 = f3.readlines()

    map_matrix1 = maze_map_to_matrix(maze_map_map1)
    depth_first_search(map_matrix1)

