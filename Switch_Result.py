#!C:\python\python


import cgi
import HostScannerDAL as HSD
import GUI_Display as GD
import threading

print("Content-type:text/html\r\n\r\n")
form = cgi.FieldStorage()
if form.getvalue("host_id"):
    host_id = form.getvalue("host_id")
if form.getvalue("host_name"):
    host_name=form.getvalue("host_name")
#host_id='192.168.1.11'
#host_name='DESKTOP-HNEACAF.home'
class Switch_Result ():
    def __init__(self, hst_id, hst_name):
        self.ip_add=hst_id
        self.h_nam=hst_name
        self.Switch_Results()

    def Switch_Results(self):
        c=HSD.HostScannerDAL()
        dat = c.read_port_status(self.ip_add, self.h_nam)
        ti=c.read_host(self.ip_add)
        for el in ti:
            tim=el[2]
        datli=[]
        for elements in dat:
            datli.append(list(elements))
        for elements in datli:
            elements.append(tim)
        print("<html><head>")
        print("<center>")
        print("<h3> RESULTS PAGE </h3>")
        print("</center>")
        print("<body>")
        print("<table border=\"1\">")
        print("<col width=\"20\"><col width=\"20\"><col width=\"20\"><col width=\"200\">")
        print("<tr><td>SCAN_ID</td><td>PORT_NUMBER</td><td>IS_OPEN</td><td align=\"center\">SCAN_TIME</td></tr>")
        print("</table>")
        html = """<HTML> <body><table><col width=\"60\"><col width=\"140\"><col width=\"60\"><col width=\"200\">{0}</table></body></HTML>"""
        tr = "<tr>{0}</tr>"
        td = "<td align=\"center\">{0}</td>"
        subitems=[tr.format(''.join([td.format(a) for a in item])) for item in reversed (datli)]
        print (html.format("".join(subitems)))
        print("</body>")
        print("</head></html>")
##        thr2 = threading.Thread(target=self.CGUI())
##        thr2.start()
##        thr2.join()

    def CGUI(self):
        self.GDD = GD.ResultsDialog(self.ip_add, self.h_nam)
        
r=Switch_Result(host_id,host_name)
