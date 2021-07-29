import pymysql
import csv
import random
with open('1/' + self.name + '.csv', 'w', newline='', encoding='utf-8')as files:
    f_csvs = csv.writer(files)
    f_csvs.writerow(
        ['v_sku', 'v_name', 'v_short_description', 'v_description', 'v_image', 'v_url', 'v_attribute',
         'v_price',
         'v_specials_price', 'v_specia  ls_expire_date', 'v_date_added', 'v_in_stock', 'v_status', 'v_viewed',
         'v_ordered', 'v_category_sku', 'v_sort_order', 'v_meta_title', 'v_meta_keywords', 'v_meta_description',
         'v_brand_filter', 'v_class_filter', 'v_color_filter', 'v_gender_filter', 'v_material_filter',
         'v_year_filter', 'v_origin_filter', 'v_series_filter', 'v_spec_filter'])
alist = random.sample(range(originate, source), 20)  # 随机选取20个
sku = 0
connectr = pymysql.connect(
    host='3.143.242.127',
    user='root',
    port=3306,
    password='Tang5230.',
    charset='utf8',
    db='zuful',
    cursorclass=pymysql.cursors.DictCursor

)
cursor = connectr.cursor()
for i in alist:
    user_iamg = 'bottoms'
    sql = 'SELECT * FROM ' + user_iamg + ' WHERE ID = %s' % i
    data_count = cursor.execute(sql)
    data = cursor.fetchall()[0]
    with open('1/' + self.name + '.csv', 'a+', newline="", encoding='utf-8')as file:
        csv_writer = csv.writer(file)
        sku += 1
        name_new = self.name + r'%04d' % sku
        a = random.uniform(22, 33)
        csv_writer.writerow(
            [name_new, data['user_name'], '', data['user_descriptions'],
             'img/' + user_iamg + '/' + data['user_iamg'], '', 'Size#XS:S:M:L:XL:2XL:3XL:4XL:5XL', round(a, 2),
             '', '', '', '1', '1', '',
             '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
             '', '', '', '', '',
             '', '', '', ''])
    user_iamg = 'dresses'
    sql = 'SELECT * FROM ' + user_iamg + ' WHERE ID = %s' % i
    data_count = cursor.execute(sql)
    data = cursor.fetchall()[0]
    with open('1/' + self.name + '.csv', 'a+', newline="", encoding='utf-8')as file:
        csv_writer = csv.writer(file)
        sku += 1
        name_new = self.name + r'%04d' % sku
        a = random.uniform(22, 33)
        csv_writer.writerow(
            [name_new, data['user_name'], '', data['user_descriptions'],
             'img/' + user_iamg + '/' + data['user_iamg'], '', 'Size#XS:S:M:L:XL:2XL:3XL:4XL:5XL', round(a, 2),
             '', '', '', '1', '1', '',
             '', user_iamg, '', data['user_name'], data['user_name'], data['user_name'],
             '', '', '', '', '',
             '', '', '', ''])
    user_iamg = 'men_s_shoes'
    sql = 'SELECT * FROM ' + user_iamg + ' WHERE ID = %s' % i
    data_count = cursor.execute(sql)
    data = cursor.fetchall()[0]
    with open('1/' + self.name + '.csv', 'a+', newline="", encoding='utf-8')as file:
        csv_writer = csv.writer(file)
        sku += 1
        name_new = self.name + r'%04d' % sku
        a = random.uniform(49, 66)
        csv_writer.writerow(
            [name_new, data['user_name'], '', data['user_descriptions'],
             'img/' + user_iamg + '/' + data['user_iamg'], '',
             'Shoes Size#EUR35=US5:EUR36=US6:EUR37=US6.5:EUR38=US7.5:EUR39=US8.5:EUR39=US7:EUR40=US7.5:EUR41=US8:EUR42=US8.5:EUR43=US9:EUR44=US10',
             round(a, 2),
             '', '', '', '1', '1', '',
             '', user_iamg.replace("_", " "), '', data['user_name'], data['user_name'], data['user_name'],
             '', '', '', '', '',
             '', '', '', ''])