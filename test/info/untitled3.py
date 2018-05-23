from flask import Flask, render_template
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
app = Flask(__name__)

'''
流程：
1.模板：render_template
2.表单：wtf，
3.数据库
4.视图
5.实现删除数据
'''

app = Flask(__name__)
# 配置密似
app.config['SECRET_KEY'] = '4psbwnFUP1akINFeWT3LdLV6hO10P7cRpvpvTMJXgQA=='
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/author_book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 给app赋予了的ORM操作的能力
db = SQLAlchemy(app)
# 定义表单类
class Form(FlaskForm):
    author = StringField(validators=[DataRequired()])
    book = StringField(validators=[DataRequired()])
    submit = SubmitField(label='保持')

class Author(db.Model):
    # 定义了表名
    __tablename__ = 'authors'
    # 定义了数据
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    book = db.Column(db.String(32),unique=True)
    def __repr__(self):
        return 'author:%s' % self.name,'book:%s' % self.book



@app.route('/',methods=['GET','POST'])
def index():
    form = Form()

    auth = Author.query.all()

    if form.validate_on_submit():
        wtf_auth = form.author.data

        au = Author(name=wtf_auth)

        try:
            db.session.add_all([au])
            db.session.commit()

        except Exception as e:
            print(e)

            db.session.rollback()
        auth = Author.query.all()


    return render_template("author.html",form=form,auth=auth)

@app.route('/delete<id>')
def del_author(id):
    author = Author.query.filter_by(id=id).first()
    db.session.delete(author)
    db.session.commit()
    return render_template(url_for('index'))



if __name__ == '__main__':
    # 先删除后创建
    db.drop_all()
    db.create_all()
    # 添加测试数据
    au_xi = Author(name='我吃西红柿',book='吞噬星空')
    au_qian = Author(name='萧潜',book='寸芒')
    au_san = Author(name='唐家三少',book='飘渺之旅')

    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san])
    # 提交会话
    db.session.commit()
    app.run(debug=True)
    app.run()
