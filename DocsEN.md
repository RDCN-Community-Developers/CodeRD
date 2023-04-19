This document is for YAML branch,in this branch,you can use yaml language to create a simple RD level,so it is also called simpleRD with the file suffix .sprd.

If you wanted to use Python directly to create a level,you can just create a python file,and import pyrd module in your project.The full Python method documention is on its way.

For simpleRD,it mainly contains 3 parts,including metadata,characters and bars.
## Metadata

The parameters that go into metadata:

```yaml
metadata:
  artist:Artist Name
  song:Song Name
  author:Author Name
  description:Describption
  seizureWarning:True/False
  difficulty:Easy/Normal/Tough/VeryTough
  tags:Tags
  rankMaxMistakes:[20,15,10,5]
  rankDescription:["F","D","C","B","A","S"]
```
Of course,the metadata information is non-essential,you can leave blank and it will automatically create an empty one.

## Character

For characters,each line of yaml defines a row with a character using a list.

It has ten parameters in total,five are required,and the rest are optional.

If you wanted to skip some of the optional ones and define other optional parameters,just add . to the parameters you wanted to skip.

```yaml
 - [characterName(or None),beatType(Classic/Oneshot),room,row,beatSound,*hideAtStart,*volume,*pitch,*pan,*offset]
```

Example:

```yaml
 - [Samurai,Classic,0,1,Stick]
 - [Cole,Oneshot,0,2,Kick]
```
## Bar

For the bar/beat,in the third section,please mark each bar into separate ones by bar number as below:

```yaml
1:
 - [PlayMusic,1,sndOrientalTechno,100,0]
```

Supported Parameters(All with "if" parameter at the last,won't list that out because it's undone):

```yaml
- [PlayMusic,beat,musicName,BPM,offset,*volume,*pitch,*pan]
- [AddClassicBeat,beat,row,length,swing] 
- [AddOneshotBeat,beat,row,length,*loop,*skipBeat,*freezeInterval,*oneshotType，*playTonk:boolean]
- [SetX,beat,row,xPattern,SyncoBeat,SyncoSwing] (SetX)
- [LongBeat,beat,row,length,swing,hold,XPattern]
- [FreeBeat_Start,beat,row]
- [FreeBeat_Pulse,beat,row,behavior,customPulse]
- [SayReadyGetSetGo,beat,content,*voice,*beatLength,*volume]
- [SetBPM,beat,bpm]
- [PlaySound,beat,soundName,*volume,*pitch,*pan,*offset,*isCustom:boolean]
- [SetCountingSound,beat,row,*voice,*isOn:boolean,*volume]
- [NarrateRow,beat,row,infoType,XPattern,*skipUnstable:boolean,*isOnlySound:boolean,*isReadSkipBeats:boolean]
- [ReadNarration,beat,text,*category]
- [ShowDialogue,beat,text,speed,*portraitSide,*playTextSound:boolean]

```

The more detailed parameter type could be found in pyrd.py,I'll maintain this document later,or you can open a pull request to update this.

After completing your coding,please execute compiler.py mylevel.sprd


## Advanced:VFX grammer(Waiting to be translated)
（进阶）VFX语法（由群内0x4D2提供）：
```yaml
- [预设特效,beat,row,特效名称,*是否激活,*属性]
```
只有个别特效具有 属性 参数。

  - 对于 落雨/JPEG失真/马赛克/海底波浪/电影噪点/暴风雪/素描/色像差/模糊/径向模糊/色调偏移：强度,缓速时长,缓速

  - 对于 自定义屏幕块/自定义滚屏：x/y

  - 对于 高光：阈值,强度,颜色,缓速时长,缓速
```yaml
- [设置背景,beat,row,模式,*颜色,*图片,*fps,*填充模式,*过滤器]
```

   * 模式: 颜色/图片
	
   * 对于 平铺 填充模式，有额外的参数：速度x,速度y,时长,缓速
	
```yaml
- [轨道涂色,beat,row,*受影响的轨道编号,*边框样式,*边框颜色,*边框透明度,*是否启动电击效果,*透明度,*是否填充,*填充颜色,*填充透明度]
```


* 受影响的轨道编号 如果为-1或"全部"，则全部轨道均受影响，
	
* 边框样式 无边框/轮廓/发光
	
* 透明度最大为100（不透明）

```yaml
- [闪烁,beat,row,时长]
```
* 时长 短/中/长
```yaml
- [注释,beat,row,注释文字,*播放时是否显示注释,*注释颜色]
```

## Example：Github exampleYAML.sprd

```yaml
metadata:
 artist: Rhythm Doctor
 song: 1-1
 author: Lu yi
 difficulty: Easy
 serizureWarning: False
 describption: This is a normal level.
charcters:
 - [Samurai,Classic,0,1,Stick]
 - [Cole,Oneshot,0,2,Kick]
bars:
 1:
  - [PlayMusic,1,sndOrientalTechno,100,0]
  - [AddPresetVFX,1,0,Rain,True]
 2:
  - [AddClassicBeat,1,1,1,0]
 3:
  - [AddClassicBeat,1,1,1,0]
 4:
  - [AddOneshotBeat,1,1,1,0]
  - [SayReadyGetSetGo,5,SayReaDyGetSetGoNew,.,1,100]
 5:
  - [AddOneshotBeat,1,2,1]
  - [AddOneshotBeat,3,2,1]
  - [AddOneshotBeat,5,2,1]
  - [AddOneshotBeat,7,2,1]
  - [SayReadyGetSetGo,8,JustSayStop,.,1,100]


```