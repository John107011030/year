#寫一個function來證明其是否為閏年(二月會多一天)
#閏年定義：
#公元年分不被4整除，為平年
#公元年分可被4整除，卻不被100整除，為閏年
#公元年分可被100整除，卻不被400整除，為平年
#公元年分可被400整除，卻不被3200整除，為閏年
def is_leap_year(year):
	if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0): #「%」為除號
		return True
	else:
		return False
a = int(input('請輸入年：'))
print(is_leap_year(a))
