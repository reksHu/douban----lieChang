from snownlp import SnowNLP
text = """
职场很空洞，恋情倒是狗血。猎场还是情场?杰克苏对现下的玛丽苏，谁也别笑谁。
"""

text2=u'今天阳光明媚,是一个非常舒服的一天'
s = SnowNLP(text)
print(s.sentiments)
# for t in s.tags:
#     print(t)

print(s.summary(3))