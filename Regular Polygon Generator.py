import matplotlib.pyplot as plt
import numpy as np

print ("Number of sides:")
num_sides = input()
if type(num_sides) == type(1) and num_sides >= 3:
    num = num_sides
    print ("Length of each side:")
    len_sides = input()
    #i=0
    if type(len_sides) != type('a') and len_sides > 0:
        len = len_sides
        theta = 2*np.pi/num
        alpha = np.linspace(0, 2*np.pi, num)
        r = 0.5*len / (np.sin(0.5*theta))
        #p1 = (r, theta*i+0.5*np.pi)
        #p2 = (r, theta*(i+1)+0.5*np.pi)
        #verts = [(r, alpha)]
        #verts = unit_poly_verts(alpha)
        #path = Path(verts)
        #i=i+1
    else: print ("Illegal input detected! Please reinput.")
else: print ("Illegal input detected! Please reinput.")

def unit_poly_verts(alpha):
    verts = [(r, t) for t in alpha]
    return verts

def draw_poly_patch(self):
    verts = unit_poly_verts(alpha)
    return plt.Polygon(verts, closed=True, edgecolor='k')

plt.show()