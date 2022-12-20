import json
from utils import replaceString

level = {
    "settings":{ },
    "rows":[ ],
    "decorations":[ ],
    "events":[ ],
};

class Character:
    characterName = " "
    room = [ ]
    row = -1
    beatType = " "
    def __init__(self,characterName:str,room:int,row:int,beatType:str,pulseSound:str,hideAtStart:bool=True,pulseVolume:int=100,pulsePitch:int=100,pulsePan:int=0,pulseOffset:int=0):
        self.characterName=replaceString(characterName)
        self.room.append(room)
        self.row = row
        self.beatType = replaceString(beatType)
        #添加角色到rows里
        characterDict={ "character": self.characterName,
                        "rowType": self.beatType,
                        "row": self.row, 
                        "rooms": self.room,
                        "player": "P1",
                        "hideAtStart": hideAtStart,
                        "pulseSound": pulseSound,
                        "pulseSoundVolume": pulseVolume,
                        "pulseSoundPitch": pulsePitch,
                        "pulseSoundPan": pulsePan,
                        "pulseSoundOffset": pulseOffset
                    }
        #将dict添加到rows中
        level['rows'].append(characterDict)
    
    #添加一个普通七拍
    def AddClassicBeat(self,bar,beat,tick,swing):
        if self.beatType != "Classic":
            raise Exception("角色\""+self.characterName+"\"为二拍轨道,而您尝试添加一个七拍.")
        beatDict={  "bar": bar, 
                    "beat": beat, 
                    "y": self.row, 
                    "type": "AddClassicBeat", 
                    "row": self.row, 
                    "tick": tick, 
                    "swing": swing, 
                    "hold": 0
                }
        level['events'].append(beatDict)
    
    #添加一个二拍轨道
    def AddOneshotBeat(self,bar,beat,pulseType,tick,squareSound=False):
        if self.beatType != "Oneshot":
            raise Exception("角色\""+self.characterName+"\"为二拍轨道,而您尝试添加一个七拍.")
        beatDict={  "bar": bar, 
                    "beat": beat, 
                    "y": self.row, 
                    "type": "AddOneshotBeat", 
                    "row": self.row, 
                    "pulseType":pulseType, 
                    "tick": tick,
                    "squareSound": squareSound
                }
        level['events'].append(beatDict)

    def SetX(self,bar,beat,pattern,syncoBeat=-1,syncoSwing=0):
        if self.beatType != "Classic":
            raise Exception("角色\""+self.characterName+"\"为二拍轨道,而您尝试添加一个七拍轨道的静音标记.")
        XDict={ "bar": bar, 
                "beat": beat, 
                "y": self.row, 
                "type": "SetRowXs", 
                "row": self.row, 
                "pattern": pattern, 
                "syncoBeat": syncoBeat, 
                "syncoSwing": syncoSwing 
        }
        level['events'].append(XDict)
    def LongPress(self,bar,beat,tick,swing,setXs,hold):
        if self.beatType != "Classic":
            raise Exception("角色\""+self.characterName+"\"为二拍轨道,而您尝试添加一个长按拍.")
        beatDict={  "bar": bar, 
                    "beat": beat, 
                    "y": self.row, 
                    "type": "AddClassicBeat", 
                    "row": self.row, 
                    "tick": tick, 
                    "swing": swing, 
                    "setXs": setXs, 
                    "hold": hold
                }
        level['events'].append(beatDict)
    def FreeBeat_Start(self,bar,beat):
        if self.beatType != "Classic":
            raise Exception("角色\""+self.characterName+"\"为二拍轨道,而您尝试添加一个自由拍.")
        beatDict={
            "bar":bar,
            "beat":beat,
            "y":self.row,
            "type":"AddFreeTimeBeat",
            "row":self.row,
            "hold":0,
            "pulse":0
        }
        level['events'].append(beatDict)
    def FreeBeat_Pulse(self,bar,beat,action,customPulse):
        if self.beatType != "Classic":
            raise Exception("角色\""+self.characterName+"\"为二拍轨道,而您尝试添加一个自由拍脉冲.")
        beatDict={  "bar": bar, 
                    "beat": beat, 
                    "y": self.row, 
                    "type": "PulseFreeTimeBeat", 
                    "row": self.row, 
                    "hold": 0, 
                    "action": action, 
                    "customPulse": customPulse 
        }
        level['events'].append(beatDict)
    
#TODO: rdnurse 移植
def CueOneShotBeep(self):
    pass

#覆写 .rdlevel中的settings
#参数从左到右依次是:艺术家,歌曲名,作者名,难度,是否开启癫痫警告,(可选)预览照片,(可选)针管图象,(可选)描述,(可选)miss对应rank,(可选)rank对应结算语
def SetLevelMeta(artist,song,author,difficulty,seizureWarning,previewImage="",syringeIcon="",description="",rankMaxMistakes=[20,15,10,5],rankDescription=["","","","","",""]):
    level['settings']={
        "version":54,
        "artist":artist,
        "song":song,
        "author":author,
        "specialArtistType": "None", 
		"artistPermission": "", 
		"artistLinks": "", 
		"author": author, 
		"difficulty": difficulty, 
		"seizureWarning": seizureWarning, 
		"previewImage": previewImage, 
		"syringeIcon": syringeIcon, 
		"previewSong": song, 
		"previewSongStartTime": 0, 
		"previewSongDuration": 2.667, 
		"songNameHue": 0, 
		"songLabelGrayscale": False, 
		"description": description, 
		"tags": "", 
		"separate2PLevelFilename": "", 
		"canBePlayedOn": "OnePlayerOnly", 
		"firstBeatBehavior": "RunNormally", 
		"multiplayerAppearance": "HorizontalStrips", 
		"levelVolume": 1, 
		"rankMaxMistakes": rankMaxMistakes, 
		"rankDescription": rankDescription,
    }

#{ "bar": 1, "beat": 1, "y": 0, "type": "PlaySong", "filename": "sndOrientalTechno", "volume": 100, "pitch": 100, "pan": 0, "offset": 0, "bpm": 100, "loop": false },
def PlayMusic(bar,beat,fileName,offset,bpm,volume=100,pitch=100,pan=0):
    musicDict={ "bar": bar,
                "beat": beat, 
                "y": 0, 
                "type": "PlaySong", 
                "filename": fileName, 
                "volume": volume, 
                "pitch": pitch, 
                "pan": pan, 
                "offset": offset, 
                "bpm": bpm, 
                "loop": False
                }
    level['events'].append(musicDict)

#{ "bar": 3, "beat": 3, "y": 0, "type": "SetRowXs", "row": 0, "pattern": "------", "syncoBeat": -1, "syncoSwing": 0 },

#{ "bar": 4, "beat": 7, "y": 0, "type": "AddClassicBeat", "row": 0, "tick": 1, "swing": 0, "setXs": "FourBeat", "hold": 3 },


#{ "bar": 2, "beat": 3, "y": 0, "type": "AddFreeTimeBeat", "row": 0, "hold": 0, "pulse": 0 },

#{ "bar": 2, "beat": 4, "y": 0, "type": "PulseFreeTimeBeat", "row": 0, "hold": 0, "action": "Increment", "customPulse": 0 },

def Export():
    fileName=level["settings"]["artist"]+"-"+level["settings"]["song"]+".rdlevel"
    with open(fileName,"w")as f:
        f.write(json.dumps(level))

