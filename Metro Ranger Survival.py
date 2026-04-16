title = "Metro Ranger Survival" # Sets the title

# Imports random to create random events
import random 


# Creates Window
from tkinter import *
my_window = Tk()
my_window.attributes('-fullscreen', True)
my_window.resizable(True, True)


# Sets variables
play_count = 0
play_clicks = 0 
filter_decrease = ""
move_clicks = 0
dist_moved = ""
random_event = ""
chat_dist = ""
chat = ""
loot= ""
hlth = ""
filt_ammo = ""
encounter = ""
suffocating = ""
luck_count = 0
clicks = 0
health = 100
filters = 3
ammo = 50
status = "alive"
dist_to_station = random.randint( 2000 , 2500)


# Creates Welcome message
welcome_message = """Welcome, Ranger. You are currently in the tunnels between 
stations. Your goal: Reach the safety of 'Polis' before your 
resources—or your life—run out.

--- THE RULES OF THE METRO ---

1. MOVEMENT: Every step forward consumes 1 Filter. 
   If you run out of Filters, the toxic air will drain 20 HP 
   per move. Keep an eye on your lungs.

2. COMBAT: While travelling through the tunnels, you may encounter
   monsters which you will fight against using the bullets you have.

3. SURVIVAL: If your HP hits 0, the Metro claims you and you lose. 
   If your Distance hits 0, you survive and arrive at the station.

Choose your actions wisely. Every bullet is a paycheck, 
and every breath is a gift.
"""

# Creates win Message
win_msg = """Congratulations
You made it to through the tunnels 
    and arrived at the station

If you would like to play again 
 press the 'play again' button """

# Creates lose message
lose_msg = """Game Over
   You ran out of resources
and couldn't reach the station.

If you would like to try again
press the 'play again' button """

#Sets message for if you win the 2nd patrol
patrol_win = """ 
       EXPEDITION ENDED

        Congratulations
        You have completed your 
        allocated patrols for this shift"""

#Sets message for if you lose the 2nd patrol
patrol_lose = """
You lose
The metro has claimed you"""


# Creates Label to show The title
title = Label(
    my_window,
    text = "Survival resource manager",
    fg = "black",
    bg = "white",
    height = 3,
    width = 30,
    font = ("Courier" , 25 , "bold")
)
title.pack( pady = (200,0) , expand = TRUE)


# Creates the resource bar at the top
resource_bar = Label(
    my_window, 
    text=f"Health: {health} | Filters: {filters} | Ammo: {ammo} | Distance: {dist_to_station} | Status : {status} | Patrol: {play_count}/2",
    font=("Courier", 20 , "bold"),
    bg="black",
    fg="white"
)

# Creates chat frame
action_frame = Frame(
    my_window,
    bd = 10, 
    relief = "groove",
    height = 600,
    width= 600
)
action_frame.pack_propagate(False)


# Creates a label which tells the distance moved
dist_lbl = Label(
    action_frame,
    text = chat_dist, 
    font=("Courier", 20 , "bold")
)


# Creates a label which tells the loot found or lost
loot_lbl = Label(
    action_frame,
    text = loot, 
    font=("Courier", 20 , "bold")
)


# Creates a label which tells the health lost or added
hlth_lbl = Label(
    action_frame,
    text = hlth, 
    font=("Courier", 20 , "bold")
)


# Creates a label which tells the player if he is suffocating
suffocating_lbl = Label(
    action_frame,
    text = suffocating, 
    font=("Courier", 20 , "bold")
)


# Creates a label which tells if the player encounters a monster
enc_lbl = Label(
    action_frame,
    text = encounter, 
    font=("Courier", 20 , "bold")
)


# Creates frame for the buttons
button_frame = Frame(
    my_window,
    bd = 10,
    height = 800, 
    relief = "groove",
)


# Creates a label which stores the win message
win_lbl = Label(
    my_window,
    text = win_msg,
    font = ("Courier" , 30 , "bold")
)


# Creates a label which stores the lose message
lose_lbl = Label(
    my_window,
    text = lose_msg,
    font = ("Courier" , 30 , "bold")
)

#Sets label for if you win the 2nd patrol
patrolwin_lbl = Label(
    my_window,
    text = patrol_win,
    font = ("Courier" , 30 , "bold")   
)

#Sets label for if you lose the 2nd patrol
patrollose_lbl = Label(
    my_window,
    text = patrol_lose,
    font = ("Courier" , 30 , "bold")   
)


