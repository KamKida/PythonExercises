VAT = 23
cenaNettoJava = 10
cenaNettoAjax = 20

cenaBruttoJava = cenaNettoJava * (1 + VAT / 100)
cenaBruttoAjax = cenaNettoAjax * (1 + VAT / 100)

print(cenaBruttoAjax)