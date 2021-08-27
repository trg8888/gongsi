from flask import render_template,request
from model import db,app,Book,Writer,Quantity



@app.route('/')
def index():
    ceshi = {
        'name':'0',
        'miam':'https://download.csdn.net/download/w837571206/10040769'

    }
    return render_template('login.html',ceshi=ceshi)


@app.route('/ceshi', methods=['POST'])
def ceshi():
    if request.method == 'POST':
        return {'name':'0'}

@app.route('/admin')
def admin():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/member-list',methods=['GET','POST'])
def member_list():
    if request.method == 'POST':
        id_ = request.form.get('id')

        if not id_:
            return '403',403
        delede = Book.query.get(id_)
        print(delede)
        if delede:
            db.session.delete(delede)
            db.session.commit()
        return render_template('member-list.html')
    quantitys = Book.query.all()

    return render_template('member-list.html',quantitys=quantitys)

@app.route('/secondary',methods=['POST'])
def secondary():
    if request.method == 'POST':
        id_ = request.form.get('id')
        if not id_:
            return '403',403
        name = Book.query.filter_by(id=id_).first()
        if request.form['verdict'] == 'True':
            name.state = False
        else:
            name.state = True
        db.session.add(name)
        db.session.commit()
        return {'name':name.state}

@app.route('/secondary_add', methods=['GET'])
def secondary_add():
    return render_template('member-add.html')

@app.route('/secondary_add_1', methods=['GET'])
def secondary_add_1():
    names = Writer.query.all()
    return render_template('member-add_1.html',names=names)

@app.route('/secondary_add_post', methods=['POST'])
def secondary_add_post():
    name = request.form.get('username')
    note = request.form.get('note')
    if not name and not note:
        return '403',403
    writer = Writer(name=name,note=note)
    db.session.add(writer)
    db.session.commit()
    return ''


@app.route('/secondary_add_1_post',methods=['POST'])
def secondary_add_1_post():
    id_ = request.form.get('shipping')
    name = request.form.get('username')
    note = request.form.get('note')
    if not name and not id_ and not note:
        return '403',403
    book = Book(writer_id=id_,name=name,note=note)
    db.session.add(book)
    db.session.commit()
    return ''

@app.route('/member-edit/<int:id_>',methods=['GET'])
def member_edit(id_):
    book = Book.query.filter_by(id=id_).first()
    names = Book.query.all()
    return render_template('member-edit.html',book=book,names=names)

@app.route('/member_edit',methods=['POST'])
def member_edit_post():
    id_new = request.form.get('id')
    name = request.form.get('username')
    noto = request.form.get('note')
    writer = request.form.get('shipping')
    if not id_new and not name and not noto and not writer:
        return '403',403
    book = Book.query.filter_by(id=id_new).first()
    print(book)
    if book:
        book.id = id_new
        book.name = name
        book.writer_id = writer
        book.note = noto
        db.session.commit()
    return 'ok'

@app.route('/secondary_add_edit',methods=['GET'])
def member_add_edit():
    return render_template('member-add_edit.html')

@app.route('/member-list_one',methods=['GET','POST'])
def member_list_one():
    if request.method == 'POST':
        id_ = request.form.get('id')
        if not id_:
            return '403',403
        delede = Writer.query.get(id_)
        if delede:
            db.session.delete(delede)
            db.session.commit()
        return ''
    quantitys = Writer.query.all()
    return render_template('member-list_one.html',quantitys=quantitys)

@app.route('/member-edit_one/<int:id>',methods=['GET'])
def member_edit_one(id):
    writer = Writer.query.get(id)
    return render_template('member-add_2.html',writer=writer)


@app.route('/secondary_add_post_one', methods=['POST'])
def secondary_add_post_one():
    name = request.form.get('username')
    note = request.form.get('note')
    id_ = request.form.get('id')
    if not name and not note and not id_:
        return '403',403
    writer = Writer.query.filter_by(id=id_).first()
    if writer:
        writer.name = name
        writer.note = note
        db.session.commit()
    else:
        return '403',403
    return 'ok'

@app.route('/secondary_dele',methods=['POST'])
def secondary_dele():
    id_ = request.form.getlist('id[]')
    if not id_:
        return '403',403
    for i in id_:
        delede = Writer.query.get(i)
        if delede:
            db.session.delete(delede)
            db.session.commit()
        else:
            return '403',403
    return ''

@app.route('/secondary_dele_one',methods=['POST'])
def secondary_dele_one():
    id_ = request.form.getlist('id[]')
    if not id_:
        return '403',403
    for i in id_:
        delede = Book.query.get(i)
        if delede:
            db.session.delete(delede)
            db.session.commit()
        else:
            return '403',403
    return ''


@app.route('/order-list',defaults={'page':1},methods=['GET'])
@app.route('/page/<int:page>')
def order_list(page):
    names = Book.query.all()
    per_page = 10
    pagination = Quantity.query.order_by(Quantity.jiontime.desc()).paginate(page,per_page=per_page)
    informations = pagination.items
    return render_template('order-list.html',informations=informations, pagination=pagination,names=names)

@app.route('/order-add/<int:id>',methods=['GET'])
def order_add(id):
    informations = Quantity.query.filter_by(id=id).first()
    books = Book.query.all()
    return render_template('order-add.html',informations=informations,books=books)

@app.route('/order-add',methods=['POST'])
def order_add_post():
    id_ = request.form.get('id')
    name = request.form.get('name')
    price = request.form.get('price')
    attribute = request.form.get('attribute')
    picture = request.form.get('picture')
    description = request.form.get('description')
    shipping = request.form.get('shipping')
    if not all([name,price,attribute,picture,description,shipping,id]):
        return '403',403
    informations = Quantity.query.filter_by(id=id_).first()
    if not informations:
        return '403',403
    informations.name = name
    informations.price = price
    informations.attribute = attribute
    informations.picture = picture
    informations.description = description
    informations.book_id = shipping
    db.session.commit()
    return ''

@app.route('/order-delete',methods=['POST'])
def order_delete():
    id_ = request.form.get('id')
    if not id_:
        return '403',403
    informations = Quantity.query.filter_by(id=id_).first()
    if not informations:
        return '403',403
    db.session.delete(informations)
    db.session.commit()
    return ''


@app.route('/order-delete_list',methods=['POST'])
def order_delete_list():
    id_ = request.form.getlist('list_id[]')
    if not id_:
        return '403',403
    for i in id_:
        informations = Quantity.query.filter_by(id=i).first()
        if not informations:
            return '403',403
        db.session.delete(informations)
        db.session.commit()
    return ''

@app.route('/order-list-list',defaults={'page':1},methods=['GET'])
@app.route('/page-list/<int:nameid>/<int:page>')
def order_list_list(page,nameid=None):
    nameids = request.args.get('id')
    if not nameids:
        nameid = nameid
    else:
        nameid = nameids
    names = Book.query.all()
    per_page = 10
    pagination = Quantity.query.filter_by(book_id=nameid).order_by(Quantity.jiontime.desc()).paginate(page,per_page=per_page)
    informations = pagination.items
    return render_template('order-list.html',informations=informations, pagination=pagination,nameid=nameid,names=names)

if __name__ == "__main__":
    app.run(debug=True)