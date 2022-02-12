import csv

#初始化csv文件
def init_csv(path):
    headers=[['Ranking','University Name','Country','Source','Private/Public university','Focus','No of students'
                 ,'Academic Reputation','Employer Reputation','Faculty Student Ratio','Citations Per Faculty'
                 ,'International Faculty Radio','International Students Radio']]

    with open(path, 'w', encoding="utf-8-sig") as f:
        f_csv = csv.writer(f)
        f_csv.writerows(headers)

#向csv文件中写入
def write_to_csv(row_list, path):
    rows=[

    ]
    rows.append(row_list)
    with open(path, 'a', encoding="utf-8-sig") as f:
        f_csv = csv.writer(f)
        f_csv.writerows(rows)
