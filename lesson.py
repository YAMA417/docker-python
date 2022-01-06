import string
s = """\
Hi $name.

$contents

Hava a good day
"""

t = string.Template(s)
contents = t.substitute(name='URI', contents='Tyr Wish Us!')
print(contents)
# with open('test.txt', 'r+') as f:
#   # f.write(s)
#   # 書き込みをしたら初めに戻るようにしないと読み込みが書き込んだ後になる
#   f.seek(0)
#   print(f.read())
