import random

class Matrix:
    '''
    Ввод функций, которые выполняет класс с Matrix[3x3]
    Опис класу повинен включати конструктори; 
    метод для виведення матриці на екран; 
    метод для визначення чи є матриця одиничною; 
    метод для визначення чи є матриця симетричною. 
    Перевантажити бінарний оператор віднімання матриць, 
    піднесення до ступеня матриці.
    '''
    def __init__(self,elements=[],random_value=False):
        '''
        Метод __init__ перегружает конструктор класса. 
        Конструктор - создание экземпляра класса.
        '''
        print('We are in constructor')
        if elements != []:
            self.elements = elements
        elif random_value:
            self.elements = [[random.randint(1,10) for i in range(3)]for j in range(3)]
        else:
            self.elements = [[0,0,0],[0,0,0],[0,0,0]]

    def print_matrix(self):
        '''
        Функция печатает введенную матрицу.
        '''
        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                print("%3d"%(self.elements[i][j]),end=" ")
            print()

    def __str__(self):
        '''
        Метод __str__(self) - вызывается функциями str, print и format. 
        Возвращает строковое представление объекта.
        '''
        result = ''
        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                result += str(self.elements[i][j])+ " "
            result += "\n"
        return result
            
    def __sub__(self, other_matrix):
        '''
        Метод __sub__(self, other) - вычитание (x - y).
        '''
        matrix3 = Matrix()
        for i in range(len(matrix3.elements)):
            for j in range(len(matrix3.elements[i])):
                matrix3.elements[i][j] = self.elements[i][j] - other_matrix.elements[i][j]
        return matrix3

    
    def isSymmetrical(self):
        '''
        Функция, проверяющая, является ли матрица симметричной.        
        '''
        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                if (self.elements[i][j] != self.elements[j][i]):
                    return False
        return True
    
    def isIdentity(self):
        '''
        Функция, проверяющая, является ли матрица единичной.
        '''
        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                if (i == j) and (self.elements[i][j] != 1):
                    return False
                elif (i != j) and (self.elements[i][j] != 0):
                    return False
        return True    
    
    
    '''
    def exponentiation(self):
        
        Функция, возводящая матрицу в степень.
        '''
    def __mul__(self,other):
      result = Matrix()
      if type(other) == Matrix :
        for k in range (len(self.elements)):
            for i in range (len(self.elements[k])):
                sum = 0
                for j in range(len(self.elements)):
                    sum = sum + self.elements[k][j] * other.elements[j][i]
                    result.elements[k][i] = sum
      elif type(other) == int :
          for i in range (len(self.elements)):
              for j in range(len(self.elements[i])):
                  result.elements[i][j] = self.elements[i][j] * other
      return result
        