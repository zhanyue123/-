from flask import Flask, render_template
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
app = Flask(__name__)

'''
流程：
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

        except Excepti333333333333333333333333333333333333

33333333333333333333333333333333333333333333333333V

33333333333333333333333333333333333

    au_xi = Author(name='我吃西红柿',book='吞噬星空')
    au_qian = Author(name='萧潜',book='寸芒')
    au_san = Author(name='唐家三少',book='飘渺之旅')

    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san])
    # 提交会话
    db.session.commit()
    app.run(debug=True)
    app.run()
