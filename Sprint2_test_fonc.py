# Import the webdriver and keys classes from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Create a new Chrome browser instance
browser = webdriver.Chrome(executable_path="chromedriver.exe")

# Go to the given site
browser.get("https://boussairi-projet-agile-disease-predictions-mdps-public-s-0gga24.streamlit.app")
browser.maximize_window()

# Find all the input elements on the page
time.sleep(5)

iframe1 = browser.find_element(By.TAG_NAME,"iframe")
browser.switch_to.frame(iframe1)

menu = browser.find_element(By.XPATH,"//*[@id='root']/div[1]/div/div/div/div/section[1]/div[1]/div[2]")

user_test_inputs = [['6','148','72','35','0','50','0.627','36'],
                    ['63','145','0','2.3','1','1','233','150','0','3','1','0','0'],
                    ['119.99200','0.00370','0.02182','21.03300','2.301442','157.30200',
                     '0.00554','0.03130','0.414783','0.284654','74.99700','0.01109',
                     '0.02182','0.815285','0.00784','0.42600','0.06545','-4.813031',
                     '0.00007','0.42600','0.02211','0.266482']]
deseases =  ["Diabetes","Heart disease","Parkinson"]
deseases_results = ["The person is diabetic","The person is having heart disease","The person does not have Parkinson's disease"]

iframe_options = menu.find_element(By.TAG_NAME,'iframe')
browser.switch_to.frame(iframe_options)
time.sleep(3)
list_menu = browser.find_element(By.TAG_NAME,"ul")

for  index,disease in enumerate(list_menu.find_elements(By.TAG_NAME,'li')) : 
    link = disease.find_element(By.TAG_NAME,'a')
    link.click()
    time.sleep(5)
    try : 
       browser.switch_to.parent_frame()
    # browser.switch_to.default_content()
      #  time.sleep(4)
    #    browser.switch_to.frame(iframe1)
    except : print("Error trying to switch to the broadest frame")
    
    divs = browser.find_elements(By.CSS_SELECTOR, "div[data-baseweb='base-input']")
    for ind ,div in enumerate(divs) : 
        input = div.find_element(By.TAG_NAME,"input") 
        input.send_keys(user_test_inputs[index][ind])
        browser.implicitly_wait(5) 
    
    validate = browser.find_element(By.XPATH,"//*[@id='root']/div[1]/div/div/div/div/section[2]/div/div[1]/div[3]/div/button")
    time.sleep(5)
    validate.click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    result = browser.find_element(By.CSS_SELECTOR,"div[role='alert']")
    par = result.find_element(By.TAG_NAME,"p")
    time.sleep(3)
    model_result = par.get_attribute("innerHTML")
    #  print(model_result)
   
    if model_result == deseases_results[index] : 
        print(f"Test of {deseases[index]} Model Passed Successfully!!\n")
    else : 
        print(f"Test of {deseases[index]} Model has failed, please check your code!!\n")
   
    
   # iframe_options = menu.find_element(By.TAG_NAME,'iframe')
    browser.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)
    try : 
        browser.switch_to.frame(iframe_options)
    except : print("Error trying to switch to the menu frame")
    