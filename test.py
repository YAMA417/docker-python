# listなどはlengthなどを用いらなくとも変数で判定できる！！

# none(null) チェックは　object is Noneで実行できる

# forとifの使い方例
# for num in range(1, 100):
#   if num % 3 == 0 and num % 5 == 0:
#     print('TrySail')
#   elif num % 3 == 0:
#     print('おわりだよー(o・∇・o)')
#   elif num % 5 == 0:
#     print('(*>△<)<ナーンナーン')
#   else:
#     print(num)

try_sail = {'ピンク': '麻倉もも', '青': '雨宮天', '黄色': '夏川椎菜'}

for k, v in try_sail.items():
  print(k + ':', v)


# say_something()

# 関数の引数には引数名指定で呼び出せば、順序が関係なくなる！
def what_is_this(color):
  print(color)


what_is_this('pink')
