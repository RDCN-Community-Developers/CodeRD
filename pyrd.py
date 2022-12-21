import json

level = {
    "settings":{},
    "rows":[],
    "decorations":[],
    "events":[],
};

#覆写 .rdlevel中的settings
#参数从左到右依次是:艺术家,歌曲名,作者名,难度,是否开启癫痫警告,(可选)预览照片,(可选)针管图象,(可选)描述,(可选)miss对应rank,(可选)rank对应结算语
def SetLevelMeta(metaDataDict):
    level['settings']={
        "version":54,
        "artist":metaDataDict["artist"],
        "song":metaDataDict["song"],
        "author":metaDataDict["author"],
        "specialArtistType": "None", 
		"artistPermission": "", 
		"artistLinks": "", 
		"difficulty": metaDataDict["difficulty"], 
		"seizureWarning": metaDataDict["seizureWarning"], 
		"previewImage": "", 
		"syringeIcon": "", 
		"previewSong": "", 
		"previewSongStartTime": 0, 
		"previewSongDuration": 2.667, 
		"songNameHue": 0, 
		"songLabelGrayscale": False, 
		"description": metaDataDict["description"], 
		"tags": "", 
		"separate2PLevelFilename": "", 
		"canBePlayedOn": "OnePlayerOnly", 
		"firstBeatBehavior": "RunNormally", 
		"multiplayerAppearance": "HorizontalStrips", 
		"levelVolume": 1, 
		"rankMaxMistakes": metaDataDict["rankMaxMistakes"], 
		"rankDescription": metaDataDict["rankDescription"],
    }

# 添加角色
# 参数从左到右依次是:角色名(有校验),轨道类型(有校验),轨道
def AddCharacter(character,rowType,rooms,row,pulseSound,hideAtStart=False,pulseSoundVolume=100,pulseSoundPitch=100,pulseSoundPan=0,pulseSoundOffset=0):
    #TODO:节拍音效校验
    #建立单个角色的dict
    characterDict={ "character": character if character else "None",
                    "rowType": rowType,
                    "row": int(row), 
                    "rooms": [int(rooms)],
                    "player": "P1",
                    "hideAtStart": hideAtStart if hideAtStart else False,
                    "pulseSound": pulseSound,
                    "pulseSoundVolume": pulseSoundVolume if pulseSoundVolume else 100,
                    "pulseSoundPitch": pulseSoundPitch if pulseSoundPitch else 100,
                    "pulseSoundPan": pulseSoundPan if pulseSoundPan else 0,
                    "pulseSoundOffset": pulseSoundOffset if pulseSoundOffset else 0
                    }
    #将dict添加到rows中
    level['rows'].append(characterDict)

#{ "bar": 1, "beat": 1, "y": 0, "type": "PlaySong", "filename": "sndOrientalTechno", "volume": 100, "pitch": 100, "pan": 0, "offset": 0, "bpm": 100, "loop": false },
def PlayMusic(bar,beat,fileName,bpm,offset,volume=100,pitch=100,pan=0):
    musicDict={ "bar": bar,
                "beat": beat, 
                "y": 0, 
                "type": "PlaySong", 
                "filename": fileName, 
                "volume": volume if volume else 100, 
                "pitch": pitch if pitch else 100, 
                "pan": pan if pan else 0, 
                "offset": offset, 
                "bpm": bpm, 
                "loop": False
                }
    level['events'].append(musicDict)
#{ "bar": 1, "beat": 1, "y": 0, "type": "AddClassicBeat", "row": 0, "tick": 1, "swing": 0, "hold": 0 },
def AddClassicBeat(bar,beat,row,tick,swing):
    beatDict={  "bar": bar, 
                "beat": beat, 
                "y": row, 
                "type": "AddClassicBeat", 
                "row": row, 
                "tick": tick, 
                "swing": swing, 
                "hold": 0
             }
    level['events'].append(beatDict)
#{ "bar": 1, "beat": 1, "y": 1, "type": "AddOneshotBeat", "row": 1, "pulseType": "Wave", "tick": 1 },
def AddOneshotBeat(bar,beat,row,tick,pulseType="Wave",squareSound=False):
    beatDict={  "bar": bar, 
                "beat": beat, 
                "y": row, 
                "type": "AddOneshotBeat", 
                "row": row, 
                "pulseType":pulseType if pulseType else "Wave", 
                "tick": tick,
                "squareSound": squareSound
            }
    level['events'].append(beatDict)
#{ "bar": 3, "beat": 3, "y": 0, "type": "SetRowXs", "row": 0, "pattern": "------", "syncoBeat": -1, "syncoSwing": 0 },
def SetX(bar,beat,row,pattern,syncoBeat=-1,syncoSwing=0):
    XDict={ "bar": bar, 
            "beat": beat, 
            "y": row, 
            "type": "SetRowXs", 
            "row": row, 
            "pattern": pattern, 
            "syncoBeat": syncoBeat, 
            "syncoSwing": syncoSwing 
        }
    level['events'].append(XDict)
