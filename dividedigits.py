#n = int(input())
#i = 2
#digit = (n % 10**i)//10**(i-1)
#i=1
#digit1 = (n % 10**i)//10**(i-1)
#print(digit,digit1)


#List comprehension
even_squares = [x**2 for x in range(4,13) if x%2 ==0]
print(even_squares) # 5 ten 12 ye kadar olan 2 ye tam bolunebilen her bir sayinin karesi

texts = ['python', 'javascript', 'html', 'css']
capitalized = [x.title() for x in texts]
lengths = [len(text) for text in texts]
print(capitalized)
print(lengths)

z = [x for x in range (0, 101) if x % 3 == 0]
print(z)

multiples = [ x * 7 for x in range (1,11)]
print(multiples)

#Nested List
dividible3 = [[3,6,9,12],[18,24,27],[30,33,36]]
all_results = [subject
                for myList in dividible3
                for subject in myList]
print(all_results)

#Matrix
matrix=[]
for i in range(3):
    matrix.append([])
    for _ in range(3):
        matrix[i].append(1)
print("Matrix  = " ,matrix) #==>Short way matrix
matrix1 = [[1 for _ in range(3)] for _ in range(3)]
print("Matrix1 = " ,matrix1)

print(61%60)
print(61//60)

