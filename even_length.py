# Python3 program to print  
#  even length words in a string  
  
def printWords(s): 
      
    # split the string  
    s = s.split(' ')  
      
    # iterate in words of string  
    for word in s:  
          
        # if length is even  
        if len(word)%2==0: 
            print(word)  
  
  
# Driver Code  
s = "This is a python language code" 
printWords(s)