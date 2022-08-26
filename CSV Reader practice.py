#FinalExam.py
"""


    Purpose: Design a GUI application that will allow the user to take a CSV file with IP, date, and port nums
             and sort it towards finding more specific information about each port, IP, or date. 

    Design: The design will add buttons with functions to return specific information about each item in the port scan file. 
            This program will utilize a Listbox and allow the user to choose the item they want information about in the 
            text area given. 

"""
from os import popen
import tkinter.filedialog
from tkinter.constants import ANCHOR
from tkinter.font import Font
from tkinter import Button
from breezypythongui import EasyFrame
from CSVTrackByCount_Class import TrackByCount
from CSVTrackByIP_Class import TrackByIpAddress
from CSVTrackByDate_Class import TrackByDate
class PortScanResults (EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title= "PortScan Results - Final Exam")
        #sets up the Title at the top of the page welcoming the user
        self.setBackground("gray")
        self.setSize(width= 1550, height= 500)
        self.FileText = ""
        self.addLabel(text= "Welcome to the Results Reader!", row= 0, column= 0, sticky = "NEW", rowspan=1, background="gray", foreground= "brown")
        #Unique Lists
        self.PortNumList = []
        self.IPAList = []
        self.DateList =[]
        #set up the start here panel and adds the button to read the file as well 
        StartPanel = self.addPanel(row = 1, column= 0, background= "white")
        StartMessage = StartPanel.addLabel(text="Start Here:", row= 0, column= 0, sticky= "NESW", foreground= "Brown")
        StartMessage["font"] = Font(family = "Cambria", size = 20, slant = "italic")
        StartPanel.addButton(text="Read File", row =1, column= 0, columnspan= 1, command= self.openFile)
        #creates a panel to contain the buttons for the different functions of the program  
        ButtonPanel = self.addPanel(row= 2, column=0, rowspan= 2, background= "black")
        #The buttons for getting popular results 
        self.PopPortBtn = ButtonPanel.addButton(text="Popular Port", row= 2, column= 0, command= self.PopularPort, state="disabled")
        self.IPResultBtn = ButtonPanel.addButton(text="IPAddress Result", row= 3, column= 0,command= self.IPResult, state= "disabled")
        self.PopDateBtn = ButtonPanel.addButton(text="Popular Date", row= 4, column= 0, command= self.PopularDate, state= "disabled")
        #The Buttons for getting specific information about each unique Port, IP, or Date 
        self.IPDateBtn = ButtonPanel.addButton(text="Get IP/Date", row= 2, column= 4, command= self.IPandDate, state="disabled")
        self.PortDateBtn = ButtonPanel.addButton(text="Get Port/Date", row= 3, column= 4,command= self.PortandDate, state= "disabled")
        self.IPnPortBrn = ButtonPanel.addButton(text="Get Ip/Port", row= 4, column= 4, command= self.IPandPort, state= "disabled")
        #Text output area 
        self.OutputArea = ButtonPanel.addTextArea(text="", row= 2, column= 1, rowspan= 3 )
        #Labels for List Boxes
        ButtonPanel.addLabel(text= "Port Number:", row= 2,  column= 2, sticky= "NESW", background= "red")
        ButtonPanel.addLabel(text= "IP Address:", row= 3,  column= 2, sticky= "NESW", background= "white")
        ButtonPanel.addLabel(text= "Date:", row= 4,  column= 2, sticky= "NESW", background= "blue")
        #List Boxes       
        self.PortLB = ButtonPanel.addListbox(row= 2, column= 3, width= 7, height= 1)
        self.IPAddressLB = ButtonPanel.addListbox(row= 3, column= 3, width= 7, height= 1, )
        self.DateLB = ButtonPanel.addListbox(row= 4, column= 3, width= 7, height= 1, )
        #Clear and Exit Buttons 
        self.ClearBtn = ButtonPanel.addButton(text = "Clear", row=5, column= 0,columnspan= 2, command= self.ClearText, state = "disabled")
        self.ExitBtn = ButtonPanel.addButton(text = "Exit", row=5, column= 1,columnspan= 2, command= self.ExitProgram)
        
        
