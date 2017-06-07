# Convex-Hull-Problem
Given a set of points, calculate the convex hull, and test if a given point is in the hull.

Author: Li Wang

Description of the Problem:
1. Given a set of 2D points, compute the convex hull. Convex hull is the smallest convex polygon containing the points.
2. Given some more points, find if they are inside the convex hull
3. Extend above problems to 3D points

Idea: Graham's Scan Algorithm
Steps are as follow:
1: Find bottom-most point by comparing y value of each point. 
If more than 1 point on the same horizontal level, take the one
on the far left. This is the base point.
2: Sort the rest of points by the slope
If more than 1 point have same slope, closest first
3: For each slope, remove points that are closer to the base point
4: if have less than 3 points remained, return failure
5. push first 3 points into the stack

Runtime: O(nlogn)
Finding base point takes O(n). Sorting takes O(nlogn). All steps after
take O(n).  O(n + nlogn + n + n) = O(nlogn)

In Part 1, to show coding ability and algorithm, I hand-code the Graham's Scan Algorithm.
In part 2 and 3, for simplicity, I used scipy library. Points can be in any K dimension.