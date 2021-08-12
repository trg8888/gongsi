import requests
import csv
from lxml import etree
import uuid
import re
import ast


class Gentlemonster(object):

    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
            'cookie': 'gentle_area=other; PHPSESSID=8uqic665tu5rb28eenpf0rno75; _fbp=fb.1.1625032337790.1095034074; _gcl_au=1.1.1937711130.1625032338; _ga=GA1.2.727496101.1625032338; _gid=GA1.2.312603734.1625032338; ak_bmsc=CA22BBF9DF9E2754DA639704C610ADB3~000000000000000000000000000000~YAAQltocuPnQ2Fp6AQAAb6WMWwytP6e7LiAh66OsWjoVnj3aF6P2mBwLAcnpl75PTzj5WbQitQAq82zH4aYfE0aiZJuhs4e+l72vqgTFjazQ51HJUHliGX0I8eP67lO+fnKX7zSCN5nNp6v3p/QFS0oWDudIueOuB+M3cWEdDjSnrCpL8DgTAl8gcwtBUJwPgv+idwrK0K1pTMJl7/yLZ9qoMU4JU04NsCYZfDzcWJVumy0TuR/GtWR7Km829T5EO/nr9SdjZEj+ZLRn9+ZEePp2Rlop92RCVNPF7GUH43PCQ1VGBtvSTPFrF09ZEnT8HSKMfwLH5E0Mx5yIrbe0okp/Ap6VoMt3aqdtX/FHqr8Wj4hqHrlAfARd7rJO+mZ7rNNcVvEOo8xtDkRP9rYeim1BJI8lSqGuX3FxBT/DVdzxHxFziS8Wih95/HhT8pWfoTixr1EvStEoMNQK6DeW1WNcrNB08ZF53Qlqe54HSGhX7pQyLXtpw96nwElbRVhvswWOZsv9TSioNnCLXgTTAw4b; 2a0d2363701f23f8a75028924a3af643=MTE5LjI4LjYuNjU%3D; _ce.s=v11.rlc~1625036452646; wcs_bt=s_1082a4ab6732:1625036927|6ec119bb66d5c8:1625036926; _uetsid=53800840d96711eba101bdad8cb6b75d; _uetvid=53808660d96711ebb6791340e00bf864; _gat_UA-49553718-1=1; bm_sv=4DF4670F996744B83F9329E0B9C35536~RdpH1YzexSPCY5IWDWW1EKbrE0HTpeskagbb6dR0umW4I4hzpQtLXdOIrt7J7jz2oPGMH+hODPO3SIhaltIhaLYzQ479vVm+y7t1kFiBRazL/9x6LInOLep1I6gJv4GqdBT/pvfdiwEPM+FEoRFN3gQW5jWZgdXkLssstTeKwKU=; inside-asia2=48855955-2bdab602530a617d7208b791448fd9a1b05ba729397f980979cae1f37abfadef-0-0'
        }
        self.item = {}
        with open('1/' + '1.csv', 'w', newline='', encoding='utf-8')as files:
            f_csvs = csv.writer(files)
            f_csvs.writerow(
                ['v_sku', 'v_name', 'v_short_description', 'v_description', 'v_image', 'v_url', 'v_attribute',
                 'v_price',
                 'v_specials_price', 'v_specials_expire_date', 'v_date_added', 'v_in_stock', 'v_status', 'v_viewed',
                 'v_ordered', 'v_category_sku', 'v_sort_order', 'v_meta_title', 'v_meta_keywords', 'v_meta_description',
                 'v_brand_filter', 'v_class_filter', 'v_color_filter', 'v_gender_filter', 'v_material_filter',
                 'v_year_filter', 'v_origin_filter', 'v_series_filter', 'v_spec_filter'])
        self.name_new = ''
        self.id = 1

    def get_all(self,url):
        text = self.session.get(url, headers=self.headers).text
        response = etree.HTML(text)
        ul = response.xpath('//div[@class="product-info__frames"]/div[@class="product-info__frame-collection-link"]/a/@href')[0]
        url = 'https://www.blenderseyewear.com' + ul
        self.get(url=url)




    def get(self, url):
        text = self.session.get(url, headers=self.headers).text
        response = etree.HTML(text)
        ul = response.xpath('//div[@id="CC-Loop"]/div/a/@href')
        for url_ in ul:
            url = 'https://www.blenderseyewear.com' + url_
            self.detail(url=url)
            self.img()
            self.csv()

    def detail(self, response=None, url=None):
        if response is None:
            if url is None:
                print('h 不存在 不传参')
                return '500'
            text = self.session.get(url, headers=self.headers).text
            response = etree.HTML(text)
        name_one = response.xpath('//h1[@class="product-details__title"]/text()')[0]
        name_two = response.xpath('//span[@class="product-polarized"]/text()')[0]
        name_three = response.xpath('//div[@class="product-details__frame"]/a[@class="product-frame"]/text()')[0]
        price = \
        response.xpath('//div[@class="product-price"]/span/span[contains(@class,"flow-price__item")]/@flow-default')[0]
        price = price.replace('$', '')
        description_new = response.xpath('//div[@class="details-text-wrap"]')[0]
        description = etree.tostring(description_new, method='html')  # 转为字符串
        description = bytes.decode(description).replace('\n', '').replace("\'", "")
        name = name_one + ' ' + name_two + ' ' + name_three
        img_new = response.xpath('//div[@class="cc-thumbs"]/div/a/@data-main')
        img =[]
        for i in img_new:
            url = 'https:' + i
            img.append(url)
        sku = uuid.uuid4().hex
        self.item['img'] = img
        self.item['name'] = name
        self.item['describe'] = description
        self.item['price'] = price
        self.name_new = r'BE-0806-%04d'
        self.item['sku'] = sku
        self.item['url'] = url


    def verification(self):
        if not self.item.get('img'):
            print('file does not exist')
            return '404'

    def img(self):
        self.verification()
        img = self.item['img']
        for id, url in enumerate(img):
            if id == 0:
                filename = self.item['sku'] + '.jpg'
            else:
                filename = self.item['sku'] + '_' + str(id) + '.jpg'
            with open('1/' + filename, 'wb')as file:
                file.write(self.session.get(url).content)

    def describe_img(self):
        self.verification()
        img = self.item['describe_img']
        for id, url in enumerate(img):
            if id == 0:
                filename = self.item['sku'] + '.jpg'
            else:
                filename = self.item['sku'] + '_' + str(id) + '.jpg'
            with open('1/1525/' + filename, 'wb')as file:
                file.write(self.session.get(url).content)
                self.item['describe'] += '<img src=' + '"MJ20210701/1525/' + filename + '">'

    def csv(self):
        self.verification()
        with open('1/' + '1.csv', 'a+', newline='', encoding='utf-8_sig')as files:
            f_csvs = csv.writer(files)
            f_csvs.writerow(
                [self.name_new % self.id, self.item['name'], self.item['url'], self.item['describe'],
                 'BE210806/' + self.item['sku'] + '.jpg', '', '', self.item['price'],
                 '', '', '', '1', '1', '',
                 '', 'north-park', '', self.item['name'], self.item['name'], self.item['name'],
                 '', '', '', '', '',
                 '', '', '', ''])
        self.id += 1
        self.item = {}


gentlemonster = Gentlemonster()
gentlemonster.get(url='https://www.blenderseyewear.com/collections/romeo')