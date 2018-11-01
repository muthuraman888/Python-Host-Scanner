import tkinter as tk
import tkinter.ttk as ttk
import HostScannerDAL as HSD

class ResultsDialog():
    def __init__(self, host_ip, host_name):
        self.root=tk.Tk()
        self.root.title("Results Dialog")
        self.c=HSD.HostScannerDAL()
        self.h_ip=host_ip
        self.h_na=host_name
        self.gui_init_()
        
    def gui_init_(self):
        self.tree= ttk.Treeview(self.root)
        self.tree["columns"]=("two","three","four")
        self.tree.column("#0",width=100)
        self.tree.column("two",width=100)
        self.tree.column("three",width=100)
        self.tree.column("four",width=200)
        self.tree.heading("#0",text="SCAN ID")
        self.tree.heading("two",text="PORT NUMBER")
        self.tree.heading("three",text="IS OPEN")
        self.tree.heading("four",text="SCAN TIME")
        self.__update_grd_()
		
    def __update_grd_(self):
        self.dat = self.c.read_port_status(self.h_ip,self.h_na)
        self.ti=self.c.read_host(self.h_ip)
        self.datli=[]
        for el in self.ti:
            self.tim=el[2]
        for elements in self.dat:
            self.datli.append(list(elements))
        for elements in self.datli:
            elements.append(self.tim)
        i=0
        for elements in reversed(self.datli):
            self.tree.insert('',i,text=elements[0],values=(elements[1],elements[2],elements[3]))
            i=i+1
        self.tree.pack()
        self.root.mainloop()
        
