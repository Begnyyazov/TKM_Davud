#coздаём класс с именем Restaurant 
class Restaurant():
    #используем метод 'init' для активации 'названия' и 'типа' ресторана
    def __init__(self, name, country)
        self.name = name 
        self.country = country
    def describe_restaurant(self): #создаём метод
        print(f'{self.name} {self.type}') 


#Создаём экземпляр
my_restaurant = Restaurant('Hrustal, Italia')
print(f'Welcome to {my_restaurant.name} in {my_restaurant.country}')   
