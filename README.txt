A solution to the following question:
A 2D polygon is described by a list of points  [(x1,y1), (x2,y2),.(xn, yn)], where n is number of vertices (3 < n < = 50), and a list of x and y coordinates for each vertex, described in counter-clockwise order. Coordinates are real numbers, and go from -100.000 to 100.000 (at most 3 digits after decimal point). Example input: [(0,0), (4,0), (4,3), (0,3)].

  a) In Python (or Java or some reasonable language), write a function split_polygon(JSON pointlist) that returns a line [(x1,y1),(x2,y2)] where the points of the line lie on the polygon, and the line splits the polygon into two segments of equal area (accurate to 0.0001).

  b) Challenge: what if the polygon vertices are *not* listed in counter-clockwise order? Assume the shape is non-overlapping. What would your algorithm look like in this case?

poly_a.py solve part a and pol_b.py solves part b.  poly_rand_points.py is a helper function to generate random polygon vertices and poly_drawer.py is another helper function to print polygons and the solution line given by the poly_a or poly_b scripts.
