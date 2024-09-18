def factorial(number):
    '''This is UDF'''
    if number>=0:
        res = 1

        for i in range(1,number+1):
            res*= i
        return res
    else:
        print('Not allowed!!')
        
        
# anagram:- two words with same count of characters

# Cheater = teacher
def check_anagram(w1,w2):
    '''To check anagram'''
        
    w1,w2 = w1.lower(),w2.lower()
    
    w1_counts = {}
    w2_counts = {}
    
    
    for i in w1:
        w1_counts[i] = w1.count(i)
        
    for j in w2:
        w2_counts[j] = w2.count(j)
    
    
        
    return 'Anagram' if w1_counts == w2_counts else 'Not an Anagram'


def check_armstrong(number):
    lt = len(str(number))
    
    ans = 0
    
    for i in str(number):
        ans += int(i)**lt
        
    return 'Armstrong Number' if ans == number else 'Not an Armstrong Number'

def give_prime_number(n1,n2):
    all_prime = []
    
    for i in range(n1,n2+1):
        
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            all_prime.append(i)
            
    return all_prime

def maxx(data):
    my_max = data[0]
    
    for i in data:
        if i>my_max:
            my_max = i
    
    return my_max

def intro(**kwargs):
    for i,j in kwargs.items():
        print(f"Your {i} is {j}")