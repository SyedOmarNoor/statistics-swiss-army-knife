#The Statistics Swiss Army Knife by Syed Omar Noor
print("The Statistics Swiss Army Knife\nby Syed Omar Noor")
while True:
    yay = " "
    data = input("Enter numbers: ")
    if "," in data:
        yay = ","
    datalist = data.split(yay)
    notimes = False
    for data1 in datalist:
        if "*" in data1:
            data2 = data1.split("*")
            datalist[datalist.index(data1)] = data2[0]
            for time in range(int(data2[1])-1):
                datalist.insert(datalist.index(data2[0]), data2[0])
    datalist = list(map(float, datalist))
    datalist.sort()
    print("Sorted list:", datalist)
    ##print(''.join(datalist))
    meansum = 0
    for i in datalist:
        meansum += i
    print("Sum of numbers:", meansum)
    print("Mean:", meansum/len(datalist) if meansum/len(datalist) % 1.0 != 0 else int(meansum/len(datalist)))
    print("Range:", round(datalist[-1] - datalist[0], 2))
    average = (datalist[int(len(datalist)/2)] + datalist[int((len(datalist)/2)-1)])/2
    if len(datalist) % 2 == 0:
        print("Median:", average if average % 1.0 != 0 else int(average))
    else:
        medianodd = datalist[len(datalist) - int(len(datalist)/2) - 1]
        print("Median:", medianodd if medianodd % 1.0 != 0 else int(medianodd))
    dictofcounts = {}#start stolen
    listofcounts = []
    for i in datalist:
        countofi = datalist.count(i) # count items for each item in list
        listofcounts.append(countofi) # add counts to list
        dictofcounts[i]=countofi # add counts and item in dict to get later
    maxcount = max(listofcounts) # get max count of items
    if maxcount ==1:
        print ("Mode: None")
    else:
        modelist = [] # if more than one mode, add to list to print out
        for key, item in dictofcounts.items():
            if item == maxcount: # get item from original list with most counts
                modelist.append(str(key))
        print ("Mode(s):",', '.join(modelist))#stop stolen
    print(f"Maximum score: {max(datalist)}")
    print(f"Minimum score: {min(datalist)}")
