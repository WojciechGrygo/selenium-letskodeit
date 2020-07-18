from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.login_page import LoginPage


class LoginTests():

    def test_valid_login(self):
        baseUrl = "https://letskodeit.teachable.com/"
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\grygo\\AppData\\Local\\Google\\Chrome\\UserData\\Default")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        ln = LoginPage(driver)
        ln.login("test@email.com", "abcabc")


        userIcon = driver.find_element(By.XPATH, "//img[@class='gravatar']")

        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        driver.quit()

lt = LoginTests()
lt.test_valid_login()



