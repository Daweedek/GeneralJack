# -*- coding: utf-8 -*- 
# ITEMS STATS

#UN-EQUIPABLE ITEMS
# hunger decrease / hp increase / thirst decrease / weight PŘIDAT!!!! / value of the item / description     Hardcore = pokud je jídlo 100% ok
items = [
    'steak', 'apple', 'roll', 'cake', 'bread', 'MRE', 'burger', 'taco', 'kebab', 'cheesecake',
     'pear', 'banana', 'broccoli', 'chips', 'cookies','water', 'sugar-water', 'energy-drink', 'dirty-water',
     'melted-snow', 'sprinkling-water', 'beer', 'vodka', 'sprint', 'koko-kola', 'apple-juice', 'lemon-juice',
     'tea', 'coffee', 'milk', 'key', 'wrench', 'tissues', 'revolver', 'pistol', 'sniper-rifle', 'knife', 'machette', 
     'bottle', 'broken-bottle', 'hunting-knife', 'syringe', 'cap', 'winter-hat', 'hat', 't-shirt', 'sweatshirt', 'coat', 
     'sweater', 'jacket', 'bomber-jacket', 'leggins', 'shorts', 'jeans', 'pants', 'tactical-pants', 'helmet', 'light-armored-helmet', 
     'heavy-armored-helmet', 'light-tactical-helmet', 'heavy-tactical-helmet', 'lab-coat', 'apron', 'winter-coat', 'vest', 
     'light-armored-vest', 'heavy-armored-vest', 'light-tactical-vest', 'heavy-tactical-vest', 'protectors', 'light-armored-protectors', 
     'heavy-armored-protectors', 'light-tactical-protectors', 'heavy-tactical-protectors', 'latex-gloves', 'winter-gloves', 'tactical-gloves', 'gloves', 
     'light-armored-gloves', 'heavy-armored-gloves', 'light-tactical-gloves', 'heavy-tactical-gloves', 'sneakers', 'high-sneakers', 'oxford-shoes', 'trainers', 
     'crocs', 'slippers', 'boots', 'light-armored-boots', 'heavy-armored-boots', 'light-tactical-boots', 'heavy-tactical-boots', 'salt'
]

