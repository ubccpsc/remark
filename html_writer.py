class Writer:
    outfile = ""
    passcolor = "A8C881"
    accomcolor = "orange"
    failcolor = "E6B5B5"
    retakepasscolor = "E0E9CF"
    mainheadercolor = "silver"
    innerheadercolor = "ECECEC"
    linecolor = "black"

    def __init__(self, file):
        self.outfile = open(file, 'wb')
        self.outfile.write("<html><center><table width=90%><tr><td>\n")

    def startTable(self):
        self.outfile.write("<table width=90% bgcolor=" + self.linecolor + " cellpadding=5 cellspacing=1 style=\"font-family:Arial; font-size:12\">\n")


    def endTable(self):
        self.outfile.write("</table>")


    def writeTableRow(self, csvrow):
        self.outfile.write(
            "<tr><td bgcolor=\"white\">" + "</td><td bgcolor=\"white\">".join(str(x) for x in csvrow) + "</td></tr>\n")

    def writeColorTableRow(self, csvrow, color):
        joinstring = "</td><td bgcolor=\"" + color + "\">"
        self.outfile.write(
            "<tr><td bgcolor=\"" + color + "\">" + joinstring.join(str(x) for x in csvrow) + "</td></tr>\n")

    def writeTableHeader(self, csvrow):
        joinstring = "</td><td bgcolor=\"" + self.mainheadercolor + "\">"
        self.outfile.write("<tr><td bgcolor=\"" + self.mainheadercolor + "\">" + joinstring.join(
                str(x) for x in csvrow) + "</td></tr>\n")

    def writeTableTitle(self, csvrow,cols):
        self.outfile.write("<tr><td bgcolor=\"" + self.mainheadercolor + "\" colspan="+str(cols)+"><h1>" + csvrow + "</td></tr>\n")

    def writeColspannedHeader(self, text, tag,cols):
        self.outfile.write("<tr><td bgcolor=\"" + self.innerheadercolor + "\" colspan="+str(cols)+">" + tag + text + "</td></tr>\n")

    def startTableRow(self):
        self.outfile.write("<tr>")

    def writeColorCell(self, cell, color):
        colorstring = "<td bgcolor=\"" + color + "\">"
        self.outfile.write(colorstring + str(cell) + "</td>\n")

    def writeCell(self, cell):
        colorstring = "<td bgcolor=\"white\">"
        self.outfile.write(colorstring + str(cell) + "</td>\n")

    def endTableRow(self):
        self.outfile.write("</tr>")

    def insert_break(self):
        self.outfile.write("<br><br><br>")


    def close(self):
        self.outfile.write("</td></tr></table>")
        self.outfile.close()