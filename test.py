# listなどはlengthなどを用いらなくとも変数で判定できる！！

# none(null) チェックは　object is Noneで実行できる

print("test")
# count = 0
# while True:
#   if count >= 5:
#     break
#   elif count == 2:
#     count += 1
#     continue
#   else:
#     print(count)
#     count += 1
# count = 0
# while count < 5:
#   if count == 1:
#     break
#   print(count)
#   count += 1
# else:
#   print('done')
while True:
  word = input('Enter:')
  num = int(word)
  if num == 100:
    break
  print('next')
