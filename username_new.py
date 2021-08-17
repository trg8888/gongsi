import requests
import re
from chaojiying import Chaojiying_Client
import pandas as pd
import random
from lxml import etree
import pymysql
import csv
import threading
import datetime


class Utopia(threading.Thread):
    def __init__(self,threadName):
        self.url = threadName
        super(Utopia, self).__init__(name=threadName)
        self.session = requests.session()
        self.size = []
        self.sku = 0
        self.path = '1'
        self.connectr = pymysql.connect(
            host='106.55.26.254',
            user='root',
            port=3306,
            password='Tang5230.',
            charset='utf8',
            db='zafulcom',
            cursorclass=pymysql.cursors.DictCursor
        )

        self.cursor = self.connectr.cursor()
        self.name = ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e',
             'd', 'c', 'b', 'a'], 7)).upper()
        with open(self.path + '/' + self.name + '.csv', 'w', newline='', encoding='utf-8')as files:
            f_csvs = csv.writer(files)
            f_csvs.writerow(
                ['v_sku', 'v_name', 'v_short_description', 'v_description', 'v_image', 'v_url', 'v_attribute',
                 'v_price',
                 'v_specials_price', 'v_specials_expire_date', 'v_date_added', 'v_in_stock', 'v_status', 'v_viewed',
                 'v_ordered', 'v_category_sku', 'v_sort_order', 'v_meta_title', 'v_meta_keywords', 'v_meta_description',
                 'v_brand_filter', 'v_class_filter', 'v_color_filter', 'v_gender_filter', 'v_material_filter',
                 'v_year_filter', 'v_origin_filter', 'v_series_filter', 'v_spec_filter'])
        with open(self.path + '/' + self.name + 'fen.csv', 'w', newline='', encoding='utf-8')as files:
            f_csvs = csv.writer(files)
            f_csvs.writerow(
                ['v_sku', 'v_name', 'v_description', 'v_image', 'v_url', 'v_parent_sku', 'v_date_added', 'v_status',
                 'v_sort_order', 'v_meta_title', 'v_meta_keywords', 'v_meta_description', '', '', '', ''])
        with open(self.path + '/' + self.name + 'size.csv', 'w', newline='', encoding='utf-8')as files:
            f_csvs = csv.writer(files)
            f_csvs.writerow(
                ['v_name', 'v_type', 'v_sort_order', 'v_value'])
        self.clothing = None
        self.clothing_ = None
        self.jewelry = None
        self.Bag = None
        self.shoe = None


    def generate(self, name, min_, max_,jia = False):
        user_iamgs = name
        user_iamg = user_iamgs.replace('is', "'s").replace('____', ',').replace('___', '-').replace('__', ' & ').replace('_', ' ')
        sql = 'select * from %s order by rand() limit %s;' % (name,str(random.randint(21,35)))
        data_count = self.cursor.execute(sql)
        data_all = self.cursor.fetchall()
        for data in data_all:
            size = 'Size#'
            siz = re.findall('(.*?):.*?;', data['size_'])
            for i__ in siz:
                self.size.append(i__)
                size += i__ +':'
            with open(self.path + '/' + self.name + '.csv', 'a+', newline="", encoding='utf-8')as file:
                csv_writer = csv.writer(file)
                self.sku += 1
                name_new = self.name + r'%04d' % self.sku
                a = random.uniform(min_, max_)
                if jia:
                    jiage = round(a, 2)
                    tejia = jiage - (jiage * round(random.uniform(0.1,0.4),2))
                else:
                    jiage = ''
                    tejia = round(a,2)
                csv_writer.writerow(
                    [name_new, data['user_name'], '', data['user_descriptions'],
                     'img/' + user_iamgs + '/' + data['user_iamg'], '', size, tejia,
                     jiage, '', '', '1', '1', '',
                     '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
                     '', '', '', '', '',
                     '', '', '', ''])
    def categorytable(self):
        secondaryclassification_one = self.clothing_[0].replace('is', "'s").replace('____', ',').replace('___', '-').replace(
            '__', ' & ').replace(
            '_', ' ')
        secondaryclassification_two = self.clothing_[1].replace('is', "'s").replace('____', ',').replace('___',
                                                                                                                  '-').replace(
            '__',
            ' & ').replace(
            '_', ' ')
        secondaryclassification_three = self.clothing[0].replace('is', "'s").replace('____', ',').replace('___', '-').replace(
            '__',
            ' & ').replace(
            '_', ' ')
        secondaryclassification_four = self.clothing[1].replace('is', "'s").replace('____', ',').replace('___', '-').replace(
            '__',
            ' & ').replace(
            '_', ' ')
        secondaryclassification_fives = self.jewelry[0].replace('is', "'s").replace('____', ',').replace('___',
                                                                                                     '-').replace('__',
                                                                                                                  ' & ').replace(
            '_',
            ' ')
        secondaryclassification_six = self.jewelry[1].replace('is', "'s").replace('____', ',').replace('___',
                                                                                                      '-').replace('__',
                                                                                                                   ' & ').replace(
            '_', ' ')
        secondaryclassification_seven = self.Bag[0].replace('is', "'s").replace('____', ',').replace('___',
                                                                                                       '-').replace(
            '__',
            ' & ').replace(
            '_', ' ')
        secondaryclassification_eight = self.shoe[0].replace('is', "'s").replace('____', ',').replace('___',
                                                                                                         '-').replace(
            '__',
            ' & ').replace(
            '_', ' ')
        secondaryclassification_nine = self.shoe[1].replace('is', "'s").replace('____', ',').replace('___',
                                                                                                         '-').replace(
            '__', ' & ').replace('_', ' ')

        firstlevel_one = random.choice(['clothing','garment','clothes','garment','habiliment','costuming','attire','Dresses'])
        firstlevel_two = random.choice(['jewelry', 'ornaments', 'jewellery'])
        firstlevel_four = random.choice(['shoe', 'shoes'])
        sdas = [[firstlevel_one, firstlevel_one, '', '', '', '', '', '1', '1', firstlevel_one, firstlevel_one,
                 firstlevel_one],
                [firstlevel_two, firstlevel_two, '', '', '', '', '', '1', '5', firstlevel_two, firstlevel_two,
                 firstlevel_two],
                [firstlevel_four, firstlevel_four, '', '', '', '', '', '1', '5', firstlevel_four, firstlevel_four,
                 firstlevel_four]]
        sdass = [[secondaryclassification_three, secondaryclassification_three, '', '', '', firstlevel_one, '', '1',
                  '5', secondaryclassification_three, secondaryclassification_three,
                  secondaryclassification_three],
                 [secondaryclassification_four, secondaryclassification_four, '', '', '', firstlevel_one, '', '1', '5',
                  secondaryclassification_four, secondaryclassification_four, secondaryclassification_four],
                 [secondaryclassification_fives, secondaryclassification_fives, '', '', '', firstlevel_two, '', '1',
                  '5',
                  secondaryclassification_fives, secondaryclassification_fives, secondaryclassification_fives],
                 [secondaryclassification_six, secondaryclassification_six, '', '', '', firstlevel_two, '', '1', '5',
                  secondaryclassification_six, secondaryclassification_six,
                  secondaryclassification_six],
                 [secondaryclassification_eight, secondaryclassification_eight, '', '', '', firstlevel_four, '', '1',
                  '5',
                  secondaryclassification_eight, secondaryclassification_eight, secondaryclassification_eight],
                 [secondaryclassification_nine, secondaryclassification_nine, '', '', '', firstlevel_four, '', '1',
                  '5',
                  secondaryclassification_nine, secondaryclassification_nine, secondaryclassification_nine]]
        sli = random.sample(sdas, 3)
        slis = random.sample(sdass, 6)
        for asdsad, sss in enumerate(sli):
            with open(self.path + '/' + self.name + 'fen.csv', 'a+', newline='', encoding='utf-8')as files:
                asdsads = asdsad + 1
                sss[8] = asdsads
                f_csvs = csv.writer(files)
                f_csvs.writerow(sss)
        list__ = [[secondaryclassification_one, secondaryclassification_one, '', '', '', '', '', '1', asdsads,
                  secondaryclassification_one, secondaryclassification_one, secondaryclassification_one],
                 [secondaryclassification_two, secondaryclassification_two, '', '', '', '', '', '1', asdsads,
                  secondaryclassification_two, secondaryclassification_two,
                  secondaryclassification_two],[secondaryclassification_seven, secondaryclassification_seven, '', '', '', '', '', '1',
                  asdsads, secondaryclassification_seven, secondaryclassification_seven,
                  secondaryclassification_seven],]
        for asdsad, sss in enumerate(list__):
            with open(self.path + '/' + self.name + 'fen.csv', 'a+', newline='', encoding='utf-8')as files:
                asdsads = asdsad + 5
                f_csvs = csv.writer(files)
                f_csvs.writerow(sss)
        for asdsad, sss in enumerate(slis):
            with open(self.path + '/' + self.name + 'fen.csv', 'a+', newline='', encoding='utf-8')as files:
                asdsads = asdsad + 8
                sss[8] = asdsads
                f_csvs = csv.writer(files)
                f_csvs.writerow(sss)

    def information(self,link_nots):
        self.fen()
        self.pymysql()
        sql_ = """INSERT INTO peizhi(url)
                                     VALUES ("%s")""" % (self.url)
        try:
            self.cursor.execute(sql_)
            self.connectr.commit()
            print('写入账户')
        except Exception as fs:
            self.connectr.rollback()
            print('账户已存在')
        link_not = link_nots
        wangzan = re.findall(r'(.*?)/', link_not)
        i = 'https://' + link_not + '/index.php'

        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        response = self.session.get(i, headers=req_header).text
        responses = re.findall('<img src="(.*?)" oncl', response)[0]
        securityToken = re.findall('<input type="hidden" value="(.*?)" name="securityToken" />', response)[0]

        response = self.session.get(responses, headers=req_header).content
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
        response = self.session.post(url=link, data=data, headers=req_header).text

        sql = 'select * from about_us order by rand() limit 1;'
        data_count = self.cursor.execute(sql)
        data = self.cursor.fetchone()

        guanyuzhongxin_link = 'https://' + link_not + '/cms_page.php?action=save'

        guanyuzhongxin_data = {
            'securityToken': securityToken,
            'cms_page[cms_page_id]': '1',
            'cms_page[name]': 'About Us',
            'cms_page[content]': data['content'],
            'cms_page[meta_title]': 'About Us',
            'cms_page[meta_keywords]': '',
            'cms_page[meta_description]': '',
            'cms_page[status]': '1',
            'cms_page[sort_order]': '10'
        }
        guanyuzhongxin_post = self.session.post(url=guanyuzhongxin_link, data=guanyuzhongxin_data, headers=req_header)

        qinchushuju = 'https://www.' + link_nots + '/import_old.php?action=clearProduct'
        qinchushuju_1 = self.session.get(url=qinchushuju, headers=req_header)

        # =======================================================================================
        shangchuan_1_data = {
            'securityToken': securityToken,
            'MAX_FILE_SIZE': '100000000',
            'action': 'product_option',

        }
        shangchuan_1_files = {
            'usrfl': ('size.csv', open(self.path + '/' + self.name + 'size.csv', 'r', encoding='utf-8'), 'application/vnd.ms-excel')
        }
        shangchuan_1 = 'https://www.' + link_nots + '/import_old.php'
        shangchuan_1_post = self.session.post(url=shangchuan_1, data=shangchuan_1_data, files=shangchuan_1_files)

        shangchuan_2_data = {
            'securityToken': securityToken,
            'MAX_FILE_SIZE': '100000000',
            'action': 'category',

        }
        wocao_1 = self.path + '/' + self.name + 'fen.csv'
        shangchuan_2_files = {
            'usrfl': ('size.csv', open(wocao_1, 'r', encoding='utf-8'), 'application/vnd.ms-excel')
        }
        shangchuan_2 = 'https://www.' + link_nots + '/import_old.php'
        shangchuan_2_post = self.session.post(url=shangchuan_2, data=shangchuan_2_data, files=shangchuan_2_files)

        shangchuan_3_data = {
            'securityToken': securityToken,
            'MAX_FILE_SIZE': '100000000',
            'action': 'product',

        }
        shangchuan_3_files = {
            'usrfl': ('1.csv', open(self.path + '/' + self.name + '.csv', 'r', encoding='utf-8'), 'application/vnd.ms-excel')
        }
        shangchuan_3 = 'https://www.' + link_nots + '/import_old.php'
        shangchuan_3_post = self.session.post(url=shangchuan_3, data=shangchuan_3_data, files=shangchuan_3_files)
        ######图片检测
        for i in range(2):
            shangchu_1 = []
            link_1 = 'https://www.' + link_nots + '/product.php?page=1'
            sad_1 = self.session.get(link_1, headers=req_header).text
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
                sad_1 = self.session.get(sadsads_1[0], headers=req_header).text
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
                ceshiasdsa = self.session.post(url=link_1 + '&action=delete', headers=req_header, data=data_1)

        # =======================================================================================
        print('开始配置数据')
        sql = 'select * from Security_and_privacy order by rand() limit 1;'

        data_count = self.cursor.execute(sql)
        data = self.cursor.fetchone()
        # print(data)

        yingsianquan_link = 'https://' + link_not + '/cms_page.php?action=save'
        yingsianquan_data = {
            'securityToken': securityToken,
            'cms_page[cms_page_id]': '3',
            'cms_page[name]': 'Privacy & Security',
            'cms_page[content]': data['user_name'],
            'cms_page[meta_title]': 'Privacy & Security',
            'cms_page[meta_keywords]': '',
            'cms_page[meta_description]': '',
            'cms_page[status]': '1',
            'cms_page[sort_order]': '30'
        }
        yingsianquan_post = self.session.post(url=yingsianquan_link, data=yingsianquan_data, headers=req_header)

        songhuofanshi_link = 'https://' + link_not + '/cms_page.php?action=save'

        sql = 'select * from Shipping_and_returns order by rand() limit 1;'
        data_count = self.cursor.execute(sql)
        data = self.cursor.fetchone()
        songhuofanshi_data = {
            'securityToken': securityToken,
            'cms_page[cms_page_id]': '4',
            'cms_page[name]': 'Shipping & Delivery',
            'cms_page[content]': data['Shipping'],
            'cms_page[meta_title]': 'Shipping & Delivery',
            'cms_page[meta_keywords]': '',
            'cms_page[meta_description]': '',
            'cms_page[status]': '1',
            'cms_page[sort_order]': '40'
        }
        songhuofanshi_post = self.session.post(url=songhuofanshi_link, data=songhuofanshi_data, headers=req_header)

        tuihuo_link = 'https://' + link_not + '/cms_page.php?action=save'
        tuihuo_shuju = data['returns']

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
        sql = 'select * from common_problem order by rand() limit 1;'
        data_count = self.cursor.execute(sql)
        data = self.cursor.fetchone()
        Faq_data = {
            'securityToken': securityToken,
            'cms_page[cms_page_id]': '7',
            'cms_page[name]': 'Faq',
            'cms_page[content]': data['content'],
            'cms_page[meta_title]': 'Faq',
            'cms_page[meta_keywords]': '',
            'cms_page[meta_description]': '',
            'cms_page[status]': '1',
            'cms_page[sort_order]': '70'
        }

        Faq_post = self.session.post(url=Faq_link, data=Faq_data, headers=req_header)

        # 先判断他使用了什么模块
        panduan = 'https://' + link_not + '/configuration.php?gID=1'
        panduan_post = self.session.get(url=panduan, headers=req_header).text
        panduan_one = etree.HTML(panduan_post)
        panduan_new = \
            panduan_one.xpath(
                '/html/body/div/div/div[2]/form/table/tbody/tr[9]/td[2]/select/option[@value!="default"]/text()')
        if not panduan_new:
            print('没有找到一次')
            panduan = 'https://' + link_not + '/configuration.php?gID=1'
            panduan_post = self.session.get(url=panduan, headers=req_header).text
            panduan_one = etree.HTML(panduan_post)
            panduan_new = \
                panduan_one.xpath(
                    '/html/body/div/div/div[2]/form/table/tbody/tr[9]/td[2]/select/option[@value!="default"]/text()')
            if not panduan_new:
                print('二次都没有找到自动退出',self.url)
                return '403'
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

        sql = 'select * from title order by rand() limit 1;'
        data_count = self.cursor.execute(sql)
        data = self.cursor.fetchone()
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
            'configuration[HEAD_DEFAULT_TITLE]': data['one'],
            'configuration[HEAD_TITLE_PREFIX]': '',
            'configuration[HEAD_TITLE_SUFFIX]': '',
            'configuration[HEAD_DEFAULT_KEYWORDS]': data['two'],
            'configuration[HEAD_DEFAULT_DESCRIPTION]': data['three'],
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

        jibenshezhi_post = self.session.post(url=jibenshezhi_link, data=jibenshezhi_data, headers=req_header)

        # -------------------------------------------------------
        liebiao = []
        for i in random.sample([4,5,6,7,8,9,10,11,12],3):
            linksss = 'https://www.' + link_not + '/product.php?filter_category_id=%s' % i
            sad = self.session.get(linksss, headers=req_header).text
            sadsadsad = re.findall('(?s)src=".*" /></td>.*?<td>\d{1,3}</td>', sad)
            liebiao_ = []
            for isss in sadsadsad:
                asdasdsadaasdsa = re.findall('<td>(\d{1,})</td>', isss)
                for issss in asdasdsadaasdsa:
                    liebiao_.append(issss)
            liebiao.extend(random.sample(liebiao_,k=4))
        ssss = liebiao
        # ----------------------------------------------------

        # -------------------------------------------------------------------------------------------------#
        canpingyouhua_link = 'https://' + link_not + '/configuration.php?gID=2'
        sadasdsadsa = ['price_asc', 'price_desc', 'date_added_desc', 'viewed_desc'][random.randint(0, 3)]
        qidong = random.randint(0,1)
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

        canpingyouhua_post = self.session.post(url='https://' + link_not + '/configuration.php?gID=3&action=save',
                                          data=canpingyouhua_data, headers=req_header)

        # ==========================================================================#
        qinglitupian = self.session.get(url='https://www.' + link_not + '/index.php?action=clearImg')
        qinglishuju = self.session.get(url='https://www.' + link_not + '/index.php?action=clearSql')
        sql_ = """UPDATE peizhi SET pz = 1 WHERE url = '%s' """ % self.url
        try:
            self.cursor.execute(sql_)
            self.connectr.commit()
            print('已经完成')
        except Exception as fs:
            self.connectr.rollback()
            print('配置出错')

    def fen(self):
        if not self.size:
            print('配置出错')
            return '403'
        color_1 = ''
        color_item = {}
        for id_, i in enumerate(self.size):
            color_1 += i + ':' + str(id_ + 1) + ';'
            color_item[i] = id_ + 1
        with open(self.path + '/' + self.name + 'size.csv', 'a+', newline="", encoding='utf-8')as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(
                ['size', 'select', '1', color_1])

    def pymysql(self):
        self.cursor.close()
        self.connectr.close()
        self.connectr = pymysql.connect(
            host='106.55.26.254',
            user='root',
            port=3306,
            password='Tang5230.',
            charset='utf8',
            db='company',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connectr.cursor()

    def run(self):
        list_ = [
            {'name': 'Bodycon_Dresses', 'min_': 22, 'max_': 33},
            {'name': 'Casual_Dresses', 'min_': 22, 'max_': 33},
            {'name': 'Mini_Dresses', 'min_': 22, 'max_': 33},
            {'name': 'Print_Dresses', 'min_': 22, 'max_': 33},
            {'name': 'Short_Sets', 'min_': 22, 'max_': 33},
            {'name': 'Skirt_Sets', 'min_': 22, 'max_': 33},
            {'name': 'Skirts', 'min_': 22, 'max_': 33},
            {'name': 'Pants', 'min_': 22, 'max_': 33},
            {'name': 'Pendant_Necklaces', 'min_': 11, 'max_': 29},
            {'name': 'Chokers', 'min_': 11, 'max_': 29},
            {'name': 'Layer_Sets', 'min_': 11, 'max_': 29},
            {'name': 'Backpack', 'min_': 56, 'max_': 74},
            {'name': 'Wallets', 'min_': 56, 'max_': 74},
            {'name': 'Handbags', 'min_': 56, 'max_': 74},
            {'name': 'Sandals', 'min_': 49, 'max_': 66},
            {'name': 'Slippers', 'min_': 49, 'max_': 66},
            {'name': 'Flats', 'min_': 49, 'max_': 66},
            {'name': 'Heels', 'min_': 49, 'max_': 66},
            {'name': 'Sneakers__Athletic', 'min_': 49, 'max_': 66},
        ]
        clothing = random.sample(['Bodycon_Dresses','Casual_Dresses','Mini_Dresses','Print_Dresses'],2)
        clothing_ = random.sample(['Short_Sets','Skirt_Sets'],1)
        clothing_.extend(random.sample(['Skirts','Pants'],1))
        self.clothing_ = clothing_
        self.clothing = clothing
        jewelry = random.sample(['Chokers','Layer_Sets'],2)
        self.jewelry = jewelry
        Bag = random.sample(['Backpack','Wallets','Handbags'],1)
        self.Bag = Bag
        shoe = random.sample(['Sandals','Slippers','Flats','Heels','Sneakers__Athletic'],2)
        self.shoe = shoe
        clothing.extend(jewelry)
        clothing.extend(Bag)
        clothing.extend(shoe)
        clothing.extend(clothing_)
        for name in clothing:
                for item in list_:
                    if item.get('name') == name:
                        self.generate(name=item['name'], min_=item['min_'], max_=item['max_'])
        self.categorytable()
        self.information(link_nots=self.url)

    def install(self, url):
        response = self.session.get(url=url).text
        nexts = etree.HTML(response)
        next_ = nexts.xpath('//a[@class="next"]/@href')
        edit = re.findall('<a href="(.*?)">编辑</a>', response)
        securityToken = re.findall('<input type="hidden" value="(.*?)" name="securityToken" />', response)[0]
        for i in edit:
            id = re.findall(r'id=(\d{1,4})', i)[0]
            response_new = self.session.get(url=i).text
            product_3 = re.findall(
                r'<td class="value"><input type="text" class="input-text" value="(.*?)" name=".*" id="product-image" /></td>',
                response_new)[0]
            inse = re.findall('img/(.*)/(.*)\.jpg', product_3)[0]
            price = re.findall(
                '<td class="value"><input type="text" class="input-text required-entry" value="(.*?)" name="product\[price]" id="product-price" /></td>',
                response_new)[0]
            sql = "SELECT * FROM " + inse[0] + " WHERE sku = '%s'" % inse[1]
            data_count = self.cursor.execute(sql)
            data = self.cursor.fetchall()[0]
            product = re.findall(
                r'<td class="value"><input type="text" class="input-text required-entry" value="(.*?)" name=".*" id="product-sku" /></td>',
                response_new)[0]
            product_5 = re.findall(r'<option selected="selected" value="(.*?)">.*</option>', response_new)[0]
            post_link = 'https://www.' + self.url + '/product.php?action=save'
            option_value = []
            size_ = data['size_']
            size_int = re.findall('(.*?):\d;', size_)
            for size_i in size_int:
                option_values = re.findall(
                    '<input type="checkbox" class="checkbox" name="option_values\[.*?" value="(.*?)" id=.*? />\r\n.*?    {0}\t.*?</td>'.format(
                        size_i),
                    response_new)
                if option_values:
                    option_value.append(option_values[0])
                else:
                    pass
            option_value_data = []
            color = data['color']
            size_int = re.findall('(.*?):\d;', color)
            for size_i in size_int:
                option_values = re.findall(
                    '<input type="checkbox" class="checkbox" name="option_values\[.*?" value="(.*?)" id=.*? />\r\n.*?    %s\t.*?</td>' % size_i,
                    response_new)
                print(option_values)
                if option_values:
                    option_value_data.append(option_values[0])
                else:
                    pass
            data = {
                'product[product_id]': id,
                'options[]': [1, 2],
                'option_requireds[]': [1, 2],
                'option_values[1][]': option_value,
                'option_values[2][]': option_value_data,
                'securityToken': securityToken,
                'product[sku]': product,
                'product[name]': data['user_name'],
                'product[description]': data['user_descriptions'],
                'product[image]': product_3,
                'product[specials_price]': '0.0000',
                'product[price]': price,
                'product[master_category_id]': product_5,
                'product_to_category[]': product_5,
                'product[meta_title]': data['user_name'],
                'product[meta_keywords]': data['user_name'],
                'product[meta_description]': data['user_name'],
                'product[stock_qty]': 0,
                'product[in_stock]': 1,
                'product[status]': 1,
                'product[sort_order]': 0,
                'product[viewed]': 0,
                'product[ordered]': 0,
            }
            post = self.session.post(url=post_link, data=data).text
        if next_:
            self.install(next_[0])



listzt = [
    "rrmhe.com/grzh1754-titan",
]
for url in listzt:
    try:
        Utopia(url).start()
    except Exception:
        print(url)