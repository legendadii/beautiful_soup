import requests
from  bs4 import BeautifulSoup


# print(htmlContent)


product_name=[]
description=[]
rating=[]
price=[]
categorie=[]
discounded_price=[]

# *************************************for mobile***********************************************

# ********************************Fridge*************************************************************

url="https://www.flipkart.com/search?q=fridge%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r=requests.get(url)
htmlContent=r.content


for j in range(10):
    soup1=BeautifulSoup(htmlContent,'html.parser')
    # soup1=soup1.find(class_="_1YokD2 _3Mn1Gg")
    # *****product_name*********
    pn=soup1.find_all("div",class_="_4rR01T")
    for i in pn:
        # print(i.string)
        product_name.append(i.string)
        categorie.append('Tv')

    # ************discounded_price**********

    dp=soup1.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in dp:
        i987=i.string
        # i987=i987[1:]
        # print(i987)
        discounded_price.append(i987)

    # ************price**********
    # print("************************************price******************************")
    # print(j)

    p=soup1.find_all("div",class_="_3I9_wc _27UcVY")
    for i in p:
        pd=list(i.strings)
        # print(pd[1])
        price.append(pd[1])
# ******************description*************
    d=soup1.find_all("ul",class_="_1xgFaf")
    for i in d:
        pd=list(i.strings)
        # print(pd)
        # print()
        description.append(pd[1])
# *******************rating****************
    
    # r1=soup1.find_all("div",class_="_1YokD2 _3Mn1Gg")

    r=soup1.find_all("div",class_="_3LWZlK")
    for i in r:
        pd=list(i.strings)
        # print(pd[0])
        # print()
        rating.append(pd[0])

    

    # length1=len(categorie)
    # rating=rating[:length1]
   

    

    next_page="https://www.flipkart.com"+soup1.find_all('a',class_="_1LKTO3")[-1].get('href')

    # print(next_page)
    # print()
    # print(j)
    # print()
    r=requests.get(next_page)
    htmlContent=r.content




length1=len(categorie)
length2=len(description)
length3=len(product_name)
length4=len(price)
length5=len(discounded_price)
length6=len(rating)

print(length1)
print(length2)
print(length3)
print(length4)
print(length5)
print(length6)








# ********************************Tv*************************************************************

url="https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r=requests.get(url)
htmlContent=r.content


for j in range(10):
    soup1=BeautifulSoup(htmlContent,'html.parser')
    # soup1=soup1.find(class_="_1YokD2 _3Mn1Gg")
    # *****product_name*********
    pn=soup1.find_all("div",class_="_4rR01T")
    for i in pn:
        # print(i.string)
        product_name.append(i.string)
        categorie.append('Tv')

    # ************discounded_price**********

    dp=soup1.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in dp:
        i987=i.string
        # i987=i987[1:]
        # print(i987)
        discounded_price.append(i987)

    # ************price**********
    # print("************************************price******************************")
    # print(j)

    p=soup1.find_all("div",class_="_3I9_wc _27UcVY")
    for i in p:
        pd=list(i.strings)
        # print(pd[1])
        price.append(pd[1])
# ******************description*************
    d=soup1.find_all("ul",class_="_1xgFaf")
    for i in d:
        pd=list(i.strings)
        # print(pd)
        # print()
        description.append(pd[1])
# *******************rating****************
    
    # r1=soup1.find_all("div",class_="_1YokD2 _3Mn1Gg")

    r=soup1.find_all("div",class_="_3LWZlK")
    for i in r:
        pd=list(i.strings)
        # print(pd[0])
        # print()
        rating.append(pd[0])

    

    # length1=len(categorie)
    # rating=rating[:length1]
   

    

    next_page="https://www.flipkart.com"+soup1.find_all('a',class_="_1LKTO3")[-1].get('href')

    # print(next_page)
    # print()
    # print(j)
    # print()
    r=requests.get(next_page)
    htmlContent=r.content




length1=len(categorie)
length2=len(description)
length3=len(product_name)
length4=len(price)
length5=len(discounded_price)
length6=len(rating)

