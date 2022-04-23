def fibo(n) -> int:
    
    """
    This function defines a list of fibonacci numbers starting with 0 and 1
    and creates a while loop with the condition that if the last number of the fibo list is greater than n, the loop
    stops and prints the second from last number [-2]. n can be any integer of float.
    """
    
    # Assign the first two fibonacci numbers
    v1 = 0
    v2 = 1
    fibo_list = [v1, v2]
    end = False
    
    while end == False:
        if fibo_list[-1] < n:  
            last_term = v1 + v2  
            v1 = v2
            v2 = last_term
    # Creates a fibonacci list such that the next number on the list is always Vn + the last term.
            fibo_list = fibo_list + [last_term]
            
        else:
            end = True
    #If Vn> n the while loop stops and prints the second from last fibonacci number on the list.       
    print(fibo_list[-2])

fibo(56)


