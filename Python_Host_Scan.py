#!C:\python\python 

import cgi

class Python_Host_Scanner:

    def __init__(self):
        print("Content-type:text/html\r\n\r\n")
        print("<html><body>")
        self.init_WebForm()
	
    def init_WebForm(self):
        print("<h2><center><span style=\"color:gold\"> WELCOME TO PYTHON HOST SCANNER</span><center> </h2>")
        print ("<form mehtod='post' action='Scanning_Update.py'>")
        print("<table border=\"1\"> <col width=\"200\"><col width=\"1000\">")
        print("<tr> <td align=\"center\"> Host IP: </td> ")
        print("<td align=\"center\"><input type ='text' name='ip'/></td></tr>")
        print("<tr><td colspan=\"2\"> <input type='submit' value='SCAN' /></td><tr>")
        print("</table>")
        print("</form>")
        print("</body></html>")
	

pht = Python_Host_Scanner()