# Creates action which happens when the button is pressed a number of times
def button_clicked():
   global clicks
   clicks += 1

   # Sets what happens if the 1st button is pressed 
   if clicks == 1:
        title.config(
            text = welcome_message,
            width= 100,
            height = 30,
            bg = "grey"
        )
        continue_button.config(
            text = "Enter The Metro"
        )

   # Sets what happens if the 2nd button is pressed 
   if clicks == 2:
        title.pack_forget()
        continue_button.pack_forget()
        resource_bar.pack(side="top", fill="x", pady=0)
        button_frame.pack(fill = "x", pady = 5)
        move_button.pack(anchor = "center" , expand = True , pady = 60)
        action_frame.pack(side="bottom", fill="x", pady=5)
        dist_lbl.pack(pady = (75 , 0))
        suffocating_lbl.pack()
        enc_lbl.pack()
        loot_lbl.pack()
        hlth_lbl.pack(pady = (0 , 75))

title.pack_configure(pady=(0, 40))


#Creates button to start game
continue_button = Button(
    my_window,
    text="Continue",
    width=30,
    height=2,
    command=button_clicked
)
continue_button.pack(pady=(0, 50))




# Creates function which happens when you move
def move_funct():
    global play_count , move_clicks, status , dist_to_station,luck_count ,dist_moved, ammo , filters, health, chat_dist , hlth , loot , suffocating , encounter, filt_ammo , filter_decrease 
    move_clicks += 1

    # Decides what happens if the button is pressed
    if health > 0:
        if move_clicks >= 0:
            
            filter_decrease = random.randint(1,3)
            if filter_decrease > 1:
                filters -= 1

            # Generates a random distance moved and removes it from the distance to station variable, Tells the distance moved
            dist_moved = random.randint(100 , 300)
            dist_to_station -= dist_moved 
            chat_dist = f"You moved {dist_moved} metres"

            # Helps stop distance going under 0
            if dist_to_station < 0:
                dist_to_station = 0

            #Stops filters from going below 0
            if filters < 0:
                filters = 0

            # Creates a random number between 1 and 10 to decide an outcome
            random_event = random.randint(1 , 10)
            
            #Checks if you can move and the outcome
            if dist_to_station < 0:
                if random_event >= 5:
                    luck_count += 1
                    if ammo >= 10:
                        fight = random.randint(1 , 100)

                        #Action for if you get ambushed and win
                        if fight <= 50:
                            ammo -= 10
                            encounter = "You came across a monster and won"

                        #Action for if you get ambushed and have lose
                        else: 
                            health -= 25
                            ammo -= 25
                            encounter = "You came across a monster and lost"
                            hlth = "while fighting you lost 25HP"
                            loot = "while fighting you lost 25 bullets"

                    #Action for if you get ambushed and have no bullets
                    else:
                        health -= 30
                        ammo -= 20
                        encounter = "You came across a monster and lost"
                        hlth = "while fighting you lost 30hp"
                        loot = "while fighting you lost due to having no bullets"


            #Creates a random event for if you find ammo or a filter
            elif random_event <= 3:
                filt_ammo = random.randint(1 , 100)
                if filt_ammo >= 50:
                    ammo += 10
                    loot = "you found 10 ammo"
                else: 
                    if filters == 0: 
                        filters += 1
                        loot = "You found 1 filter"
                    else:
                        filters += 2
                        loot = "You found 1 filter"


            #If you get attacked 3 times you find a filter
            if luck_count == 3:
                filters += 1
                loot = "You found 1 filter"
                luck_count = 0
            

            #Action for if the filters run out you lose 20HP
            else:
                if filters == 0:
                    health -= 20
                    status = "suffocating"
                    suffocating = "You are suffocating and lost 20HP"


            #Action to set status as dead and stop heath from going below 0
            if health <= 0:
                health = 0
                status = "dead"
            #Turns the resource bar red if health goes below 20
            elif health <= 20 or status == "suffocating":
                resource_bar.config(
                    bg = "red"
                )
            if health >20:
                            resource_bar.config(
                    bg = "black"
                )

    #Resets labels
    dist_lbl.config(
        text = chat_dist
    )
    loot_lbl.config(
        text = loot
    )
    hlth_lbl.config(
        text = hlth
    )
    suffocating_lbl.config(
        text = suffocating
    )
    enc_lbl.config(
        text = encounter
    )
    resource_bar.config(
        text=f"Health: {health} | Filters: {filters} | Ammo: {ammo} | Distance: {dist_to_station} | Status : {status} | Patrol: {play_count}/2",
        )
    
    #Empties values
    hlth = ""
    loot = ""
    suffocating = ""
    encounter = ""


    #Creates action for if the player wins the first patrol
    if dist_to_station == 0 and health > 0:
        #Removes game UI
        resource_bar.pack_forget()
        button_frame.pack_forget()
        move_button.pack_forget()
        action_frame.pack_forget()
        
        #Marks 1 patrol done
        play_count += 1

        #Shows Win message and play again button
        win_lbl.pack(pady = 300)
        play_again.pack()


    #Creates action for if the player dies on the 1st patrol
    if health == 0:
        #Removes game UI
        resource_bar.pack_forget()
        button_frame.pack_forget()
        move_button.pack_forget()
        action_frame.pack_forget()

        #Marks 1 patrol done
        play_count += 1

        #Shows the lose message and play again button
        lose_lbl.pack(pady = 300)
        play_again.pack()

    #Creates action for if the player wins on the 2nd game
    if play_count == 2 and dist_to_station == 0:
        #Removes the game UI
        resource_bar.pack_forget()
        action_frame.pack_forget()
        win_lbl.pack_forget()
        lose_lbl.pack_forget()
        play_again.pack_forget()

        #Shows the Win messsage and exit button
        patrolwin_lbl.pack(pady = 300)
        exit_btn.pack()

    #Creates action for if the player losses on the 2nd game
    if play_count == 2 and health == 0:
        #Removes the game UI
        resource_bar.pack_forget()
        action_frame.pack_forget()
        win_lbl.pack_forget()
        lose_lbl.pack_forget()
        play_again.pack_forget()

        #Shows the Lose message and exit button
        patrollose_lbl.pack(pady = 300)
        exit_btn.pack()


