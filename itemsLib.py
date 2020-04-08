# ITEMS STATS

#UN-EQUIPABLE ITEMS
# hunger decrease / hp increase / thirst decrease / weight PŘIDAT!!!! / value of the item / description     Hardcore = pokud je jídlo 100% ok
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
    "pear" : [60, 30, 30, "common item", "Sweet pears are made of this.."],
    "banana" : [60, 30, 30, "special item", "WHAT A POWERFUL BANANA!!!"], # special item
    "broccoli" : [60, 30, 30, "common item", "Ughh..."],
    "chips" : [5, (-1), (-5), "common item", "Salt flavouring."],
    "cookies" : [5, (-1), (-5), "common item", "Salt flavouring."],
    }

# thirst decrease / hp increase / hunger decrease / value of the item / description     Hardcore = pokud je jídlo 100% ok.. #postava se pozvrací pokud je -5 přidat [číslo]
beverageProps = {
    "water" : [30, 3, 4, "common item", ""],
    "sugar water" : [2, 12, 1 , "common item", ""],
    "energy drink" : [2, 15, 0, "common item", ""],
    "dirty water" : [5, (-1), (-5), "common item", ""],
    "melted snow" : [9, 1, 1, "common item", ""],
    "sprinkling water" : [5, (-1), (-5), "common item", ""], #edit all down
    "beer" : [5, (-1), (-5), "common item", ""],
    "vodka" : [5, (-1), (-5), "special item", "Русский стандарт!"], # special item strenght all abilities + 10 (na quest/den nějakou určitou dobu, další den bude kocovina)
    "sprint" : [5, (-1), (-5), "common item", ""],
    "koko-kola" : [5, (-1), (-5), "common item", ""],
    "apple juice" : [5, (-1), (-5), "common item", ""],
    "lemon juice" : [5, (-1), (-5), "common item", ""],
    "tea" : [5, (-1), (-5), "common item", ""],
    "coffee" : [5, (-1), (-5), "common item", ""],
    "milk" : [5, (-1), (-5), "common item", ""],
    }

toolsProps = {
    "key" : "",
    "wrench" : "",
}

#EQUIPABLE ITEMS
# weight / price / attack / defense / hp / value of the item /description
weaponsProps = {
    "revolver" : [2, 3000, 15, 0, 100, "common item", "Western-like revolver. 6 bullets, 6 targets."],
    "pistol" : [2, 3000, 12, 0, 100, "common item", "Bang! Bang! Bang!"],
    "sniper rifle" : [2, 3000, 15, 0, 100, "common item", "Huge head ripper. One shot - one kill, but you need to aim perfectly."],
    "knife" : [2, 3000, 15, 0, 100, "common item", "Hope mum is not looking for it."],
    "machette" : [2, 3000, 15, 0, 100, "common item", "Something between sword and knife."],
    "bottle" : [2, 3000, 15, 0, 100, "common item", "Wanna drink or what?"],
    "broken bottle" : [2, 3000, 15, 0, 100, "common item", "Sharp edges may cause some ... injuries"],
    "hunting knife" : [2, 3000, 15, 0, 100, "common item", "It's a deer, it's a enemy.. I don't care! I just cut things!"],
    "syringe" : [2, 3000, 15, 0, 100, "common item", "It's a deer, it's a enemy.. I don't care! I just cut things!"]
    }

#clothes
clothesProps = {
    #head
    "cap" : [0.5, 100, 0, 0, 100, "common item", "common item", "Baseball cap. Nothing special."],
    "winter hat" : [0.5, 100, 0, 0, 100, "common item", "Just a hat for showy wheather."],
    "hat" : [0.5, 100, 0, 0, 100, "common item", "Common hat."],
   
    #body
    "t-shirt" : [0.5, 100, 0, 0, 100, "common item", "Pretty much basic t-shirt."],
    "sweatshirt" : [0.5, 100, 0, 0, 100, "common item", ""],
    "coat" : [0.5, 100, 0, 0, 100, "common item", "Luxurious coat"],
    "sweater" : [0.5, 100, 0, 0, 100, "common item", "Sweater, my grandma made"],
    "jacket" : [0.5, 100, 0, 0, 100, "common item", "Waterproof jacket."],
    "bomber jacket" : [0.5, 100, 0, 0, 100, "common item", "Some stylish clothing is a need."],

    #legs
    "leggins" : [0.5, 100, 0, 0, 100, "common item", "Wanna run or what?"],
    "shorts" : [0.5, 100, 0, 0, 100, "common item", "If I was too warm."],
    "jeans" : [0.5, 100, 0, 0, 100, "common item", "Classics!"],
    "pants" : [0.5, 100, 0, 0, 100, "common item", "Good quality, good price, good pants."],
    "tactical pants" : [0.5, 100, 0, 0, 100, "common item", "One of the best pants I've ever seen..."]
    }

#armor
armorProps = {
    #head
    "helmet" : [0.5, 100, 0, 0, 100, "common item", "Classical helmet. Just to cover your head."],
    "light armored helmet" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy armored helmet" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light tactical helmet" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy tactical helmet" : [0.5, 100, 0, 20, 100, "common item", ""],

    #body
    "lab coat" : [0.5, 100, 0, 0, 100, "common item", "Little bit dirty laboratory coat."],
    "apron" : [0.5, 100, 0, 0, 100, "common item", "Dark green apron."],
    "winter coat" : [0.5, 100, 0, 0, 100, "common item", "Woolen, warm coat"],
    "vest" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light armored vest" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy armored vest" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light tactical vest" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy tactical vest" : [0.5, 100, 0, 20, 100, "common item", ""],

    #legs
    "protectors" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light armored protectors" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy armored protectors" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light tactical protectors" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy tactical protectors" : [0.5, 100, 0, 20, 100, "common item", ""]
    }

