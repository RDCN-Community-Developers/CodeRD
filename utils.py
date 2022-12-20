ARGSACCEPTED=[
            #接受直接输入的英文
            #角色部分
            "Boy","ColeGuitar","ColeSynth","Farmer","Girl","HoodieBoy","Miner","MrsStevenson","MrStevenson","NicoleCoffee","None","Owl","Parrot","Politician","Samurai",
            #节拍部分
            "Oneshot","Classic",
]

TRANSLATION={
            #方便用中文替换，减少输入英文数量
            #角色部分的翻译(仅翻译了部分常用角色)
            "洛根":"Boy",  
            "吉他科尔":"ColeGuitar", 
            "合成器科尔":"ColeSynth", 
            "农夫":"Farmer", 
            "海莉":"Girl", 
            "普通科尔":"HoodieBoy", 
            "矿工":"Miner", 
            "史蒂文森太太":"MrsStevenson", 
            "史蒂文森夫人":"MrStevenson", 
            "咖啡妮可":"NicoleCoffee",
            "无":"None", 
            "猫头鹰":"Owl", 
            "鹦鹉":"Parrot", 
            "政客":"Politician", 
            "武士":"Samurai",
            #二拍和七拍的翻译
            "二拍":"Oneshot",
            "七拍":"Classic",
            "2":"Oneshot",
            "7":"Classic",
        }
        
#中英对换，以及检查英文是否输入正确
def replaceString(string:str):
    #中英文检查
    if string.isalpha():
        if ARGSACCEPTED[string]:
            return string
        else:
            raise Exception("您提供的参数\""+string+"\"出错,如果您坚信这是一个错误,请联系硫酸铜进行处理.")
    elif TRANSLATION[string]:
        return TRANSLATION[string]
    else:
        raise Exception("您提供的中文\""+string+"\"并不在程序库中,如果您坚信这是一个错误,请联系硫酸铜进行处理.")