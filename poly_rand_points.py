# create random vertices in counterclockwise order
import random,math

def rand_list(size):
	r_max = 100.000
	r_min = 0.000
	theta_max = 2*math.pi
	theta_min = 0.000
	Vertices = []

	for i in range(0,size):
		r = random.uniform(r_min, r_max)
		theta = random.uniform(theta_min,theta_max)
		x = r,theta
		Vertices.append(x)
	#toggle sorted for poly_a and poly_b	
	Vertices = sorted(Vertices, key=lambda x: x[0])
	Vertices = sorted(Vertices, key=lambda x: x[1])
	for i in range(0,size):
		r = Vertices[i][0]
		theta = Vertices[i][1]
		x = r*math.cos(theta)
		y = r*math.sin(theta)
		Vertices[i] = x,y
	return Vertices