newitems={
    #name / equipable / type / wheretoequip / weight / price / attack / defense / hunger-- / thirst-- / hp++ / value of the item /description

    # 0-8 clothes, 9-17 armor, 18-26 gloves and shoes, 27-35 food, 36-44 beverage, 45-53 meds, 54-62 questItems, 63-71 weapons, 72-80 tools
    'id0' : ['cap',True,'clothes','Head','','','','','','','','','',],
    'id1' : ['straw-hat',True,'clothes','Head','','','','','','','','','',],
    'id2' : ['scarf','',True,'clothes','Head','','','','','','','','',],
    'id3' : ['t-shirt',True,'clothes','Body','','','','','','','','','',],
    'id4' : ['sweatshirt',True,'clothes','Body','','','','','','','','','',],
    'id5' : ['tank',True,'clothes','Body','','','','','','','','','',],
    'id6' : ['jeans',True,'clothes','Legs','','','','','','','','','',],
    'id7' : ['shorts',True,'clothes','Legs','','','','','','','','','',],
    'id8' : ['sweatpants',True,'clothes','Legs','','','','','','','','','',],
    'id9' : ['tactical-helmet',True,'armor','Head','','','','','','','','','',],
    'id10' : ['army-helmet',True,'armor','Head','','','','','','','','','',],
    'id11' : ['night-vision',True,'armor','Head','','','','','','','','','',],
    'id12' : ['tactical-vest',True,'armor','Body','','','','','','','','','',],
    'id13' : ['bulletproof-vest',True,'armor','Body','','','','','','','','','',],
    'id14' : ['protectors',True,'armor','Body','','','','','','','','','',],
    'id15' : ['tactical-pants',True,'armor','Legs','','','','','','','','','',],
    'id16' : ['armored-pants',True,'armor','Legs','','','','','','','','','',],
    'id17' : ['stealth-pants',True,'armor','Legs','','','','','','','','','',],
    'id18' : ['rubber-gloves',True,'gloves','Gloves','','','','','','','','','',],
    'id19' : ['armored-gloves',True,'gloves','Gloves','','','','','','','','','',],
    'id20' : ['tactical-gloves',True,'gloves','Gloves','','','','','','','','','',],
    'id21' : ['work-gloves',True,'gloves','Gloves','','','','','','','','','',],
    'id22' : ['army-boots',True,'shoes','Shoes','','','','','','','','','',],
    'id23' : ['slippers',True,'shoes','Shoes','','','','','','','','','',],
    'id24' : ['flip-flops',True,'shoes','Shoes','','','','','','','','','',],
    'id25' : ['sneakers',True,'shoes','Shoes','','','','','','','','','',],
    'id26' : ['boots',True,'shoes','Shoes','','','','','','','','','',],
    'id27' : ['apple',False,'food','---','','','','','','','','','',],
    'id28' : ['bread',False,'food','---','','','','','','','','','',],
    'id29' : ['steak',False,'food','---','','','','','','','','','',],
    'id30' : ['hamburger',False,'food','---','','','','','','','','','',],
    'id31' : ['potato',False,'food','---','','','','','','','','','',],
    'id32' : ['orange',False,'food','---','','','','','','','','','',],
    'id33' : ['banana',False,'food','---','','','','','','','','','',],
    'id34' : ['cereal-bar',False,'food','---','','','','','','','','','',],
    'id35' : ['mre',False,'food','---','','','','','','','','','',],
    'id36' : ['water',False,'beverage','---','','','','','','','','','',],
    'id37' : ['juice',False,'beverage','---','','','','','','','','','',],
    'id38' : ['wine',False,'beverage','---','','','','','','','','','',],
    'id39' : ['cola',False,'beverage','---','','','','','','','','','',],
    'id40' : ['vodka',False,'beverage','---','','','','','','','','','',],
    'id41' : ['beer',False,'beverage','---','','','','','','','','','',],
    'id42' : ['milk',False,'beverage','---','','','','','','','','','',],
    'id43' : ['coffee',False,'beverage','---','','','','','','','','','',],
    'id44' : ['energy-drink',False,'beverage','---','','','','','','','','','',],
    'id45' : ['painkillers',False,'meds','---','','','','','','','','','',],
    'id46' : ['steroids',False,'meds','---','','','','','','','','','',],
    'id47' : ['water-pills',False,'meds','---','','','','','','','','','',],
    'id48' : ['antihunger',False,'meds','---','','','','','','','','','',],
    'id49' : ['poison',False,'meds','---','','','','','','','','','',],
    'id50' : ['antipoison',False,'meds','---','','','','','','','','','',],
    'id51' : ['patch',False,'meds','---','','','','','','','','','',],
    'id52' : ['syringe',False,'meds','---','','','','','','','','','',],
    'id53' : ['bandage',False,'meds','---','','','','','','','','','',],
    'id54' : ['','','','','','','','','','','','','',],
    'id55' : ['','','','','','','','','','','','','',],
    'id56' : ['','','','','','','','','','','','','',],
    'id57' : ['','','','','','','','','','','','','',],
    'id58' : ['','','','','','','','','','','','','',],
    'id59' : ['','','','','','','','','','','','','',],
    'id60' : ['','','','','','','','','','','','','',],
    'id61' : ['','','','','','','','','','','','','',],
    'id62' : ['','','','','','','','','','','','','',],
    'id63' : ['','','','','','','','','','','','','',],
    'id64' : ['','','','','','','','','','','','','',],
    'id65' : ['','','','','','','','','','','','','',],
    'id66' : ['','','','','','','','','','','','','',],
    'id67' : ['','','','','','','','','','','','','',],
    'id68' : ['','','','','','','','','','','','','',],
    'id69' : ['','','','','','','','','','','','','',],
    'id70' : ['','','','','','','','','','','','','',],
    'id71' : ['','','','','','','','','','','','','',],
    'id72' : ['','','','','','','','','','','','','',],
    'id73' : ['','','','','','','','','','','','','',],
    'id74' : ['','','','','','','','','','','','','',],
    'id75' : ['','','','','','','','','','','','','',],
    'id76' : ['','','','','','','','','','','','','',],
    'id77' : ['','','','','','','','','','','','','',],
    'id78' : ['','','','','','','','','','','','','',],
    'id79' : ['','','','','','','','','','','','','',],
    'id80' : ['','','','','','','','','','','','','',]
}




