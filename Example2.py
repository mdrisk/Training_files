from Tkinter import *
from PIL import Image, ImageTk
import sys
import os

root = Tk()
location = 0
photonumber = 0
meter = 0

point1 = True
point2 = True
point3 = True
point4 = True
point5 = True
point6 = True
point7 = True
point8 = True
point9 = True
point10 = True
point11 = True
point12 = True
point13 = True

photos = [PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/start.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/lobby.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/coin.gif"),  PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/key.gif"), 
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/coininfo.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/hallway.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/room101.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/bathroom.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/body.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/hair.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/detective.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/suspects.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/victim.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/kitchen.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/cook.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/stain.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/cookinfo.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/secretpassage.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/crowbar.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/room103.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/evidence.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/room102.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/butler.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/family.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/purse.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/ballroom.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/owner.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/fortune.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/forest.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/vault.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/evil.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/fire.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/attack.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/airvent.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/airvent.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/laytonquestion.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/furry.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/death.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/more.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/cry.gif"),
PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/coinend.gif"), PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/end.gif")] 

def button1():
    global location
    global photonumber
    global meter
    if location == 0:
        location = 1
        canvas.itemconfig(img, image = photos[1])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the LOBBY. "No running!" someone yells. You were told the body is in ROOM 101. A fellow detective is already on the scene. \n 1.Talk to CONCIERGE 2.Enter HALLWAY 3.Enter KITCHEN')
        
    elif location == 1:
        location = 2
        canvas.itemconfig(img, image = photos[2])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello, I am the concierge," he says. "Welcome to the Overlooked Hotel." \n 1.Return to LOBBY 2.Ask about ROOM 101 3.Ask about hotel')
    
    elif location == 2:
        location = 1
        canvas.itemconfig(img, image = photos[1])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the LOBBY. "No running!" someone yells. You were told the body is in ROOM 101. A fellow detective is already on the scene. \n 1.Talk to CONCIERGE 2.Enter HALLWAY 3.Enter KITCHEN')
    
    elif location == 3:
        location = 2
        canvas.itemconfig(img, image = photos[2])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello, I am the concierge," he says. "Welcome to the Overlooked Hotel." \n 1.Return to LOBBY 2.Ask about ROOM 101 3.Ask about hotel')
        
    elif location == 4:
        location = 2
        canvas.itemconfig(img, image = photos[2])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello, I am the concierge," he says. "Welcome to the Overlooked Hotel." \n 1.Return to LOBBY 2.Ask about ROOM 101 3.Ask about hotel')
   
    elif location == 5:
        location = 1
        canvas.itemconfig(img, image = photos[1])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the LOBBY. "No running!" someone yells. You were told the body is in ROOM 101. A fellow detective is already on the scene. \n 1.Talk to CONCIERGE 2.Enter HALLWAY 3.Enter KITCHEN')
    
    elif location == 6:
        location = 5 
        canvas.itemconfig(img, image = photos[5])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the HALLWAY. Three doors branch off from here. The left and middle are cracked open, but the right one is locked tight. \n 1.Go back to LOBBY 2.Enter the left door 3.Enter the middle door')              
    
    elif location == 7:
        location = 6
        canvas.itemconfig(img, image = photos[6])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Here it is, the scene of the crime. A camera flashes in the BATHROOM. DETECTIVE Brawnsfeld must be inside. \n 1.Go back to HALLWAY 2.Enter BATHROOM 3.---')
    
    elif location == 8:
        location = 7
        canvas.itemconfig(img, image = photos[7])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The BODY is resting in the bathtub. It looks particularly gruesome, and you hesitate to get close. The DETECTIVE is investigating the other end of the room. \n 1.Go back to ROOM 101 2.Investigate BODY 3.Talk to DETECTIVE')
    
    elif location == 9:
        location = 8
        canvas.itemconfig(img, image = photos[8])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The BODY is horribly mutilated; she is almost unrecognizable as the young, rich socialite this woman once was. \n 1.Go back to BATHROOM 2.Search BODY 3.---')                                                                                
      
    elif location == 10:
        location = 7
        canvas.itemconfig(img, image = photos[7])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The BODY is resting in the bathtub. It looks particularly gruesome, and you hesitate to get close. The DETECTIVE is investigating the other end of the room. \n 1.Go back to ROOM 101 2.Investigate BODY 3.Talk to DETECTIVE')
      
    elif location == 11:
        location = 10
        canvas.itemconfig(img, image = photos[10])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello there!" a voice booms. Your old pal from the station stands confidently in the roomy restroom. "This is a shame, it sure is," he says sullenly. "But now that we are on the job, this killer will be brought to justice, eh?" \n 1.Go back to BATHROOM 2.Ask about SUSPECTS 3.Ask about VICTIM')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    
    elif location == 12:
        location = 10
        canvas.itemconfig(img, image = photos[10])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello there!" a voice booms. Your old pal from the station stands confidently in the roomy restroom. "This is a shame, it sure is," he says sullenly. "But now that we are on the job, this killer will be brought to justice, eh?" \n 1.Go back to BATHROOM 2.Ask about SUSPECTS 3.Ask about VICTIM')
        
    elif location == 13:
        location = 1
        canvas.itemconfig(img, image = photos[1])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the LOBBY. "No running!" someone yells. You were told the body is in ROOM 101. A fellow detective is already on the scene. \n 1.Talk to CONCIERGE 2.Enter HALLWAY 3.Enter KITCHEN')
    
    elif location == 14:
        location = 13
        canvas.itemconfig(img, image = photos[13])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the KITCHEN. Compared to the rest of the hotel, it almost seems ultra-modern. Guess OSHA came through recently. A COOK stands over a pot of stew. It smells heavenly. However, a draft near the far end of the KITCHEN catches your eye as well. \n 1.Return to the LOBBY 2.Talk to COOK 3.Investigate draft')
    
    elif location == 15:
        location = 14
        canvas.itemconfig(img, image = photos[14])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The COOK turns and greets you with a smile. "Hello there honey!" she grins. "My name is Mama Cass, short for Casserole, and I am the COOK here at the Overlooked Hotel. How ya doin?" \n 1.Return to KITCHEN 2.Ask about MYSTERIOUS STAINS 3.Ask about VICTIM')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    elif location == 16:
        location = 14
        canvas.itemconfig(img, image = photos[14])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The COOK turns and greets you with a smile. "Hello there honey!" she grins. "My name is Mama Cass, short for Casserole, and I am the COOK here at the Overlooked Hotel. How ya doin?" \n 1.Return to KITCHEN 2.Ask about MYSTERIOUS STAINS 3.Ask about VICTIM')
   
    elif location == 17:
        location = 13
        canvas.itemconfig(img, image = photos[13])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the KITCHEN. Compared to the rest of the hotel, it almost seems ultra-modern. Guess OSHA came through recently. A COOK stands over a pot of stew. It smells heavenly. However, a draft near the far end of the KITCHEN catches your eye as well. \n 1.Return to the LOBBY 2.Talk to COOK 3.Investigate draft')
    
    elif location == 18:
        location = 17
        canvas.itemconfig(img, image = photos[17])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Taking a closer look, you find a secret passage. The COOK does not appear to notice you leave. You slip through the passage and look around. Scary messages are written on the walls, probably by unlucky hotel guests before they got devoured by groundhogs. You should not stay here. \n 1.Return to KITCHEN 2.Grope around in the dark 3.Continue blindly onward')
    
    elif location == 19:
        location = 17
        canvas.itemconfig(img, image = photos[17])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the secret passage. Scary messages are written on the walls, probably by unlucky hotel guests before they got devoured by groundhogs. You should not stay here. \n 1.Return to KITCHEN 2.Grope around in the dark 3.Continue blindly onward')     
    
    elif location == 20:
        location = 19
        canvas.itemconfig(img, image = photos[19])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The door to ROOM 103 appears to be locked from the inside, allowing you to get out but no one else to get in. \n 1.Return to PASSAGE 2.Search ROOM 103 3.Enter HALLWAY')      
    
    elif location == 21:
        location = 5 
        canvas.itemconfig(img, image = photos[5])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the HALLWAY. Three doors branch off from here. The left and middle are cracked open, but the right one is locked tight. \n 1.Go back to LOBBY 2.Enter the left door 3.Enter the middle door') 
    
    elif location == 22:
        location = 21
        canvas.itemconfig(img, image = photos[21])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter ROOM 102. It is the most ornate room you have encountered thus far. A short, stocky man is trying to clean on top of a shelf, but cannot reach. Large double doors lead deeper into the hotel.  \n 1.Go back to HALLWAY 2.Talk to BUTLER 3.Enter BALLROOM')                              
    
    elif location == 23:
        location = 22
        canvas.itemconfig(img, image = photos[22])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh h-hello *nyah*... I am the butler in this establishment. Nobody ever appreciates me though... Say, if you help me clean this top shelf, you can interview me!" the little man says. You say you are legally allowed to interview him regardless of the dust content of the shelf, so long as you respect his constitutional rights. He sighs and resigns himself to your questions. \n 1.Go back to ROOM 102 2.Ask about HOTEL 3.Ask about VICTIM')                                                      
    
    elif location == 24:
        location = 22
        canvas.itemconfig(img, image = photos[22])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh h-hello *nyah*... I am the butler in this establishment. Nobody ever appreciates me though... Say, if you help me clean this top shelf, you can interview me!" the little man says. You say you are legally allowed to interview him regardless of the dust content of the shelf, so long as you respect his constitutional rights. He sighs and resigns himself to your questions. \n 1.Go back to ROOM 102 2.Ask about HOTEL 3.Ask about VICTIM')                                                      
    
    elif location == 25:
        location = 21
        canvas.itemconfig(img, image = photos[21])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter ROOM 102. It is the most ornate room you have encountered thus far. A short, stocky man is trying to clean on top of a shelf, but cannot reach. Large double doors lead deeper into the hotel.  \n 1.Go back to HALLWAY 2.Talk to BUTLER 3.Enter BALLROOM')                                                                                                                                                                                                        
    
    elif location == 26:
        location = 25
        canvas.itemconfig(img, image = photos[25])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter an elaborate BALLROOM. Against one end of the wall is a very high-tech safe. Pacing in front of it is the OWNER of the hotel. It is recommended you have at least a score of 10 on your MAGICAL MYSTERY METER before preceding to the safe. \n 1.Return to ROOM 102 2.Talk to OWNER 3.Enter SAFE')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    
    elif location == 27:
        location = 26
        canvas.itemconfig(img, image = photos[26])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh thank heavens you have arrived. I am absolutely beside myself with worry and grief! My own daughter, shoved off this mortal coil! And with her dies the only hope of getting into this SAFE! Woe is me, whatever will I, Baron von Trumpo III, do?" \n 1.Go back to BALLROOM 2.Ask about SAFE 3.Ask about HOTEL')                              
    
    elif location == 28:
        location = 26
        canvas.itemconfig(img, image = photos[26])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh thank heavens you have arrived. I am absolutely beside myself with worry and grief! My own daughter, shoved off this mortal coil! And with her dies the only hope of getting into this SAFE! Woe is me, whatever will I, Baron von Trumpo III, do?" \n 1.Go back to BALLROOM 2.Ask about SAFE 3.Ask about HOTEL')                              
    
    elif location == 29:
        location = 30
        canvas.itemconfig(img, image = photos[30])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You steal the treasure! Everyone is after you! Quickly, make your escape! \n 1.Jump out the window 2.Sic the groundhogs 3.Crawl through the air vent')                              
    
    elif location == 30:
        location = 98
        canvas.itemconfig(img, image = photos[31])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You jump out the window. Too bad you are four stories up. SPLAT! The groundhogs make a meal out of your carcass. Press any button to continue.')
    
    elif location == 34:
        location = 98
        canvas.itemconfig(img, image = photos[36])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Only one person could have commited this dastardly crime," you say. "And that person is YOU!" The BUTLER quivers and faints. Brawnsfeld walks over and handcuffs him. "This man did not murder Lady Evelynn," says Detective Brawnsfeld. "Even worse, he was a FURRY." While the killer of Lady Evelynn was never brought to justice, everyone in the hotel breathed a sigh of relief. \n Press any button to continue')
    
    elif location == 35:
        location = 34
        canvas.itemconfig(img, image = photos[35])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'It is time to accuse a suspect. Based on the evidence you gathered, who do you think murdered Lady Evelynn? \n 1.BUTLER 2.COOK 3.MORE OPTIONS')
    
    elif location == 100:
        restart_program()
                   
    else:
        location = 100
        photonumber = len(photos)-1
        canvas.itemconfig(img, image = photos[photonumber])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The End. \n 1.RESTART 2.--- 3.QUIT')
        
