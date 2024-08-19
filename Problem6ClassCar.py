# Alex Hurtado
# Date: 2024-08-11



class Car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        # Return a string with all attributes
        return (f"Model: {self.model}, Year: {self.year}, Color: {self.color}, "
                f"Type: {self.type}, Manufacturer: {self.manufacturer}")

# Create car instances with the additional attributes
car1 = Car("Sports", 2012, "Blue", "Coupe", "Ferrari")
car2 = Car("Sedan", 2020, "Black", "Sedan", "Toyota")

# Print various attributes and full specifications
print(car1.get_color())           # Output: Blue
print(car1.get_model())           # Output: Sports
print(car2.get_color())           # Output: Black
print(car1.fullspecs())           # Output: Model: Sports, Year: 2012, Color: Blue, Type: Coupe, Manufacturer: Ferrari
print(car2.fullspecs())           # Output: Model: Sedan, Year: 2020, Color: Black, Type: Sedan, Manufacturer: Toyota