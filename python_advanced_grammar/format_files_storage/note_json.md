# JSON
- 在线工具
    - https://www.sojson.com/
    - http://www.w3school.com.cn/json/
    - http://www.runoob.com/json/json-tutorial.html
- JSON(JavaScriptObjectNotation)
- 轻量级的数据交换格式，基于ECMAScript
- json格式就是一个键值对格式的数据集
    - key: 字符串
    - value: 字符串，数字，列表，json
    - json使用大括号包裹
    - 键值对直接用逗号隔开
    
            student={
                “name":"liudana",
                "age": 18,
                "mobile":"15509871234"
                }
- json和python格式的对应：
    - 字符串：字符串
    - 数字：数字
    - 队列：列表
    - 对象：字典
    - 布尔值：布尔值（大小写转换）
- python for json
    - json包
    - json和python对象的转换
        - json.dumps(): 对对象编码，把python格式表示成json格式
        - json.loads(): 对对象解码，把json格式转换成python格式
    - python读取json文件：
        - json.dump(): 把内容写入文件
        - json.load(): 把json文件内容读入python
    - 案例----------V07.py
    - 案例----------V08.py读取文件
        
        
    