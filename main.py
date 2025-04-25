from pet import Pet

print("Hello, this is main.py running.")  # test print

# Create a pet
pet = Pet("Miffie")

# Interactions
pet.eat()
pet.play()
pet.sleep()

# Teach some tricks
pet.train("roll over")
pet.train("play dead")

# Show final status
pet.get_status()
