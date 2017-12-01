#число вводит пользователь;
#число может иметь различное число знаков;
#ввод с клавиатуры и вывод результата оформить в виде отдельной функции, вывод оформить с помощью метода format;
#вычисление суммы цифр оформить в виде отдельной функции;
#тесты оформить с помощью pytest в отдельном файле.
def inp():
  num = input("input the number: ")
  return num
  
def summer(num):
  summ = 0
  for i in num:
    summ += int(i)
  return summ

def out(summ):
  print ("sum of digits is {}".format(summ))

if __name__ == "__main__":
	out(summer(inp()))