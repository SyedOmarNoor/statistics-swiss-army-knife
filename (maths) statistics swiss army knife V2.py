#The Statistics Swiss Army Knife V2 by Syed Omar Noor
##Changelog: added Quartiles and Standard Deviation, functions and much more

##(written 8/8/20) circa 21/6/20: functions moved to stat_defs.py
from stat_defs import *

print("\nThe Statistics Swiss Army Knife V2 (28/5/2020 and later)\nby Syed Omar Noor\n")
    
while True:
    data = listify(input("Enter numbers: "))
    print()
    datalist = multiplylist(data)
    intify(datalist)
    datalist.sort()
    datadict = {item:datalist.count(item) for item in datalist}
    print(
            f"Sorted dict: {datadict}"
            if sum(datadict.values())/len(datadict.keys()) > 2
            else f"Sorted list: {datalist}"
        )
    print("Number count:", len(datalist))
    print("Sum of numbers:", sum(datalist))
    print("Mean:", mean(datalist)) 
    print("Range:", round(datalist[-1] - datalist[0], 2))
    print("Median:", median(datalist))
    
    print(mode(datalist))
    
    print("Maximum score:", max(datalist))
    print("Minimum score:", min(datalist))
    
    #New from here
    print("Quartile 1:", quartile(datalist, 1))
    print("Quartile 2 (same as Median):", quartile(datalist, 2))
    print("Quartile 3:", quartile(datalist, 3))
    print("Interquartile Range:", dataiqr := iqr(datalist))
    print("Standard Deviation (Population) (n, Sigma n):", deviation(datalist))
    print("Standard Deviation (Sample) (n-1, sigma n):", deviation(datalist, typeof = 1))
    print("Minor Outliers (IQR x 1.5):", outlier(datalist))
    print("Major Outliers (IQR x 3):", outlier(datalist, multiplier = 2))
    print("5-point summary:", summary(datalist))
    choiceboxplot = input("Do you want to generate a box plot? (Y for yes): ")
    if choiceboxplot.lower() == "y":
        plot(summary(datalist))
    print()
