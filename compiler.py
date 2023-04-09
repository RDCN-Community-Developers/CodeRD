from pyrd import *
from utils import *
import yaml
import sys

# 所有支持的参数列表
FUNCTION_DICT={
    "播放音乐":PlayMusic,
    "PlayMusic":PlayMusic,
    "七拍":AddClassicBeat,
    "AddClassicBeat":AddClassicBeat,
    "二拍":AddOneshotBeat,
    "AddOneshotBeat":AddOneshotBeat,
    "长按拍":LongBeat,
    "LongBeat":LongBeat,
    "自由拍开始":FreeBeat_Start,
    "FreeBeat_Start":FreeBeat_Start,
    "自由拍脉冲":FreeBeat_Pulse,
    "FreeBeat_Pulse":FreeBeat_Pulse,
    "设置静音":SetX,
    "SetX":SetX,
    "设置护士音效":SayReadyGetSetGo,
    "SayReadyGetSetGo":SayReadyGetSetGo,
    "设置BPM":SetBeatsPerMinute,
    "SetBPM":SetBeatsPerMinute,
    "播放音效":PlaySound,
    "PlaySound":PlaySound,
    "设置数拍音效": SetCountingSound,
    "SetCountingSound":SetCountingSound,
    "朗读轨道": NarrateRowInfo,
    "NarrateRow":NarrateRowInfo,
    "朗读说明": ReadNarration,
    "ReadNarration":ReadNarration,
    "显示对话": ShowDialogue,
    "ShowDialogue":ShowDialogue,
    "预设特效":AddPresetVFX,
    "AddPresetVFX":AddPresetVFX,
    "设置背景":SetBackgroundColor,
    "SetBackgroundColor":SetBackgroundColor,
    "闪烁":Flash,
    "Flash":Flash,
    "注释":Comment,
    "Comment":Comment,
    "轨道涂色":TintRows,
    "TintRows":TintRows
}

# 读取metadata
def parseMetaData(metadatas: dict):
    metadataDict = {
        "artist": "",
        "song": "",
        "author": "",
        "difficulty": "",
        "seizureWarning": False,
        "description": "",
        "tags": "",
        "rankMaxMistakes": [20, 15, 10, 5],
        "rankDescription": ["F", "D", "C", "B", "A", "S"]
    }
    for key in metadatas.keys():
        metadataDict[replaceStringIfNecessary(
            key)] = replaceStringIfNecessary(metadatas[key])
    SetLevelMeta(metadataDict)

# 读取角色定义
def parseCharacter(characters):
    for character in characters:
        args = character
        for i in range(len(args)):
            if args[i] == ".":
                args[i] = None
            args[i] = replaceStringIfNecessary(args[i])
        AddCharacter(*args)

# 读取小节定义
def parseCommand(head,argList,barNum):
    for i in range(len(argList)):
        if argList[i] == ".":
            argList[i] = None
        try:
            argList[i] = eval(argList[i])
        except:
            argList[i]=replaceStringIfNecessary(argList[i])
    argList.insert(0,barNum)
    FUNCTION_DICT[head](*argList)

# 读取小节定义
def parseBar(commands: list, barNum,customPattern:dict|None):
    for i in range(len(commands)):
        command = commands[i]
        head = command[0]
        argList = command[1:]
        if customPattern:
            if head in customPattern.keys():
                beatNum=command[1]
                parseCustomPatterns(customPattern[head],barNum,beatNum)
            else:
                parseCommand(head,argList,barNum)
        else:
            parseCommand(head,argList,barNum)
        
# 读取自定义方法定义
def parseCustomPatterns(commands,barNum,beatNum):
    for command in commands: #对于customPatterns 是有args的，没有args的是调用customPatterns的bars
        head = command[0]
        revBeat = command[1]
        argsList = command[2:]
        beat=revBeat+beatNum # 重新构建绝对beatNum
        argsList.insert(beat,0)# 重新构建argsList
        parseCommand(head,argsList,barNum)

# 对读取的sprd文件进行语法检查
def syntaxCheck(sprdYAML):
    metadata = sprdYAML["metadata"]
    characters = sprdYAML["角色"]
    bars = sprdYAML['小节']
    customPattern=None
    try:
        customPattern = sprdYAML['自定义方法']
    except:
        customPattern = None
    for key in metadata.keys():
        if key not in ["artist","song","author","difficulty","seizureWarning","description","tags","rankMaxMistakes","rankDescription"]:
            raise Exception("metadata中有无效的键值对")
    for character in characters:
        if len(character)!=5:
            raise Exception("角色定义不符合规范")
    for barNum in bars.keys():
        for command in bars[barNum]:
            if len(command)<2:
                raise Exception("小节定义不符合规范")
            head = command[0]
            if head not in FUNCTION_DICT.keys():
                raise Exception("小节定义不符合规范")
    if customPattern:
        for customPatternName in customPattern.keys():
            for command in customPattern[customPatternName]:
                if len(command)<2:
                    raise Exception("自定义方法定义不符合规范")
                head = command[0]
                if head not in FUNCTION_DICT.keys():
                    raise Exception("自定义方法定义不符合规范")
    print("语法检查通过")

# 读取sprd文件
def run(fileName):
    with open(fileName,'r',encoding="utf-8") as f:
        sprdYAML=yaml.load(f, Loader=yaml.SafeLoader)
        syntaxCheck(sprdYAML)
        metadata = sprdYAML["metadata"]
        characters = sprdYAML["角色"]
        bars = sprdYAML['小节']
        customPattern=None
        try:
            customPattern = sprdYAML['自定义方法']
        except:
            customPattern = None
        parseMetaData(metadata)
        parseCharacter(characters)
        for barNum in bars.keys():
            parseBar(bars[barNum],int(barNum),customPattern)
        Export()
        print("Done.")

# 读取命令行参数
import sys
run(sys.argv[1])
