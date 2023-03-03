import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoBrowserCommands():
    def demo_commands(self):
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            driver.get("https://www.microsoft.com/sr-latn-rs/")
            driver.maximize_window()
            time.sleep(10)
            driver.close()

demo_commands = DemoBrowserCommands()
demo_commands.demo_commands()

