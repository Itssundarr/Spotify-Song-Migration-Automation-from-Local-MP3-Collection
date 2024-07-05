from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

print("##############################################")
print("#                                            #")
print("#     Spotify MP3 Song Migration Automation  #")
print("#                                            #")
print("##############################################\n")

print("Welcome to the Spotify MP3 Song Migration Automation!")
print("This tool will help you migrate your MP3 collection to Spotify by automating the search and add process.\n")

username = input("Enter your Spotify registered mail id: ")
password = input("Enter your password: ")

print("\nInitializing the browser and logging into Spotify...\n")

service = Service(executable_path="C:\\SUNDAR\\vs-code\\Python\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://accounts.spotify.com/en/login")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "login-username"))
)
driver.find_element(By.ID, "login-username").send_keys(username)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "login-password"))
)
driver.find_element(By.ID, "login-password").send_keys(password)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "login-button"))
)
driver.find_element(By.ID, "login-button").click()

print("Successfully logged into Spotify!\n")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="web-player-link"]'))
)
driver.find_element(By.CSS_SELECTOR, '[data-testid="web-player-link"]').click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

print("Navigating to Spotify web player...\n")

song_directory = "C:\\car\\Latest Songs"
songs = os.listdir(song_directory)

print(f"Found {len(songs)} songs in the directory '{song_directory}' to process.\n")

for song in songs:
    driver.get("https://open.spotify.com/search")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="search-input"]'))
    )
    driver.find_element(By.CSS_SELECTOR, '[data-testid="search-input"]').send_keys(song)
    
    print(f"Processing song: {song}")
    time.sleep(5)
    
    song_path = os.path.join(song_directory, song)
    if os.path.exists(song_path):
        os.remove(song_path)

print("All songs have been processed and added to your Spotify liked songs (if you clicked 'like' during the 5-second window).\n")
print("Thank you for using the Spotify MP3 Song Migration Automation tool!")

time.sleep(20000)
driver.quit()
