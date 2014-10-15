#!/usr/bin/python
import sys
import argparse
def loopfile(polyfile):
	polyline=''
	with open(polyfile,'r') as f:
		read_data = f.readlines()
	f.close()
	polylines = []
	polyline = ""
	countend = 0
#	countpoly = 0
	for l in read_data:
		s = l.strip()
		if len(s) > 1:
		    try:
		        x = ''
		        y = ''
		        if int(s[0]) > -180:
		            xy = s.split(" ")
		            x = xy[0]
		            for v in xy:
		                if x != v:
		                    if len(v) > 1:
		                        if int(v[0])> -90:
		                            y = v
		            polyline += x + " " + y + ","
		    except ValueError:
		        pass

		if len(s) == 1:
                  polyline = "("
#		    countpoly += 1
#		    if countpoly == 1:
#		        polyline = "POLYGON (("
#                     
#		    else:
#		        polyline = "POLYGON (("
		if s == "END":
		    countend += 1
		    if (countend%2) == 1:
		        polyline = polyline[0:len(polyline)-1]
		        polyline += ")" #)"
		        polylines.append(polyline)
	return polylines
 
def createwkt(polylines):
    polygon=""
    if len(polylines) >0:
        polygon = "POLYGON ("
        for p in polylines:
            polygon += p +","
        polygon = polygon[0:len(polygon)-1]
        polygon += ")"
    return polygon
    
parser = argparse.ArgumentParser(description='convert a .poly file in .wkt format')
parser.add_argument('infile', metavar='infile', type=str,
                   help='inputfile')
parser.add_argument('-o',dest='outfile', type=str,help='output file',default=None)
parser.add_argument('-i', '--insertsql', dest='sqlstring',default=False,action='store_true',
                help='create insert sql string')
parser.add_argument('-c', '--createtable', dest='createtable',default=False,action='store_true',
                help='create sql string with create table')
parser.add_argument('-t', '--tablename', dest='tablename',default='poly',action='store_true',
                help='to assign a name of the table (default=poly')
parser.add_argument('-s','--silent', dest='silent',help="dont'show output, if you don't need a output file this is si default",
                    action='store_true',default=False)
args = parser.parse_args()

tablename = args.tablename
wkt = createwkt(loopfile(args.infile))
out = None

if (args.sqlstring):
    out = "INSERT INTO %s (geom) values (GeometryFromText('%s'),4326))\n;" % (tablename,wkt)
if (args.createtable):
    out = "CREATE TABLE %s (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT);\n" % (tablename)
    out += "SELECT AddGeometryColumn('%s', 'geom', 4326, 'POLYGON', 2);\n" % (tablename)
    out += "INSERT INTO %s (geom) values (GeometryFromText('%s',4326));\n" % (tablename,wkt)
if out == "":
    out = wkt
if (out is None):
    out = wkt
    
if (args.outfile is not None):
    with open(args.outfile,'w') as f:
        f.write(out)
        f.close()

if (args.silent == False):
    print out