foodProps = {
    "steak" : [30, 10, 2, "common item", "Medium rare steak."],
    "apple" : [6, 3, 3, "common item", "An apple a day keeps doctor away!"],
    "roll" : [2, 5, (-1), "common item", "Just a roll."],
    "cake" : [12, 10, 1, "common item", "Mmmmm..."],
    "bread" : [20, 9, (-1), "common item", "Loaf of a bread."],
    "MRE" : [60, 30, 30, "common item", "Meal Ready to Eat."],
    "burger" : [60, 30, 30, "common item", "Double-decker cheeseburger."], #edit all down
    "taco" : [60, 30, 30, "common item", "Just taco."],
    "kebab" : [60, 30, 30, "common item", "Mouthwatering."],
    "cheesecake" : [60, 30, 30, "common item", "cheese. cake. cheesecake."],
    "salt" : [-2, 0, -8, "common item", "just a salt."]
    }

# thirst decrease / hp increase / hunger decrease / value of the item / description     Hardcore = pokud je jídlo 100% ok.. #postava se pozvrací pokud je -5 přidat [číslo]
beverageProps = {
    "water" : [30, 3, 4, "common item", ""],
    "sugar-water" : [2, 12, 1 , "common item", ""],
    "energy-drink" : [2, 15, 0, "common item", ""],
    "dirty-water" : [5, (-1), (-5), "common item", ""],
    "melted-snow" : [9, 1, 1, "common item", ""],
    "sprinkling-water" : [5, (-1), (-5), "common item", ""], #edit all down
    "beer" : [5, (-1), (-5), "common item", ""],
    "vodka" : [5, (-1), (-5), "special item", "Русский стандарт!"], # special item strenght all abilities + 10 (na quest/den nějakou určitou dobu, další den bude kocovina)
    "sprint" : [5, (-1), (-5), "common item", ""],
    "koko-kola" : [5, (-1), (-5), "common item", ""],
    "apple-juice" : [5, (-1), (-5), "common item", ""],
    "lemon-juice" : [5, (-1), (-5), "common item", ""],
    "tea" : [5, (-1), (-5), "common item", ""],
    "coffee" : [5, (-1), (-5), "common item", ""],
    "milk" : [5, (-1), (-5), "common item", ""],
    }

toolsProps = {
    "key" : "",
    "wrench" : "",
    "tissues" : "",
}

#EQUIPABLE ITEMS
# weight / price / attack / defense / hp / value of the item /description
weaponsProps = {
    "revolver" : [2, 3000, 15, 0, 100, "common item", "Western-like revolver. 6 bullets, 6 targets."],
    "pistol" : [2, 3000, 12, 0, 100, "common item", "Bang! Bang! Bang!"],
    "sniper-rifle" : [2, 3000, 15, 0, 100, "common item", "Huge head ripper. One shot - one kill, but you need to aim perfectly."],
    "knife" : [2, 3000, 15, 0, 100, "common item", "Hope mum is not looking for it."],
    "machette" : [2, 3000, 15, 0, 100, "common item", "Something between sword and knife."],
    "bottle" : [2, 3000, 15, 0, 100, "common item", "Wanna drink or what?"],
    "broken-bottle" : [2, 3000, 15, 0, 100, "common item", "Sharp edges may cause some ... injuries"],
    "hunting-knife" : [2, 3000, 15, 0, 100, "common item", "It's a deer, it's a enemy.. I don't care! I just cut things!"],
    "syringe" : [2, 3000, 15, 0, 100, "common item", "It's a deer, it's a enemy.. I don't care! I just cut things!"]
    }

