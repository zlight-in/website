def search(items):
    data = []
    ite = {}
    ite2 = {}
    pricelist = {}
    length = len(items)
    for k in items:
        try:
            pricelist[int(k["productIdentifier"])].append(k["productPrice"])
            ite[int(k["productIdentifier"])].append([{"businessIdentifier":k["businessIdentifier"],'businessName':k['businessName'],'businessIdentifier':k['businessIdentifier'],"quantityType":k["quantityType"],"discountedPrice":k["discountedPrice"],"rating":k["rating"],"productPrice":k["productPrice"]}])
        except:
            ite[int(k["productIdentifier"])] = []
            pricelist[int(k["productIdentifier"])] = []
            pricelist[int(k["productIdentifier"])].append(k["productPrice"])
            ite[int(k["productIdentifier"])].append([{"businessIdentifier":k["businessIdentifier"],'businessName':k['businessName'],'businessIdentifier':k['businessIdentifier'],"quantityType":k["quantityType"],"discountedPrice":k["discountedPrice"],"rating":k["rating"],"productPrice":k["productPrice"]}])
    print(length)
    for i in range(length):
        j = items[i]
        buslength = len(ite[j["productIdentifier"]])
        print((buslength))
        if buslength%2 == 0:
            print("here")
            medianprice = (float(pricelist[int(j["productIdentifier"])][int(buslength/2)+1]) + float(pricelist[int(j["productIdentifier"])][int(buslength/2)]))/2
        else:
            medianprice = pricelist[int(j["productIdentifier"])][int(buslength/2)]
        ite2.update({int(j["productIdentifier"]):{"productName":j['productName'],"productIdentifier":j["productIdentifier"],"avgprice":medianprice,'sellers':ite[j["productIdentifier"]]}})
        #productlist.append(j["productIdentifier"])
    data = []
    for i in ite2:
        data.append(ite2[i])
    return data