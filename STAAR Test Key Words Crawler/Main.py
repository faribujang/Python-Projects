import time
import InputNormalizer

class word:
    value = ""
    index = 0
    occurance = 1
    def __init__(self, text, occuranceindex):
        value = text
        index = occuranceindex

class dataSorter:
    
    alphabeticalDictionary = [ [] for x in range(26) ]
    wordFrequency = []
    wordFrequencyRegions = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def __init__(self):
        
    def insertWord(self, input):

    def handleAlphabeticalInsert(self,input):

    def charToIndex(self, input):
        return ord(input) - 97
    
    def indexToChar(self, input):
        return chr(input + 97)

    def insertWordFrequency(self, input):
        if len(wordFrequencyRegions) < len(input):
            while(len(wordFrequencyRegions) < len(input)):
                wordFrequencyRegions.append(0)

        inputindex = wordFrequencyRegions[len(input)-1]
        wordFrequency.append(inputindex,input)

        for i in range(len("aaa")-1,len(wordFrequencyRegions)):
	        wordFrequencyRegions[i] = 1 + wordFrequencyRegions[i]
    
    


if __name__ == "__main__":

    filelocation = "EngII2011.txt"
    with open(filelocation) as g:
        filedata = g.readlines()
    filedata = [x.strip() for x in filedata]

    data = InputNormalizer.dataWrapper(filedata)