#clothes
clothesProps = {
    #head
    "cap" : [0.5, 100, 0, 0, 100, "common item", "common item", "Baseball cap. Nothing special."],
    "winter-hat" : [0.5, 100, 0, 0, 100, "common item", "Just a hat for showy wheather."],
    "hat" : [0.5, 100, 0, 0, 100, "common item", "Common hat."],
   
    #body
    "t-shirt" : [0.5, 100, 0, 0, 100, "common item", "Pretty much basic t-shirt."],
    "sweatshirt" : [0.5, 100, 0, 0, 100, "common item", ""],
    "winter-coat" : [0.5, 100, 0, 0, 100, "common item", "Luxurious coat"],
    "sweater" : [0.5, 100, 0, 0, 100, "common item", "Sweater, my grandma made"],
    "jacket" : [0.5, 100, 0, 0, 100, "common item", "Waterproof jacket."],
    "bomber-jacket" : [0.5, 100, 0, 0, 100, "common item", "Some stylish clothing is a need."],

    #legs
    "leggins" : [0.5, 100, 0, 0, 100, "common item", "Wanna run or what?"],
    "shorts" : [0.5, 100, 0, 0, 100, "common item", "If I was too warm."],
    "jeans" : [0.5, 100, 0, 0, 100, "common item", "Classics!"],
    "pants" : [0.5, 100, 0, 0, 100, "common item", "Good quality, good price, good pants."],
    "tactical-pants" : [0.5, 100, 0, 0, 100, "common item", "One of the best pants I've ever seen..."]
    }

#armor
armorProps = {
    #head
    "helmet" : [0.5, 100, 0, 0, 100, "common item", "Classical helmet. Just to cover your head."],
    "light-armored-helmet" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy-armored-helmet" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light-tactical-helmet" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy-tactical-helmet" : [0.5, 100, 0, 20, 100, "common item", ""],

    #body
    "lab-coat" : [0.5, 100, 0, 0, 100, "common item", "Little bit dirty laboratory coat."],
    "apron" : [0.5, 100, 0, 0, 100, "common item", "Dark green apron."],
    "winter-coat" : [0.5, 100, 0, 0, 100, "common item", "Woolen, warm coat"],
    "vest" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light-armored-vest" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy-armored-vest" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light-tactical-vest" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy-tactical-vest" : [0.5, 100, 0, 20, 100, "common item", ""],

    #legs
    "protectors" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light-armored-protectors" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy-armored-protectors" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light-tactical-protectors" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy-tactical-protectors" : [0.5, 100, 0, 20, 100, "common item", ""]
    }

glovesProps = {
    # normale hands
    "latex-gloves" : [0.5, 100, 0, 0, 100, "common item", "Feel like a doctor with these!"],
    "winter-gloves" : [0.5, 100, 0, 0, 100, "common item", "Pretty warming experience..."],
    "tactical-gloves" : [0.5, 100, 3, 20, 100, "common item","Cutting heads, or deactivating bombs? Both!"],
    
    #armored hands
    "gloves" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light-armored-gloves" : [0.5, 100, 3, 0, 100, "common item", ""],
    "heavy-armored-gloves" : [0.5, 100, 5, 0, 100, "common item", ""],
    "light-tactical-gloves" : [0.5, 100, 7, 0, 100, "common item", ""],
    "heavy-tactical-gloves" : [0.5, 100, 10, 20, 100, "common item", ""]

    #newly added gloves
    }