glovesProps = {
    # normale hands
    "latex gloves" : [0.5, 100, 0, 0, 100, "common item", "Feel like a doctor with these!"],
    "winter gloves" : [0.5, 100, 0, 0, 100, "common item", "Pretty warming experience..."],
    "tactical gloves" : [0.5, 100, 3, 20, 100, "common item","Cutting heads, or deactivating bombs? Both!"],
    
    #armored hands
    "gloves" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light armored gloves" : [0.5, 100, 3, 0, 100, "common item", ""],
    "heavy armored gloves" : [0.5, 100, 5, 0, 100, "common item", ""],
    "light tactical gloves" : [0.5, 100, 7, 0, 100, "common item", ""],
    "heavy tactical gloves" : [0.5, 100, 10, 20, 100, "common item", ""]

    #newly added gloves
    }

shoesProps = {
    #normal shoes
    "sneakers" : [0.5, 100, 0, 0, 100, "common item", ""],
    "high sneakers" : [0.5, 100, 0, 0, 100, "common item", ""],
    "oxford shoes" : [0.5, 100, 0, 0, 100, "common item", ""],
    "trainers" : [0.5, 100, 0, 0, 100, "common item", ""],
    "crocs" : [0.5, 100, 0, 0, 100, "common item", ""],
    "slippers" : [0.5, 100, 0, 0, 100, "common item", ""],

    #armored shoes
    "boots" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light armored boots" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy armored boots" : [0.5, 100, 0, 0, 100, "common item", ""],
    "light tactical boots" : [0.5, 100, 0, 0, 100, "common item", ""],
    "heavy tactical boots" : [0.5, 100, 0, 20, 100, "common item", ""]
    }

# ITEM TYPE  key : [ "type" , "place on a figure" ]
#EQUIPABLE ITEMS (clothes, armor, weapons, shoes, gloves)
itemType = {
    
    #CLOTHES
    #head
    "cap" : ["clothes", "Head"],
    "winter hat" : ["clothes" ,"Head"],
    "hat" : ["clothes" ,"Head"],


    #body
    "t-shirt" : ["clothes", "Body"],
    "sweatshirt" : ["clothes", "Body"],
    "coat" : ["clothes", "Body"],
    "winter coat" : ["clothes", "Body"],
    "sweater" : ["clothes", "Body"],
    "jacket" : ["clothes", "Body"],
    "bomber jacket" : ["clothes", "Body"],
    
    #legs
    "leggins" : ["clothes", "Legs"],
    "pants" : ["clothes", "Legs"],
    "jeans" : ["clothes", "Legs"],
    "shorts" : ["clothes", "Legs"],
    "tactical pants" : ["clothes", "Legs"],

    #ARMOR
    #head
    "helmet" : ["armor", "Head"],
    "light armored helmet" : ["armor", "Head"],
    "heavy armored helmet" : ["armor", "Head"],
    "light tactical helmet" : ["armor", "Head"],
    "heavy tactical helmet" : ["armor", "Head"],

    
    #body
    "vest" : ["armor", "Body"],
    "light armored vest" : ["armor", "Body"],
    "heavy armored vest" : ["armor", "Body"],
    "light tactical vest" : ["armor", "Body"],
    "heavy tactical vest" : ["armor", "Body"],
    
    #legs
    "protectors" : ["armor", "Legs"],
    "light armored protectors" : ["armor", "Legs"],
    "heavy armored protectors" : ["armor", "Legs"],
    "light tactical protectors" : ["armor", "Legs"],
    "heavy tactical protectors" : ["armor", "Legs"],

    #WEAPONS
    "hunting knife" : ["weapons", "Melee"],

    # GLOVES
    # normal gloves
    "latex gloves" : ["gloves", "Gloves"],
    "winter gloves" : ["gloves", "Gloves"],
    "tactical gloves" : ["gloves", "Gloves"],
    
    #armored gloves
    "gloves" : ["gloves", "Gloves"],
    "light armored gloves" : ["gloves", "Gloves"],
    "heavy armored gloves" : ["gloves", "Gloves"],
    "light tactical gloves" : ["gloves", "Gloves"],
    "heavy tactical gloves" : ["gloves", "Gloves"],

    # SHOES
    #normal shoes
    "sneakers" : ["shoes", "Shoes"],
    "high sneakers" : ["shoes", "Shoes"],
    "oxford shoes" : ["shoes", "Shoes"],
    "trainers" : ["shoes", "Shoes"],
    "crocs" : ["shoes", "Shoes"],

    #armored shoes
    "boots" : ["shoes", "Shoes"],
    "light armored boots" : ["shoes", "Shoes"],
    "heavy armored boots" : ["shoes", "Shoes"],
    "light tactical boots" : ["shoes", "Shoes"],
    "heavy tactical boots" : ["shoes", "Shoes"],

    #UN-EQUIPABLE ITEMS (tools, food, beverages)
     }
