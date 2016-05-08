# polygon splitting in python, part b
#  by Ryan Soussan
# Same algorithm as in part a, except 
# the list is first sorted into counterclockwise
# order by converting to polar coordinates and back

import json, math

def split_polygon(pointlist): 
	sorted_list = sortList(pointlist)
	area = getPolygonArea(sorted_list)
	vertices = sorted_list
	max_error = 0.0001
	summed_triangles_area = 0
	too_large_triangle_area = 0
	i = 1
	#add triangles until surpass half of total area
	while (summed_triangles_area < area/2):
		triangle_area = getTriangleArea(vertices[0][0],vertices[0][1],vertices[i][0],vertices[i][1],vertices[i+1][0],vertices[i+1][1])
		summed_triangles_area = summed_triangles_area + triangle_area
		too_large_triangle_area = triangle_area
		i = i+1
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
		#binomial search along line of too large vertex and not large enough vertex for new point
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
	return new_x,new_y


def sortList(pointlist):
	vert_temp = json.dumps(pointlist)
	Vertices = json.loads(vert_temp) 
	size = len(Vertices)
	#convert to polar coordinates
	for i in range(0,size):
		x = Vertices[i][0]
		y = Vertices[i][1]
		r = math.sqrt(x*x + y*y)
		theta = math.atan2(y,x)
		if (theta < 0):
			theta = theta + 2*math.pi
		Vertices[i] = r,theta
	# sort in counterclockwise order
	Vertices = sorted(Vertices, key=lambda x: x[0])
	Vertices = sorted(Vertices, key=lambda x: x[1])
	#convert back to cartesian coordinates
	for i in range(0,size):
		r = Vertices[i][0]
		theta = Vertices[i][1]
		x = r*math.cos(theta)
		y = r*math.sin(theta)
		Vertices[i] = x,y
	return Vertices
	

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