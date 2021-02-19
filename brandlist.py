#------------------------heading---------------------------
tableheadlist=['SNO','brand','openbt','receviedbt','totalbt','closingbt','closingvl','salesbt','mrp','salesvl']
headlen=len(tableheadlist)
head_var = []


#-----------------------------------MLLISTS------------
mllist=["180ml","325ml","375ml","500ml","650ml","750ml","1000ml"]
#---------------------------------MRPLIST---------------------------
mrplist=["120","140","160","240","280","320","560"]
mrp180ml=["120","140","160"]
mrp375ml=["240","280","320"]
mrp650ml=["560"]

#------------------------- ML 180 : TOTAL ITEM:30-----------------------
ml180120=["","Red Sea(W)","Mistry Red(W)","Globu(W)","Express(Br)","Vorlon(Br)","Binniex(Br)","Beamens(Br)",
"Top Star(Br)","Mens Club(Br)","Honey Day(Br)","Black Pearl(Br)","Old Chef(Br)","Monitor(Br)","Molene(Br)",
"Golden Choice(Br)","Golden Eagle(Br)","Jet(Br)","Monitor(Wky)","Diamond(R)","Old Secret(R)","Old Monk(R)","Old Chef(R)",
"Vorion(R)","Jet(R)","Black Parel(R)"]
ml180120len=len(ml180120)

# ML 180 : TOTAL ITEM:27
ml180140=["","MC(Br)","Honey Bee(Br)","Copper(Br)","Day Night(Br)","UNJ No(Br)","Brihans Grape(Br)",
"All Gold VSOP(Br)","Evening Walker(Br)","Accord(Br)","Cardinal(Br)","Triple Crown VSOP(Br)","MGM No.1 VSOP(Br)",
"Roman Castle(Br)","Emperor(Br)","Brigadiers(Br)","Golden Vats(Br)","Black Magic(Br)","Tropicana VSOP(Br)",
"Role Model(R)","Copper(R)","Carribeen(R)","Accords Organge(V)","MGM Apple(V)","MGM Orange(V)","Power Orange(V)",
"Power Orange(V)","Activator Vannila(V)"]
ml180140len=len(ml180140)

# ML 180 : TOTAL ITEM:62
ml180160=["","MC VSOP Brandy","Sea Breeze Brandy","Accord French Brandy","Old Nepolen Brandy","Empees Nepolen Brandy","Stalin Rum",
"Classio Rum","MGM Richman Rum","Royal Nepolean Brandy","Cardinal VSOP Brandy","MGM Richman Brandy","King Nepolean Brandy",
"MALS Nepolean Brandy","Old monk Gold Rum","Arabian Night Rum","VSOP Exshaw Gold B","La Martine VSOP Brandy","Royal Accord Brandy",
"Royal Palace Brandy","Manison House Brandy","XO Brandy","Elcanso Brandy","MGM Gold VSOP Brandy","SPARTA VSOP Brandy","Carte Royal Brandy",
"SNJ VSOP Brandy","Courier Nepolean Brandy","Niyakra Lemon Rum","1848 Brandy","king Louis Brandy","Royal Accord Blue Brandy",
"Black & Gold Brandy","Chevalier Brandy","Aspira Lemon Rum","Aspiran berry Rum","Holandas Brandy","Marpheous Brandy","Signature Whisky",
"1848 Whisky","Royal Challenge Whisky","Spice Vodka","Blue Vodka","Ancient Cask Rum","Louies Varrnet B","British Empire Brandy",
"Bols Brandy","Missionary Monk Brandy","Kyron Brandy","Saint Louis Brandy","Bacardi Lemon","Florence Brandy","Clovies Brandy",
"Juno Vodka","MGM Gold Resereve B","Pink Vodka","Signout Brandy","Morpheous Blue Brandy","Lechaantee Brandy","Age De Oak Brandy",
"Anti Quity Whisky","Hobson Brandy","100 Piper Whiskey"]
ml180160len=len(ml180160)
ml180list=ml180120.copy()
ml180list.extend(ml180140)
ml180list.extend(ml180160)
ml180listlen=len(ml180list)

ml180opbtlist = []
for x in range(ml180listlen):
    ml180opbtlist.append(0)



# ML 375 : TOTAL ITEM:8
ml375240=["Express Brandy","Top Star Brandy","Vorion Brandy","Black Peral Brandy","Mens Clup Brandy","Diamond Rum",
"Vorion Rum"]

# ML 375 : TOTAL ITEM:12
ml375280=["MC Brandy","Hones Bee Brandy","Accord Brandy","Tirple Crown Brandy","SNJ No 1 Brandy","Brgadier Brandy",
"MGM N 1 Brandy","Golden Wats Brandy","Copper Brandy","Roman Castle Brandy","Black Magic Brandy","Emperor Brandy"]

# ML 375 : TOTAL ITEM:26
ml375320=["Mc VSOP Brandy","Accord French Brandy","Stalin Rum","King Nepolean Brandy","Old Monk Gold Rum","La Martin Brandy"
"VSOP exshaw Gold B","Royal Accord Brandy","Royal Palace Brandy","Eleanso Brandy","Mansion House Brandy","MGM Gold VSOP Brandy",
"Sparta Brandy","King Louis Brandy","1848 Brandy","Royal Accord Blue","Marpheous Brandy","Signature Whiskey","Royal Challenge Whisky",
"Ancient Cask Rum","Louis Varnnet Brandy","Missonery Monk Brandy","Bacardi Lemon Rum","Clovies","Juno Vodka","Signout Brnady"]

# ML 750 : TOTAL ITEM:40
ml750560=["Cardinal Brandy","MGM No.1 VSOP Brand","MGM Apple Vodka","MGM Orange Vodka","MC Vsop Brandy","Accord French Brandy",
"Stalin Rum","Old Monk Gold Rum","Xo Franch Brandy","Mansion House Brandy","La Martine Brandy","Royal Accord Brandy",
"MGM Gold Vsop","1848 Brandy","King Louies Brandy","Black & Gold Brandy","Royal Accord Blue Brandy","Eristoff vodka","Morpheous Brandy",
"Holandos Brandy","Signature Whiskey","Royal Challenge Whisky","Blue Vodka","Spice Vodka","Magic Movement Vodka","Ancient Cask Rum",
"Louis Vernnet Brandy","Missionery Monk Brandy","Koniefusion Brandy","Kyron Brandy","Bacardi Lemon Rum","Bacardi Apple Rum","Clovies Brandy",
"Juno Pink Vodka","MGM Gold Reserve Brandy","Sipping Resoulte Vodka","Agdoak Brandy","Classic Signout Brandy","Lecharnte Brandy",
"Hobson Brandy"]

# ML 650 : TOTAL ITEM:16
ml650beer=["Amstal","Kingfisher Magnum","British SS","Calsbereg","Tuboreg","Kingfisher Blue","Zingaro SS","SNJ 10000",
"Streen 8","Royal Accord","10000 Volts","KOLE","High Voltage","Black Pearl trible","British","Kingfisher Select"]

# ML500 : TOTAL ITEM:3
ml500=["British(Can)","Streen(Can)","SNJ 10000 (Can)"]

# ML 325 : TOTAL ITEM:4
ml325=["Kingfisher Strong","Kingfisher Blue","Streen","Kingfisher Select"]