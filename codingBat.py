def not_string(str):
  if str[0:3] == 'not':
    return str
  else :
    return 'not ' + str

print(not_string('Samira'))
print(not_string('not'))
print(not_string('not bad'))

def missing_char(str, n):
   return print(str[0:n] + str[n+1:])

  
print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))

missing_char('kitten', 1)


#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) == 1:
      return str
    else :
        first = str[0] 
        last = str[len(str)-1]
        return last + str[1:-1] + first
        
   

print(front_back('code'))
print(front_back('a')) 
print(front_back('ab')) 
print(front_back('bahar'))

def front3(str):
    if len(str) <= 3 : 
        return str*3
    else :
        return str[0:3]*3

print(front3('Java'))  #'JavJavJav'
print(front3('Chocolate'))  #'ChoChoCho'
print(front3('abc'))#→ 'abcabcabc'
print(front3('ab')) 
print(front3('abcd'))

def string_times(str, n):
  return str*n

print(string_times('Hi', 2)) #→ 'HiHi'
print(string_times('Hi', 3)) #→ 'HiHiHi'
print(string_times('Hi', 1)) #→ 'Hi'

def front_times(str, n):
  if len(str) <= 3:
    return str*n
  return str[0:3]*n

print(front_times('Chocolate', 2)) #→ 'ChoCho'


def string_splosion(str):
   for i in str:   
    return print(i)
   

print(string_splosion('Code')) #→ 'CCoCodCode'
print(string_splosion('abc')) #→ 'aababc'
print(string_splosion('ab')) #→ 'aab'





