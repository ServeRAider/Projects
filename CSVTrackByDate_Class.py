#TrackByDate.py
""" Tracks By Date


"""
class TrackByDate():
    """
    {Date:(IpNum, PortNum),…} A dictionary where the Date is the key and the
    value is the tuple IpNum, and PortNum. Items in the dictionary are sorted by Date. Save
    into file LNameDate.csv where each line contains the Date, IPNum, and Port number
    separated by commas.
    
    Design: 
    1. Read the contents of the file and create the dictionary.
    2. save the dict to the file 
    """
    def __init__(self):
        self.IPDateDnary = {}
        self.NumMaxDates = 0 
        self.MaxDateStr = ""
        self.MaxPortNumsList = []
        self.DateListUnique = []
        
    def PopulateDnary(self, FC):
        """
        Traverse the file and split it to extrapolate the Date as a key, and the IPNum, Portnum as the value 

        1. Split each line of the file in to parts
        2. create the unique list of Dates
        3. save the each date to a dictionary with a blank list as a value 
        4. Go through the list again and add the IP and Port numb to a list 
        5. Traverse the dictionary and for the Date in that line save the IP and Portnum to its value list 

        
        """
        DateList = []
        AllLines = FC.split("\n")
        for Aline in AllLines:
            if Aline != "":
                ALineParts = Aline.strip().split(",")
                DateList.append(ALineParts[2])
        #check with a print
        
        self.DateListUnique = list(set(DateList))
        for ADate in self.DateListUnique:
            Alist =[]
            self.IPDateDnary[ADate] = Alist   #Assigns the value of the IP to a blank list. Dont assign as self.IPAddDnary [AnAddress] = [] or it will be blank list everytime < *This is a common mistake          
        
        #traverse the FC again and populate the address dictionary 

        for Aline in AllLines:
            if Aline != "":                                          #breaks down each line and will append to the list for the port num and date 
                IPPortNumList = []
                ALineParts = Aline.strip().split(",")
                IPPortNumList.append((ALineParts[1]))                   #IP is item 1
                IPPortNumList.append(ALineParts[0])                     #PortNumb is item 0 
                self.IPDateDnary[ALineParts[2]].append(IPPortNumList)
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
        1. create a list of the dnary keys
        2. sort the list
        3. convert the sorted list into a dictionary  

        

        """
    
        DateKeysList = list(self.IPDateDnary.keys()) #Converts the keys to a list 
        DateKeysList.sort()         #sorts the list
        DateSorted = {}                                 
        for IPA in DateKeysList:                                    #converts the sorted list to a dictionary by stating the value for key IPA in DateSorted is going to be equal to the value for the key of self.IPDateDnary
            DateSorted[IPA] = self.IPDateDnary[IPA]
        
        Ofile = open(FName, "w")
        for k,v in DateSorted.items():                                  #writes the items of the sorted list to a file thats passed as a paramter from the main called FName
            for Aval in v:
                if len(v) > self.NumMaxDates:                           #Gets the ports that were found on the date that occured most frequently 
                    self.NumMaxDates = len(v)
                    self.MaxDateStr = k
                    self.MaxPortNumsList = []
                    for Tval in v:
                        self.MaxPortNumsList.append(Tval[1])
                    Ofile.write(f"{k}, {Aval[0]}, {Aval[1]}\n")

        Ofile.close()
        
    def GetNumMax(self):
        return self.NumMaxDates
    
    
    def GetMaxDateStr(self):
        return self.MaxDateStr
    def GetMaxPortNumList(self):
        return self.MaxPortNumsList
    
    def GetDateListUnique(self):
        return self.DateListUnique

    def GetDateDnary(self):
        return self.IPDateDnary