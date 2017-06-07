"""
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

"""
from Point import Point

class Solution(object):
	def solution(self, points, n):
		# type points: List[Point]
		# type n: int
		# rtype: List[Point]




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
	def orientation(p1, p2, p3):
		val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
		if val == 0: return 0
		elif val > 0: return 1
		else: return 2

	# compare() compares two points against base point.
	# return -1 or 1 based on position
	def compare(self, p1, p2):
		val = self.orientation(base, p1, p2)
		if val == 0:
			if self.sq_dist(base, p2) >= self.sq_dist(base, p1): return -1

		if val == 2: return -1
		else: return 1


