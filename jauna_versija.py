from doctest import testmod
def parbaudit_diapazonu(koord_x:float):
    '''Uzdevums pārbauda x koordināti
    
    >>> parbaudit_diapazonu(3.9)
    False
    >>> parbaudit_diapazonu(6)
    True
    >>> parbaudit_diapazonu(-2)
    False
    '''
    if koord_x > 3.9:
        return True
    else:
        return False
    
    testmode(verbose = True)