def button2():
    global location
    global photonumber
    global meter
    global point1
    global point3
    global point5
    global point6
    global point7
    global point8
    global point10
    global point12
    if location == 0:
        location = 1
        canvas.itemconfig(img, image = photos[1])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the LOBBY. "No running!" someone yells. You were told the body is in ROOM 101. A fellow detective is already on the scene. \n 1.Talk to CONCIERGE 2.Enter HALLWAY 3.Enter KITCHEN')
      
    elif location == 1:
        location = 5 
        canvas.itemconfig(img, image = photos[5])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the HALLWAY. Three doors branch off from here. The left and middle are cracked open, but the right one is locked tight. \n 1.Go back to LOBBY 2.Enter the left door 3.Enter the middle door') 
        
    elif location == 2:
        if point1:
            meter += 1
            mmm(meter)
            point1 = False
        location = 3
        canvas.itemconfig(img, image = photos[3])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"ROOM 101 is down the HALLWAY to the left. Do be careful. Not many guests are in the hotel, but there is still riffraff ruffling about." \n Press any button to go back')
     
    elif location == 3:
        location = 2
        canvas.itemconfig(img, image = photos[2])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello, I am the concierge," he says. "Welcome to the Overlooked Hotel." \n 1.Return to LOBBY 2.Ask about ROOM 101 3.Ask about hotel')      
    
    elif location == 4:
        location = 2
        canvas.itemconfig(img, image = photos[2])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello, I am the concierge," he says. "Welcome to the Overlooked Hotel." \n 1.Return to LOBBY 2.Ask about ROOM 101 3.Ask about hotel')
    
    elif location == 5:
        location = 6
        canvas.itemconfig(img, image = photos[6])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Here it is, the scene of the crime. A camera flashes in the BATHROOM. DETECTIVE Brawnsfeld must be inside. \n 1.Go back to HALLWAY 2.Enter BATHROOM 3.---')
    
    elif location == 6:
        location = 7
        canvas.itemconfig(img, image = photos[7])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The BODY is resting in the bathtub. It looks particularly gruesome, and you hesitate to get close. The DETECTIVE is investigating the other end of the room. \n 1.Go back to ROOM 101 2.Investigate BODY 3.Talk to DETECTIVE')              
    
    elif location == 7:
        location = 8
        canvas.itemconfig(img, image = photos[8])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The BODY is horribly mutilated; she is almost unrecognizable as the young, rich socialite this woman once was. \n 1.Go back to BATHROOM 2.Search BODY 3.---')
        
    elif location == 8:
        if point7:
            meter += 1
            mmm(meter)
            point7 = False
        location = 9
        canvas.itemconfig(img, image = photos[9])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The woman has had her hair removed, like someone had pulled it out by the roots. You collect a sample. Not much else can be done with the body at the moment. \n Press any button to go back')
    
    elif location == 9:
        location = 8
        canvas.itemconfig(img, image = photos[8])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The BODY is horribly mutilated; she is almost unrecognizable as the young, rich socialite this woman once was. \n 1.Go back to BATHROOM 2.Search BODY 3.---')
   
    elif location == 10:
        if point8:
            meter += 1
            mmm(meter)
            point8 = False
        location = 11
        canvas.itemconfig(img, image = photos[11])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'There are three main suspects. The CONCIERGE is cleared of any wrongdoing because he seems pretty nice. The other three are the COOK, the OWNER, and the BUTLER. Interview them all and see what you can get out of them. The COOK is obviously in the kitchens, and the other two are around here somewhere. My money is on the BUTLER; the man looks too shifty... \n Press any button to go back')     
     
    elif location == 11:
        location = 10
        canvas.itemconfig(img, image = photos[10])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello there!" a voice booms. Your old pal from the station stands confidently in the roomy restroom. "This is a shame, it sure is," he says sullenly. "But now that we are on the job, this killer will be brought to justice, eh?" \n 1.Go back to BATHROOM 2.Ask about SUSPECTS 3.Ask about VICTIM')             
     
    elif location == 12:
        location = 10
        canvas.itemconfig(img, image = photos[10])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello there!" a voice booms. Your old pal from the station stands confidently in the roomy restroom. "This is a shame, it sure is," he says sullenly. "But now that we are on the job, this killer will be brought to justice, eh?" \n 1.Go back to BATHROOM 2.Ask about SUSPECTS 3.Ask about VICTIM')                                        
    
    elif location == 13:
        location = 14
        canvas.itemconfig(img, image = photos[14])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The COOK turns and greets you with a smile. "Hello there honey!" she grins. "My name is Mama Cass, short for Casserole, and I am the COOK here at the Overlooked Hotel. How ya doin?" \n 1.Return to KITCHEN 2.Ask about MYSTERIOUS STAINS 3.Ask about VICTIM')
       
    elif location == 14:
        if point3:
            meter += 1
            mmm(meter)
            point3 = False
        location = 15
        canvas.itemconfig(img, image = photos[15])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"These stains? Oh, honey, I just finished getting rid of a nasty groundhog! This area is known for our bigguns, but this guy was a real whopper. I needed both my rolling pin and my CROWBAR to take him down! I seem to have misplaced my CROWBAR though... If you find it let me know!" \n Press any button to go back')  
   
    elif location == 15:
        location = 14
        canvas.itemconfig(img, image = photos[14])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The COOK turns and greets you with a smile. "Hello there honey!" she grins. "My name is Mama Cass, short for Casserole, and I am the COOK here at the Overlooked Hotel. How ya doin?" \n 1.Return to KITCHEN 2.Ask about MYSTERIOUS STAINS 3.Ask about VICTIM')                                                                                                                                                                                                                                            
 
    elif location == 16:
        location = 14
        canvas.itemconfig(img, image = photos[14])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The COOK turns and greets you with a smile. "Hello there honey!" she grins. "My name is Mama Cass, short for Casserole, and I am the COOK here at the Overlooked Hotel. How ya doin?" \n 1.Return to KITCHEN 2.Ask about MYSTERIOUS STAINS 3.Ask about VICTIM')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    elif location == 17:
        if point5:
            meter += 1
            mmm(meter)
            point5 = False
        location = 18
        canvas.itemconfig(img, image = photos[18])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You find a CROWBAR! It is flecked with blood, and a single blond hair. \n Press any button to return to the darkness')
    
    elif location == 18:
        location = 17
        canvas.itemconfig(img, image = photos[17])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Taking a closer look, you find a secret passage. The COOK does not appear to notice you leave. You slip through the passage and look around. Scary messages are written on the walls, probably by unlucky hotel guests before they got devoured by groundhogs. You should not stay here. \n 1.Return to KITCHEN 2.Grope around in the dark 3.Continue blindly onward')
    
    elif location == 19:
        if point6:
            meter += 1
            mmm(meter)
            point6 = False
        location = 20
        canvas.itemconfig(img, image = photos[20])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Pouring over the room, you discover a file folder hidden under the mattress. My goodness! The file is all about Lady Evelynn. It seems to be the work of a crazed madman, the killer perhaps? The file gives one clue to the identity of the murderer. An order slip for blue shoes...  \n Press any button to go back')      
      
    elif location == 20:
        location = 19
        canvas.itemconfig(img, image = photos[19])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The door to ROOM 103 appears to be locked from the inside, allowing you to get out but no one else to get in. \n 1.Return to PASSAGE 2.Search ROOM 103 3.Enter HALLWAY')      
    
    elif location == 21:
        location = 22
        canvas.itemconfig(img, image = photos[22])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh h-hello *nyah*... I am the butler in this establishment. Nobody ever appreciates me though... Say, if you help me clean this top shelf, you can interview me!" the little man says. You say you are legally allowed to interview him regardless of the dust content of the shelf, so long as you respect his constitutional rights. He sighs and resigns himself to your questions. \n 1.Go back to ROOM 102 2.Ask about HOTEL 3.Ask about VICTIM')                                                      
    
    elif location == 22:
        if point10:
            meter += 1
            mmm(meter)
            point10 = False
        location = 23
        canvas.itemconfig(img, image = photos[23])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"The Overlooked Hotel has been in the Trumpo family for generations. Lady Evelynn dying does not make her the first death in this building, nor, I doubt, the last." \n Press any button to go back')                                                      
    
    elif location == 23:
        location = 22
        canvas.itemconfig(img, image = photos[22])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh h-hello *nyah*... I am the butler in this establishment. Nobody ever appreciates me though... Say, if you help me clean this top shelf, you can interview me!" the little man says. You say you are legally allowed to interview him regardless of the dust content of the shelf, so long as you respect his constitutional rights. He sighs and resigns himself to your questions. \n 1.Go back to ROOM 102 2.Ask about HOTEL 3.Ask about VICTIM')                                                      
    
    elif location == 24:
        location = 22
        canvas.itemconfig(img, image = photos[22])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh h-hello *nyah*... I am the butler in this establishment. Nobody ever appreciates me though... Say, if you help me clean this top shelf, you can interview me!" the little man says. You say you are legally allowed to interview him regardless of the dust content of the shelf, so long as you respect his constitutional rights. He sighs and resigns himself to your questions. \n 1.Go back to ROOM 102 2.Ask about HOTEL 3.Ask about VICTIM')                                                      
    
    elif location == 25:
        location = 26
        canvas.itemconfig(img, image = photos[26])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh thank heavens you have arrived. I am absolutely beside myself with worry and grief! My own daughter, shoved off this mortal coil! And with her dies the only hope of getting into this SAFE! Woe is me, whatever will I, Baron von Trumpo III, do?" \n 1.Go back to BALLROOM 2.Ask about SAFE 3.Ask about HOTEL')                              
    
    elif location == 26:
        if point12:
            meter += 1
            mmm(meter)
            point12 = False
        location = 27
        canvas.itemconfig(img, image = photos[27])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"You see, the only way to get inside the safe is to use the DNA of dearly departed Evelynn. That rotten detective will not let me near my daugther to secure it! Uh, I mean, your hardworking partner. It is crucial that no rapscallion gets his hands on her fortune. Otherwise, the Overlooked Hotel might have to close... How else are we to afford the cost of groundhog exterminators? \n Press any button to go back')                              
    
    elif location == 27:
        location = 26
        canvas.itemconfig(img, image = photos[26])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh thank heavens you have arrived. I am absolutely beside myself with worry and grief! My own daughter, shoved off this mortal coil! And with her dies the only hope of getting into this SAFE! Woe is me, whatever will I, Baron von Trumpo III, do?" \n 1.Go back to BALLROOM 2.Ask about SAFE 3.Ask about HOTEL')                              
    
    elif location == 28:
        location = 26
        canvas.itemconfig(img, image = photos[26])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh thank heavens you have arrived. I am absolutely beside myself with worry and grief! My own daughter, shoved off this mortal coil! And with her dies the only hope of getting into this SAFE! Woe is me, whatever will I, Baron von Trumpo III, do?" \n 1.Go back to BALLROOM 2.Ask about SAFE 3.Ask about HOTEL')                              

    elif location == 29:
        location = 34
        canvas.itemconfig(img, image = photos[35])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'It is time to accuse a suspect. Based on the evidence you gathered, who do you think murdered Lady Evelynn? \n 1.BUTLER 2.COOK 3.MORE OPTIONS')
    
    elif location == 30:
        location = 98
        canvas.itemconfig(img, image = photos[32])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'With quick thinking, you sound the mating call of the mighty groundhog. The furry beasts swarm the guests and employees, and in the confusion you escape unharmed. The CONCIERGE however, is completely devoured. Time for Fiji! Press any button to continue.')
    
    elif location == 34:
        location = 98
        canvas.itemconfig(img, image = photos[37])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Only one person could have commited this dastardly crime," you say. "And that person is YOU!" The COOK gasps. "Good call boss," Brawnsfeld says as he prepares to cuff her. The COOK lashes out, knocking your partner dead with one fell swoop of her rolling pin. She was not the murderer of Lady Evelynn. You still go home with a killer in your paddywagon, but with two bodies instead of one... \n Press any button to continue')
    
    elif location == 35:
        location = 98
        canvas.itemconfig(img, image = photos[39])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Only one person could have commited this dastardly crime," you say. "And that person is YOU!" The OWNER gasps. "Always thought he was up to no good," Brawnsfeld says as he cuffs him. The OWNER sobs, "Oh Evelynn, who will take care of my hotel now..." He was not the murderer of Lady Evelynn. Years later you hear the Overlooked Hotel closed for good. \n Press any button to continue')                                            
    
    else:
        photonumber = len(photos)-1
        canvas.itemconfig(img, image = photos[photonumber])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The End. \n 1.RESTART 2.--- 3.QUIT')
        
