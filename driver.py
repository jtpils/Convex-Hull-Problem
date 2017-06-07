from Solution import Solution
from Point import Point
import numpy as np

s = Solution()
points = [Point(0,3), Point(1,1), Point(2,2), Point(4,4), Point(0,0), Point(1,2), Point(3,1), Point(3,3)]
n = len(points)
res = [(p.x, p.y) for p in s.solution(points, n)]
print "Corner Points of the Convex Hull:"
print res

# Randomly generate a 2-D point to test using ConvexHull class
test = np.random.rand(1,2)
print "Test Point:"
print test
print "In Convex Hull?"
print s.in_hull(res, test)

# Extend to 3-D points. Randomly generate test point and hull points using
# Delaunay class
tested = np.random.rand(1,3)
cloud  = np.random.rand(50,3)

print "3-D Case:"
print "Test Points:"
print tested
print "In Convex Hull?"
print s.higher_d_in_hull(tested,cloud)