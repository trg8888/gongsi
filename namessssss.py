import requests
from lxml import etree
import re
def indexss(link,cookie):
    headers = {
        'Cookie': 'PHPSESSID='+cookie
    }
    response = requests.get(link, headers=headers).text
    sadsa = re.findall('<a href="(.*?)">编辑</a>', response)
    securityToken = re.findall('<input type="hidden" value="(.*?)" name="securityToken" />', response)[0]
    nexts = etree.HTML(response)

    for i in sadsa:
        id = re.findall(r'id=(\d{1,4})',i)[0]
        response_new = requests.get(url=i, headers=headers).text
        product = re.findall(
            r'<td class="value"><input type="text" class="input-text required-entry" value="(.*?)" name=".*" id="product-sku" /></td>',
            response_new)[0]
        product_1 = re.findall(
            r'<td class="value"><input type="text" class="input-text required-entry" value="(.*?)" name=".*" id="product-name" /></td>',
            response_new)[0]
        product_2 = re.findall(r'<textarea name="product.*" id="product-description">(.*?)</textarea>',response_new)[0]
        product_3 = re.findall(r'<td class="value"><input type="text" class="input-text" value="(.*?)" name=".*" id="product-image" /></td>',response_new)[0]
        product_4 = re.findall(r'<td class="value"><input type="text" class="input-text required-entry" value="(.*?)" name=".*" id="product-price" /></td>',response_new)[0]
        product_5 = re.findall(r'<option selected="selected" value="(.*?)">.*</option>',response_new)[0]
        linkss = re.findall(r'https://www.(.*?)/product', link)[0]
        post_link = 'https://www.'+linkss+'/product.php?action=save'
        response_xpath = etree.HTML(response_new)
        response_xpaths = response_xpath.xpath('//tbody[@id="option-1"]//input[@class="checkbox"]/@value')
        data = {
            'product[product_id]': id,
            'options[]': 1,
            'option_requireds[]': 1,
            'option_values[1][]': response_xpaths,
            'securityToken': securityToken,
            'product[sku]':product,
            'product[name]':product_1,
            'product[description]':product_2,
            'product[image]':product_3,
            'product[specials_price]':'0.0000',
            'product[price]':product_4,
            'product[master_category_id]':product_5,
            'product_to_category[]':product_5,
            'product[meta_title]':product_1,
            'product[meta_keywords]':product_1,
            'product[meta_description]':product_1,
            'product[stock_qty]': 0,
            'product[in_stock]': 1,
            'product[status]': 1,
            'product[sort_order]': 0,
            'product[viewed]': 0,
            'product[ordered]': 0,

        }
        post = requests.post(url=post_link,data=data,headers=headers).text
    sadas = nexts.xpath('//a[@title="Next"]/@href')
    if sadas:
        indexss(link=sadas[0],cookie=cookie)
def Linsert(link,cookie):
    headers = {
        'Cookie': 'PHPSESSID='+cookie
    }
    session = requests.session()
    response = session.get(link, headers=headers).text
    sadsa = re.findall('<a href="(.*?)">编辑</a>', response)
    securityToken = re.findall('<input type="hidden" value="(.*?)" name="securityToken" />', response)[0]
    nexts = etree.HTML(response)

    for i in sadsa:
        id = re.findall(r'id=(\d{1,4})',i)[0]
        response_new = session.get(url=i, headers=headers).text
        product = re.findall(
            r'<td class="value"><input type="text" class="input-text required-entry" value="(.*?)" name=".*" id="product-sku" /></td>',
            response_new)[0]
        product_1 = re.findall(
            r'<td class="value"><input type="text" class="input-text required-entry" value="(.*?)" name=".*" id="product-name" /></td>',
            response_new)[0]
        product_2 = re.findall(r'<textarea name="product.*" id="product-description">(.*?)</textarea>',response_new)[0]
        product_3 = re.findall(r'<td class="value"><input type="text" class="input-text" value="(.*?)" name=".*" id="product-image" /></td>',response_new)[0]
        product_4 = re.findall(r'<td class="value"><input type="text" class="input-text required-entry" value="(.*?)" name=".*" id="product-price" /></td>',response_new)[0]
        product_5 = re.findall(r'<option selected="selected" value="(.*?)">.*</option>',response_new)[0]
        linkss = re.findall(r'https://www.(.*?)/product', link)[0]
        post_link = 'https://www.'+linkss+'/product.php?action=save'
        print(id)
        data = {
            'product[product_id]': id,
            'options[]': 2,
            'option_requireds[]': 2,
            'option_values[2][]': [7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            'securityToken': securityToken,
            'product[sku]':product,
            'product[name]':product_1,
            'product[description]':product_2,
            'product[image]':product_3,
            'product[specials_price]':'0.0000',
            'product[price]':product_4,
            'product[master_category_id]':product_5,
            'product_to_category[]':product_5,
            'product[meta_title]':product_1,
            'product[meta_keywords]':product_1,
            'product[meta_description]':product_1,
            'product[stock_qty]': 0,
            'product[in_stock]': 1,
            'product[status]': 1,
            'product[sort_order]': 0,
            'product[viewed]': 0,
            'product[ordered]': 0,

        }
        # responsesss = session.post(url=post_link,data=data).text
        # prit = etree.HTML(responsesss)
        # sadas = prit.xpath('//p[@class="success-msg"]/text()')
        # print(responsesss)
    sadas = nexts.xpath('//a[@title="Next"]/@href')
    if sadas:
        Linsert(link=sadas[0],cookie=cookie)

# indexss(link='https://www.vtetni.com/grzh1037-titan/product.php?filter_category_id=1',cookie='vilo8hb7vtk8eheb74cil74rmu1quasv')