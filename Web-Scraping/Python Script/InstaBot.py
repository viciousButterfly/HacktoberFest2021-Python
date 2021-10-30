# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Webscraping Instagram with Selenium
# 
# ## Imports

# %%
#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# %%
#Other imports here
import os
import wget
import time

# %% [markdown]
# ## Download Chrome Driver
# 
# From: https://chromedriver.chromium.org/
# <br>
# And save in a location on your computer
# %% [markdown]
# ## Log In to Your Instagram Account

# %%
#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Firefox(executable_path="C:\webdrivers\geckodriver.exe")

#open the webpage
driver.get("http://www.instagram.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("altreemedia")
password.clear()
password.send_keys("052002")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!

# %% [markdown]
# ## Handle Alerts
# you might only get a single alert, or you might get 2 of them
# please adjust the cell below accordingly

# %%
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# %% [markdown]
# 
# ## Search for a certain hashtag

# %%
#target the search input field
time.sleep(5)
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#search for the hashtag cat
keyword = "#eid"
searchbox.send_keys(keyword)
 
#FIXING THE DOUBLE ENTER
time.sleep(5) # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

# %% [markdown]
# ## Scroll Down
# 
# Increase n_scrolls to select more photos (depending on screen resolution)  
# **Example:**
# 
# - 2 scrolls cover approx. 35 photos
# - 3 scrolls cover approx. 45 photos

# %%
#scroll down 2 times
#increase the range to scroll more
n_scrolls = 2
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)


# %%
#target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
#narrow down all links to image links only
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

print('Found ' + str(len(anchors)) + ' links to images')
anchors[:5]


# %%
images = []

#follow each image link and extract only image at index=1
for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])
    
images[:5]

# %% [markdown]
# 
# ## Save images to computer
# First we'll create a new folder for our images somewhere on our computer.  
# Then, we'll save all the images there.

# %%
# import os
# import wget
path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

#create the directory
os.mkdir(path)

path


# %%
#download images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
