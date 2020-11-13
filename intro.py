print ("ciao\n")
# per farlo girare sulla shell scrivi : 
# python intro.py 

lst = [1,2,3]
print(sum(lst))

def sommatoria (lst):
    somma = 0 ; 
    for item in lst:
        somma += item
    return somma

print ("La somma è uguale a :", sommatoria(lst))