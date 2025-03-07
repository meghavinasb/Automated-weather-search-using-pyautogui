import pyautogui as p
import time as t

# Using prompt for user input
a = p.prompt("Which metropolitan city/city/town/village weather do you want to find out?")
b = p.prompt("Which state is the metropolitan city/city/town/village present at?")
Temp = p.confirm("Do you want the temperature value in Celsius or Fahrenheit?", buttons=['Celsius', 'Fahrenheit'])

# Pressing windows search bar and typing 'chrome' to search for Chrome App
p.press('win')
t.sleep(2)
p.typewrite('weather')
t.sleep(2)
p.press('enter')
t.sleep(2)

# Clicking the search bar in weather app
x = 1664
y = 65
p.click(x, y)
p.typewrite(a + ' ' + b)
t.sleep(2)

# Coordinates to click on search 
z = 1899
q = 55
p.click(z,q)

# Adding a delay to let the page load fully 
t.sleep(2)

# Clicking the Temperature button
r = 1731
s = 100
p.click(r, s)
t.sleep(2)


# Clicking on the temperature unit based on user choice
if Temp == 'Celsius':
    p.click(1588, 200)  # Coordinates to click on Celsius option
elif Temp == 'Fahrenheit':
    p.click(1477, 203)  # Coordinates to click on Fahrenheit option
else:
    print("Invalid choice!")
