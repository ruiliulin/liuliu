import re

# 1. 匹配一行文字中所有开头的字母
s = "i love you but you don\'t love me"

# \b\w findall
content = re.findall(r"\w\b", s)
print(content)


# 2. 匹配一行文字中所有数字开头的内容
s1 = "i 22love 33you 44but 5you don\'t66 777love 99me"

# \d
content = re.findall(r"\b\d", s1)
print(content)


# 3. 匹配只含数字和字母的行
s2 = "i love you \n2222KKKKk but \ndeff122 you dont love \n23244as"

content = re.findall(r"\w+", s2, re.M)
print(content)


# 4. 写一个正则表达式，使其能匹配以下字符：‘bit', 'but', 'hat', 'hit', 'hut'
s3 = "'bit', 'but', 'hat', 'hit', 'hut'"

content = re.findall(r'..t', s3)
print(content)


# 5. 提取每行中 完整的年月日和时间段
s3 = 'se2332 1993-10-17 22:44:55 fhdsajklgh 2019-10-18 09:47:25'

content = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', s3)
print(content)


# 6. 提取电子邮件格式
s4 = """xxxxx@email.com xxxx@qq.com baidu.com 999.com jkjk@163.com"""

content = re.findall(r'\w+@\w+.com', s4)
print(content)


# 7. 把以上的合法的电子邮件地址替换成我自己的电子邮件地址
content = re.sub(r'\w+@+\w+.com', "llr@tuling.com", s4)
print(content)


# 8. 使用正则提取字符串中的单词
s5 = "i love you not because who 244 of 789fjasd not"
content = re.findall(r'\b[a-zA-Z]+\b', s5)
print(content)

# 9. 使用正则提取字符串中的单词
s6 = "i love you not because who 244 of 789fjasd not"
content = re.match(r'\b[a-zA-Z]+\b', s6)
content1 = re.search(r'^[a-zA-Z+\b]', s6)
print(content.group())
print(content1.group())
