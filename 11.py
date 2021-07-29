import requests
from lxml import etree
import re
import pymysql

class Master(object):
    def __init__(self):
        self.switch = True
        self.headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'cookie':'user_3071155707=4575ec4ac5ec40a0858c016634001737; INGRESSCOOKIE=1621827882.858.4989.585249; PHPSESSID=976387489491cfcac86bafe1e6402f2e; _csrf=309a65d81798698ba34082671f57b962a7a6be48487520d007c4db9c67de8e3ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22P6iESMv-A6xOjUnD2lw_alaR7XYAL_28%22%3B%7D; Hm_lvt_df2da21ec003ed3f44bbde6cbef22d1c=1621827883; _pk_testcookie.3.7c47=1; NTKF_T2D_CLIENTID=guestBAD2C13E-E696-CA78-716C-9C798FFE38E6; nTalk_CACHE_DATA={uid:kf_9479_ISME9754_guestBAD2C13E-E696-CA,tid:1621827883006310}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221799c79aa535-02c2c0befc7075-2363163-2073600-1799c79aa54dc6%22%2C%22%24device_id%22%3A%221799c79aa535-02c2c0befc7075-2363163-2073600-1799c79aa54dc6%22%2C%22props%22%3A%7B%7D%7D; anonymousId=1799c79aa535-02c2c0befc7075-2363163-2073600-1799c79aa54dc6; QDS_COOKIE=user%3Ainfo%3AEF9D3818-96DC-17D2-735F-4855EB5B04FE; QDS_LOGIN_INFO=%7B%22userName%22%3A%22qds7201686%22%2C%22avtar%22%3A%22%22%7D; _pk_ses.3.7c47=1; _pk_id.3.7c47=adad8e2a79e78648.1621827883.2.1621835103.1621834890.; Hm_lpvt_df2da21ec003ed3f44bbde6cbef22d1c=1621835103'}

    def first(self,key):
        url = 'https://so.quandashi.com/search/search/search-list'
        data = {
            'key': key,
            'param': '2',
            'page': '0',
            'pageSize': '20',
            'styles': 'all,jingzhun,high_low_similar,bufen,jiazi,jianzi,bianzi,huanxu,pinyin,teshuzi,xingjinzi',
            'host': 'so.quandashi.com',
            'brandSource': '0',
            'reviewWrit': '0',
            'isReload': '1'
        }
        req = requests.post(url=url, data=data, headers=self.headers).text
        adas = re.findall('"detailId":"(.*?)","', req)
        if adas:
            self.switch = False
            return adas
        return '403'

        return adas
    def page(self,adas):
        if self.switch:
            print('key错误')
            return '403'
        url = 'https://so.quandashi.com/index/searchdetail/' + adas + '.html?type_flag=000'
        i = requests.get(url=url, headers=self.headers).text
        i_new = etree.HTML(i)
        name = i_new.xpath('//div[@class="brand-left"]/div[@class="brand-img"]/img/@alt')[0]
        Commodity_category = re.findall('<span>商品类别：(.*?)</span>', i)[0]
        Applicant = i_new.xpath('//td[@class="td-content"]//i/text()')[0]
        address = re.findall('<td class="td-title">申请人地址</td>\n.*?<td class="td-content">(.*?)</td>', i)[0]
        service_items = i_new.xpath('//ul[@class="product-list"]/li//text()')
        service = ''
        for iasd in service_items:
            service += iasd + '\n'
        Agent_name = i_new.xpath('//td[@class="td-content"]/a[@target="_blank"]/text()')[0]
        times = re.findall('<td class="td-title">申请日期</td>\n.*?<td class="td-content">(.*?)</td>', i)[0]
        falu = re.findall('<td class="td-title">法律状态</td>\n.*?<td class="td-content"><strong>(.*?)</strong></td>',i)[0]
        item = {'法律状态':falu,'名字': name,'商品类别':Commodity_category,'申请日期':times,'申请人名称':Applicant,'申请人地址':address,'商品/服务项目':service,'代理人名称':Agent_name}
        return item
    def mysql(self,item):
        if self.switch:
            print('key错误')
            return '403'
        connectr = pymysql.connect(
            host='localhost',
            user='root',
            port=9999,
            password='Tang5230',
            charset='utf8',
            db='quan'
        )
        cursor = connectr.cursor()
        sql = """INSERT INTO athletic_shoes(Trade_name,Commodity_category, Applicantis_name, Applicantis_address,Date_of_Application,GoodsServices,Agent_name)
                         VALUES ("%s","%s","%s","%s","%s","%s","%s")""" % (item['名字'],item['商品类别'],item['申请人名称'],item['申请人地址'],item['申请日期'],item['商品/服务项目'],item['代理人名称'])
        cursor.execute(sql)
        connectr.commit()
        cursor.close()
        connectr.close()

master = Master()
adas = master.first(key=1)
for i in adas:
    item = master.page(i)
    print(item)