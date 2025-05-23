a_list = [3, 4, 62, 27, 83 ,956, 26, 58, 3, 78, 168, 64, 78]
print(len(a_list))
print(len([1, 2, 3, 4, 5]))
print('='*50)
def print_list(a):
    for i in a:
        print(i)

print_list(a_list)
print('='*50)
def boy():
    print('I am a boy.')
    print('You are a girl.')
boy()
print('='*50)
def compare(x,y):
    if x>y:
        print('%s > %s' %(x,y))
    elif x<y:
        print('%s < %s' %(x,y))
    else:
        print('%s == %s' %(x,y))
x = int(input("x의 값"))
y = int(input("y의 값"))
compare(x,y)
print('='*50)
def numOfDigits(num):
    print(len(str(num)))
print('='*50)
def multi():
    for m in range(2,10):
        for n in range(1,10):
            print(f'{m} * {n} = {m*n:2d}')
        print('-'*50)
multi()
print('='*50)
def f1(x):
    a=3
    b=5
    y=a*x+b
    return y
c = f1(10)
print(c)
print('='*50)
# %% 여기서부터 실행
print(1 + 1 == 2)
# %%
print(1+1 == 3)

# %%
if 1 + 1 == 2:
    print('yes')
else:
    print('no')


# %%
def quiz():
    ans = input('1+2 = ')
    return 1 + 2 == int(ans)
print(quiz())
# %%
def korean_number(num):
    if num == 1:
        return '일'
    elif num == 2:
        return '이'
    elif num == 3:
        return '삼'
    elif num == 4:
        return '사'
    elif num == 5:
        return '오'
    elif num == 6:
        return '육'
    elif num == 7:
        return '칠'
    elif num == 8:
        return '팔'
    elif num == 9:
        return '구'
    elif num == 10:
        return '십'
    else:
        return '불가능'
print(korean_number(1))
# %%
def triple(x):
    return x * 3
print(triple('x'))
# %%
def korean_age(birth_year):
    from datetime import datetime
    today = datetime.today()
    return today.year - birth_year + 1
print(korean_age(2002))

# %%
if __name__ == '__main__':
    print("triple(2):", triple(2))
    print("triple('x')", triple('x'))
    print("korean_age(2002):", korean_age(2002))
# %%
def simple_interest(p, r, t):
    return p*r*t

def simple_interest_amount(p, r, t):
    return p * (1+r*t)

if __name__=='__main__':
    print('Quiz 1')
    print('ex 1:', simple_interest(10000000, 0.03875, 5))
    print('ex 2:', simple_interest(1100000, 0.05, 5/12))

    print('\nQuiz 2')
    print('ex 1:', simple_interest_amount(10000000, 0.03875, 5))
    print('ex 2:', simple_interest_amount(1100000, 0.05, 5/12))

# %%
def read(text):
    ridename, restrictions = text.split(":")
    ridename = ridename.strip()
    restrictions = restrictions.strip()

    cmmin = cmmax = None

    if "~" in restrictions:
        parts = restrictions.split("~")
        cmmin = int(parts[0].strip().replace("cm", "").strip())
        cmmax = int(parts[1].strip().replace("cm", "").strip())
    elif "이상" in restrictions and "이하" in restrictions:
        pass
    else:
        if "이상" in restrictions:
            cmmin = int(restrictions.split("cm")[0].strip())
        elif "이하" in restrictions:
            cmmax = int(restrictions.split("cm")[0].strip())
    return ridename, cmmin, cmmax

if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input("정보:"))
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

# %%
def a():
    result = []
    for i in range(5):
        result.append(i**2)
    print(result)
a()

# %%
list(filter(lambda x : x%2 == 0, range(10)))
# %%
list(filter(lambda x : x%2 != 0, range(10)))
# %%
list(filter(lambda x : x%2 , range(10)))
# %%
