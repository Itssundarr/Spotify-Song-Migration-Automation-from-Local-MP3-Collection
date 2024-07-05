# Spotify Song Migration Automation from Local MP3 Collection

This project automates the process of migrating your old MP3 song collection to Spotify. It leverages Selenium WebDriver to search for each song on Spotify and assists in adding them to your liked songs.

## Features

- Automated login to Spotify.
- Searches for songs listed in a specified directory.
- Allows manual addition of songs to liked songs on Spotify.
- Deletes songs from the directory after they have been processed to avoid redundancy.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/Itssundarr/Spotify-Song-Migration-Automation-from-Local-MP3-Collection
    cd Spotify-Song-Migration-Automation-from-Local-MP3-Collection
    ```

2. **Install the required Python packages**:

    ```sh
    pip install selenium
    ```

3. **Download ChromeDriver**:

    - Download the ChromeDriver executable from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the `chromedriver.exe` file in an accessible location and update the `executable_path` in the script.

## Usage

1. **Update the script with your credentials**:
   
    Ensure that the script prompts for your Spotify username and password:

    ```python
    username = input("Enter your Spotify registered mail id : ")
    password = input("Enter your password : ")
    ```

2. **Specify the path to your ChromeDriver**:

    Update the `executable_path` with the location of your `chromedriver.exe`:

    ```python
    service = Service(executable_path="C:\\path\\to\\chromedriver.exe")
    ```

3. **Specify the path to your songs directory**:

    Update the script with the path to the directory containing your songs:

    ```python
    for song in os.listdir("C:\\car\\Latest Songs"):
    ```

4. **Run the script**:

    ```sh
    python spotify_automation.py
    ```

## How it Works

1. **Login to Spotify**: The script launches a Chrome browser using Selenium WebDriver, navigates to the Spotify login page, and enters your credentials.

2. **Navigate to the Spotify Web Player**: After logging in, the script navigates to the Spotify web player.

3. **Search and Process Songs**: The script iterates through the songs in the specified directory:
    - It reads the name of each song and searches for it on Spotify.
    - It waits for 5 seconds to allow you to manually click the "Add to liked songs" button on Spotify.
    - After 5 seconds, the song is removed from the directory to prevent it from being processed again if the script is restarted.

4. **Repeat Until Completion**: This process continues until all songs in the directory have been processed.

## Important Notes

- **Manual Intervention**: The script waits for 5 seconds after pasting the song name into the search bar, during which you need to manually add the song to your liked songs on Spotify.
- **Security**: Ensure that you handle your credentials securely. Avoid hardcoding them in the script.
- **Compatibility**: This script is compatible with the latest version of ChromeDriver and the corresponding version of Google Chrome.
- **Stopping and Restarting**: If you stop the script and restart it, it will only process the remaining songs in the directory, as processed songs are deleted.