#{ "bar": 4, "beat": 7, "y": 0, "type": "AddClassicBeat", "row": 0, "tick": 1, "swing": 0, "setXs": "FourBeat", "hold": 3 },
def LongBeat(bar,beat,row,tick,swing,hold,setXs):
    beatDict={  "bar": bar, 
                "beat": beat, 
                "y": row, 
                "type": "AddClassicBeat", 
                "row": row, 
                "tick": tick, 
                "swing": swing, 
                "setXs": setXs, 
                "hold": hold
            }
    level['events'].append(beatDict)

#{ "bar": 2, "beat": 3, "y": 0, "type": "AddFreeTimeBeat", "row": 0, "hold": 0, "pulse": 0 },
def FreeBeat_Start(bar,beat,row):
    beatDict={
        "bar":bar,
        "beat":beat,
        "y":row,
        "type":"AddFreeTimeBeat",
        "row":row,
        "hold":0,
        "pulse":0
    }
    level['events'].append(beatDict)
#{ "bar": 2, "beat": 4, "y": 0, "type": "PulseFreeTimeBeat", "row": 0, "hold": 0, "action": "Increment", "customPulse": 0 },
def FreeBeat_Pulse(bar,beat,row,action,customPulse):
    beatDict={  "bar": bar, 
                "beat": beat, 
                "y": row, 
                "type": "PulseFreeTimeBeat", 
                "row": row, 
                "hold": 0, 
                "action": action, 
                "customPulse": customPulse 
    }
    level['events'].append(beatDict)

def AddPresetVFX(bar,beat,row,preset,enable,*ex):
    actionDict={ "bar": bar,
                 "beat": beat,
                 "y": row,
                 "type": "SetVFXPreset",
                 "rooms": [0],
                 "preset": preset,
                 "enable": enable
    }
    sp1=["Rain","JPEG","Mosaic","ScreenWaves","Grain","Blizzard","Drawing","Aberration","Blur","HueShift"]
    sp2=["TileN","CustomScreenScroll"]
    if preset in sp1:
        actionDict.update({"intensity": ex[0],
                           "duration": ex[1],
                           "ease": ex[2]
                           })
    elif preset in sp2:
        actionDict.update({"floatX": ex[0],
                           "floatY": ex[1]
                           })
    elif preset=="Bloom":
        actionDict.update({"threshold": ex[0],
                           "intensity": ex[1],
                           "color": ex[2],
                           "duration": ex[3],
                           "ease": ex[4]
                           })
    level['events'].append(actionDict)
    
def SetBackgroundColor(bar,beat,row,mode,color="FFFFFFFF",image=[],fps=130,cmode="ScaleToFill",ft="NearestNeighbor",x=0,y=0,duration=0,ease="Linear"):
    actionDict={ "bar": bar,
                 "beat": beat,
                 "y": row,
                 "type": "SetBackgroundColor",
                 "rooms": [0],
                 "backgroundType": mode,
                 "contentMode": cmode,
                 "color": color,
                 "image": [image],
                 "fps": fps,
                 "filter": ft,
                 "scrollX": x,
                 "scrollY": y,
                 "duration": duration,
                 "ease": ease }
    level['events'].append(actionDict)

def Flash(bar,beat,row,duration):
    actionDict={ "bar": bar,
                 "beat": beat,
                 "y": row,
                 "type": "Flash",
                 "rooms": [0],
                 "duration": duration }
    level['events'].append(actionDict)

def Comment(bar,beat,row,text,tab,show=False,color="F2E644"):
    actionDict={ "bar": bar,
                 "beat": beat,
                 "y": row,
                 "type": "Comment",
                 "tab": tab,
                 "show": show,
                 "text": text,
                 "color": color }
    level['events'].append(actionDict)

#{ "bar": 1, "beat": 4, "y": 0, "type": "SayReadyGetSetGo", "phraseToSay": "SayReaDyGetSetGoNew", "voiceSource": "Nurse", "tick": 1, "volume": 100 },
def SayReadyGetSetGo(bar,beat,phraseToSay,voice="Nurse",tick=1,volume=100):
    voiceDict={
        "bar":bar,
        "beat":beat,
        "y":1,
        "type":"SayReadyGetSetGo",
        "phraseToSay":phraseToSay,
        "voiceSource":voice if voice else "Nurse",
        "tick":tick if tick else 1,
        "volume":volume if volume else 100
    }
    level['events'].append(voiceDict)

#{ "bar": 1, "beat": 3, "y": 0, "type": "SetBeatsPerMinute", "beatsPerMinute": 100 },
def SetBeatsPerMinute(bar,beat,bpm):
    BPMDict = { "bar": bar,
                "beat": beat, 
                "y": 0, 
                "type": "SetBeatsPerMinute", 
                "beatsPerMinute": bpm 
            }
    level['events'].append(BPMDict)

def Export():
    fileName=level["settings"]["artist"]+"-"+level["settings"]["song"]+".rdlevel"
    with open(fileName,"w",encoding="utf-8")as f:
        f.write(json.dumps(level,sort_keys=True, indent=2).encode('utf-8').decode("unicode_escape"))
