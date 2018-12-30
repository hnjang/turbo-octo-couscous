numbers = ['0','1','2','3','4','5','6','7','8','9']
password = input('비밀번호를 입력하세요. ')
print('비밀번호의 길이는', len(password), '입니다.')
found = []
for letter in password:
    if letter in numbers:
        found.append(letter)
print('숫자를', len(found), '개 사용하셨습니다.')
for f in found:
    print(f)