shoesProps = {
    #normal shoes
    "sneakers" : [0.5, 100, 0, 0, 100, "common item", ""],
    "high-sneakers" : [0.5, 100, 0, 0, 100, "common item", ""],
    "oxford-shoes" : [0.5, 100, 0, 0, 100, "common item", ""],
    "trainers" : [0.5, 100, 0, 0, 100, "common item", ""],
    "crocs" : [0.5, 100, 0, 0, 100, "common item", ""],
    "slippers" : [0.5, 100, 0, 0, 100, "common item", ""],

    #armored shoes
    "boots" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light-armored-boots" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy-armored-boots" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light-tactical-boots" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy-tactical-boots" : [0.5, 100, 0, 20, 100, "common item", ""]
    }

# ITEM TYPE  key : [ "type" , "place on a figure" ]
#EQUIPABLE ITEMS (clothes, armor, weapons, shoes, gloves)
itemType = {
    "all" : ["all", "all"],
    
    #CLOTHES
    #head
    "cap" : ["clothes", "Head"],
    "winter-hat" : ["clothes" ,"Head"],
    "hat" : ["clothes" ,"Head"],


    #body
    "t-shirt" : ["clothes", "Body"],
    "sweatshirt" : ["clothes", "Body"],
    "coat" : ["clothes", "Body"],
    "winter-coat" : ["clothes", "Body"],
    "sweater" : ["clothes", "Body"],
    "jacket" : ["clothes", "Body"],
    "bomber-jacket" : ["clothes", "Body"],
    
    #legs
    "leggins" : ["clothes", "Legs"],
    "pants" : ["clothes", "Legs"],
    "jeans" : ["clothes", "Legs"],
    "shorts" : ["clothes", "Legs"],
    "tactical-pants" : ["clothes", "Legs"],

    #ARMOR
    #head
    "helmet" : ["armor", "Head"],
    "light-armored helmet" : ["armor", "Head"],
    "heavy-armored helmet" : ["armor", "Head"],
    "light-tactical helmet" : ["armor", "Head"],
    "heavy-tactical helmet" : ["armor", "Head"],

    
    #body
    "vest" : ["armor", "Body"],
    "light-armored vest" : ["armor", "Body"],
    "heavy-armored vest" : ["armor", "Body"],
    "light-tactical vest" : ["armor", "Body"],
    "heavy-tactical vest" : ["armor", "Body"],
    
    #legs
    "protectors" : ["armor", "Legs"],
    "light-armored protectors" : ["armor", "Legs"],
    "heavy-armored protectors" : ["armor", "Legs"],
    "light-tactical protectors" : ["armor", "Legs"],
    "heavy-tactical protectors" : ["armor", "Legs"],

    #WEAPONS
    "hunting-knife" : ["weapons", "Melee"],

    # GLOVES
    # normal gloves
    "latex-gloves" : ["gloves", "Gloves"],
    "winter-gloves" : ["gloves", "Gloves"],
    "tactical-gloves" : ["gloves", "Gloves"],
    
    #armored gloves
    "gloves" : ["gloves", "Gloves"],
    "light-armored gloves" : ["gloves", "Gloves"],
    "heavy-armored gloves" : ["gloves", "Gloves"],
    "light-tactical gloves" : ["gloves", "Gloves"],
    "heavy-tactical gloves" : ["gloves", "Gloves"],

    # SHOES
    #normal shoes
    "sneakers" : ["shoes", "Shoes"],
    "high-sneakers" : ["shoes", "Shoes"],
    "oxford-shoes" : ["shoes", "Shoes"],
    "trainers" : ["shoes", "Shoes"],
    "crocs" : ["shoes", "Shoes"],

    #armored shoes
    "boots" : ["shoes", "Shoes"],
    "light-armored boots" : ["shoes", "Shoes"],
    "heavy-armored boots" : ["shoes", "Shoes"],
    "light-tactical boots" : ["shoes", "Shoes"],
    "heavy-tactical boots" : ["shoes", "Shoes"],

    #UN-EQUIPABLE ITEMS (tools, food, beverages)
     }
