#Function: def fun():
#     print("hello world")
#fun()



#return is store karta hai and repeat karta hai function ke task ko


def fun(price, quant):
        total_sale=price*quant
        return total_sale


kaju_cost=10
kaju_quant=23

badam_cost=40
badam_quant=90

print(fun(kaju_cost,kaju_quant)+fun(badam_cost,badam_quant))


