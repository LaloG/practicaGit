def fibonacciService(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Por favor ingrese un número entero positivo")
    
    # if there is only one term, return n1
    elif nterms == 1:
        print("Secuencia de Fibonacci hasta",nterms,":")
        print(n1)
    
    # generate fibonacci sequence
    else:
        print("Fibonacci secuencia:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
    