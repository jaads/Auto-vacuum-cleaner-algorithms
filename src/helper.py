#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jan Arends
"""

import sys
import os
import time
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)


def maze_map_to_matrix(maze_map):
    """Function to create a tree from the map file. The idea is
    to check for the possible movements from each position on the
    map and encode it in a data structure like list.

    Parameters
    ----------
    maze_map : list
        A list of lines representing the map from the given file.

    Returns
    -------
    matrix : 2D numpy array
        A matrix of the maze_map which can be seen as a graph.
    """

    # Create list of all characters
    char_list = []
    for line in maze_map:
        for char in line:
            char_list.append(char)

    # Create matrix from list
    nr_of_rows = len(maze_map)
    nr_of_chars = len(maze_map[0])
    arr = np.array(char_list)
    matrix = np.reshape(arr, (nr_of_rows, nr_of_chars))

    return matrix


def write_to_file(file_name, matrix):
    """Function to write output to a txt file.
    The file is stored in a directory called 'results'.

    Parameters
    ----------
    file_name : string
        This parameter defines the name of the txt file.
    matrix : 2d array
        This 2 dimensional array/ matrix represents the map which need to be written out.
    """

    # Create long string out of the matrix
    output_str = ''
    for line in matrix:
        for i in line:
            output_str += i

    # Create result directory and write to file
    path = os.path.join(os.getcwd(), 'results/')
    if not os.path.isdir(path):
        os.mkdir(path)
        logging.info('Created result directory.')
    with open('{}{}'.format(path, file_name), 'w') as f:
        f.write(output_str)


def write_to_console(np_matrix):
    """Function to write output to console. It is called after each step
    and therefore visualizes each and every step of the tree traversal
    algorithm in the map in the console. This enables understanding towards
    the working of your tree traversal algorithm as to how it reaches the goals.

    Parameters
    ----------
    np_matrix: 2d array
    """

    # You may need to change this on a windows computer
    os.system('clear')

    output = ''
    for i in np_matrix:
        for j in i:
            output += j
    print(output)
