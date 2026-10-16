class Country:
    def __iter__(self):
        return (country for country in ["Ukraine", "Poland", "United Kingdom", "Italy"])

countries = Country()

for country in countries:
    print(country)