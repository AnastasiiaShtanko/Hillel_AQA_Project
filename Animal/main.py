# Імпорт класів

from catfamily import CatFamily
from dogfamily import DogFamily
from cat import Cat
from lion import Lion

# Створення об'єктів

cat_family_member = CatFamily("Cat Ted")
dog_family_member = DogFamily("Buddy")
cat = Cat("Cat")
lion = Lion("Simba")

# Виклик методів


print(cat_family_member)
print(cat_family_member.climb_trees())
print(cat_family_member.make_sound())

print(dog_family_member)
print(dog_family_member.fetch_ball())
print(dog_family_member.make_sound())

print(cat.hunt_mice())
print(cat.make_sound())

print(lion)
print(lion.roar())


