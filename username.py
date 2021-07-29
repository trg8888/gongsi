import requests
import re
from chaojiying import Chaojiying_Client
import pandas as pd
import random
from lxml import etree
import pymysql
import csv

def hello(link_nots, qidong):
    connectr = pymysql.connect(
        host='3.143.242.127',
        user='root',
        port=3306,
        password='Tang5230.',
        charset='utf8',
        db='jollychics',
        cursorclass=pymysql.cursors.DictCursor

    )
    cursor = connectr.cursor()
    name = ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
         'e',
         'd', 'c', 'b', 'a'], 7)).upper()
    with open('1/'+name+'.csv', 'w', newline='',encoding='utf-8')as files:
        f_csvs = csv.writer(files)
        f_csvs.writerow(
            ['v_sku', 'v_name', 'v_short_description', 'v_description', 'v_image', 'v_url', 'v_attribute',
             'v_price',
             'v_specials_price', 'v_specials_expire_date', 'v_date_added', 'v_in_stock', 'v_status', 'v_viewed',
             'v_ordered', 'v_category_sku', 'v_sort_order', 'v_meta_title', 'v_meta_keywords', 'v_meta_description',
             'v_brand_filter', 'v_class_filter', 'v_color_filter', 'v_gender_filter', 'v_material_filter',
             'v_year_filter', 'v_origin_filter', 'v_series_filter', 'v_spec_filter'])

    alist = random.sample(range(0, 150), 20)

    sku = 0
    for i in alist:
        user_iamgs = 'Two_piece_suit'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(22, 33)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', 'Size#XS:S:M:L:XL:2XL:3XL:4XL:5XL', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        user_iamgs = 'Skirts'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(22, 33)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', 'Size#XS:S:M:L:XL:2XL:3XL:4XL:5XL', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg.replace("_"," "), '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        user_iamgs = 'Menis_Shorts'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(22, 33)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', 'Size#XS:S:M:L:XL:2XL:3XL:4XL:5XL', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        user_iamgs = 'Menis_Set'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(22, 33)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', 'Size#XS:S:M:L:XL:2XL:3XL:4XL:5XL', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        user_iamgs = 'Womenis_Rings'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(11, 28)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', '', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        user_iamgs = 'Womenis_Hair_Accessories'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(11, 28)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', '', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        user_iamgs = 'Menis_Boots'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(22, 39)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', 'Size#XS:S:M:L:XL:2XL:3XL:4XL:5XL', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        user_iamgs = 'Loafers'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(49, 66)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', 'Shoes Size#EUR35=US5:EUR36=US6:EUR37=US6.5:EUR38=US7.5:EUR39=US8.5:EUR39=US7:EUR40=US7.5:EUR41=US8:EUR42=US8.5:EUR43=US9:EUR44=US10', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        user_iamgs = 'Wallet'
        user_iamg = user_iamgs.replace('_',' ')
        sql = 'SELECT * FROM ' + user_iamgs + ' WHERE ID = %s' % i
        data_count = cursor.execute(sql)
        data = cursor.fetchall()[0]
        with open('1/'+name+'.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            sku += 1
            name_new = name + r'%04d' % sku
            a = random.uniform(49, 66)
            csv_writer.writerow(
                [name_new, data['user_name'], '', data['user_descriptions'],
                 'img/' + user_iamgs + '/' + data['user_iamg'], '', 'Shoes Size#EUR35=US5:EUR36=US6:EUR37=US6.5:EUR38=US7.5:EUR39=US8.5:EUR39=US7:EUR40=US7.5:EUR41=US8:EUR42=US8.5:EUR43=US9:EUR44=US10', round(a, 2),
                 '', '', '', '1', '1', '',
                 '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                 '', '', '', '', '',
                 '', '', '', ''])

    # sdas = [['clothing', 'clothing', '', '', '', '', '', '1', '1', 'clothing', 'clothing', 'clothing'],
    #         ['Shoes', 'Shoes', '', '', '', '', '', '1', '5', 'Shoes', 'Shoes', 'Shoes'],
    #         ['jewelry', 'jewelry', '', '', '', '', '', '1', '5', 'jewelry', 'jewelry', 'jewelry'],
    #         ['Bag', 'Bag', '', '', '', '', '', '1', '5', 'Bag', 'Bag', 'Bag']]
    firstlevel_one = 'clothing'
    firstlevel_two = 'Shoes'
    firstlevel_three = 'jewelry'
    firstlevel_four = 'Bag'
    sdas = [[firstlevel_one, firstlevel_one, '', '', '', '', '', '1', '1', firstlevel_one, firstlevel_one, firstlevel_one],
            [firstlevel_two, firstlevel_two, '', '', '', '', '', '1', '5', firstlevel_two, firstlevel_two, firstlevel_two],
            [firstlevel_three, firstlevel_three, '', '', '', '', '', '1', '5', firstlevel_three, firstlevel_three, firstlevel_three],
            [firstlevel_four, firstlevel_four, '', '', '', '', '', '1', '5', firstlevel_four, firstlevel_four, firstlevel_four]]
    secondaryclassification_one = 'Two_piece_suit'.replace("_", " ")
    secondaryclassification_two = 'Skirts'.replace("_", " ")
    secondaryclassification_three = 'Menis_Shorts'.replace("_", " ")
    secondaryclassification_four = 'Menis_Set'.replace("_", " ")
    secondaryclassification_fives = 'Menis_Boots'.replace("_", " ")
    secondaryclassification_six = 'Loafers'.replace("_", " ")
    secondaryclassification_seven = 'Womenis_Rings'.replace("_", " ")
    secondaryclassification_eight = 'Womenis_Hair_Accessories'.replace("_"," ")
    secondaryclassification_nine = 'Wallet'.replace("_", " ")
    sdass = [[secondaryclassification_one, secondaryclassification_one, '', '', '', firstlevel_one, '', '1', '5', secondaryclassification_one, secondaryclassification_one, secondaryclassification_one],
             [secondaryclassification_two, secondaryclassification_two, '', '', '', firstlevel_one, '', '1', '5', secondaryclassification_two, secondaryclassification_two,
              secondaryclassification_two],
             [secondaryclassification_three, secondaryclassification_three, '', '', '', firstlevel_one, '', '1', '5', secondaryclassification_three, secondaryclassification_three,
              secondaryclassification_three],
             [secondaryclassification_four, secondaryclassification_four, '', '', '', firstlevel_one, '', '1', '5', secondaryclassification_four, secondaryclassification_four, secondaryclassification_four],
             [secondaryclassification_fives, secondaryclassification_fives, '', '', '', firstlevel_two, '', '1', '5',
              secondaryclassification_fives, secondaryclassification_fives, secondaryclassification_fives],
             [secondaryclassification_six, secondaryclassification_six, '', '', '', firstlevel_two, '', '1', '5', secondaryclassification_six, secondaryclassification_six,
              secondaryclassification_six],
             [secondaryclassification_seven, secondaryclassification_seven, '', '', '', firstlevel_three, '', '1', '5', secondaryclassification_seven, secondaryclassification_seven,
              secondaryclassification_seven],
             [secondaryclassification_eight, secondaryclassification_eight, '', '', '', firstlevel_three, '', '1', '5',
              secondaryclassification_eight, secondaryclassification_eight, secondaryclassification_eight],
             [secondaryclassification_nine, secondaryclassification_nine, '', '', '', firstlevel_four, '', '1',
              '5',
              secondaryclassification_nine, secondaryclassification_nine, secondaryclassification_nine]]
    sli = random.sample(sdas, 4)
    slis = random.sample(sdass, 9)
    print('写入文件成功')
    with open('1/'+name+'fen.csv', 'w', newline='',encoding='utf-8')as files:
        f_csvs = csv.writer(files)
        f_csvs.writerow(
            ['v_sku', 'v_name', 'v_description', 'v_image', 'v_url', 'v_parent_sku', 'v_date_added', 'v_status',
             'v_sort_order', 'v_meta_title', 'v_meta_keywords', 'v_meta_description', '', '', '', ''])

    for asdsad, sss in enumerate(sli):
        with open('1/'+name+'fen.csv', 'a+', newline='',encoding='utf-8')as files:
            asdsads = asdsad + 1
            sss[8] = asdsads
            f_csvs = csv.writer(files)
            f_csvs.writerow(sss)
    for asdsad, sss in enumerate(slis):
        with open('1/'+name+'fen.csv', 'a+', newline='',encoding='utf-8')as files:
            asdsads = asdsad + 5
            sss[8] = asdsads
            f_csvs = csv.writer(files)
            f_csvs.writerow(sss)
    ##############################################################
    link_not = link_nots
    #############################################################
    wangzan = re.findall(r'(.*?)/', link_not)
    i = 'https://' + link_not + '/index.php'

    session = requests.session()

    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    response = session.get(i, headers=req_header).text

    responses = re.findall('<img src="(.*?)" oncl', response)[0]
    securityToken = re.findall('<input type="hidden" value="(.*?)" name="securityToken" />', response)[0]
    # print(responses)

    response = session.get(responses, headers=req_header).content
    with open('a.jpg', 'wb')as file:
        file.write(response)

    chaojiying = Chaojiying_Client('trg8888', 'trg8888', '914366')
    im = open('a.jpg', 'rb').read()
    yzm = chaojiying.PostPic(im, 1902)['pic_str']
    # print(yzm)

    link = 'https://' + link_not + '/login.php?action=loginPost'

    data = {
        'securityToken': securityToken,
        'action': 'loginPost',
        'username': 'manager',
        'password': 'WmYEYnPt4CoOAmd7',
        'captcha': yzm
    }
    response = session.post(url=link, data=data, headers=req_header).text

    df = pd.read_excel(r'后台信息\关于我们.xlsx')
    data = df.values
    guanyuzhongxin = data[random.randint(0, 26)][0]

    guanyuzhongxin_link = 'https://' + link_not + '/cms_page.php?action=save'

    guanyuzhongxin_data = {
        'securityToken': securityToken,
        'cms_page[cms_page_id]': '1',
        'cms_page[name]': 'About Us',
        'cms_page[content]': guanyuzhongxin,
        'cms_page[meta_title]': 'About Us',
        'cms_page[meta_keywords]': '',
        'cms_page[meta_description]': '',
        'cms_page[status]': '1',
        'cms_page[sort_order]': '10'
    }

    guanyuzhongxin_post = session.post(url=guanyuzhongxin_link, data=guanyuzhongxin_data, headers=req_header)

    qinchushuju = 'https://www.' + link_nots + '/import_old.php?action=clearProduct'
    qinchushuju_1 = session.get(url=qinchushuju, headers=req_header)

    # =======================================================================================
    shangchuan_1_data = {
        'securityToken': securityToken,
        'MAX_FILE_SIZE': '100000000',
        'action': 'product_option',

    }
    shangchuan_1_files = {
        'usrfl': ('属性.csv', open(r'属性.csv', 'r',encoding='utf-8'), 'application/vnd.ms-excel')
    }
    shangchuan_1 = 'https://www.' + link_nots + '/import_old.php'
    shangchuan_1_post = session.post(url=shangchuan_1, data=shangchuan_1_data, files=shangchuan_1_files)

    shangchuan_2_data = {
        'securityToken': securityToken,
        'MAX_FILE_SIZE': '100000000',
        'action': 'category',

    }
    wocao_1 = '1/'+name+'fen.csv'
    shangchuan_2_files = {
        'usrfl': ('属性.csv', open(wocao_1, 'r',encoding='utf-8'), 'application/vnd.ms-excel')
    }
    shangchuan_2 = 'https://www.' + link_nots + '/import_old.php'
    shangchuan_2_post = session.post(url=shangchuan_2, data=shangchuan_2_data, files=shangchuan_2_files)

    shangchuan_3_data = {
        'securityToken': securityToken,
        'MAX_FILE_SIZE': '100000000',
        'action': 'product',

    }
    shangchuan_3_files = {
        'usrfl': ('1.csv', open('1/'+name+'.csv', 'r',encoding='utf-8'), 'application/vnd.ms-excel')
    }
    shangchuan_3 = 'https://www.' + link_nots + '/import_old.php'
    shangchuan_3_post = session.post(url=shangchuan_3, data=shangchuan_3_data, files=shangchuan_3_files)
    ######图片检测
    for i in range(2):
        shangchu_1 = []
        link_1 = 'https://www.' + link_nots + '/product.php?page=1'
        sad_1 = session.get(link_1, headers=req_header).text
        sadas_1 = etree.HTML(sad_1)
        asdasdas_1 = sadas_1.xpath('//img[@src="images/no_image.jpg"]')
        if asdasdas_1:
            sadsadsad_1 = re.findall('(?s)src="images/no_image.jpg" /></td>.*?<td>\d{1,3}</td>', sad_1)
            # print(sadsadsad_1)
            for i in sadsadsad_1:
                asdasdsadaasdsa_1 = re.findall('<td>(\d{1,})</td>', i)
                for i in asdasdsadaasdsa_1:
                    shangchu_1.append(i)
        sadsads_1 = sadas_1.xpath('//*[@id="productFm"]/div//a[@title="Next"]/@href')
        while sadsads_1:
            sad_1 = session.get(sadsads_1[0], headers=req_header).text
            sadas_1 = etree.HTML(sad_1)
            asdasdas_1 = sadas_1.xpath('//img[@src="images/no_image.jpg"]')
            if asdasdas_1:
                sadsadsad = re.findall('(?s)src="images/no_image.jpg" /></td>.*?<td>\d{1,3}</td>', sad_1)
                for i in sadsadsad:
                    asdasdsadaasdsa = re.findall('<td>(\d{1,})</td>', i)
                    for i in asdasdsadaasdsa:
                        shangchu_1.append(i)
            sadsads_1 = sadas_1.xpath('//*[@id="productFm"]/div//a[@title="Next"]/@href')
            # print(sadsads_1)
            # print(shangchu_1)
        for shang in shangchu_1:
            data_1 = {
                'securityToken': securityToken,
                'selected[]': shang
            }
            ceshiasdsa = session.post(url=link_1 + '&action=delete', headers=req_header, data=data_1)
    # =======================================================================================
    print('开始配置数据')
    df = pd.read_excel(r'后台信息\关于我们.xlsx')
    data = df.values
    yingsianquan = data[random.randint(0, 23)][0]

    yingsianquan_link = 'https://' + link_not + '/cms_page.php?action=save'
    yingsianquan_data = {
        'securityToken': securityToken,
        'cms_page[cms_page_id]': '3',
        'cms_page[name]': 'Privacy & Security',
        'cms_page[content]': yingsianquan,
        'cms_page[meta_title]': 'Privacy & Security',
        'cms_page[meta_keywords]': '',
        'cms_page[meta_description]': '',
        'cms_page[status]': '1',
        'cms_page[sort_order]': '30'
    }
    yingsianquan_post = session.post(url=yingsianquan_link, data=yingsianquan_data, headers=req_header)

    songhuofanshi_link = 'https://' + link_not + '/cms_page.php?action=save'

    df = pd.read_excel(r'后台信息\运输与退货.xlsx', usecols=[0, 1])
    songhuofanshi_shuju = df.values
    songhuofanshi_shuju = songhuofanshi_shuju[random.randint(0, 19)]
    songhuofanshi_shujuone = songhuofanshi_shuju[0]
    songhuofanshi_data = {
        'securityToken': securityToken,
        'cms_page[cms_page_id]': '4',
        'cms_page[name]': 'Shipping & Delivery',
        'cms_page[content]': songhuofanshi_shujuone,
        'cms_page[meta_title]': 'Shipping & Delivery',
        'cms_page[meta_keywords]': '',
        'cms_page[meta_description]': '',
        'cms_page[status]': '1',
        'cms_page[sort_order]': '40'
    }
    songhuofanshi_post = session.post(url=songhuofanshi_link, data=songhuofanshi_data, headers=req_header)

    tuihuo_link = 'https://' + link_not + '/cms_page.php?action=save'
    tuihuo_shuju = songhuofanshi_shuju[1]

    tuihuo_data = {
        'securityToken': securityToken,
        'cms_page[cms_page_id]': '5',
        'cms_page[name]': 'Return Policy',
        'cms_page[content]': tuihuo_shuju,
        'cms_page[meta_title]': 'Return Policy',
        'cms_page[meta_keywords]': '',
        'cms_page[meta_description]': '',
        'cms_page[status]': '1',
        'cms_page[sort_order]': '50'
    }

    Faq_link = 'https://' + link_not + '/cms_page.php?action=save'
    df = pd.read_excel(r'后台信息\常见问题.xlsx')
    data = df.values
    Faq_shuju = data[random.randint(0, 21)][0]
    Faq_data = {
        'securityToken': securityToken,
        'cms_page[cms_page_id]': '7',
        'cms_page[name]': 'Faq',
        'cms_page[content]': Faq_shuju,
        'cms_page[meta_title]': 'Faq',
        'cms_page[meta_keywords]': '',
        'cms_page[meta_description]': '',
        'cms_page[status]': '1',
        'cms_page[sort_order]': '70'
    }

    Faq_post = session.post(url=Faq_link, data=Faq_data, headers=req_header)

    # 先判断他使用了什么模块
    panduan = 'https://' + link_not + '/configuration.php?gID=1'
    panduan_post = session.get(url=panduan, headers=req_header).text
    panduan_one = etree.HTML(panduan_post)
    panduan_new = \
    panduan_one.xpath('/html/body/div/div/div[2]/form/table/tbody/tr[9]/td[2]/select/option[@value!="default"]/text()')
    if not panduan_new:
        print('没有找到一次')
        panduan = 'https://' + link_not + '/configuration.php?gID=1'
        panduan_post = session.get(url=panduan, headers=req_header).text
        panduan_one = etree.HTML(panduan_post)
        panduan_new = \
            panduan_one.xpath(
                '/html/body/div/div/div[2]/form/table/tbody/tr[9]/td[2]/select/option[@value!="default"]/text()')
        if not panduan_new:
            print('二次都没有找到自动退出')
            return 0
    panduan_new = panduan_new[0]
    #

    def ranstr(num):
        # 猜猜变量名为啥叫 H
        H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        salt = ''
        for i in range(num):
            salt += random.choice(H)

        return salt

    def hello(num):
        # 猜猜变量名为啥叫 H
        H = '0123456789'

        salt = ''
        for i in range(num):
            salt += random.choice(H)

        return salt

    salt = ranstr(4)
    sass = hello(3)

    jibenshezhi_link = 'https://' + link_not + '/configuration.php?gID=1&action=save'

    df = pd.read_excel(r'后台信息\标题.xlsx', usecols=[0, 1, 2])
    data = df.values
    jibenshezhi_datas = data[random.randint(0, 62)]
    jibenshezhi_data = {
        'securityToken': securityToken,
        'configuration_group_id': '1',
        'configuration[STORE_NAME]': salt.upper() + sass,
        'configuration[STORE_WEBSITE]': wangzan[0],
        'configuration[STORE_EMAIL]': '',
        'configuration[STORE_TELEPHONE]': '',
        'configuration[STORE_WELCOME]': '',
        'configuration[STORE_CURRENCY]': 'USD',
        'configuration[STORE_COUNTRY]': '234',
        'configuration[STORE_LANGUAGE]': 'en',
        'configuration[STORE_TEMPLATE_DIR]': panduan_new,
        'configuration[STORE_DISABLE_EMAIL]': '@northeastlink.net',
        'configuration[HEAD_DEFAULT_TITLE]': jibenshezhi_datas[0],
        'configuration[HEAD_TITLE_PREFIX]': '',
        'configuration[HEAD_TITLE_SUFFIX]': '',
        'configuration[HEAD_DEFAULT_KEYWORDS]': jibenshezhi_datas[1],
        'configuration[HEAD_DEFAULT_DESCRIPTION]': jibenshezhi_datas[2],
        'configuration[HEADER_LOGO_SRC]': 'logo.png',
        'configuration[HEADER_LOGO_ALT]': 'Logo Alt',
        'configuration[FOOTER_COPYRIGHT]': '©' + wangzan[0] + '. All Rights Reserved.',
        'configuration[FOOTER_ABSOLUTE_FOOTER]': '',
        'configuration[ONLINE_SERVICE]': '',
        'configuration[SHOPPING_CART_MODE]': '0',
        'configuration[POPULAR_SEARCH_KEYWORDS]': '',
        'configuration[POPULAR_SEARCH_LIMIT]': '',
        'configuration[POPULAR_SEARCH_SIDEBAR_LIMIT]': '',
        'configuration[FACEBOOK_ID]': '',
        'configuration[SEND_EMAIL_ACCOUNT]': '',
        'configuration[SEND_EMAIL_PASSWORD]': 'VFa7MncJuGL75muF',
        'configuration[SEND_EMAIL_HOST]': 'smtpdm-ap-southeast-2.aliyun.com',
        'configuration[SEND_EMAIL_PORT]': '465',
        'configuration[OA_API_URL]': 'http://liwenoa.veveveve.com',
        'configuration[OA_API_TOKEN]': 'eYzNKDzDRQbSEh7Y',
        'configuration[OA_API_IP_CHECK_COUNTRY]': '',
        'configuration[OA_API_IP_CHECK_SWITCH]': '1',
        'configuration[OA_API_IP_CHECK_JUMP]': '',
        'configuration[EPAYPAL_API_URL]': 'http://liwenapi.vipsmerchant.com/v1/',
        'configuration[EPAYPAL_API_TOKEN]': 'LogLq39yiSYJUnbR',
        'configuration[EPAYPAL_PAYMENT_MD5KEY]': '55zEcsG9LbdtvmHh',
    }

    jibenshezhi_post = session.post(url=jibenshezhi_link, data=jibenshezhi_data, headers=req_header)

    # -------------------------------------------------------
    liebiao = []
    for i in range(1, 10):
        linksss = 'https://www.' + link_not + '/product.php?page=%s' % i
        sad = session.get(linksss, headers=req_header).text
        sadsadsad = re.findall('(?s)src=".*" /></td>.*?<td>\d{1,3}</td>', sad)
        for isss in sadsadsad:
            asdasdsadaasdsa = re.findall('<td>(\d{1,})</td>', isss)
            for issss in asdasdsadaasdsa:
                liebiao.append(issss)
    ssss = random.sample(liebiao, k=12)
    # ----------------------------------------------------

    # -------------------------------------------------------------------------------------------------#
    canpingyouhua_link = 'https://' + link_not + '/configuration.php?gID=2'
    sadasdsadsa = ['price_asc', 'price_desc', 'date_added_desc', 'viewed_desc'][random.randint(0, 3)]
    canpin = ['12,24,36,48', '16,32,48,64'][qidong]
    # print(canpin)
    canpins = ['12', '16'][qidong]
    canpingyouhua_data = {
        'securityToken': securityToken,
        'configuration_group_id': '3',
        'configuration[CATEGORY_PAGE_SHOW_MODE]': '0',
        'configuration[INDEX_CATEGORY_LIST]': '',
        'configuration[PRODUCT_LIST_MODE]': 'grid-list',
        'configuration[PRODUCT_LIST_SORT]': sadasdsadsa,
        'configuration[PRODUCT_GRID_PER_PAGE_VALUES]': canpin,
        'configuration[PRODUCT_GRID_PER_PAGE]': canpins,
        'configuration[PRODUCT_GRID_PER_ROW]': '4',
        'configuration[PRODUCT_LIST_PER_PAGE_VALUES]': '5,10,15',
        'configuration[PRODUCT_LIST_PER_PAGE]': '5',
        'configuration[PRODUCT_LIST_SHORT_DESCRIPTION_LENGTH]': '150',
        'configuration[PRODUCT_NAME_MAX_LENGTH]': '50',
        'configuration[PRODUCT_NAME_SIDEBAR_MAX_LENGTH]': '20',
        'configuration[REVIEW_CONTENT_MAX_LENGTH]': '150',
        'configuration[REVIEW_LIMIT]': '10',
        'configuration[REVIEW_CONTENT_SIDEBAR_MAX_LENGTH]': '100',
        'configuration[REVIEW_SIDEBAR_LIMIT]': '5',
        'configuration[PRODUCT_LIST_SHOW_FILTER]': '1',
        'configuration[PRODUCT_SHOW_SAVE_OFF]': '1',
        'configuration[PRODUCT_SIDEBAR_SHOW_SAVE_OFF]': '1',
        'configuration[PRODUCT_PAGE_SHOW_SAVE_OFF]': '1',
        'configuration[ALSO_PURCHASED_LIMIT]': '4',
        'configuration[ALSO_PURCHASED_PER_ROW]': '4',
        'configuration[ALSO_PURCHASED_SIDEBAR_LIMIT]': '3',
        'configuration[BESTSELLERS_IDS]': ssss[0] + ',' + ssss[1] + ',' + ssss[2] + ',' + ssss[3] + ',' + ssss[
            4] + ',' + ssss[5] + ',' + ssss[6] + ',' + ssss[7] + ',' + ssss[8] + ',' + ssss[9] + ',' + ssss[
                                              10] + ',' + ssss[11],
        'configuration[BESTSELLERS_SKUS]': '',
        'configuration[BESTSELLERS_LIMIT]': '15',
        'configuration[BESTSELLERS_PER_ROW]': '4',
        'configuration[BESTSELLERS_SIDEBAR_LIMIT]': '3',
        'configuration[BESTSELLERS_PAGE_LIMIT]': '30',
        'configuration[FEATURED_IDS]': '',
        'configuration[FEATURED_SKUS]': '',
        'configuration[FEATURED_LIMIT]': '12',
        'configuration[FEATURED_PER_ROW]': '4',
        'configuration[FEATURED_SIDEBAR_LIMIT]': '3',
        'configuration[FEATURED_PAGE_LIMIT]': '30',
        'configuration[NEW_PRODUCTS_IDS]': '',
        'configuration[NEW_PRODUCTS_SKUS]': '',
        'configuration[NEW_PRODUCTS_LIMIT]': '0',
        'configuration[NEW_PRODUCTS_PER_ROW]': '4',
        'configuration[NEW_PRODUCTS_SIDEBAR_LIMIT]': '3',
        'configuration[NEW_PRODUCTS_PAGE_LIMIT]': '30',
        'configuration[RECENT_VIEWED_LIMIT]': '4',
        'configuration[RECENT_VIEWED_PER_ROW]': '4',
        'configuration[RECENT_VIEWED_SIDEBAR_LIMIT]': '3',
        'configuration[RELATED_SHOW]': '1',
        'configuration[RELATED_LIMIT]': '3',
        'configuration[RELATED_PER_ROW]': '3',
        'configuration[RELATED_SIDEBAR_LIMIT]': '3',
        'configuration[SPECIALS_IDS]': '',
        'configuration[SPECIALS_SKUS]': '',
        'configuration[SPECIALS_LIMIT]': '8',
        'configuration[SPECIALS_PER_ROW]': '4',
        'configuration[SPECIALS_SIDEBAR_LIMIT]': '3',
        'configuration[SPECIALS_PAGE_LIMIT]': '30',
        'configuration[ORDERED_PRODUCTS_IDS]': '',
        'configuration[ORDERED_PRODUCTS_SKUS]': '',
        'configuration[ORDERED_PRODUCTS_LIMIT]': '8',
        'configuration[ORDERED_PRODUCTS_PER_ROW]': '4',
        'configuration[ORDERED_PRODUCTS_SIDEBAR_LIMIT]': '3',
        'configuration[RECENT_ORDERS_SIDEBAR_LIMIT]': '10',
        'configuration[PRODUCT_FILTER_1]': 'Filter 1',
        'configuration[PRODUCT_FILTER_2]': 'Filter 2',
        'configuration[PRODUCT_FILTER_3]': 'Filter 3',
        'configuration[PRODUCT_FILTER_4]': 'Filter 4',
        'configuration[PRODUCT_FILTER_5]': 'Filter 5',
        'configuration[PRODUCT_FILTER_6]': 'Filter 6',
        'configuration[PRODUCT_FILTER_7]': 'Filter 7',
        'configuration[PRODUCT_FILTER_8]': 'Filter 8',
        'configuration[PRODUCT_FILTER_9]': 'Filter 9',
        'configuration[PRODUCT_FILTER_10]': 'Filter 10',
        'configuration[PRODUCT_FILTER_11]': 'Filter 11',
        'configuration[PRODUCT_FILTER_12]': 'Filter 12',
        'configuration[PRODUCT_FILTER_13]': 'Filter 13',
        'configuration[PRODUCT_FILTER_14]': 'Filter 14',
        'configuration[PRODUCT_FILTER_15]': 'Filter 15',
        'configuration[PRODUCT_FILTER_16]': 'Filter 16',
        'configuration[PRODUCT_FILTER_17]': 'Filter 17',
        'configuration[PRODUCT_FILTER_18]': 'Filter 18',
        'configuration[PRODUCT_FILTER_19]': 'Filter 19',
        'configuration[PRODUCT_FILTER_20]': 'Filter 20',
    }

    canpingyouhua_post = session.post(url='https://' + link_not + '/configuration.php?gID=3&action=save',
                                      data=canpingyouhua_data, headers=req_header)

    # ==========================================================================#
    qinglitupian = session.get(url='https://www.' + link_not + '/index.php?action=clearImg')
    qinglishuju = session.get(url='https://www.' + link_not + '/index.php?action=clearSql')
    print('成功')

if __name__ == '__main__':
    while True:
        sdads = input('请输入网站\n:')
        hello(link_nots=sdads, qidong=0)
