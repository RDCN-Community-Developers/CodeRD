# PyRD - 为视障谱师写节奏医生谱子的一种全新的尝试
大家好,这里是硫酸铜.
其实不知道大家注意过没有,节奏医生做了很多无障碍方面的内容,很大一部分原因在于节奏医生致力于给视障玩家带来同样的游玩体验.
而其中有一部分玩家,除了能完整的体验到游戏,还在往制谱方向发展.最熟为人知的应该就是卢毅.
但是,因为视障,谱师的写谱被限制在直接编辑.rdlevel文件,一个JSON格式的文件.
抛开繁琐的JSON语法不提,一旦写出问题,谱师们是难以纠错的,我们写一整个谱面的时间可能他们只能完成十来个小节.
所以,我想要尝试用一种方式来优化这个流程,于是我用python写了这样一个小的工具模块.
虽然,用python写的门槛仍旧不低,但是它比JSON编辑简单多了,对吧.
我会尽力将语法简化,步骤减少,也希望有更多人能够参与进来一起维护这个项目.
因为每一个人,都值得我们去善待.
# PyRD - A new way to create Rhythm Doctor Level by Python
Hello,this is Eric Guo from the Rhythm Doctor Chinese community.
I've been wondering,that RD has created a lot of contents to imporve accessibility for the blind players.
And then,some of them,despite of enjoying the game,they participated in making community maps for the game.(For the most famous,the one made 千本桜 with 3q4a and 来因洛特,卢毅,is a completely blind player and mapper.)
But,because of being blind,the mapping method was limited to directly creating .rdlevel file,that is,a JSON file.
JSON is complicated,despite of that,a single error(like accidentally deleting a '}') can cause a lot of time to correct. (While RD don't have a detailed load error traceback.)
So,I wanted to create a way to simplify this.That's why PyRD was born.
Although python is another language to learn for the mappers,but I've tried to simplify the cost of learning,and reduce the steps to make a chart.
I hope more of you guys can join in to maintain this project.
Because everyone is a treasure to be treated nicely.

# 使用说明
这只是一个很简单的模块，具体的内容在pyrd模块里有比较全面的注释，后期会加入Docs进行说明，如果想要使用，直接下载项目并新建Python文件，输入下面内容引用模块即可。
```python
from pyrd import *
```
# Usage
For now this is a simple module,and it‘s yet uncompleted.The detailed functions are all in pyrd.py,you can get in and have a look.for using this,just download this project,create a python file and import the module using the code above.

# TODO:
· 将角色封装为一个类 / Make Character a class
· 错误检验 / Error check and mapper
· 添加二拍提示音(参见rdnurse) / Generate Oneshot nurse sound(will have a look on project rdnurse)
# WON’T DO:
· VFX相关，因为本项目是比较针对于视障群体的，所以并不考虑对视觉和装饰部分逻辑进行处理（主要是没时间） / Functions about visual effects.Despite that this project is aimed to blind people,also I don‘t have a lot of time to code.
(如果你们谁有时间可以自己fork然后做了往我这里提pr) / If you guys have plenty of time you can fork,do it and submit pull request.