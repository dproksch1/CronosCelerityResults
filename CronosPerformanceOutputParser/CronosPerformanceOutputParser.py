import numpy as np
import re

from decimal import *
getcontext().prec = 9

def fetchPerformanceOutput(file_obj, fix):
    perf = []
    for line in file_obj:
        if "Time needed for substeps:" in line:
            if not fix:
                nextLine = next(file_obj)
                perf.append(Decimal(re.findall('for full step: *(?!\.)(\d+\.\d+|\d+)(?:[eE][+-]?\d+)?', nextLine)[0]))
            else:
                p1 = Decimal(re.findall('(?!\.)(\d+\.\d+|\d+)(?:[eE][+-]?\d+)?', line)[1])
                nextLine = next(file_obj)
                p2 = Decimal(re.findall('for full step: *(?!\.)(\d+\.\d+|\d+)(?:[eE][+-]?\d+)?', nextLine)[0])
                perf.append(p1+p2)
    return perf
        
                
def splitPerformances(perf, steps):
    n = len(perf) // (steps * 2)
    
    if (len(perf) % (steps * 2)) != 0:
        print("Error: wrong step count")
        exit()

    stepList = [perf[i * n:(i + 1) * n] for i in range((len(perf) + n-1) // n)]
    rk1 = [element for sublist in stepList[::2] for element in sublist]
    rk2 = [element for sublist in stepList[1::2] for element in sublist]

    return [rk1, rk2]

def toExcelOutput(rk):
    s = "("
    l = len(rk)
    i = 0
    for e in rk:
        i += 1
        s += str(e)
        if i < l:
            s += ' + '
    return s + (")/" + str(l))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--file", dest="outputFile", help="Import output file", required=True)
    parser.add_argument('-s', "--steps", dest="steps", type=int, default=1, help="Number of PDE steps in the file")
    parser.add_argument("--fix", dest="outputFix", action='store_true', default=False, help="fix printout errors")
    parser.add_argument("--excel", dest="excelOutput", action='store_true', default=False, help="automatically convert to excel output")
    args = parser.parse_args()
    outputFile = args.outputFile
    steps = args.steps
    fix = args.outputFix
    excelOutput = args.excelOutput

    with open(outputFile, "r") as f:
        perf = fetchPerformanceOutput(f, fix)
        if not excelOutput:
            print([[float(i) for i in rk] for rk in splitPerformances(perf, steps)])
        else:
            for rk in splitPerformances(perf, steps):
                print(toExcelOutput(rk))

