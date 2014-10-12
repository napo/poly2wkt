poly2wkt
========

a converter from POLY format to WKT with spatial sql syntax

A script to convert a polygon used in OpenStreetMap in WKT format
http://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format

```
usage: poly2wkt.py [-h] [-o OUTFILE] [-i] [-c] [-t] [-s] infile

convert a .poly file in .wkt format

positional arguments:
  infile             inputfile

optional arguments:
  -h, --help         show this help message and exit
  -o OUTFILE         output file
  -i, --insertsql    create insert sql string
  -c, --createtable  create sql string with create table
  -t, --tablename    to assign a name of the table (default=poly
  -s, --silent       dont'show output (default behavior)
```
