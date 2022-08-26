#CSV_TrackByIPAddress.py
""" Tracks By IP


"""

from os import register_at_fork
from typing import Counter


class TrackByIpAddress():
    """
    {IPAddress:(Portnum, Date), …} A dictionary where the ipAddress is the key
    and the value is the tuple PortNum, and Date. Items in the dictionary are sorted by IP
    numbers (string). Save into file LNameIPAddress.csv where each line contains the
    IPAddress, Port number and Date separated by commas
    
    Design: 

    1. read the file and create the IPAddress Dictionary. Done using method Populatednary(self,FC):
    


    2. save the dict to a file 
    
    """
    def __init__(self):
        # print(f"Class TrackByIPAddress Created")
        self.IPAddDnary = {}  #My dictionary to hold Portnum/Date list
                              #{IPA : [[portnum, date]], IPA : [[portnum, date] [portnum, date]] #how it will look, may possibly have duplicates
        self.CountOfOnePNDate = 0
        self.IPAddrListUnique = []
        
    def PopulateDnary(self, FC):
        """
        A dictionary where the ipAddress is the key
        and the value is the tuple PortNum, and Date. Items in the dictionary are sorted by IP
        numbers (string).
        1. split the file into lines
        2. seperate the items by a ","
        3. add the IP to a list
        4. remove duplicate IPs and make that a special list 
        5. Assign the IP to the key in a dictionary and initialize the value as a blank list to store Port numb, Date.
        6. traverse each line again, create a blank list everytime that adds the PortNum, Date to the list
        7. for the IP on that line which would be the same as a key in self.IPAddDnary, add those elements to the value list for that key
        8. reset the list and do it again for each line

        
        """
        IPAddrList = []
        AllLines = FC.split("\n")
        for Aline in AllLines:
            if Aline != "":
                ALineParts = Aline.strip().split(",")
                IPAddrList.append(ALineParts[1])
        #check with a print
        # self.IPAddrListUnique = []
        self.IPAddrListUnique = list(set(IPAddrList))                #Set removes duplicates and then list converts the unique list not containing duplicates back to a list 
        for AnAddress in self.IPAddrListUnique:
            Alist =[]
            self.IPAddDnary[AnAddress] = Alist   #Assigns the value of the IP to a blank list. Dont assign as self.IPAddDnary [AnAddress] = [] or it will be blank list everytime < *This is a common mistake          
        
        #traverse the FC again and populate the address dictionary 

        for Aline in AllLines:
            if Aline != "":                                          #breaks down each line and will append to the list for the port num and date 
                PNDateList = []
                ALineParts = Aline.strip().split(",")
                PNDateList.append(int(ALineParts[0]))               #port num is item 0
                PNDateList.append(ALineParts[2])                     #date is item 2 
                self.IPAddDnary[ALineParts[1]].append(PNDateList)       #appends the value for the key [ALineParts[1]] to equal PNDateList
        # print(f"Length of IPAddDnary : {len(self.IPAddDnary)}")
        # Count = 0
        # for k,v in self.IPAddDnary.items():
        #     print(f"Key Value in IPAddDnary is :{k}, {v}")
        #     Count +=1
        #     if Count == 10:
        #         break

    def SaveDnaryToFile(self,FName):
        """
        Design: 

        create a sorted dictionary based on the IP address
        1. Create list of keys of dictionary
        2. Sort the keys
        3. Create a new dict using the sorted keys
        4. Count the number IPs that occured on only one day 
        """
    
        IPAKeysList = list(self.IPAddDnary.keys()) #Converts the keys to a list 
        IPAKeysList.sort()
        IPAddSorted = {}
        for IPA in IPAKeysList:
            IPAddSorted[IPA] = self.IPAddDnary[IPA]         #for the IP Address in the sorted list of IP's, the value for the IP Address is going to be equal to the value of the self.IPAddDnary with the same key
        
        Ofile = open(FName, "w")
        for k,v in IPAddSorted.items():
            if len(v) ==1 :
                self.CountOfOnePNDate += 1                                          #traverses the list and if the value for that key has more than 1 entry add a count
            for Aval in v:
                Ofile.write(f"{k}, {Aval[0]}, {Aval[1]}\n")


        Ofile.close()
    
    def GetCountOf(self):
        return self.CountOfOnePNDate

    def GetUniqueIP(self):
        return self.IPAddrListUnique