# The methods for clear and exit buttons
    def ClearText(self):
        """Event Handler for clearing Text Area and list boxes"""
        self.OutputArea.setText("")
        

    def ExitProgram(self):
        """Event handler for closing program """
        exit(0)



#The method for reading the file button 
    def openFile(self):                                             #reads the file and passes it to the variable self.FileText
        """This is the event handler for the Read File button. 
            It should open the dialog box, allow the user to read
            the file. """
        #sets up the dialog box to read the file that user chooses. 
        fList = [("Python Files", "*.py"), ("Text Files", "*.txt"), ("Comma Seperated Value Files", "*.csv"), ("Log Files", "*.log")]
        filename = tkinter.filedialog.askopenfilename(parent= self, filetypes= fList)
        #if the file name isnt blank then read the file and change the state of the other buttons 
        if filename != "":
            file = open(filename, "r")
            self.FileText = file.read()
            file.close
            # self.OutputArea.setText(self.FileText)
            self.PopPortBtn["state"] = "normal"
            self.IPResultBtn["state"] = "normal"
            self.PopDateBtn["state"] = "normal"
            self.ClearBtn["state"] = "normal" 
    
 #The methods for the Pop port, IPResult, and PopDate buttons    
    def PopularPort(self):
        """This is the event handler for the Popular Port button. On clicking,
            the program calls the class TrackByCount. It creates the dictionary,
            saves it to a file and prints the most popular port found. """
        PopPort = TrackByCount()
        PopPort.PopulateDnary(self.FileText)                                                                
        SortedCountDnary = PopPort.SaveDnaryToFile("PortCount.csv")
        self.OutputArea.setText(f"The most popular port that was found open was: Port Number {SortedCountDnary[0][0]} Count: {SortedCountDnary[0][1]} ") 
        self.IPDateBtn["state"] = "normal"
        self.PopPortBtn["state"] = "disabled"
        self.PopulatePortLB()

    def IPResult(self):
        """This is the even handler for the IPAddress Result button. On clicking, 
            the program calls the class TrackByIPAddress. It creates the dictionary,
            saves it to a file and prints the number of IPs with only 1 {Portnum,Date}
            combo. 
            """
        ResultIP = TrackByIpAddress()
        ResultIP.PopulateDnary(self.FileText)
        ResultIP.SaveDnaryToFile("IPAddress.csv") 
        self.OutputArea.setText(f"The number of IP Addresses that have only one PN, Date combination: {ResultIP.GetCountOf()}")
        self.PortDateBtn["state"] = "normal"
        self.IPResultBtn["state"] = "disabled"
        self.PopulateIPLB()

    def PopularDate(self):
        """This is the event handler for the Popular Date button. On clicking, 
            the program uses TrackByDate to create the dictionary, save it to a file
            and display the date where the most portnunms were found, how many, and the
            list of them."""
        PopDate = TrackByDate()
        PopDate.PopulateDnary(self.FileText)
        PopDate.SaveDnaryToFile("Date.csv")
        self.OutputArea.setText(f"Entries Found on the date : {PopDate.GetNumMax()} Max Ports Date: {PopDate.GetMaxDateStr()}\nThe ports on that date were: {PopDate.GetMaxPortNumList()}")
        self.IPnPortBrn["state"] = "normal"
        self.PopDateBtn["state"] = "disabled"
        self.PopulateDateLB()
 #The methods for the IP/Date, Port/Date, and IP/port buttons   
    def IPandDate(self):
        """ This is the event handler for the Get/IP date button. On clicking,
            the program traverses the dictionaries passed and allows the user
            to get two sorted lists and print them based on their selection in
            PopulatePortLB"""
        PortNum = self.PortLB.get(ANCHOR)
        PopPort = TrackByCount()
        PopPort.PopulateDnary(self.FileText)                                                                
        PopPort.SaveDnaryToFile("GammillPortCount.csv")
        SortedDnary = PopPort.GetSortedDnary()
        IPAndDateDnary = PopPort.GetPortDnary()                                         #The dictionary of {Port: [IP,Date],[IP,Date] ...}
        IPList = []                                                                     #a blank list for the list of tuples
        TheIPAnchorList = IPAndDateDnary[str(PortNum)]                                  #The values isolated by the choice of the menu (PortNum)
        for Value in TheIPAnchorList:                                                    
            IPDateTupe = (tuple(Value))                                                 #converts to tuples and adds to list of tuples 
            IPList.append(IPDateTupe)
        IPList.sort(key=lambda x:x[0])                                                  #sorts by IP 
        IPDateStr = ""
        for items in IPList:
            IPDateStr += (f"IPNumber: {items[0]:<3}      Date: {items[1]}\n")
        DateIPDnary = PopPort.GetPortDateDnary()
        DateList = [] 
        TheDateAnchorList = DateIPDnary[str(PortNum)]
        for Value in TheDateAnchorList:
            DateIPTupe = (tuple(Value))                                 #adding the lists of lists to make it a list of tuples
            DateList.append(DateIPTupe)
        DateList.sort(key=lambda x:x[0])                                #sorts the tuples by date 
        DateIPStr = ""                                                  #adding the list of sorted tuples to a string 
        for item in DateList:
            DateIPStr += (f"Date: {item[0]:<3}      IPNumber: {item[1]}\n")

        self.OutputArea.setText(f"Port number {PortNum} was found {SortedDnary[str(PortNum)]} times\n\nList Sorted by IP Address:\n\n{IPDateStr}\n\nSorted by Date:\n\n{DateIPStr}")
        

    def PortandDate(self):
        pass

    def IPandPort(self):
        pass


 #The methods for the ListBoxes for Port, IP, and Date 
    def PopulatePortLB(self):
        """This list box will populate when the Popular Port button is pressed.
            It provides a list of the port numbers in a sorted order"""
        self.PortLB.clear()     
        PopPort = TrackByCount()
        PopPort.PopulateDnary(self.FileText)
        TheList = PopPort.GetPortListUnique()                           #calls to get the unique list of Port nums without duplicates
        for item in TheList:
            self.PortNumList.append(int(item))              
        self.PortNumList.sort()                                         #sorts the list of Port nums
        self.PortLB.clear()                                             #clears all list boxes
        indx = 0 
        for port in self.PortNumList:                                   #adds the items to the list box
            self.PortLB.insert(indx, port)
            indx += 1
        

    def PopulateIPLB(self):
        """This list box will populate when the IPResult button is pressed.
            It provides a list of the IP Addresses in a sorted order"""
        self.IPAddressLB.clear()
        PopIP = TrackByIpAddress()
        PopIP.PopulateDnary(self.FileText)
        TheList = PopIP.GetUniqueIP()                                   #calls to get the unique list of IP Addresses
        for item in TheList:
            self.IPAList.append(item)
        self.IPAList.sort()                                             #sort the list
        self.IPAddressLB.clear()
        indx = 0
        for IPA in self.IPAList:                                        #adds the items to the list 
            self.IPAddressLB.insert(indx, IPA)
            indx += 1 
            
                
    def PopulateDateLB(self):
        """This list box will populate when the Popular Date button is pressed.
            It provides a list of the Dates in a sorted order"""
        self.DateLB.clear()
        PopDate = TrackByDate()
        PopDate.PopulateDnary(self.FileText)
        TheList = PopDate.GetDateListUnique()
        for item in TheList:
            self.DateList.append(item)
        self.DateList.sort()
        self.DateLB.clear()
        indx = 0
        for Date in self.DateList:
            self.DateLB.insert(indx, Date)
            indx += 1
        


# The main method
def main():
    try:
        PortScanResults().mainloop()
    except(FileNotFoundError):
        print("File Not Found!")

if __name__== "__main__":
    main()
