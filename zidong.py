import requests
import re
from lxml import etree
import csv
import random
sadass = 666
sadasd = 0
asd = []
for i in range(29):
    intss = random.randint(19,25)
    sadasd += intss
    asd.append(sadasd)
asd.append(sadass)
id = []
with open('fen/' +  '9999999999.csv', 'w', newline='')as files:
    f_csvs = csv.writer(files)
    f_csvs.writerow(
        ['v_sku', 'v_nickname', 'v_rating', 'v_content', 'v_status', 'v_date_added'])
for iss in range(1,4):
    link = 'https://www.jvipshop.site/mj38lw-titan/product_ordered.php?page=%s' % iss

    headers = {
        'cookie':'PHPSESSID=4rsch94i48du0krqvtkor44j55qapeeo'
    }
    link_post = requests.get(url=link,headers=headers,verify=False).text

    sad = etree.HTML(link_post)
    sads = sad.xpath('/html/body/div/div/div[2]/div/table/tbody/tr//td[2]/text()')
    for i in sads:
        id.append(i)
with open(r"C:\Users\Admin\Desktop\1111111.csv","r") as f:
    reader = csv.reader(f)
    for row_id,row in enumerate(reader):
        if not row_id == 0:
            if row_id <= asd[0]:
                row[0] = id [0]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[1]:
                row[0] = id [1]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[2]:
                row[0] = id [2]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[3]:
                row[0] = id [3]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[4]:
                row[0] = id [4]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[5]:
                row[0] = id [5]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[6]:
                row[0] = id [6]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[7]:
                row[0] = id [7]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[8]:
                row[0] = id [8]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[9]:
                row[0] = id [9]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[10]:
                row[0] = id [10]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[11]:
                row[0] = id [11]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[12]:
                row[0] = id [12]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[13]:
                row[0] = id [13]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[14]:
                row[0] = id [14]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[15]:
                row[0] = id [15]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[16]:
                row[0] = id [16]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[17]:
                row[0] = id [17]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[18]:
                row[0] = id [18]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[19]:
                row[0] = id [19]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[20]:
                row[0] = id [20]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[21]:
                row[0] = id [21]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[22]:
                row[0] = id [22]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[23]:
                row[0] = id [23]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[24]:
                row[0] = id [24]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[25]:
                row[0] = id [25]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[26]:
                row[0] = id [26]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[27]:
                row[0] = id [27]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[28]:
                row[0] = id [28]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
            elif row_id <= asd[29]:
                row[0] = id [29]
                with open('fen/' + '9999999999.csv', 'a+', newline='')as files:
                    f_csvs = csv.writer(files)
                    f_csvs.writerow(row)
        else:
            print(row)


print(asd)
print(id)