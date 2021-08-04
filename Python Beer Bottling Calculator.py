3
print("Welcome to the Cap Counter Program :)")
print("This will calculate how many caps are required based on the number and size of bottles required.")
fermenter_volume = float(input("First: Enter gals in fermenter:"))
six_packs = int(input("Now, Enter how many 12 oz six packs you would like:"))

print("The remaining number of 22 oz bottles is calculated below.")
#six pack volume is fermenter volume converted to ounces
#and subtracting user input: six_packs converted to ounces
#6 bottles/pack times 12 ounce/bottle
print()
print()
six_pack_volume = six_packs * 6 *12

#floor division to get how many 22 oz bottles go into fermenter volume
#after subtracting six_pack_volume
#multiply fermenter volume in gallons by 128 oz/gal to get ounces
number_of_22oz = (fermenter_volume *128 - six_pack_volume)// 22

bottle_caps_needed = number_of_22oz + six_packs * 6


print("number of 22 ounce bottles: ", number_of_22oz)
print("number of six packs: ", six_packs,"but you already said that!!")
print("You will also need: ", bottle_caps_needed,"bottle caps!")    

    
