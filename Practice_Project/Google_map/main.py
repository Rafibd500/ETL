import undetected_chromedriver as uc
import time
driver = uc.Chrome(version_main=147)
driver.get('https://www.google.com/maps/@23.8066298,90.3584425,1989m/data=!3m1!1e3?hl=en&entry=ttu')
time.sleep(1)
driver.maximize_window()
inputBox = driver.find_element('xpath', '//input[@class="UGojuc fontBodyMedium EmSKud lpggsf "]')
# inputBox.click()
input_text = 'dentists in New York City, NY, USA'
inputBox.send_keys(input_text)
submit = driver.find_element('xpath', '(//button[@aria-label="Search"])[1]')
submit.click()
time.sleep(2)
i=1
st = set()
while True:
    
    items = driver.find_elements('xpath', '//div[@role="article"]')
    for item in items:
        # print(item.get_attribute('href'))
        name = item.get_attribute('aria-label')
        # print(name)
        st.add(name)
    panel = driver.find_element('xpath', '//div[@role="feed"]')
    driver.execute_script('arguments[0].scrollIntoView(true);', items[-1])
    time.sleep(2)
    # print(item)
    try:
        if(driver.find_element('xpath', '//span[@class="HlvSq"]').text == "You've reached the end of the list."):
            break
    except:
        pass
    # i+=1
print(st)
print(len(st))
time.sleep(500)