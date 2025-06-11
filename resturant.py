import json
#import pprint
with open("menu.json",'r') as f:
    data=json.load(f)
#pprint.pprint(data)

items=data.get("items",[])

def getrating(reviews):
    rating=5
    if reviews:
        rating=sum(reviews)//len(reviews)
    return '⭐'*rating

while True:
    print('-'*40)
    print("UDUPI VEG RESTURANT")
    print('-'*40)
    print("1.Show Menu")
    print("2.Order Menu")
    print("3.update Menu")
    print("4.Add Review")
    print("5.Exit")
    print('-'*40)
    choice=int(input("enter the choice"))


    if choice==1:
        print('-'*50)
        print('ID\tNAME\t\t\tPrice\tRating')
        print('-'*50)
        for item in items:
            print(f'{item.get("id")}\t{item.get("name")}\t\t{item.get("price")}\t{getrating(item.get("reviews",[]))}')
        print('-'*50)
        print("show menu")

    elif choice==2:
        ordered_items={}
        order_items= list(map(int,input("Enter the item you wanna try:").split(',')))
        print('-'*40)
        print('ID\tNAME\t\t\tPrice\tQuantity\tAmount')
        print('-'*40)
        totalbill=0
        for order_item in order_items:
            for item in items:
                if item['id']==order_item:
                   if order_item in ordered_items:
                       ordered_items[order_item]['quantity']+=1
                   else:  
                       ordered_items[order_item]=item 
                       ordered_items[order_item]['quantity']=1
                   break 

        for item in ordered_items:
            name=ordered_items[item]['name']  
            price=ordered_items[item]['price'] 
            quantity=ordered_items[item]['quantity'] 
            amount=price*quantity
            totalbill+=amount

            print(f'{item}\t{name}\t{price}\t{quantity}\t{amount}')
        print('-'*40)
        print(f'\tTotal Amount:{totalbill}')
        print('-'*40)
        
    elif choice==3:
        name=input("enter the name of dish:")
        iprice=int(input("enter price:"))
        itype=input("veg or nonveg:")
        items.append({
            'id':len(items)+1,
            'name':name,
            'price':iprice,
            'veg':True if itype=='veg' else False,
            'reviews':[],

        })
        data['items']=items
        with open('menu.json','w') as f:
            json.dump(data, f)
        print("item is addedd")

    elif choice==4:
       item_id=int(input('enter item_id:'))
       rating=int(input("enter rating from 1 to 5:"))
       for i,item in enumerate(items):
           if item['id']==item_id:
               items[i]['reviews'].append(rating)
               break
       print("thankyou!!Your rating has been recorded")
           
    else:
        data['items']=items
        with open('menu.json','w') as f:
            json.dump(data, f)
        print("Thank you for visiting")
        break
            

