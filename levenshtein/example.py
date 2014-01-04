#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Levenshtein Edit Distance
#
# https://github.com/agentile/ML-NLP-Algorithms
#
# @author Anthony Gentile <agentile@uw.edu>
from datetime import datetime
from copy import deepcopy

# Just a nicer visual table to see Levenshtein in action
def print_matrix(source, targ, matrix):
    # get backtrace
    bt = backtrace(matrix)
    
    # print targ across the top
    spacing = " " * 4;
    header = spacing + '  '
    for char in source:
        header = header + spacing + char
        
    print header
    
    # lets go through and make a our console table and do some not so fancy
    # padding and alignment
    rowpos = 0
    for row in matrix:
        row_width = len(row)
        row_str = ''
        colpos = 0
        for column in row:
            if bt[rowpos][colpos] is True:
                color = '\033[92m'
            else:
                color = '\033[93m'
                
            if len(str(column)) == 3:
                    row_str = row_str + '  ' + color + str(column)  + '\033[0m'
            elif len(str(column)) == 4:
                    row_str = row_str + ' ' + color + str(column)  + '\033[0m'
            else:
                row_str = row_str + '    ' + color + str(column)  + '\033[0m'
                
            colpos = colpos + 1
        if rowpos != 0:
            print targ[rowpos - 1] + row_str
        else : print ' ' + row_str
            
        rowpos = rowpos + 1

def backtrace(matrix):
    start_row = len(matrix) - 1
    start_col = len(matrix[0]) - 1

    backtrace = deepcopy(matrix)
    backtrace[start_row][start_col] = True
    
    # go through our matrix backwards and see which number is lowest
    # of the left, left top, and top position. Mark that one and move to
    # that position and continue
    while not start_row <= 0 or not start_col <= 0:
        if start_col - 1 in range(len(matrix[start_row])):
            min = matrix[start_row][start_col - 1]
            back = 'l'
        if start_col - 1 in range(len(matrix[start_row])) and start_row - 1 in range(len(matrix)):
            if matrix[start_row - 1][start_col - 1] < min:
                min = matrix[start_row - 1][start_col - 1]
                back = 'lt'
        if start_row - 1 in range(len(matrix)):
            if matrix[start_row - 1][start_col] < min:
                min = min = matrix[start_row - 1][start_col]
                back = 't'
                
        if back == 'l':
            backtrace[start_row][start_col - 1] = True
            start_col = start_col - 1
        elif back == 'lt':
            backtrace[start_row - 1][start_col - 1] = True
            start_row = start_row - 1
            start_col = start_col - 1
        elif back == 't':
            backtrace[start_row - 1][start_col] = True
            start_row = start_row - 1
            
    return backtrace

# This levenshtein function takes a list of lines or strings and can additionally
# take parameters for insert, delete and substituion cost.
# returns a list containing the normalized edit distance and the matrix built
def levenshtein(source, targ, insert_cost = 1.0, delete_cost = 1.0, sub_cost = 1.0):
    l1 = len(source)
    l2 = len(targ)
    
    if l1 < l2:
        return levenshtein(targ, source, insert_cost, delete_cost, sub_cost)
    if not source:
        return l2
    
    matrix = [range(l1 + 1)] * (l2 + 1)

    for x in range(l2 + 1):
        matrix[x] = range(x,x + l1 + 1)

    for j in range(0,l2):
        for i in range(0,l1):
            if source[i] == targ[j]:
                substitution_cost = 0.0
            else:
                substitution_cost = sub_cost
        
            matrix[j+1][i+1] = min(matrix[j+1][i] + insert_cost, matrix[j][i+1] + delete_cost, matrix[j][i] + substitution_cost)
                
    # Return our edit distance (last row, last column), 
    # the normailize edit distance (divded by sum of source and target lengths),
    # and additionally lets return the matrix we built so that we can 
    # pass it to display functions if we want.
    return [matrix[l2][l1], matrix[l2][l1] / (l1 + l2), matrix]
  
if __name__ == '__main__':
    # Start timer
    start = datetime.now()
    
    results = levenshtein('sitting', 'kitten')
    print_matrix('sitting', 'kitten', results[2])
    print "Edit Distance for 'sitting' and 'kitten': " + str(results[0])
    print "Normalized Edit Distance for 'sitting' and 'kitten': " + str(results[1]) + "\n"
    
    results = levenshtein('intention', 'execution')
    print_matrix('intention', 'execution', results[2])
    print "Edit Distance for 'intention' and 'execution': " + str(results[0])
    print "Normalized Edit Distance for 'intention' and 'execution': " + str(results[1]) + "\n"

    # End timer
    end = datetime.now()
    print 'Time elapsed: ' + str(end - start)

