a = input('Enter a string of characters: ')

if len(a)<16:
    print ('Number of characters: ',len(a))
    print ('Calculation of results: ',len(a)*2)
elif len(a)<30:
    print ('Number of characters:  ',len(a))
    print ('Calculation of results: ',len(a)**2)
else:
    print ('Number of characters:  ',len(a))
    print ('Calculation of results: ',len(a)/2)
input()
