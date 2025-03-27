hesap1 = {
    'ad': "ayse",
    "bakiye": 5000,
    "ek": 2000
}
hesap2 = {
    'ad': "can",
    "bakiye": 3000,
    "ek": 1000
}

def paracek(hesap, miktar):
    print(hesap["ad"])
    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        sorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ek"]
    if (toplam >= miktar):
        kalan = miktar - hesap["bakiye"]
        hesap["bakiye"] = 0
        hesap["ek"] -= kalan
        sorgula(hesap)
    else:
        print("bakiye yetersiz")

def sorgula(hesap):
    print(
        f"{hesap["ad"]}, adlı hesabınızda kalan bakiyeniz:{hesap["bakiye"]}, ek hesapta kalan bakiye:{hesap["ek"]} dir")

paracek(hesap1, 3500)
