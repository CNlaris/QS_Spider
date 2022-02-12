import time

import requests
from selenium.webdriver.common.by import By
from lxml import etree

from Get_Funding_Time import get_Funding_Time
from Get_Website import get_Website
from WriteToCSV import write_to_csv


# 爬取QS
def get_QS_Ranking(driver, path):
    print("正在爬取QS榜单数据")
    driver.get('https://www.qschina.cn/university-rankings/world-university-rankings/2022')
    time.sleep(15)
    use_cookie = driver.find_element(By.XPATH, '//*[@id="popup-buttons"]/button[2]')
    use_cookie.click()
    time.sleep(1)
    option4 = driver.find_element(By.XPATH,
                                  '//*[@id="dd-lang-switch"]')
    option4.click()
    option5 = driver.find_element(By.XPATH,
                                  '//*[@id="page"]/header/div[1]/div/div[2]/ul/li[1]/div/div/div/div/div/div/a')
    option5.click()
    time.sleep(5)
    option1 = driver.find_element(By.XPATH, '//*[@id="qs-rankings-datatables"]/div[1]/ul/li[2]/a')
    option1.click()
    driver.execute_script("window.scrollTo(0,3600);")
    time.sleep(10)
    option2 = driver.find_element(By.XPATH, '//*[@id="qs-rankings-indicators_length"]/label/span[2]')

    option2.click()
    # 定位‘All’元素
    option3 = driver.find_element(By.XPATH,
                                  '//*[@id="qs-rankings-indicators_length"]/label/span[2]/div/div/span/span/ul/li[5]')
    # 模拟鼠标点击，点击 ‘All’
    option3.click()
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    html = etree.HTML(driver.page_source)
    for i in range(1, 1300):
        href_path = '//*[@id="qs-rankings-indicators_wrapper"]/div[2]/div[3]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[2]/div/div/a/@href '
        school_path = '//*[@id="qs-rankings-indicators_wrapper"]/div[2]/div[3]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[2]/div/div/a/text() '
        rank_path = '//*[@id="qs-rankings-indicators_wrapper"]/div[2]/div[3]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[1]/text() '
        location_path = '//*[@id="qs-rankings-indicators_wrapper"]/div[2]/div[3]/div[2]/div/table/tbody/tr[' + str(
            i) + ']/td[2]/div/div/div/text() '
        href_list = html.xpath(href_path)
        school_list = html.xpath(school_path)
        rank_list = html.xpath(rank_path)
        location_list = html.xpath(location_path)
        academic_reputation_list = html.xpath(
            '//*[@id="qs-rankings-indicators"]/tbody/tr[' + str(i) + ']/td[8]/div/div/text()')
        employer_reputation_list = html.xpath(
            '//*[@id="qs-rankings-indicators"]/tbody/tr[' + str(i) + ']/td[9]/div/div/text()')
        faculty_student_ratio_list = html.xpath(
            '//*[@id="qs-rankings-indicators"]/tbody/tr[' + str(i) + ']/td[6]/div/div/text()')
        citations_per_faculty_list = html.xpath(
            '//*[@id="qs-rankings-indicators"]/tbody/tr[' + str(i) + ']/td[7]/div/div/text()')
        international_faculty_ratio_list = html.xpath(
            '//*[@id="qs-rankings-indicators"]/tbody/tr[' + str(i) + ']/td[5]/div/div/text()')
        international_students_ratio_list = html.xpath(
            '//*[@id="qs-rankings-indicators"]/tbody/tr[' + str(i) + ']/td[4]/div/div/text()')
        academic_reputation = clean_List_Data(academic_reputation_list)
        employer_reputation = clean_List_Data(employer_reputation_list)
        faculty_student_ratio = clean_List_Data(faculty_student_ratio_list)
        citations_per_faculty = clean_List_Data(citations_per_faculty_list)
        international_faculty_ratio = clean_List_Data(international_faculty_ratio_list)
        international_students_ratio = clean_List_Data(international_students_ratio_list)
        if len(href_list) > 0:
            href = href_list[0]
        else:
            href = "null"
        if len(school_list) > 0:
            school = school_list[0]
        else:
            school = "null"
        if len(rank_list) > 0:
            rank = rank_list[0]
        else:
            rank = "null"
        if len(location_list) > 0:
            location = location_list[0]
        else:
            location = "null"
        if href != "null":
            url = "https://www.qschina.cn" + href

            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
            href_html1 = requests.get(url=url, headers=headers)
            href_html1.encoding = 'utf-8'
            href_html1.close()
            href_html = etree.HTML(href_html1.text)

            '''driver.get(url)
            href_html = etree.HTML(driver.page_source)'''

            university_nature_list = href_html.xpath(
                '//*[@id="block-tu-d8-content"]/div/article/div/div[1]/div/div[2]/div/div/div/ul/li[2]/span/b/text()')
            student_number_list = href_html.xpath(
                '//*[@id="block-tu-d8-content"]/div/article/div/div[1]/div/div[2]/div/div/div/ul/li[4]/span/b/text()')
            research_results_list = href_html.xpath(
                '//*[@id="block-tu-d8-content"]/div/article/div/div[1]/div/div[2]/div/div/div/ul/li[3]/span/b/text()')

            if len(university_nature_list) > 0:
                university_nature = university_nature_list[0]
            else:
                university_nature = "null"

            if len(student_number_list) > 0:
                student_number = student_number_list[0]
            else:
                student_number = "null"

            if len(research_results_list) > 0:
                research_results = research_results_list[0]
            else:
                research_results = "null"
            funding_time = ' '
            website = ' '
            funding_time = get_Funding_Time(school)
            website = get_Website(school)
        print("QS第" + str(
            i) + "所 " + school + " " + rank + " " + location + " " + university_nature + " " + research_results + " " + student_number)
        print(
            academic_reputation + " " + employer_reputation + " " + faculty_student_ratio + " " + citations_per_faculty + " " + international_faculty_ratio + " " + international_students_ratio
            + " " + funding_time + " " + website)
        row_list = []
        row_list.append(rank)
        row_list.append(school)
        row_list.append(location)
        row_list.append("QS")
        row_list.append(university_nature)
        row_list.append(research_results)
        row_list.append(student_number)
        row_list.append(academic_reputation)
        row_list.append(employer_reputation)
        row_list.append(faculty_student_ratio)
        row_list.append(citations_per_faculty)
        row_list.append(international_faculty_ratio)
        row_list.append(international_students_ratio)
        row_list.append(funding_time)
        row_list.append(website)
        write_to_csv(row_list, path)
        time.sleep(10)


def clean_List_Data(list):
    if len(list) > 0:
        return list[0]
    else:
        return "-"
