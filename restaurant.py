#CS 175L

#Angela An

#restaurant

keep_going = 'yes'

while keep_going == 'yes':
    vegetarian = False
    vegan = False
    gluten_free = False
    vegetarian_input = input("Is anyone in your party a vegetarian? ")
    if vegetarian_input.lower() == "yes":
        vegetarian = True
    vegan_input = input("Is anyone in your party vegan? ")
    if vegan_input.lower() == "yes":
        vegan = True
    gluten_free_input = input("Is anyone in your party gluten-free? ")
    if gluten_free_input.lower() == "yes":
        gluten_free = True
    print()
    print("Here are your restaurant choices:")

    if not vegetarian and not vegan and not gluten_free:
        print("Joe's Gourmet Burgers\nMama's Fine Italian\nMain Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
    elif vegetarian and not vegan and not gluten_free:
        print("Mama's Fine Italian\nMain Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
    elif not vegetarian and not vegan and gluten_free:
        print("Main Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
    elif vegetarian and not vegan and gluten_free:
        print("Main Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
    elif not vegetarian and vegan and not gluten_free:
        print("Corner Cafe\nThe Chef's Kitchen")
    elif not vegetarian and vegan and gluten_free:
        print("Corner Cafe\nThe Chef's Kitchen")
    elif vegetarian and vegan and not gluten_free:
        print("Corner Cafe\nThe Chef's Kitchen")
    elif vegetarian and not vegan and gluten_free:
        print("Corner Cafe\nThe Chef's Kitchen")
    elif vegetarian and vegan and gluten_free:
        print("Corner Cafe\nThe Chef's Kitchen")
    print()
    keep_going = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): ")
    print()
