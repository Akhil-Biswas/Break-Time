items=[]
class Items:
    def __init__(self,itemId,itemName,itemPrice,itemType, imgurl):
        self.itemId = itemId
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemType = itemType
        self.img = imgurl
        #defult velue for get item
        self.isfev = False
        self.quantity = 0
        self.totalFev = 0
        
    def saveItemInDatabase(self):
         items.append({"itemId":self.itemId ,
         "itemName":self.itemName,
         "itemPrice":self.itemPrice,
         "itemType":self.itemType,"img":self.img
         })
         
        # print(items)
        
    @staticmethod
    def getAllItem():
        #get data from server
        #exemple by list
        return items
        
item1 = Items(
itemId = 1,
        itemName = "samosa",
        itemPrice = 10,
        itemType = "veg",
        imgurl ='1'+".jpg"
).saveItemInDatabase()

item2 = Items(
itemId = 2,
        itemName = "Roti",
        itemPrice = 10,
        itemType = "veg",
        imgurl ='2'+".jpg"
).saveItemInDatabase()
#for display in html
getitemlist=Items.getAllItem()

for item in getitemlist:
        itemId = item["itemId"]
        print(itemId)
        itemName = item["itemName"]
        itemPrice = item["itemPrice"]
        itemType = item["itemType"]
        print(itemName)
        print(itemPrice)
        print(itemType)
        print('=======')
  