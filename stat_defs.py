def median(deflist):
    if len(deflist) % 2 == 0:  # if length even
        result = (
            deflist[int(len(deflist)/(2))]  # (n+2)/2 but code so n/2
            + 
            deflist[int((len(deflist)/(2))-1)]  # n/2 but code so (n-2)/2 or n/2 - 1
            )/2
    else:  # if length odd
        result = deflist[
            int(len(deflist)/(2))  # (n+1)/2 but code so (n+1)/2 - 1
        ]
    return result if result % 1 != 0 else int(result)

def quartile(deflist, quarter = 1):
    half = int((len(deflist))/2)
    q0 = deflist[0]
    lower = deflist[:half]  #
    middle = deflist  # q2, median
    upper = deflist[-half:]
    q4 = deflist[-1]
    for ll in (listlist := [q0, lower, middle, upper, q4]):
        quarterl = listlist[quarter]
    return median(quarterl)

def deviation(deflist, typeof = 0):
    avg = sum(deflist)/len(deflist)
    deviationavg = (sum([(x-avg)**2 for x in deflist])/(len(deflist)-typeof))**0.5
    return deviationavg

def multiplylist(deflist):
    list2 = []
    for x in deflist:
        if "*" in x:  # occurences
            xlist = x.split("*")
            list2.extend([float(xlist[0]) for xx in range(int(xlist[1]))])
        elif "x" in x:  # times
            xlist = x.split("x")
            list2.append(float(xlist[0]) * float(xlist[1]))
        else:
            list2.append(float(x))
    return list2

def mode(deflist):
    #start stolen from Stack Overflow
    dictofcounts = {}
    listofcounts = []
    for i in deflist:
        countofi = deflist.count(i) # count items for each item in list
        listofcounts.append(countofi) # add counts to list
    dictofcounts={item:deflist.count(item) for item in deflist} # add counts and item in dict to get later
    maxcount = max(listofcounts) # get max count of items
    if maxcount ==1:
        return "None"
    else:
        modelist = [] # if more than one mode, add to list to print out
        for key, item in dictofcounts.items():
            if item == maxcount: # get item from original list with most counts
                modelist.append(str(key))
        
        return ', '.join(modelist)
    #end stolen

def iqr(deflist):
    return quartile(deflist, 3)-quartile(deflist)

def outlier(deflist, multiplier = 1):
    iqr1 = iqr(deflist)
    answer = ", ".join([
            str(x)
            for x in list(set(deflist))
            if (
                x > iqr1 * 1.5 * multiplier + quartile(deflist, 3) #x higher than q3 + iqr x 1.5/3
                or
                x < quartile(deflist, 1) - iqr1 * 1.5 * multiplier # lower than q1 - iqr x 1.5/3
                )
            ])
    return answer if answer else "None"

plottimescount = False
def plot(deflist):
    global plottimescount
    
    if not plottimescount:
        print("Loading boxplot modules...")
        
    import pandas as pd
    import matplotlib.pyplot as plt
    
    if not plottimescount:
        print("Boxplot modules loaded!")
        plottimescount = True
    
    df = pd.DataFrame(deflist) #create data frame
    df.boxplot(grid='True', vert = "False", showfliers=True)    #create boxplot from dataframe             
    plt.show() #show boxplot

def summary(deflist):
    inlier = [x for x in deflist if str(x) not in outlier(deflist).split(", ")]
    return [
        min(inlier), 
        quartile(deflist, 1), 
        median(deflist), 
        quartile(deflist, 3), 
        max(inlier)
        ]

def mean(deflist):
    listmean = sum(deflist)/len(deflist)
    return listmean if listmean % 1.0 != 0 else int(listmean) #make int if .0 else float

def intify(deflist):
    for x in range(len(deflist)):
        if not (deflist[x] % 1.0):
            deflist[x] = int(deflist[x])
    return deflist

def listify(defstring):
    return defstring.replace(",", " ").replace("|", " ").split()

def multiplelists(func, *deflist):
    list2 = []
    for li in deflist:
        list2.append(func(li))
    return list2


def allfunctions(defstring):
    returndict = {}
    deflist = multiplylist(listify(defstring))
    highestdecimal = 0
    for x in deflist:
        x = str(x)
        if "." not in x:
            pass
        else:
            x = x.split(".")
            if len(x[1]) > highestdecimal:
                highestdecimal = len(x[1])
    intify(deflist)
    deflist.sort()
    defdict = {item:deflist.count(item) for item in deflist}
    returndict["sorted"] = (
        defdict
        if sum(defdict.values())/len(defdict.keys()) > 3
        else deflist
        )
    returndict["count"] = len(deflist)
    returndict["sum"] = sum(deflist)
    returndict["mean"] = mean(deflist)
    returndict["range"] = round(deflist[-1] - deflist[0], highestdecimal)
    returndict["median"] = median(deflist)
    returndict["mode"] = mode(deflist)
    returndict["max"] = max(deflist)
    returndict["min"] = min(deflist)
    for x in [1, 2, 3]:
        exec(f"returndict['q{x}'] = quartile(deflist, {x})")
    returndict["iqr"] = round(iqr(deflist), highestdecimal+1)
    returndict["pop_dev"] = deviation(deflist)
    returndict["samp_dev"] = deviation(deflist, typeof = 1)
    returndict["min_out"] = outlier(deflist)  # IQR * 1.5
    returndict["maj_out"] = outlier(deflist, multiplier = 2)  # IQR * 3 i.e. 1.5 * 2
    returndict["summary"] = summary(deflist)
    returndict["expected"] = sum(deflist)
    returndict["exsquared"] = sum([x*x for x in deflist])
    returndict["variance"] = deviation(deflist)**2
    return returndict
if __name__ == '__main__':
    for x in (yay := allfunctions("1 2 1 23 4 123 4 12 231 234")):
        print(f"\"{x}\"", end=", ")
    plot(yay["summary"])
