class  India:
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken langauge of India.")
    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington D.C. is the capital of the USA.")
    def language(self):
        print("Englishe is the msot spoken language in the USA.")
    def type(self):
        print("USA is a developed country.")

obj_ind=India()
obj_usa=USA()

for country in(obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()