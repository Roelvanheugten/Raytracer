import numpy as np



center = (0.5,0.79,1)
maxdist = 350

def distantcenter(maxdist,center):
    factor = (maxdist/np.sqrt(center[0]**2 + center[1]**2+center[2]**2))
    distantcenter = (factor*center[0],factor*center[1],factor*center[2])
    return distantcenter,factor

distcenter = distantcenter(maxdist,center)[0]
factor = distantcenter(maxdist,center)[1]

def cartesian_to_spherical(x, y, z):
    # Calculate the radius
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)

    # Calculate the polar angle
    theta = np.arccos(z / r)

    # Calculate the azimuthal angle
    phi = np.arctan2(y, x)

    return r, theta, phi
def grid(centercoord,numlength,Size,factor):
    stepsize = Size/numlength
    xpixels = []
    ypixels = []
    zpixels = []
    radius, theta, phi = cartesian_to_spherical(centercoord[0],centercoord[1],centercoord[2])
    angle = Size/radius
    print(centercoord[0],radius*np.sin(theta)*np.cos(phi))
    print(centercoord[1],radius*np.sin(theta)*np.sin(phi))
    print(centercoord[2],radius*np.cos(theta))
    #i is x direction j is y direction
    anglepart = angle/numlength
    for i in range(numlength):
        thetastep = theta + angle/2 -anglepart*i
        for j in range(numlength):
            phistep = phi + angle / 2 - anglepart*j
            x = radius*np.sin(thetastep)*np.cos(phistep)
            y = radius*np.sin(thetastep)*np.sin(phistep)
            z = radius*np.cos(thetastep)
            xpixels.append(x)
            ypixels.append(y)
            zpixels.append(z)
    return xpixels,ypixels,zpixels

file_path = 'Catalog_file.txt'
Pixelnumber = 300
Sizefield = 10
coordinates = grid(distcenter,Pixelnumber,Sizefield,factor)

with open(file_path, 'w') as file:
    file.write('X Y Z VX VY VZ\n')
    for i in range(len(coordinates[0])):
        file.write(f'{coordinates[0][i]}, {coordinates[1][i]}, {coordinates[2][i]}, 0, 0, 0\n')