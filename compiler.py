from pyrd import *
from utils import *


def parseMetaData(metadatas):
    metadataDict = {
        "artist":"",
        "song":"",
        "author":"",
        "difficulty":"",
        "seizureWarning":False,
        "description":"",
        "tags":"",
        "rankMaxMistakes":[20,15,10,5],
        "rankDescription":["F","D","C","B","A","S"]
    }
    for metadata in metadatas:
        dataName,dataContent=metadata.split(" ")
        metadataDict[replaceString(dataName)]=replaceStringIfNecessary(dataContent)
    SetLevelMeta(metadataDict)

def parseCharacter(charactersText):
    characters=[]
    for characterText in charactersText:
        args = characterText.split(",")
        for i in range(len(args)):
            if args[i] == ".":
                args[i] = None
        character = Character(*args)
        characters.append(character)
    return characters



content = []
#fileName = input("请输入sprd文件名:")
fileName = "example.sprd"
with open(fileName,'r',encoding="utf-8") as f:
    sprd = f.read()
    content = sprd.split("---")
    metadata = content[0].split('\n')
    metadata = [x.strip() for x in metadata if x.strip()!=""]
    character = content[1].split('\n')
    character = [x.strip() for x in character if x.strip()!=""]
    bar = content[2:]
    bar = [x.strip() for x in bar if x.strip()!=""]
    parseMetaData(metadata)
    characters=parseCharacter(character)
    Export()