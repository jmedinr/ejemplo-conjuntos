import csv

file = open("sample-sales.csv",'rt')
reader = csv.reader(file)
vegetables = set()
cereal = set()
fruits = set()
for row in reader:
        customer = (row[0],row[1])
        category = row[2]
        if category == "Vegetables":
                vegetables.add(customer)
        if category == "Cereal":
                cereal.add(customer)
        if category == "Fruits":
                fruits.add(customer)
file.close()

print("%s customers have purchased vegetables" % len(vegetables))
print("%s customers have purchased cereal" % len(cereal))
print("%s customers have purchased vegetables but not cereal" % len(vegetables - cereal))
print("%s customers have purchased vegetables and cereal" % len(vegetables & cereal))
print("%s customers have purchases vegetables and fruits" % len(vegetables & fruits))
print("%s customers have purchased vegetables, cereal and fruits" % len(vegetables & cereal & fruits))
print("The following customers are our most valued. They have purchased vegetables & cereal & fruits:")
for customer in vegetables & cereal & fruits:
        print(customer)