#Creates action for play again button
def play_agn():
    global play_clicks , play_clicks ,move_clicks, status , dist_to_station,luck_count ,dist_moved, ammo , filters, health, chat_dist , hlth , loot , suffocating , encounter, filt_ammo , filter_decrease

    #resets the values
    health = 100
    status = "alive"
    filters = 3
    ammo = 50
    dist_to_station = random.randint( 2000 , 2500)
    move_clicks = 1
    luck_count = 0
    

    #Resets the labels
    dist_lbl.config(
        text = ""
    )
    suffocating_lbl.config(
        text = ""
    )
    enc_lbl.config(
        text = ""
    )
    loot_lbl.config(
        text = ""
    )
    hlth_lbl.config(
        text = ""
    )
    resource_bar.config(
        text=f"Health: {health} | Filters: {filters} | Ammo: {ammo} | Distance: {dist_to_station} | Status : {status} | Patrol: {play_count}/2",
        bg="black"
        )
    

    #Packs game UI
    resource_bar.pack(side="top", fill="x", pady=0)
    button_frame.pack(fill = "x", pady = 5)
    move_button.pack(anchor = "center" , expand = True , pady = 60)
    action_frame.pack(side="bottom", fill="x", pady=5)
    dist_lbl.pack(pady = (75 , 0))
    suffocating_lbl.pack()
    enc_lbl.pack()
    loot_lbl.pack()
    hlth_lbl.pack(pady = (0 , 75))

 
    #Forgets win/lose messages and play again button
    win_lbl.pack_forget()
    lose_lbl.pack_forget()
    play_again.pack_forget()



    my_window.update_idletasks() # Updates window
    move_funct() # calls move function


#Creates function for after the player has played twice
def exit_funct():
    if play_count == 2:
        my_window.destroy()



#Creates play again button
play_again = Button(
    my_window,
    text = "play again",
    width = 30,
    height = 2,
    command = play_agn
)


#Creates button used to close the game
exit_btn = Button(
    my_window,
    text = "Exit To desktop",
    width = 40,
    height = 3,
    command = exit_funct
)


# Creates Button used to move
move_button = Button (
    button_frame,
    text = "Move",
    width = 40,
    height = 10,
    font=("Courier", 20 , "bold"), 
    bg = "grey",
    fg = "blue",
    command=move_funct
)

    



    
# Keeps window open
my_window.mainloop()
