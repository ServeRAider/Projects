#CSVTrackByCount_Class.py
""""Track By Count Class


"""
class TrackByCount():
    """{OPN:Count,…} A dictionary where the port number is the key and the
        number of times that port was found to be open. Items in the dictionary are sorted by
        port numbers. Save into file LNamePortCount.csv where each line contains the port
        number and count separated by a comma. 

        Create a dictionary called PortCountDnary {OPN: Count, OPN: Count, OPN: Count...}


"""

    def __init__(self):
        #print(f"Class TrackByCount Created")
        self.PortCountDnary = {}                    #MAin Dnary that holds a port number its count 
        self.PortsListUnique = []
        self.SortedDnary = {}
        self.PortDnary ={}
        self.PortDnaryByDate ={}
        
    def PopulateDnary(self,FC):                                         #FC is the file being passed directly to this method from the main 
        """
        This method populates PortCountDnaryby splitting the file passed as a parameter
        and using a loop to count the number of times the prot number appears 

        step 1: Split the file contents to each line using ("\n")
        step 2: traverse each line and splitting by ","
        step 3: Grab the port number from each line (item 0) and append to a list 
        step 4: create the list of all unique port numbers 
        step 5: Initialize the port count dictionary to 0
        step 6: Traverse PortsList and increment count in PortCountDnary
        """
        # print(f"In populate Dnary len FC = {len(FC)}")
        PortsList = [] 
        AllLines = FC.split("\n")                                       #Break up the file content into strings 
        # print(f"Number of Lines = {len(AllLines)}")
        for Aline in AllLines:
            if Aline != "":                                             #Do not process blank Lines 
                ALineParts = Aline.strip().split(",")                   #split each line by a comma 
                PortsList.append(ALineParts[0])                         #Appends the first item in the line to the list which is the port number 
        # print(f"Length of Port List = {len(PortsList)}")
        # for index in range(0,10):
        #     print(f"port list items = {PortsList[index]}")            #Just to prove ports are correct when being read from the file into the list 

        self.PortsListUnique = list(set(PortsList))                          #Set removes duplicates and then list converts the unique list not containing duplicates back to a list 
        for APort in self.PortsListUnique:
            Alist = []
            BList =[]
            self.PortDnary [APort] = Alist
            self.PortDnaryByDate[APort] = BList
        for ALine in AllLines:
            if ALine != "":
                IPDateList = []
                DateIPList = []
                ALinePart = ALine.strip().split(",")
                IPDateList.append(ALinePart[1])
                IPDateList.append(ALinePart[2])
                DateIPList.append(ALinePart[2])
                DateIPList.append(ALinePart[1])
                self.PortDnary[ALinePart[0]].append(IPDateList)
                self.PortDnaryByDate[ALinePart[0]].append(DateIPList)
        # SortedIPDateList = sorted(self.PortDnary.items(), key = lambda x:x[1]) 
        # SortedDateIPList = sorted(self.PortDnaryByDate.items(), key = lambda x:x[1]) 
        # self.PortDnary = dict(SortedIPDateList)
        # self.PortDnaryByDate = dict(SortedDateIPList)
        
        
        
        # print(f"Length of Unique Port List = {len(PortsListUnique)}")
        # for index in range(0,10):
        #     print(f"Unique port list items = {PortsListUnique[index]}") 
        # #Initialize my dictionary count to 0
        for pn in self.PortsListUnique:                              
            self.PortCountDnary[pn] = 0                                 #initializes each ports count as 0
       
        for pn in PortsList:
            self.PortCountDnary[pn] += 1     
            
        # print(len(self.PortCountDnary))                           #traverses the original port list to count how many times its found and if that key is found in the port list it increases its count
        # print(f"length of my dict is  = {len(self.PortCountDnary)}")
        # count = 0
        # for k,v in self.PortCountDnary.items():
        #     print(f" Key, Values of Dictionary are :{k} , {v}")
        
        #     count += 1 
        #     if count == 10:
        #         break
        
    def SaveDnaryToFile(self, FName):
            """
            Save the dnary to a file. Sorts the dnary by count
            param is FName of file to save dictionary
            returns the most commonly open port in dnary 
            """
            OFile = open(FName, "w")                                                                                #Create file to write
            #sort the dictionary by count using lambda function and make a list of sorted tuples  
            SortedDictList = sorted(self.PortCountDnary.items(), key = lambda x:x[1], reverse=True)                 #.items() gives the dictionary as tuples
            self.SortedDnary = dict(SortedDictList)                                                                      #It was a sorted list of tuples so this turns it back into a dictionary
            # print(f"Length of sorted Dnary = {len(SortedDnary)}")
            for k,v in self.SortedDnary.items():                                                                         #writes the dictionary to a file
                OFile.write(f"{k}, {v}\n")
            OFile.close()
            return SortedDictList
    

    def GetPortListUnique(self):
        return self.PortsListUnique
    
    def GetSortedDnary(self):
        return self.SortedDnary
    
    def GetPortDnary(self):
        return self.PortDnary
    
    def GetPortDateDnary(self):
        return self.PortDnaryByDate
