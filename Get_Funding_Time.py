import requests
from lxml import etree

#获取学校创建时间
def get_Funding_Time(school):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    url = 'https://zh.wiki.hancel.org/wiki/' + school
    html = requests.get(url=url, headers=headers)
    html.encoding = 'utf-8'
    html.close()
    html = etree.HTML(html.text)
    value = "未找到"
    for i in [1, 2]:
        tbody_list = html.xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[' + str(i) + ']/tbody/tr')
        for tr in tbody_list:
            key_path = 'th/text()'
            key_list = tr.xpath(key_path)
            if len(key_list) > 0:
                key = key_list[0]
            else:
                key = "null"
            if key == "创办时间":
                value_path = 'td/text()'
                value_list = tr.xpath(value_path)
                if len(value_list) > 0:
                    value = value_list[0]
                else:
                    value_path = 'td/span/text()'
                    value_list = tr.xpath(value_path)
                    if len(value_list) > 0:
                        value = value_list[0]
                    else:
                        value = "null"
    return value



