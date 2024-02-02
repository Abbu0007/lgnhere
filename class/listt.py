a={"a":1,"b":2,"c":3}
old_key="a"
new_key="z"
a[new_key]=a.pop(old_key)
print(a)