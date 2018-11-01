#!C:\python\python

import cgi
from socket import *
import HostScannerDAL as HSD
import threading

print("Content-type:text/html\r\n\r\n")
host_id = None
form = cgi.FieldStorage()
if form.getvalue("ip"):
    host_id = form.getvalue("ip")

class Helper_Python_Host_Scanner():
    def __init__(self, host_id):
        print("<html><head>")
        print("<center>")
        print("<h3> SCANNING PAGE </h3>")
        print("</center>")
        print("<body>")
        print ("<p>Received Host ID =  " + host_id + "</p>")
        print("</body>")
        print("</head></html>")
        self.update_host_name()
	# store value of ip address from user
	# store value from user hostname
	
    def update_host_name(self):
        print("<html><body>")
        self.host_name = gethostbyaddr(host_id)
        print("<p>Started scanning = " + self.host_name[0] + "</p>")
        print("</body></html>")
        self.start_scan()
        
    def start_scan(self):
        ob=HSD.HostScannerDAL()
        self.host_num=ob.create_host(host_id,self.host_name[0])
        self.scanid=ob.create_scan(self.host_num)
        self.scan_port(130,140)
	# gets the host number from Hosts table in DAL
	# calls the create scan table method in DAL

    def scan_port(self, min_port, max_port):
        s=socket(AF_INET,SOCK_STREAM)
        ob=HSD.HostScannerDAL()
        for port in range(min_port,max_port):
            code=s.connect_ex((host_id,port))
            print("<html><body>")
            print("<p>Started port number " + str(port) + ", for given Host -->"+host_id+"</p>")
            if code==0:
                #print("port open")
                is_open=0
                pass
            else:
                is_open=1
                #print("closed")
                pass
            ob.create_port_status(self.scanid,port,is_open)
        
        print("<p> Finished scanning </p>")
        s.close()
        ob.update_scan_end_time(self.scanid)
        print ("<form mehtod='post' action='Switch_Result.py'>")
        print("<input type='submit' value='View Results' />")
        print("<input type='hidden' name='host_id' value='%s'/>"%(host_id))
        print("<input type='hidden' name='host_name' value='%s'/>"%(self.host_name[0]))
        print("</form>")
        print("</body></html>")	
	# Updates which port number is being scanned to the HTML page
    	# Update the scan table for scan completion time
	

if host_id is not None:
    Helper_Python_Host_Scanner(host_id)

else:
    print('''

            <html> 
                <head>
                <style>
                </style>
                <center> 
                        <h3> SCANNING PAGE </h3>
                </center> 
            </head>
            <body>
                          
                    Received host = Host ID not received
              
            </body>
            </html>
            '''
          )
