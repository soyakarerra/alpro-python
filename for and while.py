# for letter in 'python':
#     if letter == 'h':
#         break
#     print('current letter :',format(letter))

# for a in [0,1,-1,2,-2,3,-3]:
#     if a <=0:
#         continue 
#     print('Elemen positif :',format (a))

# var=10
# while (var >0):
#     var = var - 1
#     if var == 5:
#         continue
#     print('current value :',format(var))


# for n in range(2,10):
#     for a in (2,n):
#         if n % a==0 :
#         print(n,'equals',a,'*',n/a)
#         break
# else :
#     print(n,'bilangan prima')

n=5
while n>0 :
    n=n-1
    if n==2:
        break 
    print(n)
else:
    print('loop berhenti')
