
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_sec(time_str):
    """Get seconds from time."""
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)

#create an empty dictionary
task_dict = { "Drawing 1/6" : 20, "Drawing 2/6" : 20, "Drawing 3/6" : 20, "Drawing 4/6" : 20, "Drawing 5/6" : 20, "Drawing 6/6" : 20}


driver = webdriver.Firefox()
driver.get('https://quickdraw.withgoogle.com/');


# click the "Lets Start" button to start the game

startbutton = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID, "button-play")))
startbutton.click()
time.sleep(2)
print("Begining Quick Draw")


isGameOn = True
while isGameOn :
  # Get the current drawing eg. Drawing 1/6
  drawing_div = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID, "challengetext-level")))
  print("Current Drawing: " + drawing_div.text)
  curr_drawing_text = drawing_div.text
  
  
  
  # Waiting to click the "Got It !" button to start the drawing
  drawing_round_button = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID, "button-newround-play")))
  print("Waiting for user to start " + curr_drawing_text)
  
  while drawing_round_button.is_displayed() :
    pass
  
  print(curr_drawing_text +  " is started")
  
  
  # Waiting until a new Drawing appears or game is ended ( checking by seeing playagainbutton)

  while True:
    if drawing_div.is_displayed() :
       break
    elif WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID, "button-timesup-play"))).is_displayed():
       isGameOn = False
       break
    
   
  # Fetch the remaining time 
  timeleft_div = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID, "clock-time")))
  timeleft = get_sec(timeleft_div.text)
  
  timeconsumed = 20 - timeleft
  #print("Time left: " + str(timeleft))
  #print("User completed " + curr_drawing_text + " in: " + str(timeconsumed))
  print(curr_drawing_text + " is finished or timed out in " + str(timeconsumed))
  
  # Update the dictionary with time consumed
  task_dict[curr_drawing_text] = timeconsumed
  

print("All Drawings recorded time")
print(task_dict)

