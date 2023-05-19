import json
test = open("test.json",encoding = "utf8")
armor = json.load(test)

inventory_size = 50
class Item:
    def __init__ (self,id,name,rarity,slots):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.slots = slots
    def __str__ (self):
        return (self.id,self.name,self.rarity,self.slots)

inventory_list = []

def add_item (id,name,rarity,slots):
    new_item = Item(id,name,rarity,slots)
    inventory_list.append(new_item)
    for i in inventory_list:
        print(name,rarity,slots)
    
id = armor[0]["id"]
name = armor[0]["name"]
rarity = armor[0]["rarity"]
slots = armor[0]["slots"]

add_item(id,name,rarity,slots)