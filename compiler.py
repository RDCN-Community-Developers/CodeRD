from pyrd import *
from utils import *
import re
FUNCTION_DICT={
    "播放音乐":PlayMusic,
    "七拍":AddClassicBeat,
    "二拍":AddOneshotBeat,
    "设置静音":SetX,
}

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
            args[i] = replaceStringIfNecessary(args[i])
        AddCharacter(*args)

def parseBar(bar:str,barNum):
    commands=bar.split("\n")
    print("Bar "+str(barNum))
    for i in range(len(commands)):
        print(commands[i])
        command = commands[i].strip()
        head,args=command.split(" ")
        argList = args.split(",")
        for i in range(len(argList)):
            if argList[i] == ".":
                argList[i] = None
            try:
                argList[i]=eval(argList[i])
            except:
                pass
        argList.insert(0,barNum)
        FUNCTION_DICT[head](*argList)
    

content = []
#fileName = input("请输入sprd文件名:")
fileName = "debug/1.sprd"
with open(fileName,'r',encoding="utf-8") as f:
    sprd = f.read()
    content = sprd.split("```")
    metadata = content[0].split('\n')
    metadata = [x.strip() for x in metadata if x.strip()!=""]
    character = content[1].split('\n')
    character = [x.strip() for x in character if x.strip()!=""]
    bar = content[2]
    pattern = re.compile(r'\[(\d+)\](?>\n)(.*?)(?=\[|$)', re.S)
    result = re.findall(pattern, bar)
    parseMetaData(metadata)
    parseCharacter(character)
    for bar in result:
        barNum,barContent = bar
        parseBar(barContent.strip(),int(barNum))
    Export()