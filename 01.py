dictionary = {"hello" : "salam",
              "student" : "okuwcy",
              "human" : "adam",
              "picture" : "surat" }

while True:
    print("""* * * * * My Dictionary Program * * * * * 
    1.Show
    2.Add
    3.Edit
    4.Delete
    5.Exit""")
    buyruk = int(input("Your choise?: "))
    if 1 == buyruk:
        for i,j in dictionary.items():
            print(i, " - ", j)
    elif 2 == buyruk:
        english = input("English soz: ")
        turkmen = input("Turkmen soz: ")
        dictionary[english] = turkmen
        print("Added")
    elif 3 == buyruk:
        word = input("Enter the word in english: ")
        word1 = input("Enter the word in turkmen: ")
        dictionary[word] = word1
        print("Editted")
    elif 4 == buyruk:
        soz = input("Enter the word in english: ")
        del dictionary[soz]
        print("Deleted")
    elif 5 == buyruk: 
        print("Thank you for using this program!")
        break
    else:
        print("Wrong command...")