def button3():
    global location
    global photonumber
    global meter
    global point2
    global point4
    global point9
    global point11
    global point13
    if location == 0:
        location = 1
        canvas.itemconfig(img, image = photos[1])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the LOBBY. "No running!" someone yells. You were told the body is in ROOM 101. A fellow detective is already on the scene. \n 1.Talk to CONCIERGE 2.Enter HALLWAY 3.Enter KITCHEN')
       
    elif location == 1:
        location = 13
        canvas.itemconfig(img, image = photos[13])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the KITCHEN. Compared to the rest of the hotel, it almost seems ultra-modern. Guess OSHA came through recently. A COOK stands over a pot of stew. It smells heavenly. However, a draft near the far end of the KITCHEN catches your eye as well. \n 1.Return to the LOBBY 2.Talk to COOK 3.Investigate draft')
        
    elif location == 2:
        if point2:
            meter += 1
            mmm(meter)
            point2 = False
        location = 4
        canvas.itemconfig(img, image = photos[4])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"This hotel was established over a hundred years ago. It has been a top attraction for those looking for an elegant, yet rustic hotel experience. With a history as old as ours, there is bound to be some talk of ghosts! Just urban legends of course, hoho." \n Press any button to go back')
        
    elif location == 3:
        location = 2
        canvas.itemconfig(img, image = photos[2])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello, I am the concierge," he says. "Welcome to the Overlooked Hotel." \n 1.Return to LOBBY 2.Ask about ROOM 101 3.Ask about hotel')  
        
    elif location == 4:
        location = 2
        canvas.itemconfig(img, image = photos[2])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello, I am the concierge," he says. "Welcome to the Overlooked Hotel." \n 1.Return to LOBBY 2.Ask about ROOM 101 3.Ask about hotel')
        
    elif location == 5:
        location = 21
        canvas.itemconfig(img, image = photos[21])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter ROOM 102. It is the most ornate room you have encountered thus far. A short, stocky man is trying to clean on top of a shelf, but cannot reach. Large double doors lead deeper into the hotel.  \n 1.Go back to HALLWAY 2.Talk to BUTLER 3.Enter BALLROOM')
    
    elif location == 6:
        location = 6
        canvas.itemconfig(img, image = photos[6])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Here it is, the scene of the crime. A camera flashes in the BATHROOM. DETECTIVE Brawnsfeld must be inside. \n 1.Go back to HALLWAY 2.Enter BATHROOM 3.---')
    
    elif location == 7:
        location = 10
        canvas.itemconfig(img, image = photos[10])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello there!" a voice booms. Your old pal from the station stands confidently in the roomy restroom. "This is a shame, it sure is," he says sullenly. "But now that we are on the job, this killer will be brought to justice, eh?" \n 1.Go back to BATHROOM 2.Ask about SUSPECTS 3.Ask about VICTIM')
    
    elif location == 8:
        location = 8
        canvas.itemconfig(img, image = photos[8])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The BODY is horribly mutilated; she is almost unrecognizable as the young, rich socialite this woman once was. \n 1.Go back to BATHROOM 2.Search BODY 3.---')
    
    elif location == 9:
        location = 8
        canvas.itemconfig(img, image = photos[8])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The BODY is horribly mutilated; she is almost unrecognizable as the young, rich socialite this woman once was. \n 1.Go back to BATHROOM 2.Search BODY 3.---')
    
    elif location == 10:
        if point9:
            meter += 1
            mmm(meter)
            point9 = False
        location = 12
        canvas.itemconfig(img, image = photos[12])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The VICTIM is Lady Evelynn, heiress to the hotel fortune. When her father, the OWNER, retired the fortune was made out in her name and he lost access to it. We believe the motive was to gain access to the vault in the hotel that contains the fortune. She appears to have been bludgeoned to death with some sort of blunt object, perhaps a CROWBAR? \n Press any button to go back')
    
    elif location == 11:
        location = 10
        canvas.itemconfig(img, image = photos[10])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello there!" a voice booms. Your old pal from the station stands confidently in the roomy restroom. "This is a shame, it sure is," he says sullenly. "But now that we are on the job, this killer will be brought to justice, eh?" \n 1.Go back to BATHROOM 2.Ask about SUSPECTS 3.Ask about VICTIM')
    
    elif location == 12:
        location = 10
        canvas.itemconfig(img, image = photos[10])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Hello there!" a voice booms. Your old pal from the station stands confidently in the roomy restroom. "This is a shame, it sure is," he says sullenly. "But now that we are on the job, this killer will be brought to justice, eh?" \n 1.Go back to BATHROOM 2.Ask about SUSPECTS 3.Ask about VICTIM')
    
    elif location == 13:
        location = 17
        canvas.itemconfig(img, image = photos[17])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Taking a closer look, you find a secret passage. The COOK does not appear to notice you leave. You slip through the passage and look around. Scary messages are written on the walls, probably by unlucky hotel guests before they got devoured by groundhogs. You should not stay here. \n 1.Return to KITCHEN 2.Grope around in the dark 3.Continue blindly onward')
    
    elif location == 14:
        if point4:
            meter += 1
            mmm(meter)
            point4 = False
        location = 16
        canvas.itemconfig(img, image = photos[16])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"I know honey, it was dreadful! Lady Evelynn murdered in cold blood! It all happened after the dinner party last night. If you ask me, her father seemed awful angry he no longer had access to the fortune. He always was a bitter man... But what do I know, I have just been here baking the whole time! Hehe..." \n Press any button to go back')
    
    elif location == 15:
        location = 14
        canvas.itemconfig(img, image = photos[14])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The COOK turns and greets you with a smile. "Hello there honey!" she grins. "My name is Mama Cass, short for Casserole, and I am the COOK here at the Overlooked Hotel. How ya doin?" \n 1.Return to KITCHEN 2.Ask about MYSTERIOUS STAINS 3.Ask about VICTIM')
    
    elif location == 16:
        location = 14
        canvas.itemconfig(img, image = photos[14])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The COOK turns and greets you with a smile. "Hello there honey!" she grins. "My name is Mama Cass, short for Casserole, and I am the COOK here at the Overlooked Hotel. How ya doin?" \n 1.Return to KITCHEN 2.Ask about MYSTERIOUS STAINS 3.Ask about VICTIM')
    
    elif location == 17:
        location = 19
        canvas.itemconfig(img, image = photos[19])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Emerging from the dark passageway, you enter ROOM 103. The door appears to be locked from the inside, allowing you to get out but no one else to get in. \n 1.Return to PASSAGE 2.Search ROOM 103 3.Enter HALLWAY')      
    
    elif location == 18:
        location = 17
        canvas.itemconfig(img, image = photos[17])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Taking a closer look, you find a secret passage. The COOK does not appear to notice you leave. You slip through the passage and look around. Scary messages are written on the walls, probably by unlucky hotel guests before they got devoured by groundhogs. You should not stay here. \n 1.Return to KITCHEN 2.Grope around in the dark 3.Continue blindly onward')
    
    elif location == 19:
        location = 5 
        canvas.itemconfig(img, image = photos[5])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter the HALLWAY. The door to ROOM 103 slams shut and locks behind you! Two other doors branch off from here. The left and middle are cracked open. \n 1.Go back to LOBBY 2.Enter the left door 3.Enter the middle door') 
    
    elif location == 20:
        location = 19
        canvas.itemconfig(img, image = photos[19])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The door to ROOM 103 appears to be locked from the inside, allowing you to get out but no one else to get in. \n 1.Return to PASSAGE 2.Search ROOM 103 3.Enter HALLWAY')       
    
    elif location == 22:
        if point11:
            meter += 1
            mmm(meter)
            point11 = False
        location = 24
        canvas.itemconfig(img, image = photos[24])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Lady Evelynn was not the kindest soul. She was incredibly rude to me, to everyone here at the hotel. I do not think anyone was sad to see her go. A rich spoiled brat, that was all she amounted to. If only I could have wrung her neck myself! Oops silly me. Sometimes I just get... violent." \n Press any button to go back')                                                      
    
    elif location == 21:
        location = 25
        canvas.itemconfig(img, image = photos[25])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'You enter an elaborate BALLROOM. Against one end of the wall is a very high-tech safe. Pacing in front of it is the OWNER of the hotel. It is recommended you have at least a score of 10 on your MAGICAL MYSTERY METER before preceding to the safe. \n 1.Return to ROOM 102 2.Talk to OWNER 3.Enter SAFE')                                                      
    
    elif location == 23:
        location = 22
        canvas.itemconfig(img, image = photos[22])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh h-hello *nyah*... I am the butler in this establishment. Nobody ever appreciates me though... Say, if you help me clean this top shelf, you can interview me!" the little man says. You say you are legally allowed to interview him regardless of the dust content of the shelf, so long as you respect his constitutional rights. He sighs and resigns himself to your questions. \n 1.Go back to ROOM 102 2.Ask about HOTEL 3.Ask about VICTIM')                                                      
    
    elif location == 24:
        location = 22
        canvas.itemconfig(img, image = photos[22])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh h-hello *nyah*... I am the butler in this establishment. Nobody ever appreciates me though... Say, if you help me clean this top shelf, you can interview me!" the little man says. You say you are legally allowed to interview him regardless of the dust content of the shelf, so long as you respect his constitutional rights. He sighs and resigns himself to your questions. \n 1.Go back to ROOM 102 2.Ask about HOTEL 3.Ask about VICTIM')                                                      
    
    elif location == 25:
         location = 29
         canvas.itemconfig(img, image = photos[29])
         textbox.delete('1.0', END)
         textbox.insert('1.0', 'You have chosen to finish the story. The SAFE door swings open, revealing a marvelous pile of moo-lah! The comotion draws everyone into the BALLROOM. The OWNER is hopping mad. It is time to finish this. \n 1.STEAL THE TREASURE 2.ACCUSE A SUSPECT 3.---')
               
    elif location == 26:
        if point13:
            meter += 1
            mmm(meter)
            point13 = False
        location = 28
        canvas.itemconfig(img, image = photos[28])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"The Overlooked is indeed one of the most overlooked tourist destinations this side of the Rockies. A nice, log cabin feel complete with rustic atmosphere, this HOTEL is my pride and joy. Nothing can take it from me. \n Press any button to go back')                              
    
    elif location == 27:
        location = 26
        canvas.itemconfig(img, image = photos[26])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh thank heavens you have arrived. I am absolutely beside myself with worry and grief! My own daughter, shoved off this mortal coil! And with her dies the only hope of getting into this SAFE! Woe is me, whatever will I, Baron von Trumpo III, do?" \n 1.Go back to BALLROOM 2.Ask about SAFE 3.Ask about HOTEL')                              
   
    elif location == 28:
        location = 26
        canvas.itemconfig(img, image = photos[26])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Oh thank heavens you have arrived. I am absolutely beside myself with worry and grief! My own daughter, shoved off this mortal coil! And with her dies the only hope of getting into this SAFE! Woe is me, whatever will I, Baron von Trumpo III, do?" \n 1.Go back to BALLROOM 2.Ask about SAFE 3.Ask about HOTEL')                                                                                                                        
    
    elif location == 29:
         location = 29
         canvas.itemconfig(img, image = photos[29])
         textbox.delete('1.0', END)
         textbox.insert('1.0', 'You have chosen to finish the story. The SAFE door swings open, revealing a marvelous pile of moo-lah! The comotion draws everyone into the BALLROOM. The OWNER is hopping mad. It is time to finish this. \n 1.STEAL THE TREASURE 2.ACCUSE A SUSPECT 3.---')
        
    elif location == 30:
        location = 98
        canvas.itemconfig(img, image = photos[33])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Channeling your inner Bruce Willis, you flee into the vents of the Overlooked Hotel. The OWNER seems to be thrusting a butter knife through the vents with very poor accuracy. You deftly avoid his stabs and escape into the wilderness. Aruba, Jamaica, here you come! Press any button to continue.')
    
    elif location == 34:
        location = 35
        canvas.itemconfig(img, image = photos[38])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'Your brow furrows in even deeper thought. \n 1.BACK 2.OWNER 3.CONCIERGE')
   
    elif location == 35:
        location = 98
        canvas.itemconfig(img, image = photos[40])
        textbox.delete('1.0', END)
        textbox.insert('1.0', '"Only one person could have commited this dastardly crime," you say. "And that person is YOU! The only person to be wearing blue shoes! An order form for new blue suede was found in this incriminating evidence!" "I do not think that is conclusive," Brawnsfeld mumbles. The CONCIERGE yelps. "I admit it! I wanted the money! I used my position to not get caught!" The killer has been found. You win! \n Press any button to continue')
    
    elif location == 98:
        location = 666
        photonumber = len(photos)-1
        canvas.itemconfig(img, image = photos[photonumber])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The End. \n 1.RESTART 2.--- 3.QUIT')
                
    elif location == 666:
        root.destroy()
    
    else:
        location = 666
        photonumber = len(photos)-1
        canvas.itemconfig(img, image = photos[photonumber])
        textbox.delete('1.0', END)
        textbox.insert('1.0', 'The End. \n 1.RESTART 2.--- 3.QUIT')

def mmm(meter):
    meterbox.delete('1.0', END)
    meterbox.insert('1.0', 'MAGICAL MYSTERY METER: '+str(meter))
    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    if location == 100:
        restart_program()

canvas = Canvas(root, width = 400, height = 400)
canvas.grid(row = 0, column = 0, columnspan = 3)

photo = PhotoImage(file = "C:/Users/Mrisk/Desktop/Adventure/start.gif")
img = canvas.create_image(200,200, image = photo)

b1 = Button(root, text="Choice 1", command=button1)
b1.grid(row = 1, column =0)

b2 = Button(root, text="Choice 2", command=button2)
b2.grid(row = 1, column =1)

b3 = Button(root, text="Choice 3", command=button3)
b3.grid(row = 1, column =2)

textbox = Text(root, width = 100, height = 6)
textbox.insert('1.0', 'Hello! You have been called to solve a deadly murder at an upscale hotel in the woods. Press any button to go inside.')
textbox.grid(row = 3, column = 0, columnspan = 3)

meterbox = Text(root, width = 25, height = 1)
meterbox.insert('1.0', 'MAGICAL MYSTERY METER: '+str(meter))
meterbox.grid(row = 7, column = 0, columnspan = 3)

root.mainloop()