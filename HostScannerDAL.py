import sqlite3 as db
import time

class HostScannerDAL:
    def __init__(self):
        self.is_conn_open = False
        self.__connect_()

    def __connect_(self):
        self.conn= db.connect("C:/Apache24/htdocs/HostScanner.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM HOST")
        rows = self.cur.fetchall()
        self.elements=[]
        for row in rows:
            rowDict = dict(zip([c[0] for c in self.cur.description], row))
            self.elements.append(rowDict)
##            '''
##		Connect to database using the .db file provided
##				
##		'''
##		# connect to the database
##		# retrieve the values in form of db dictionary
##		# create a new cursor
##	#if not self.is_conn_open:
	
    def read_host(self, host_ip, host_name=None):
        for i in self.elements:
            if i['HostIP']!=host_ip:
                pass
            else:
                readhost=i
        query=''' SELECT * FROM Scan
                 Where HostID = ?'''
        self.cur.execute(query,(readhost['HostId'],))
        timeentry=self.cur.fetchall()
        return timeentry
		
		# CHECKS IF THE RECORD IS ALREADY PRESENT AND GIVES A VARIABLE
		
		# CHECK FOR THE FIRST TIME ENTRY
	
		#return read_host_result
    def create_host(self, host_ip, host_name):
        inr=0
        self.return_host_numb=0
        for i in self.elements:
            if i['HostIP']==host_ip:
                inr=1
                self.return_host_numb=i['HostId']
        if inr==0:
            self.cur.execute("select HostId from HOST where HostId IN (select max(HostId) from HOST)")
            li=self.cur.fetchone()
            self.cur.execute("CREATE TABLE IF NOT EXISTS HOST(HostID,HostIP,HostName)")
            self.cur.execute('''INSERT INTO HOST(HostID,HostIP,HostName) VALUES (?,?,?)''',(li[0]+1,host_ip,host_name))
            self.conn.commit()
            self.return_host_numb=li[0]+1
        return self.return_host_numb
	
		# Inserts default value if table is empty
		
		# Inserts max value +1 if table is not empty
		
		#return self.return_host_numb
    def create_scan(self, host_id):
        self.cur.execute("select ScanId from Scan where ScanId IN (select max(ScanId) from Scan)")
        li=self.cur.fetchone()
        #ScanStartTime=datetime.now()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Scan(ScanId,HostID,ScanStartTime,ScanEndTime)")
        if self.return_host_numb!=0:
            self.cur.execute('''INSERT INTO Scan(ScanId,HostID,ScanStartTime,ScanEndTime) VALUES (?,?,?,?)''',(li[0]+1,host_id,time.strftime("%a %b %d %H:%M:%S %Y"),0))
            self.conn.commit()
            self.return_scan_id=li[0]+1
        return self.return_scan_id

    def update_scan_end_time(self, scan_id):
        query='''UPDATE Scan
                 SET ScanENDTIME = ?
                 WHERE ScanId = ?'''
        #ScanEndTime=datetime.now()
        self.cur.execute(query,(time.strftime("%a %b %d %H:%M:%S %Y"),scan_id))
        self.conn.commit()
		
    def read_port_status(self, host_ip, host_name):
        query='''SELECT HostId FROM HOST
                WHERE HostIP=? AND HostName=? '''
        self.cur.execute(query,(host_ip,host_name))
        host_id=self.cur.fetchone()
        self.cur.execute("SELECT ScanId FROM Scan ORDER BY ScanId DESC LIMIT 1")
##        query1='''SELECT * FROM Scan 
##                  WHERE HostId = ?'''
##        self.cur.execute(query1,(host_id[0],))
        scan_id = self.cur.fetchone()
##        self.cur.execute("select ScanId from Scan where ScanId IN (select max(ScanId) from Scan)")
##        scan_id=self.cur.fetchone()
        query2='''SELECT * FROM PortStatus
                 WHERE ScanId =?'''
        self.cur.execute(query2,(scan_id))
        return self.cur.fetchall()
	
		#return self.cur.fetchall()
    def create_port_status(self, scan_id, port, is_open):
        self.cur.execute('''INSERT INTO PortStatus(ScanId,PortNumber,IsPortOpen) VALUES (?,?,?)''',(scan_id,port,is_open))
        self.conn.commit()
            
    def __close_connection_(self):
        self.cur.close()
        del self.cur

        
    def __del__(self):
        self.__close_connection_()
	