print(length1)
print(length2)
print(length3)
print(length4)
print(length5)
print(length6)


# ***********************************mobile****************************************

url="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r=requests.get(url)
htmlContent=r.content



for j in range(10):
    soup1=BeautifulSoup(htmlContent,'html.parser')
    # *****product_name*********
    pn=soup1.find_all(class_="_4rR01T")
    for i in pn:
        # print(i.string)
        product_name.append(i.string)
        categorie.append('mobile')

    # ************discounded_price**********

    dp=soup1.find_all(class_="_30jeq3 _1_WHN1")
    for i in dp:
        i987=i.string
        i987=i987[1:]
        # print(i987)
        discounded_price.append(i987)

    # ************price**********

    p=soup1.find_all(class_="_3I9_wc _27UcVY")
    for i in p:
        pd=list(i.strings)
        # print(pd[1])
        price.append(pd[1])
# ******************description*************
    d=soup1.find_all("ul",class_="_1xgFaf")
    for i in d:
        pd=list(i.strings)
        # print(pd)
        # print()
        description.append(pd[1])
# *******************rating****************
    
    # r1=soup1.find_all("div",class_="_1YokD2 _3Mn1Gg")

    r=soup1.find_all("div",class_="_3LWZlK")
    for i in r:
        pd=list(i.strings)
        # print(pd[0])
        # print()
        rating.append(pd[0])

    

    # length1=len(price)
    # rating=rating[:length1]
   

    

    next_page="https://www.flipkart.com"+soup1.find_all('a',class_="_1LKTO3")[-1].get('href')

    # print(next_page)
    # print()
    # print(j)
    # print()
    r=requests.get(next_page)
    htmlContent=r.content

length1=len(categorie)
length2=len(description)
length3=len(product_name)
length4=len(price)
length5=len(discounded_price)
length6=len(rating)

print(length1)
print(length2)
print(length3)
print(length4)
print(length5)
print(length6)





# ***********************************mobile****************************************

url="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r=requests.get(url)
htmlContent=r.content



for j in range(10):
    soup1=BeautifulSoup(htmlContent,'html.parser')
    # *****product_name*********
    pn=soup1.find_all(class_="_4rR01T")
    for i in pn:
        # print(i.string)
        product_name.append(i.string)
        categorie.append('mobile')

    # ************discounded_price**********

    dp=soup1.find_all(class_="_30jeq3 _1_WHN1")
    for i in dp:
        i987=i.string
        i987=i987[1:]
        # print(i987)
        discounded_price.append(i987)

    # ************price**********

    p=soup1.find_all(class_="_3I9_wc _27UcVY")
    for i in p:
        pd=list(i.strings)
        # print(pd[1])
        price.append(pd[1])
# ******************description*************
    d=soup1.find_all("ul",class_="_1xgFaf")
    for i in d:
        pd=list(i.strings)
        # print(pd)
        # print()
        description.append(pd[1])
# *******************rating****************
    
    # r1=soup1.find_all("div",class_="_1YokD2 _3Mn1Gg")

    r=soup1.find_all("div",class_="_3LWZlK")
    for i in r:
        pd=list(i.strings)
        # print(pd[0])
        # print()
        rating.append(pd[0])

    

    # length1=len(price)
    # rating=rating[:length1]
   

    

    next_page="https://www.flipkart.com"+soup1.find_all('a',class_="_1LKTO3")[-1].get('href')

    # print(next_page)
    # print()
    # print(j)
    # print()
    r=requests.get(next_page)
    htmlContent=r.content

length1=len(categorie)
length2=len(description)
length3=len(product_name)
length4=len(price)
length5=len(discounded_price)
length6=len(rating)

print(length1)
print(length2)
print(length3)
print(length4)
print(length5)
print(length6)








import pandas as pd
df=pd.DataFrame({"Categories":categorie[:236],"Description":description[:236],"Product_name":product_name[:236],"Price":price[:236],"Discounded_price":discounded_price[:236],"rating":rating[:236]})
df.to_csv("C:/Users/DELL/Desktop/flipkart8.csv")



   
   