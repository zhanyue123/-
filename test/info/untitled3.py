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
    




    au_xi = Author(name='我吃西红柿',book='吞噬星空')
    au_qian = Author(name='萧潜',book='寸芒')
    au_san = Author(name='唐家三少',book='飘渺之旅')

    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san])
    # 提交会话
    db.session.commit()
    app.run(debug=True)
    app.run()
