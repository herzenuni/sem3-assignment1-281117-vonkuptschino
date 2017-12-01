#python3 -m pytest test_powsum.py -v 
from powsum import digitsSum
import pytest

def test_2dig():
	res = []
	for i in range(10, 100):
		if digitsSum(i) % 17 == 0:
			res.append(i)
	assert(res == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92])
