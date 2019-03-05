import re
import pandas as pd
import numpy as np

class dataWrapper:

    Data = None
    
    def __init__(self, sourceArray):
        Data = sourceArray
        Data = dimensionFlattener(Data)
        Data = removeInternalSpace(Data)
        Data = cleanDataset(Data)

    def removeInternalSpace(self, dataset):
        workingDataset = []
        for i in range(len(dataset)):
            if dataset[i].find(" ")>0:
                temp = dataset[i].split()
                for j in range(len(temp)):
                    workingDataset.append(temp[j])
            else:
                workingDataset.append(dataset[i])
        return workingDataset

    def dimensionFlattener(self, dataset):
        for i in range(arrayDepth(dataset)-1):
            workingDataset = []
            for j in range(len(dataset)):
                if isinstance(dataset[j],list):
                    for k in range(len(dataset[j])):
                        workingDataset.append(dataset[j][k])
                else:
                    workingDataset.append(dataset[j])
            dataset = workingDataset
        return dataset

    def arrayDepth(self, dataset):
        if isinstance(dataset, list):
            return 1 + max(depth(item) for item in dataset)
        else:
            return 0

    def cleanDataset(self, dataset):
        for i in range(len(dataset)):
            dataset[i] = cleanDataPoint(dataset[i])
        return dataset

    def cleanDataPoint(self, dataPoint):
        dataPoint = dataPoint.strip()
        dataPoint = re.sub("[^a-zA-Z-']+", "", dataPoint)
        dataPoint = dataPoint.lower()
        return dataPoint

    def appendDataSet(self, dataSet):
        dataSet = dimensionFlattener(dataSet)
        dataSet = removeInternalSpace(dataSet)
        dataSet = cleanDataset(dataSet)
        global Data 
        for i in range(len(dataset)):
            Data.append(dataset[i])

    def appendDataPoint(self, dataPoint):
        appendDataSet([dataPoint])

    def getDataPoint(self, dataPointIndex):
        return Data[dataPointIndex]

    def getDatasetSize(self):
        return len(Data)