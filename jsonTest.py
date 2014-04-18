import json,os

print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print json.dumps("\"foo\bar")

l = list(os.listdir(os.getcwd()))
print json.dumps({'reuslt': l})