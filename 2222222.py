import requests



shangchuan_3_data = {
    'securityToken': '209475d07f825b05bc0e6f117983e86d',
    'MAX_FILE_SIZE': '100000000',
    'action': 'product',
}

shangchuan_3_files = {
    'usrfl': ('1.csv', open(r'C:\Users\Admin\Desktop\NIMA\1.csv', 'r'), 'application/vnd.ms-excel')
}
shangchuan_3 = 'https://www.tabmzo.com/grzh1259-titan/import_old.php'
shangchuan_3_post = requests.post(url=shangchuan_3, data=shangchuan_3_data, files=shangchuan_3_files)
print(shangchuan_3_post.text)