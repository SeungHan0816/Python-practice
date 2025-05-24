삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)
#%%
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
# %%
s = "hello"
t = "python"
print(s+"!", t)
# %%
2+2*3
# %%
a = "132"
print(type(a))
# %%
num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int))
# %%
num = 100
num_str = str(num)
print(num_str, type(num_str))
# %%
str = "15.79"
str_float = float(str)
print(str_float, type(str_float))
# %%
year = "2020"
year = int(year)
print(int(year)-3)
print(int(year)-2)
print(int(year)-1)
# %%
월 = 48584
총금액 = 월 * 36
print(총금액)
# %%
letters = 'python'
print(letters[0], letters[2])
# %%
license_plate = "24가 2210"
print(license_plate[3:].strip())
# %%
string = "홀짝홀짝홀짝"
print(string[::2])
# %%
string ="PYTHON"
print(string[::-1])
# %%
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))
# %%
phone_number = "010-1111-2222"
print(phone_number.replace("-", ""))
# %%
ur1 = "http://sharebook.kr"
print(ur1.split('.')[1].strip())
# %%
string = 'abcdefe2a354a32a'
print(string.replace('a', 'A'))
# %%
a = '3'
b = '4'
print(a+b)
# %%
t1 = 'python'
t2 = 'java'
print((t1+' '+ t2+' ')*4)
# %%
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print('이름:',name1, '나이:', age1)
print('이름:', name2, '나이:', age2)
# %%
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print(f'이름: {name1}, 나이: {age1}')
print(f'이름: {name2}, 나이: {age2}')
# %%
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print('이름: {}, 나이: {}'.format(name1, age1))
print('이름: {}, 나이: {}'.format(name2,age2))
# %%
삼성주식수 = "5,969,782,550"
삼성주식수 = int(삼성주식수.replace(',',''))
print(삼성주식수, type(삼성주식수))
# %%
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
# %%
data = "   삼성전자    "
print(data.split()[0])
# %%
data = "   삼성전자    "
data = data.strip()
print(data)
# %%
ticker = "btc_krw"
print(ticker.upper())
# %%
ticker = "BTC_KRW"
print(ticker.lower())
# %%
a = "hello"
print(a.capitalize())
# %%
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
# %%
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))
# %%
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
# %%
a = "hello world"
print(a.split(" "))
# %%
ticker = "btc_krw"
print(ticker.split("_"))
# %%
date = "2020-05-01"
print(date.split("-"))
# %%
data = "039490     "
print(data.rstrip())
# %%
data = "039490     "
print(data.strip())
# %%
