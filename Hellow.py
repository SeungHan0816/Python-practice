print ("VS Code 설치 다 했다!")
print ("Hellow World")
a = 1
b = "python"
c = [1,2,3]
id(c)
a = [1,2,3]
id(a)
print(a)
a = [1,2,3]
b = [4,5,6]
a+b
print(a+b)
print(id(a))
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." % treehit)
    if treehit == 10:
        print("나무가 넘어갑니다")

print("="*50)
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학색은 불합격입니다." %number)
print("="*50)

marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)

    num = int(input())

i = 0
while i < num:
    print('', num)
    i += 1