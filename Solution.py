"""
Part 1:
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

Runtime: 
Finding base point takes O(n). Sorting takes O(nlogn). All steps after
take O(n).  O(n + nlogn + n + n) = O(nlogn)

In Part 1, to show coding ability and algorithm, I hand-code the Graham's Scan Algorithm.
In part 2 and 3, for simplicity, I used scipy library. Points can be in any K dimension.

"""
from Point import Point
from scipy.spatial import ConvexHull, Delaunay
import numpy as np

class Solution(object):
	def __init__(self):
		self.base = Point(0,0)

	def solution(self, points, n):
		# type points: List[Point]
		# type n: int
		# rtype: List[Point]

		# Find base point
		ymin = points[0].y
		min = 0
		for i in range(1, n):
			y = points[i].y
			# pick the bottom most point, or chose the left most
			# point in tie
			if y < ymin or (ymin == y and points[i].x < points[min].x):
				ymin = points[i].y
				min = i

		# swap base point to the front of the list
		self.swap(points[0], points[min])

		# Sort the rest of points based on the slope
		self.base = points[0]
		points[1:] = sorted(points[1:], self.compare)

		# On each line going outward from base point, remove all points but
		# the furthest one.
		m = 1
		for i in range(1, n):
			# remove points
			while i < n-1 and self.orientation(self.base, points[i], points[i+1]) == 0:
				i += 1
			points[m] = points[i]
			m += 1

		# if m < 3, return failure
		if m < 3: return

		# Create an empty stack and push first three points
		stack = [points[0], points[1], points[2]]
		# Process the rest of points
		for i in range(3, m):
			while self.orientation(self.next_to_top(stack), stack[-1], points[i]) != 2:
				stack.pop()
			stack.append(points[i])

		# stack now contains result points. Return stack
		return stack

	# Use scipy.spatial library; test if p inside points hull
	def in_hull(self, points, p):
		hull = ConvexHull(points)
		new_points = np.append(points, p, axis=0)
		new_hull = ConvexHull(new_points)
		return list(hull.vertices) == list(new_hull.vertices)
	
	# Higher demension case
	def higher_d_in_hull(self, points, hull):
		if not isinstance(hull, Delaunay):
			hull = Delaunay(hull)
		return hull.find_simplex(points) >= 0

###################################################################################	
	# next_to_top() helper function. Return second top element
	# in the stack
	def next_to_top(self, stack):
		return stack[-2]

	# swap() helper function. Swap values of two points
	def swap(self, p1, p2):
		# type p1, p2: Point
		p1.x, p2.x = p2.x, p1.x
		p1.y, p2.y = p2.y, p1.y

	# sq_dist() calculate the square distance between
	# 2 points
	def sq_dist(self, p1, p2):
		# type p1, p2: Point
		return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

	# orientation() find orientation of ordered tuple
	# (point1, point2, point3)
	# return 0 if three points are on same line
	# 1 means clockwise. 2 means counterclockwise
	def orientation(self, p1, p2, p3):
		val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
		if val == 0: return 0
		elif val > 0: return 1
		else: return 2

	# compare() compares two points against base point.
	# return -1 or 1 based on position
	def compare(self, p1, p2):
		base = self.base
		val = self.orientation(base, p1, p2)
		if val == 0:
			if self.sq_dist(base, p2) >= self.sq_dist(base, p1): return -1

		if val == 2: return -1
		else: return 1
