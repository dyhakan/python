import math

def ustel_hesaplama (sayi,ust):
    '''
    Bu fonksiyon üstel hesaplama yapar.
    Parametreler : int sayi , int ust
    Sonuc : verilen sayini verilen üstünü verir
    '''
    # sayinin üstünü hesapla
    # üstel sayi = sayi ** ust
    ustel = math.pow(sayi, ust)
    print(ustel)
    return ustel

ustel_hesaplama(2,8)
help(ustel_hesaplama)
