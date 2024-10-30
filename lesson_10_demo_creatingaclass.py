class Tea:
    '''varieties of tea for my tea shop'''

    def __init__(self, name , type, allergen = 'none',instock = 'y' ):
        self.name = name
        self.type = type
        self.allergen = allergen
        self.instock = instock

    def brew(self):
        print(f"How about a nice cup of {self.name}?")
        print(f'Please collect your tea from the counter.')

    def restock(self):
        print(f'Tea emergency! We are out of {self.name}, which is not good!')

gr_jas = Tea('jasmine green tea','green')
oo_peo = Tea('white peony oolong tea', 'oolong')
bl_alm = Tea('almond darjeeling','black','tree nut')

#print(f"Can I have a cup of {gr_jas.name}?")
#oo_peo.brew()

print(f'Known allergens: \n{gr_jas.name} : {gr_jas.allergen} \n{oo_peo.name} : {gr_jas.allergen}')

gr_jas.restock()