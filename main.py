class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(self.name, "Мурчить)

    def eat(self):
        print(self.name, "Їсть.")

    def sleep(self):
        print(self.name, "Спить.")


cat = Cat("Мілка", 2)

print("Ім'я:", cat.name)
print("Вік:", cat.age)

cat.meow()
cat.eat()
cat.sleep()