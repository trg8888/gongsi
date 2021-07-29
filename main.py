import random

from flask import Flask, request, render_template,session,redirect,url_for
from one import RegisterForm
from MysqlUtil import MysqlUtil
from namessssss import indexss,Linsert  #index是衣服
app = Flask(__name__)
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'
from username import hello

@app.route('/register', methods=['GET', 'POST'])
def register():
    usernames = '赶快注册'
    form = RegisterForm(request.form)
    print(request.method)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        print(email)
        username = form.username.data
        password = form.password.data
        db = MysqlUtil()
        sql = "insert into users(email,username,password)values ('%s','%s','%s')" % (email,username,password)
        db.insert(sql)
        usernames = '注册成功'

    return render_template('register.html', form=usernames)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        return redirect('/3')
    messages = '内部'
    if 'iogged_in' in session:
        return redirect(url_for('register'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = "select * from users where username = '%s'" % username
        db = MysqlUtil()
        result = db.fetchone(sql)
        if result:
            if password == result['password']:
                session['logged_in'] = True
                session['username'] = username
                return redirect('/3')
            else:
                messages = '密码错误'
        else:
            messages = '用户不存在'

    return render_template('index.html',messages=messages)

@app.route('/3', methods=['GET', 'POST'])
def is_log():
    if 'logged_in' in session:
        sju = '内部一键配置网站'
        if request.method == 'POST':
            username = request.form['username']
            password = random.randint(0,1)
            if not username :
                return render_template('three.html',sadsado='参数不全')
            sju = hello(link_nots=username,qidong=int(password))
            if sju != '200':
                sju = hello(link_nots=username,qidong=int(password))
        return render_template('three.html',sadsado=sju)
    else:
        return '请登录',403
#yifu=sadas&xiezi=dasd&baobao=sadasd&Cookie=asdsa
@app.route('/4',methods=['GET', 'POST'])
def is_logs():
    if 'logged_in' in session:
        if request.method == 'POST':
            Cookie = request.form['Cookie']
            if not Cookie:
                return 'Cookie不存在禁止发送'
            yifu = request.form['yifu']
            xiezi = request.form['xiezi']
            baobao = request.form['baobao']
            print(yifu,xiezi,baobao)
            if yifu:
                indexss(link=yifu,cookie=Cookie)
            else:
                yifu = ''
            if xiezi:
                Linsert(link=xiezi,cookie=Cookie)
            else:
                xiezi = ''
            if baobao:
                Linsert(link=baobao,cookie=Cookie)
            else:
                baobao = ''
            return '成功，你使用的网站'+yifu+'\n'+xiezi+'\n'+baobao
        return render_template('4.html')
    else:
        return '请登录',403
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
