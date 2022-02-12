from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from QS_ranking import get_QS_Ranking
from WriteToCSV import init_csv

if __name__ == '__main__':
    path = 'ranking.csv' #保存csv的地址
    option = webdriver.ChromeOptions()
    service = Service(r"chromedriver的文件路径") #必须要改
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    init_csv(path)
    get_QS_Ranking(driver,path)
