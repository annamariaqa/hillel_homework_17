import random
import randominfo
import sys
from io import StringIO

old_stdout = sys.stdout
sys.stdout = StringIO()

countries = ["USA", "India", "Canada", "Australia", "UK", "Germany", "France", "Italy", "Japan", "Brazil"]
random_country = random.choice(countries)

person = randominfo.Person()

sys.stdout = old_stdout

print(person.full_name, person.gender, random_country, person.address)
