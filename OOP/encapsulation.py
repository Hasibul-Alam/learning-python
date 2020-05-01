class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print('Selling Price: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

''' change the price but do not change
because class treat __maxprice as a private variable'''
c.__maxprice = 1000
c.sell()

# using the setter function
c.setMaxPrice(1500)
c.sell()
