# polygon splitting in python, part a
#  by Ryan Soussan
# The algorithm starts with the first vertex in the list
# and finds a new point on the polygon such that a line drawn 
# through the first and new point will split the polygon  
# into two polygons of approximately equal area

import json

def split_polygon(pointlist): 
	area = getPolygonArea(pointlist)
	vert_temp = json.dumps(pointlist)
	vertices = json.loads(vert_temp)
	max_error = 0.0001
	summed_triangles_area = 0
	too_large_triangle_area = 0
	i = 1
	#add triangles until surpass half of total area
	while (summed_triangles_area < area/2):
		triangle_area = getTriangleArea(vertices[0][0],vertices[0][1],vertices[i][0],vertices[i][1],vertices[i+1][0],vertices[i+1][1])
		summed_triangles_area = summed_triangles_area + triangle_area
		i = i+1
	too_large_triangle_area = triangle_area
	#find new point
	too_large_vertex = i
	start_x = vertices[too_large_vertex-1][0]
	start_y = vertices[too_large_vertex-1][1]
	end_x = vertices[too_large_vertex][0]
	end_y = vertices[too_large_vertex][1]
	summed_triangles_area = summed_triangles_area - too_large_triangle_area
	desired_area = area/2 - summed_triangles_area
	new_triangle_area = 0
	fraction = 1.0/2
	max_frac = 1
	min_frac = 0
	iterations = 1
	while ((new_triangle_area - desired_area)*(new_triangle_area - desired_area) > max_error*max_error):
		#binary search along line of too large vertex and not large enough vertex for new point
		new_x = start_x + fraction*(end_x - start_x)
		new_y = start_y + fraction*(end_y - start_y)
		new_triangle_area = getTriangleArea(vertices[0][0],vertices[0][1],start_x,start_y,new_x,new_y)
		if (new_triangle_area - desired_area) > 0:
			max_frac = fraction
			fraction = (max_frac + min_frac)/2
		else:
			min_frac = fraction
			fraction = (max_frac + min_frac)/2
		iterations = iterations+1
	# Testing Code
	#
	# poly1 = []
	# poly2 = []
	# print "too_large_vertex =", too_large_vertex
	# for j in range(0,too_large_vertex):
	# 	poly1.append(vertices[j])
	# new_point = new_x,new_y
	# poly1.append(new_point)
	# origin  = vertices[0]
	# poly2.append(origin)
	# poly2.append(new_point)
	# size = len(vertices)
	# for j in range(too_large_vertex,size):
	# 	poly2.append(vertices[j])
	# area1 = getPolygonArea(poly1)
	# area2 = getPolygonArea(poly2)
	# print "vertices =", vertices
	# print "poly1 =",poly1
	# print "poly2 =",poly2
	# print "area1 = ",area1
	# print "area2 = ",area2
	# print "sum areas =", area1+area2
	# print "difference =", area - area1-area2

	return new_x,new_y




def getTriangleArea(A_x,A_y,B_x,B_y,C_x,C_y):
	area = A_x*(B_y-C_y) + B_x*(C_y-A_y) + C_x*(A_y-B_y)
	area = area/2
	if (area < 0):
		area = area*(-1)
	return area


def getPolygonArea(pointlist):
	vert_temp = json.dumps(pointlist)
	vertices = json.loads(vert_temp) 
	area = 0
	size = len(vertices)
	j = size-1
	for i in range(0,size):
		area = area + (vertices[j][0] + vertices[i][0])*(vertices[i][1] - vertices[j][1])
		j = i
	return area/2