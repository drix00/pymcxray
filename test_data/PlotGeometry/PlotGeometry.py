#!/usr/bin/python3

from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

sam_in = open("FeAl_sphere.sam","r")
#sam_in = open("Alcylinder.sam","r")

lines = sam_in.readlines()
sam_in.close();
del lines[0:21]

# Get number of regions
Nregions_str = lines[0]
Nregions = int(Nregions_str[-2])
del lines[0:2]
del lines[-1]

elts = [[] for _ in range(Nregions)]
shape = []
param = [] 
reg = []
regtemp = []

# Split data into regions and extract numbers
for lin in lines:
    if lin!="\n" and lin[0:4]!="User":
        lin=lin[:-1]
        regtemp.append(lin.split("=",1)[1])
    elif lin=="\n":
        reg.append(regtemp)
        regtemp = []
reg.append(regtemp)
del regtemp

cnt = 0
for i in reg:
    nel = int(i[0])
    if nel==0:
        elts[cnt].append(0)
    for j in range(1,(2*nel+1)):
        elts[cnt].append(float(i[j]))

    # Box is equal to 0, sphere is equal to 1
    if i[2*nel+1] == "BOX":
        shape.append(0)
        param.append(i[-1].split())
    elif i[2*nel+1] == "SPHERE":
        shape.append(1)
        param.append(i[-1].split())
    elif i[2*nel+1] == "CYLINDER":
        shape.append(2)
        param.append(i[-1].split())
    cnt+=1

# Set geometry parameters in nm
param = [[(float(j)/10) for j in i] for i in param]

# Plot shapes
def rect_prism(x_range,y_range,z_range):
    xx,yy = np.meshgrid(x_range,y_range)
    ax.plot_wireframe(xx,yy,z_range[0])
    ax.plot_surface(xx,yy,z_range[0],alpha=0.2)
    ax.plot_wireframe(xx,yy,z_range[1])
    ax.plot_surface(xx,yy,z_range[1],alpha=0.2)

    yy,zz = np.meshgrid(y_range,z_range)
    ax.plot_wireframe(x_range[0],yy,zz)
    ax.plot_surface(x_range[0],yy,zz,alpha=0.2)
    ax.plot_wireframe(x_range[1],yy,zz)
    ax.plot_surface(x_range[1],yy,zz,alpha=0.2)

    xx,zz = np.meshgrid(x_range,z_range)
    ax.plot_wireframe(xx,y_range[0],zz)
    ax.plot_surface(xx,y_range[0],zz,alpha=0.2)
    ax.plot_wireframe(xx,y_range[1],zz)
    ax.plot_surface(xx,y_range[1],zz,alpha=0.2)

def sphere(x0,y0,z0,r):
    theta = np.linspace(0,2*np.pi,100)
    phi = np.linspace(0,np.pi,100)
    
    x = r*np.outer(np.cos(theta),np.sin(phi))+x0
    y = r*np.outer(np.sin(theta),np.sin(phi))+y0
    z = r*np.outer(np.ones(np.size(theta)),np.cos(phi))+z0

    ax.plot_surface(x,y,z,alpha = 0.4)

def cylinder(x0,y0,z0,xd,yd,zd,r,h):
    X = np.linspace(x0-r,x0+r,100)
    Z = np.linspace(z0,z0+h,100)

    xx,zz = np.meshgrid(X,Z)
    yy = np.sqrt(r**2-(xx-x0)**2)+y0

    u = np.array([0,0,1])
    direc = np.array([xd,yd,zd])
    beta = np.arccos(np.dot(u,direc)/(LA.norm(u)*LA.norm(direc)))
    nu = np.cross(u,direc)
    nu = nu/LA.norm(nu)

    Rot = np.zeros(shape=(3,3))
    Rot[0][0] = np.cos(beta)+nu[0]*nu[0]*(1-np.cos(beta));
    Rot[0][1] = nu[0]*nu[1]*(1-np.cos(beta))-nu[2]*np.sin(beta);
    Rot[0][2] = nu[0]*nu[2]*(1-np.cos(beta))+nu[1]*np.sin(beta);
    Rot[1][0] = nu[1]*nu[0]*(1-np.cos(beta))+nu[2]*np.sin(beta);
    Rot[1][1] = np.cos(beta)+nu[1]*nu[1]*(1-np.cos(beta));
    Rot[1][2] = nu[1]*nu[2]*(1-np.cos(beta))-nu[0]*np.sin(beta);
    Rot[2][0] = nu[2]*nu[0]*(1-np.cos(beta))-nu[1]*np.sin(beta);
    Rot[2][1] = nu[2]*nu[1]*(1-np.cos(beta))+nu[0]*np.sin(beta);
    Rot[2][2] = np.cos(beta)+nu[2]*nu[2]*(1-np.cos(beta));

    xxp = np.zeros(shape=(100,100))
    yyp = np.zeros(shape=(100,100))
    zzp = np.zeros(shape=(100,100))
    xxm = np.zeros(shape=(100,100))
    yym = np.zeros(shape=(100,100))
    zzm = np.zeros(shape=(100,100))

    for i in range(0,100):
        for j in range(0,100):
            vec_oldp = np.array([xx[i][j],yy[i][j],zz[i][j]])
            vec_newp = np.matmul(Rot,vec_oldp)
            vec_oldm = np.array([xx[i][j],-yy[i][j],zz[i][j]])
            vec_newm = np.matmul(Rot,vec_oldm)
            xxp[i][j] = vec_newp[0]
            yyp[i][j] = vec_newp[1]
            zzp[i][j] = vec_newp[2]
            xxm[i][j] = vec_newm[0]
            yym[i][j] = vec_newm[1]
            zzm[i][j] = vec_newm[2]

    ax.plot_surface(xxp,yyp,zzp,alpha=0.2)
    ax.plot_surface(xxm,yym,zzm,alpha=0.2)

#    floor = Circle((x0, y0), r,alpha=0.2)
#    ax.add_patch(floor)
#    art3d.pathpatch_2d_to_3d(floor, z=z0, zdir="z")
#
#    ceiling = Circle((x0, y0), r, alpha = 0.2)
#    ax.add_patch(ceiling)
#    art3d.pathpatch_2d_to_3d(ceiling, z=z0+h, zdir="z")
    
#####################################################
fig = plt.figure()
ax = fig.gca(projection='3d')
colormap = plt.cm.gist_ncar
plt.gca().set_prop_cycle(plt.cycler('color',plt.cm.jet(np.linspace(0,1,Nregions))))
#ax.set_aspect("equal")

for i in range(0,Nregions):
    if elts[i] == [0]:
        continue
    if shape[i] == 0:
        X=np.array([param[i][0],param[i][1]])
        Y=np.array([param[i][2],param[i][3]])
        Z=np.array([param[i][4],param[i][5]])

        rect_prism(X,Y,Z)
    if shape[i] == 1:
        sphere(param[i][0],param[i][1],param[i][2],param[i][3])
    if shape[i] == 2:
        cylinder(param[i][0],param[i][1],param[i][2],param[i][3]*10,param[i][4]*10,param[i][5]*10,param[i][6],param[i][7])

ax.set_aspect("equal")
ax.set_xlabel('X (nm)')
ax.set_ylabel('Y (nm)')
ax.set_zlabel('Z (nm)')
plt.show()

