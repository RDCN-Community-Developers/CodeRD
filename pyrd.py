import json

CHARACTERS=["Adog", "Barista", "Beat", "Bodybuilder", "Boy", "BoyRaya", "BoyTangzhuang", "Buro", "Clef", "Cockatiel", "ColeGuitar", "ColeSynth", "Controller", "Edega", "Farmer", "FarmerAlternate", "Girl", "GirlCNY", "HoodieBoy", "HoodieBoyAlternate", "HoodieBoyBlue", "Ian", "IanBubble", "Kanye", "Lucia", "Marija", "Miner", "MrsStevendog", "MrsStevenson", "MrStevendog", "MrStevenson", "NicoleCigs", "NicoleCoffee", "NicoleMints", "None", "Oriole", "Owl", "Paige", "Parrot", "Politician", "Purritician", "Quaver", "Rin", "Rodney", "Samurai", "SamuraiBlue", "SamuraiBoss", "SamuraiBossAlt", "SamuraiGirl", "SamuraiGreen", "SamuraiYellow", "SmokinBarista", "Tentacle", "Treble"]

level = {
    "settings":{},
    "rows":[],
    "decorations":[],
    "events":[],
};

#覆写 .rdlevel中的settings
#参数从左到右依次是:艺术家,歌曲名,作者名,难度,是否开启癫痫警告,(可选)预览照片,(可选)针管图象,(可选)描述,(可选)miss对应rank,(可选)rank对应结算语
def 设置关卡信息(artist,song,author,difficulty,seizureWarning,previewImage="",syringeIcon="",description="",rankMaxMistakes=[20,15,10,5],rankDescription=["","","","","",""]):
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

# 添加角色
# 参数从左到右依次是:角色名(有校验),轨道类型(有校验),轨道
def 添加角色(character,rowType,row,rooms,hideAtStart,pulseSound):
    #进行了一些本地化常见替换
    if character == '无':
        character = "None"
    if rowType == '七拍':
        rowType = 'Classic'
    elif rowType == '二拍':
        rowType = "Oneshot"
    #有效性检测
    if not ((character in CHARACTERS)): 
        raise Exception("您在添加角色时使用了错误的角色名"+character+",如果您不想添加角色,请在角色参数填无")
    if not (rowType == "Classic" or rowType == "Oneshot"):
        raise Exception("您在添加角色"+character+"时使用了错误的节拍类型，对于七拍轨道,请输入Classic或者\"七拍\";对于单发拍子,请输入Oneshot或者\"二拍\".注意,字母开头大写.")
    #TODO:节拍音效校验
    #建立单个角色的dict
    characterDict={ "character": character,
                    "rowType": rowType,
                    "row": row, 
                    "rooms": rooms,
                    "player": "P1",
                    "hideAtStart": hideAtStart,
                    "pulseSound": pulseSound,
                    "pulseSoundVolume": 100,
                    "pulseSoundPitch": 100,
                    "pulseSoundPan": 0,
                    "pulseSoundOffset": 0
                    }
    #将dict添加到rows中
    level['rows'].append(characterDict)

#{ "bar": 1, "beat": 1, "y": 0, "type": "PlaySong", "filename": "sndOrientalTechno", "volume": 100, "pitch": 100, "pan": 0, "offset": 0, "bpm": 100, "loop": false },
def 播放音乐(bar,beat,fileName,offset,bpm,volume=100,pitch=100,pan=0):
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
#{ "bar": 1, "beat": 1, "y": 0, "type": "AddClassicBeat", "row": 0, "tick": 1, "swing": 0, "hold": 0 },
def Classic(bar,beat,row,tick,swing):
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
def Oneshot(bar,beat,row,pulseType,tick,squareSound=False):
    beatDict={  "bar": bar, 
                "beat": beat, 
                "y": row, 
                "type": "AddOneshotBeat", 
                "row": row, 
                "pulseType":pulseType, 
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
def LongBeat(bar,beat,row,tick,swing,setXs,hold):
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
def Export():
    fileName=level["settings"]["artist"]+"-"+level["settings"]["song"]+".rdlevel"
    with open(fileName,"w")as f:
        f.write(json.dumps(level))

