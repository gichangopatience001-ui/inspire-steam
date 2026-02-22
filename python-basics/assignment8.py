# Name : Patience Mukuhi Gichango
# Date : 22/02/2026
# ASSIGNMENT:
# Run the code in your PC to see the game's output
# See the problems below, try to solve them
# Ensure you can at least solve the first problem

# PROBLEM 1:
# When a character kicks another character, the opponent gets more damage than what the character deals
# Once this problem is solved, the final health of the warrior after taking damage should be 120

# PROBLEM 2:
# The function to takle other opponents is not defined.
# Solve the method, then let the warrior character takle the ninja character
# once this problem is solved, the final speed of the Ninja character should be 40

# In both cases use the report_status methods to verify of damages are done

class FighterCharacter:  
     def init (self, role, health, damage, speed):
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed

def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")

def report_status(self):
        print(f"\nCharacter Log: \n Role: {self.character_role} \n Health: {self.character_health} \n Damage: {self.character_damage} \n Speed: {self.characterspeed}\n __ \n")

def kick(self, opponent):
        character_damage = self.character_damage
        opponent.character_health = opponent.character_health - character_damage
        print(f"Game Log: {self.character_role} deals a damage of {character_damage} to the {opponent.character_role}.")

def takle(self, opponent):
      opponent.character_speed -= self.character_damage
      print(f"Game Log: {self.character_role} tackles {opponent.character_role}, reducing their speed by {self.character_damage}!")
        

# Create FighterCharacter    
ninja_character = FighterCharacter("Ninja", health=100, damage=40, speed=120)
warrior_character = FighterCharacter("warrior", health=160, damage=80, speed=80)


ninja_character.report_status()
warrior_character.report_status()

ninja_character.run("Up")
ninja_character.kick(warrior_character)

ninja_character.report_status()
warrior_character.report_status()
 
ninja_character.run("Up")
ninja_character.kick(warrior_character)

#NEW CODE FOR TACKLE
warrior_character.tackle(ninja_character)

ninja_character.report_status()
warrior_character.report_status()