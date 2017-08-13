# -*- coding: utf-8 -*-
#####
#Lamparski Jakub, 3.12.2016
#v2.0
#Program computes azimuth between all points in the csv file (all combinations). Output in gradians.
#Output is placed into the same directory as input
#####

from math import atan
from math import pi
from math import fabs
import os
import sys
from itertools import combinations

print
print "Program computes azimuth between all points in the csv file (all combinations). Output in gradians."
print "Every point in the file should be formated in the following form: n;x;y"
print "where: n - number of point, x,y - cartesian point coordinates in geodetic axis layout (X - axis of ordinates, Y - axis of abscissas)."
print "Full stop decimal mark."
csv_input = raw_input("Path to csv: ")
extension = os.path.splitext(csv_input)[1]

if extension != ".csv":
    csv_input += ".csv"
else:
    csv_input = csv_input

data_list = []
fh = open(csv_input, 'r')
for line in fh:
    data_list.append(line.strip().split(';'))

nrlist = []
for every_list in data_list:
    nrlist.append(every_list[0])
xlist = []
for every_list in data_list:
    xlist.append(float(every_list[1]))
ylist = []
for every_list in data_list:
    ylist.append(float(every_list[2]))

coordinates = zip(xlist,ylist)

def azimuth(p,k):
    xp,yp = p
    xk,yk = k
    dx = xk - xp
    dy = yk - yp
    division = dy/dx
    adiv = fabs(division)
    fi = atan(adiv)
    if dy > 0 and dx > 0:
        fi = fi
    elif dy > 0 and dx < 0:
        fi = pi-fi
    elif dy < 0 and dx < 0:
        fi = fi+pi
    elif dy < 0 and dx > 0:
        fi = 2*pi-fi
    if fi > 2*pi:
        fi = fi - 2 * pi
        fi = fi*(200/pi)
        return fi
    else:
        fi = fi * (200 / pi)
        return fi

def numeration(nrp,nrk):
    return str(nrp)+" i "+str(nrk)

comb_a = [azimuth(*combo) for combo in combinations(coordinates,2)]
comb_nr = [numeration(*combo) for combo in combinations(nrlist,2)]

combo_list = []
numeration_list = []
for every_a in comb_a:
    combo_list.append(every_a)
for every_nr in comb_nr:
    numeration_list.append(every_nr)

rev_azimuth = 0
rev_azimuth_list = []

for every_azimuth in combo_list:
    if every_azimuth < 200:
        rev_azimuth = every_azimuth + 200
        rev_azimuth_list.append(rev_azimuth)
    elif every_azimuth > 200:
        rev_azimuth = every_azimuth - 200
        rev_azimuth_list.append(rev_azimuth)
    elif every_azimuth == 200:
        rev_azimuth = 0
        rev_azimuth_list.append(rev_azimuth)


a_nr = zip(numeration_list,combo_list,rev_azimuth_list)

output_path = str(os.path.dirname(csv_input))+"\\"+"output.txt"
sys.stdout = open(output_path, 'w')

for every_item in a_nr:
    nr = every_item[0]
    a = every_item[1]
    r = every_item[2]
    print "Azimuth between points %s = %f. Inverse azimuth = %f." % (nr, a, r)