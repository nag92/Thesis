import numpy as np

def eq(ang, a=1.0):
    theta = np.radians(ang)
    return a*(1.08 * pow(theta, 4) - 11.18 * pow(theta, 3) + 26.54 * pow(theta, 2) - 0.825 * theta)

def make_file(min_dist,max_dist, name):

    theta = np.radians(70)
    #d = 289-273.2
    d = max_dist-min_dist
    dem = eq(70)
    min_angle = 0
    max_angle = 145
    step = 5
    msg = "my_offset_"

    a = d/dem
    with open (name + ".txt", 'w') as f:
        f.write(" \"name\" =" + name + "\n")
        f.write(" \"a\" =" + str(a) + "\n")
        current_angle = min_angle
        while current_angle < max_angle:
            trans = eq(current_angle)
            f.write("\"" +  msg + str(current_angle) + "\"" + "=" + str(trans) + "mm \n" )
            current_angle+=step


