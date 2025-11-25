#The Statistics Swiss Army Knife V2.5 by Syed Omar Noor
##Changelog: it's all 1 function now!

from stat_defs import *

print("\nThe Statistics Swiss Army Knife V2.5 (11/8/2020 and later)\nby Syed Omar Noor\n")
    
while True:
    data = allfunctions(input("Enter numbers: "))
    print()
    print(f"Sorted {type(data['sorted']).__name__}:", data['sorted'])
    print("Number count:", data["count"])
    print("Sum of numbers:", data["sum"])
    print("Mean:", data["mean"]) 
    print("Range:", data["range"])
    print("Median:", data["median"])
    
    print(data["mode"])
    
    print("Maximum score:", data["max"])
    print("Minimum score:", data["min"])
    
    #New from here
    for x in [1, 2, 3]:
        exec(f"print('Quartile {x}:', data['q{x}'])")
    print("Interquartile Range:", data["iqr"])
    print("Standard Deviation (Population) (n, Sigma n):", data["pop_dev"])
    print("Standard Deviation (Sample) (n-1, sigma n):", data["samp_dev"])
    print("Minor Outliers (IQR x 1.5):", data["min_out"])
    print("Major Outliers (IQR x 3):", data["maj_out"])
    print("5-point summary:", data["summary"])
    choiceboxplot = input("Do you want to generate a box plot? (Y for yes): ")
    if choiceboxplot.lower() == "y":
        plot(data["summary"])
    print()
