import time

import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

openai.api_key = open('env', 'r').read()

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input("Hello I am EvadeGPT, how can I help you today?")}
    ]
)

response = completion.choices[0].message['content']
print(response)

# Open browser and navigate to zerogpt.com
driver = webdriver.Edge()
driver.get("https://zerogpt.com")

# Give time for Edge to finish loading
driver.implicitly_wait(10)

# Find the text area and dump the OpenAI response
text_area = driver.find_element(by=By.ID, value="textArea")
text_area.send_keys(response)
text_area.send_keys(Keys.RETURN)

# Click the button with class "scoreButton"
score_button = driver.find_element(by=By.CLASS_NAME, value="scoreButton")
score_button.click()

time.sleep(100)