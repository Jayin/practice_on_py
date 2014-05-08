#endcoding:utf-8
from _ast import UAdd
import json


class User:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        print ('<User age=', str(self.age), ' name=', self.name, '>')
        return ''.join(('<User age=', str(self.age), ' name=', self.name, '>'))


def user_to_json(user):
    return {
        'age': user.age,
        'name': user.name
    }


user = User(12, 'jayin ton')
user_to_json(user)
print json.dumps(user, default=user_to_json)
"""
 注意不能直接dumps 对象，可以通过default 来规定序列化规则
"""

'偷懒方法：'
"""
因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
也有少数例外，比如定义了__slots__的class。

indent参数是缩进的意思  sort_keys（对dict对象进行排序
"""
print json.dumps(user, default=lambda obj: obj.__dict__,sort_keys=True,indent=4)

"""
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例：

"""


def dict2user(u):
    return User(u['name'], u['age'])


# json_str = '{"age": 20, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2user))