from pyrd import *
from utils import *
import yaml

FUNCTION_DICT={
    "播放音乐":PlayMusic,
    "七拍":AddClassicBeat,
    "二拍":AddOneshotBeat,
    "设置静音":SetX,
    "预设特效":AddPresetVFX,
    "设置护士音效":SayReadyGetSetGo,
    "设置BPM":SetBeatsPerMinute,
    "设置背景":SetBackgroundColor,
    "闪烁":Flash,
    "注释":Comment,
    "轨道涂色":TintRows,
}

def parseMetaData(metadatas:dict):
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
    for key in metadatas.keys():
        metadataDict[replaceStringIfNecessary(key)]=replaceStringIfNecessary(metadatas[key])
    SetLevelMeta(metadataDict)

def parseCharacter(characters):
    for character in characters:
        args = character
        for i in range(len(args)):
            if args[i] == ".":
                args[i] = None
            args[i] = replaceStringIfNecessary(args[i])
        AddCharacter(*args)

def parseBar(commands:list,barNum):
    for i in range(len(commands)):
        command = commands[i]
        head=command[0]
        argList=command[1:]
        for i in range(len(argList)):
            if argList[i] == ".":
                argList[i] = None
            try:
                argList[i]=eval(argList[i])
            except:
                argList[i]=replaceStringIfNecessary(argList[i])
        argList.insert(0,barNum)
        FUNCTION_DICT[head](*argList)
    
def run(fileName):
    content = []
    with open(fileName,'r',encoding="utf-8") as f:
        sprdYAML=yaml.load(f, Loader=yaml.SafeLoader)
        metadata = sprdYAML["metadata"]
        characters = sprdYAML["角色"]
        bars = sprdYAML['小节']
        parseMetaData(metadata)
        parseCharacter(characters)
        for barNum in bars.keys():
            parseBar(bars[barNum],int(barNum))
        Export()
        print("Done.")

if __name__ == "__main__":
    run("exampleYAML.sprd")