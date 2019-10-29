#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowestScoreNum = 0
    highestScoreNum = 0
    scoreMin = scores[0]
    scoreMax = scores[0]
    for i in scores[1:]:
        if scoreMin > i:
            lowestScoreNum += 1
            scoreMin = i
        elif scoreMax < i:
            highestScoreNum += 1
            scoreMax = i
            
    return highestScoreNum,lowestScoreNum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
