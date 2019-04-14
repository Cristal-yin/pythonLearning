#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def my_def(a,b,c):
	coeffic = [a,b,c]
	leng = len(coeffic)

	for num in coeffic:
		if not isinstance(num,(int,float)):
			raise TypeError('bad operand type')


	print('''二元一次方程:
		-------------------''') 
	for i in (0,2):
		_i = leng - i
		if coeffic[i] != 0:
			if coeffic[i] > 0:
				if i != 0:
					print('+',end = '')
		if coeffic[i] != 1:
			print(str(coeffic[i]),end = '')
		if i != 1 and i != 2:
			print('x^%s' %(_i),end = '')
	print('''=0
		------------------''')

	der = pow(b,2)-4*a*c

	if der > 0:
		print('二元一次方程两个实数根')
		solution_1 = (-b-math.sqrt(der))/(2*a)
		solution_2 = (-b+math.sqrt(der))/(2*a)
		return (solution_1,solution_2)

	elif der == 0:
		print('二元一次方程有一个实数根:')
		solution = (-b-qurt(der))/(2*a)
		return solution

	elif der < 0:
		print('二元一次方程有两个复数根:')
		real = -b/(2*a)
		imaginary = math.sqrt(-der)/(2*a)
		if real == 0:
			solution_1 = str(imaginary) + 'i'
			solution_2 = '-'+str(imaginary)+'i'

		else:
			solution_1 = str(real)+'+'+str(imaginary)+'i'
			solution_2 = str(real)+'-'+str(imaginary)+'i'

	return(solution_1,solution_2)
