'''
Created on Jun 6, 2012

@author: Joe
'''

from pyquery import PyQuery as pq
import re

d = pq(url='http://wiki.vg/Protocol')
out = open("../Packets.py", "w")

out.write("import Types\n" "\n"
          "structures = []\n"
          "\n")

headings = d("h3 span.mw-headline")
for heading in headings:
    node = d(heading)
    packet_name = node.text()
    packet_id = re.match("^.*\((0x[0-9A-F]+)\).*$",packet_name).group(1)
    table = node.parent().nextAll("table").eq(0)("tr")
    #print "table %s" % table
    
    types = []
    
    i = 0
    for rowi in table:
        tnode = table(rowi)("td")
        if tnode.eq(0).text() != None and len(tnode) > 2:
            count = len(tnode)
            #print "%s %s\t\t%s\t\t%s" % (packet_id, packet_name, tnode.eq(count-3).text(), tnode.eq(count-4).text())
            
            dtype = tnode.eq(count-3).text().strip().lower()
            dname = tnode.eq(count-4).text()
            ntype = "*"+dtype+"*"
            if dtype == "byte":
                ntype = "Types.Byte"
            elif dtype == "unsigned byte":
                ntype = "Types.UnsignedByte"
                
            elif dtype == "short":
                ntype = "Types.Short"
            elif dtype == "unsigned short":
                ntype = "Types.UnsignedShort"
                
            elif dtype == "int":
                ntype = "Types.Integer"
            elif dtype == "long":
                ntype = "Types.Long"
            elif dtype == "float":
                ntype = "Types.Float"
            elif dtype == "double":
                ntype = "Types.Double"
            elif dtype == "string":
                ntype = "Types.String"
            elif dtype == "boolean" or dtype == "bool":
                ntype = "Types.Bool"
            elif dtype == "metadata":
                ntype = "Types.Metadata"
            types.append(ntype)
            
    #print packet_name+" "+str(types)
    #sout = '#%s\nstructures[%s] = (' % (packet_name, packet_id)
    sout = ''
    for dtype in types:
        if dtype[0] == "*":
            dtype = "'"+dtype+"'"
        sout = sout+dtype+", "
    sout = "#%s\nstructures[%s] = (%s)\n\n" % (packet_name, packet_id,sout[0:len(sout)-2])
    out.write(sout.encode('iso-8859-1'))