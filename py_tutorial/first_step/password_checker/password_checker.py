numbers = ['0','1','2','3','4','5','6','7','8','9']
password = input('비밀번호를 입력하세요. ')
print('비밀번호의 길이는 {}입니다.'.format(len(password)))
found = []
for letter in password:
    if letter in numbers:
        found.append(letter)
print('숫자를 {}개 사용하셨습니다.'.format(len(found)))
for f in found:
    print(f)
