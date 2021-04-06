from time import time
from random import randint
iter_count = 1000000
time_summ = 0
time_count = 0
for i in range(0, iter_count):
	time_start = time()
	u = randint(1, 32)
	if u == 1:
		answer = 'вы ввели не 0'
	elif u == 2:
		answer = 'вы ввели не 1'
	elif u == 3:
		answer = 'вы ввели не 2'
	elif u == 4:
		answer = 'вы ввели не 3'
	elif u == 5:
		answer = 'вы ввели не 4'
	elif u == 6:
		answer = 'вы ввели не 5'
	elif u == 7:
		answer = 'вы ввели не 6'
	elif u == 8:
		answer = 'вы ввели не 7'
	elif u == 9:
		answer = 'вы ввели не 8'
	elif u == 10:
		answer = 'вы ввели не 9'
	elif u == 11:
		answer = 'вы ввели не 10'
	elif u == 12:
		answer = 'вы ввели не 11'
	elif u == 13:
		answer = 'вы ввели не 12'
	elif u == 14:
		answer = 'вы ввели не 13'
	elif u == 15:
		answer = 'вы ввели не 14'
	elif u == 16:
		answer = 'вы ввели не 15'
	elif u == 17:
		answer = 'вы ввели не 16'
	elif u == 18:
		answer = 'вы ввели не 17'
	elif u == 19:
		answer = 'вы ввели не 18'
	elif u == 20:
		answer = 'вы ввели не 19'
	elif u == 21:
		answer = 'вы ввели не 20'
	elif u == 22:
		answer = 'вы ввели не 21'
	elif u == 23:
		answer = 'вы ввели не 22'
	elif u == 24:
		answer = 'вы ввели не 23'
	elif u == 25:
		answer = 'вы ввели не 24'
	elif u == 26:
		answer = 'вы ввели не 25'
	elif u == 27:
		answer = 'вы ввели не 26'
	elif u == 28:
		answer = 'вы ввели не 27'
	elif u == 29:
		answer = 'вы ввели не 28'
	elif u == 30:
		answer = 'вы ввели не 29'
	elif u == 31:
		answer = 'вы ввели не 30'
	time_stop = time()
	if time_stop - time_start != 0.0:
		time_summ += time_stop - time_start
		time_count += 1
print(time_summ / time_count)


time_summ = 0
time_count = 0
days = ['что-то тут' for i in range(0, 32)]
for i in range(0, iter_count):
	time_start = time()
	u = randint(0, 31)
	answer = days[u]
	time_stop = time()
	if time_stop - time_start != 0.0:
		time_summ += time_stop - time_start
		time_count += 1
print(time_summ / time_count)


time_summ = 0
time_count = 0
days = {
	1: 'что-то',
	2: 'что-то',
	3: 'что-то',
	4: 'что-то',
	5: 'что-то',
	6: 'что-то',
	7: 'что-то',
	8: 'что-то',
	9: 'что-то',
	10: 'что-то',
	11: 'что-то',
	12: 'что-то',
	13: 'что-то',
	14: 'что-то',
	15: 'что-то',
	16: 'что-то',
	17: 'что-то',
	18: 'что-то',
	19: 'что-то',
	20: 'что-то',
	21: 'что-то',
	22: 'что-то',
	23: 'что-то',
	24: 'что-то',
	25: 'что-то',
	26: 'что-то',
	27: 'что-то',
	28: 'что-то',
	29: 'что-то',
	30: 'что-то',
	31: 'что-то',
}
for i in range(0, iter_count):
	time_start = time()
	u = randint(1, 31)
	answer = days[u]
	time_stop = time()
	if time_stop - time_start != 0.0:
		time_summ += time_stop - time_start
		time_count += 1
print(time_summ / time_count)


time_summ = 0
time_count = 0


def get_day(u):
	return {
		u in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]: 'что-то',
		u in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]: 'что-то',
	}


for i in range(0, iter_count):
	time_start = time()
	u = randint(1, 31)
	answer = get_day(u)
	time_stop = time()
	if time_stop - time_start != 0.0:
		time_summ += time_stop - time_start
		time_count += 1
print(time_summ / time_count)
