import json

level = {
    "settings": {},
    "rows": [],
    "decorations": [],
    "events": [],
}

# 覆写 .rdlevel中的settings
# 参数从左到右依次是:艺术家,歌曲名,作者名,难度,是否开启癫痫警告,(可选)预览照片,(可选)针管图象,(可选)描述,(可选)miss对应rank,(可选)rank对应结算语


def SetLevelMeta(metaDataDict):
    level['settings'] = {
        "version": 54,
        "artist": metaDataDict["artist"],
        "song": metaDataDict["song"],
        "author": metaDataDict["author"],
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


def parseIf(dict, If):
    if If:
        dict['if'] = If
    return dict

# 添加角色
# 参数从左到右依次是:角色名(有校验),轨道类型(有校验),轨道


def AddCharacter(character, rowType, rooms, row, pulseSound, hideAtStart=False, pulseSoundVolume=100, pulseSoundPitch=100, pulseSoundPan=0, pulseSoundOffset=0, If: str = ""):
    # TODO:节拍音效校验
    # 建立单个角色的dict
    characterDict = {"character": character if character else "None",
                     "rowType": rowType,
                     "row": int(row),
                     "rooms": [int(rooms)],
                     "player": "P1",
                     "hideAtStart": hideAtStart if hideAtStart else False,
                     "pulseSound": pulseSound,
                     "pulseSoundVolume": pulseSoundVolume if pulseSoundVolume else 100,
                     "pulseSoundPitch": pulseSoundPitch if pulseSoundPitch else 100,
                     "pulseSoundPan": pulseSoundPan if pulseSoundPan else 0,
                     "pulseSoundOffset": pulseSoundOffset if pulseSoundOffset else 0,
                     }
    # 将dict添加到rows中
    level['rows'].append(parseIf(characterDict, If))

# { "bar": 1, "beat": 1, "y": 0, "type": "PlaySong", "filename": "sndOrientalTechno", "volume": 100, "pitch": 100, "pan": 0, "offset": 0, "bpm": 100, "loop": false },


def PlayMusic(bar, beat, fileName, bpm, offset, volume=100, pitch=100, pan=0, If: str = ""):
    musicDict = {"bar": bar,
                 "beat": beat,
                 "y": 0,
                 "type": "PlaySong",
                 "filename": fileName,
                 "volume": volume if volume else 100,
                 "pitch": pitch if pitch else 100,
                 "pan": pan if pan else 0,
                 "offset": offset,
                 "bpm": bpm,
                 "loop": False,
                 }
    level['events'].append(parseIf(musicDict, If))
# { "bar": 1, "beat": 1, "y": 0, "type": "AddClassicBeat", "row": 0, "tick": 1, "swing": 0, "hold": 0 },


def AddClassicBeat(bar, beat, row, tick, swing, If: str = ""):
    beatDict = {"bar": bar,
                "beat": beat,
                "y": row,
                "type": "AddClassicBeat",
                "row": row,
                "tick": tick,
                "swing": swing,
                "hold": 0
                }
    level['events'].append(parseIf(beatDict, If))
# { "bar": 1, "beat": 1, "y": 1, "type": "AddOneshotBeat", "row": 1, "pulseType": "Wave", "tick": 1 },


def AddOneshotBeat(bar, beat, row, tick,loops=0,skipShot=False,interval=0,pulseType="Wave", squareSound=False, If: str = ""):
    beatDict = {"bar": bar,
                "beat": beat,
                "y": row,
                "type": "AddOneshotBeat",
                "row": row,
                "pulseType": pulseType if pulseType else "Wave",
                "tick": tick,
                "squareSound": squareSound,
                "loops": loops if loops else 0,
                "interval": interval if interval else 0,
                "skipshot":skipShot if skipShot else False,
                }
    level['events'].append(parseIf(beatDict, If))
# { "bar": 3, "beat": 3, "y": 0, "type": "SetRowXs", "row": 0, "pattern": "------", "syncoBeat": -1, "syncoSwing": 0 },


def SetX(bar, beat, row, pattern, syncoBeat=-1, syncoSwing=0, If: str = ""):
    XDict = {"bar": bar,
             "beat": beat,
             "y": row,
             "type": "SetRowXs",
             "row": row,
             "pattern": pattern,
             "syncoBeat": syncoBeat,
             "syncoSwing": syncoSwing
             }
    level['events'].append(parseIf(XDict, If))
# { "bar": 4, "beat": 7, "y": 0, "type": "AddClassicBeat", "row": 0, "tick": 1, "swing": 0, "setXs": "FourBeat", "hold": 3 },


def LongBeat(bar, beat, row, tick, swing, hold, setXs, If: str = ""):
    beatDict = {"bar": bar,
                "beat": beat,
                "y": row,
                "type": "AddClassicBeat",
                "row": row,
                "tick": tick,
                "swing": swing,
                "setXs": setXs,
                "hold": hold
                }
    level['events'].append(parseIf(beatDict, If))

# { "bar": 2, "beat": 3, "y": 0, "type": "AddFreeTimeBeat", "row": 0, "hold": 0, "pulse": 0 },


def FreeBeat_Start(bar, beat, row, If: str = ""):
    beatDict = {
        "bar": bar,
        "beat": beat,
        "y": row,
        "type": "AddFreeTimeBeat",
        "row": row,
        "hold": 0,
        "pulse": 0
    }
    level['events'].append(parseIf(beatDict, If))
# { "bar": 2, "beat": 4, "y": 0, "type": "PulseFreeTimeBeat", "row": 0, "hold": 0, "action": "Increment", "customPulse": 0 },


def FreeBeat_Pulse(bar, beat, row, action, customPulse, If: str = ""):
    beatDict = {"bar": bar,
                "beat": beat,
                "y": row,
                "type": "PulseFreeTimeBeat",
                "row": row,
                "hold": 0,
                "action": action,
                "customPulse": customPulse
                }
    level['events'].append(parseIf(beatDict, If))

# { "bar": 1, "beat": 4, "y": 0, "type": "SayReadyGetSetGo", "phraseToSay": "SayReaDyGetSetGoNew", "voiceSource": "Nurse", "tick": 1, "volume": 100 },


def SayReadyGetSetGo(bar, beat, phraseToSay, voice="Nurse", tick=1, volume=100, If: str = ""):
    voiceDict = {
        "bar": bar,
        "beat": beat,
        "y": 1,
        "type": "SayReadyGetSetGo",
        "phraseToSay": phraseToSay,
        "voiceSource": voice if voice else "Nurse",
        "tick": tick if tick else 1,
        "volume": volume if volume else 100
    }
    level['events'].append(parseIf(voiceDict, If))


def AddPresetVFX(bar, beat, row, preset, enable=True, *ip):
    ex = list(ip)
    for _ in range(4):
        ex.append(None)
    actionDict = {"bar": bar,
                  "beat": beat,
                  "y": row,
                  "type": "SetVFXPreset",
                  "rooms": [0],
                  "preset": preset,
                  "enable": enable if enable else True
                  }
    sp1 = ["Rain", "JPEG", "Mosaic", "ScreenWaves", "Grain", "Blizzard",
           "Drawing", "Aberration", "Blur", "RadialBlur", "HueShift"]
    sp2 = ["TileN", "CustomScreenScroll"]
    if preset in sp1:
        actionDict.update({"intensity": ex[0] if ex[0] else 100,
                           "duration": ex[1] if ex[1] else 0,
                           "ease": ex[2] if ex[2] else "Linear"
                           })
    elif preset in sp2:
        actionDict.update({"floatX": ex[0] if ex[0] else 1,
                           "floatY": ex[1] if ex[1] else 1
                           })
    elif preset == "Bloom":
        actionDict.update({"threshold": ex[0] if ex[0] else 0.3,
                           "intensity": ex[1] if ex[1] else 2,
                           "color": ex[2] if ex[2] else "000000",
                           "duration": ex[3] if ex[3] else 0,
                           "ease": ex[4] if ex[4] else "Linear"
                           })
    level['events'].append(actionDict)


def SetBackgroundColor(bar, beat, row, mode, color="FFFFFFFF", image="", fps=130, cmode="ScaleToFill", ft="NearestNeighbor", x=0, y=0, duration=0, ease="Linear"):
    actionDict = {"bar": bar,
                  "beat": beat,
                  "y": row,
                  "type": "SetBackgroundColor",
                  "rooms": [0],
                  "backgroundType": mode,
                  "contentMode": cmode,
                  "color": color if color else "FFFFFFFF",
                  "image": [image] if image else [],
                  "fps": fps if fps else 130,
                  "filter": ft if ft else "NearestNeighbor",
                  "scrollX": x if x else 0,
                  "scrollY": y if y else 0,
                  "duration": duration if duration else 0,
                  "ease": ease if ease else "Linear"}
    level['events'].append(actionDict)


def TintRows(bar, beat, row, change=-1, border="None", color="FFFFFF", opacity=100, effect=False, totalOpacity=100, tint=False, fillColor="FFFFFF", fillOpacity=100):
    actionDict = {"bar": bar,
                  "beat": beat,
                  "y": row,
                  "type": "TintRows",
                  "rooms": [0],
                  "row": change if change else -1,
                  "border": border if border else "None",
                  "borderColor": color if color else "FFFFFF",
                  "borderOpacity": opacity if opacity else 100,
                  "opacity": totalOpacity if totalOpacity else 100,
                  "tint": tint if tint else False,
                  "tintColor": fillColor if fillColor else "FFFFFF",
                  "tintOpacity": fillOpacity if fillOpacity else 100}
    if effect:
        actionDict.update({"effect": "Electric"})
    level['events'].append(actionDict)


def Flash(bar, beat, row, duration):
    actionDict = {"bar": bar,
                  "beat": beat,
                  "y": row,
                  "type": "Flash",
                  "rooms": [0],
                  "duration": duration}
    level['events'].append(actionDict)


def Comment(bar, beat, row, text, tab, show=False, color="F2E644"):
    actionDict = {"bar": bar,
                  "beat": beat,
                  "y": row,
                  "type": "Comment",
                  "tab": tab,
                  "show": show if show else False,
                  "text": text,
                  "color": color if color else "F2E644"}
    level['events'].append(actionDict)


# { "bar": 1, "beat": 3, "y": 0, "type": "SetBeatsPerMinute", "beatsPerMinute": 100 },


def SetBeatsPerMinute(bar, beat, bpm, If: str = ""):
    BPMDict = {"bar": bar,
               "beat": beat,
               "y": 0,
               "type": "SetBeatsPerMinute",
               "beatsPerMinute": bpm
               }
    level['events'].append(parseIf(BPMDict, If))


def PlaySound(bar, beat, fileName, volume=100, pitch=100, pan=0, offset=0, isCustom=False, customSoundType="CueSound", If: str = ""):
    soundDict = {"bar": bar,
                 "beat": beat,
                 "y": 0,
                 "type": "PlaySound",
                 "filename": fileName,
                 "volume": volume if volume else 100,
                 "pitch": pitch if pitch else 100,
                 "pan": pan if pan else 0,
                 "offset": offset if offset else 0,
                 "isCustom": isCustom if isCustom else False,
                 "customSoundType": customSoundType if customSoundType else "CueSound"
                 }
    level['events'].append(parseIf(soundDict, If))


def SetCountingSound(bar, beat, row, voiceSource="IanCountCalm", enabled=True, volume=100, If: str = ""):
    countSoundDict = {
        "bar": bar,
        "beat": beat,
        "y": 0,
        "type": "SetCountingSound",
        "row": row,
        "voiceSource": voiceSource if voiceSource else "IanCountCalm",
        "enabled": enabled if enabled else True,
        "volume": volume if volume else 100
    }
    level['events'].append(parseIf(countSoundDict, If))


def NarrateRowInfo(bar, beat, row, infoType, customPattern, skipUnstable=False, soundOnly=False, narrateSkipBeats="on", If: str = ""):
    narrateRowDict = {
        "bar": bar,
        "beat": beat,
        "y": 0,
        "type": "NarrateRowInfo",
        "row": row,
        "infoType": infoType,
        "customPattern": customPattern,
        "soundOnly": soundOnly if soundOnly else False,
        "narrateSkipBeats": narrateSkipBeats if narrateSkipBeats else "on",
        "skipUnstable": skipUnstable if skipUnstable else False
    }
    level['events'].append(parseIf(narrateRowDict, If))


def ReadNarration(bar, beat, text, category="Describption", If: str = ""):
    narrationDict = {
        "bar": bar,
        "beat": beat,
        "y": 0,
        "type": "ReadNarration",
        "text": text,
        "category": category if category else "Describption"
    }
    level['events'].append(parseIf(narrationDict, If))


def ShowDialogue(bar, beat, text, speed, portraitSide="Left", playTextSounds=True, If: str = ""):
    dialogueDict = {
        "bar": bar,
        "beat": beat,
        "y": 0,
        "type": "ShowDialogue",
        "text": text,
        "speed": speed,
        "portraitSide": portraitSide if portraitSide else "Left",
        "playTextSounds": playTextSounds if playTextSounds else True
    }
    level['events'].append(parseIf(dialogueDict, If))


def Export():
    fileName = level["settings"]["artist"] + \
        "-"+level["settings"]["song"]+".rdlevel"
    with open(fileName, "w", encoding="utf-8")as f:
        f.write(json.dumps(level, sort_keys=True, indent=2).encode(
            'utf-8').decode("unicode_escape"))
