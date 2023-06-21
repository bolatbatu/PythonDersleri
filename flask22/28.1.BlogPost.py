from flask import Flask, render_template, request, redirect


from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session 
from datetime import datetime

app = Flask(__name__)

engine = create_engine('sqlite:///blog_0.1.db')

# declarative base class
class Base(DeclarativeBase):
    pass

# user class
class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    posts: Mapped[list["BlogPost"]] = relationship(back_populates="user")

# blog post class
class BlogPost(Base):
    __tablename__ = "blog_post"

    id = mapped_column(Integer, primary_key=True)
    content: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    user_id = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="posts")

Base.metadata.create_all(engine)

# create session
session = Session(engine)
aktif_kullanici = str()
# create user
@app.route('/')
def home():
    return 'Welcome to the blogging application!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        kayit(username, password)
        return redirect('/login')
    return render_template('flask22/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        gisis(username, password)
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not aktif_kullanici:
        return redirect('/login')
    return render_template('dashboard.html', user=aktif_kullanici)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        content = request.form['content']
        post_ekle(content)
        return redirect('/dashboard')
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run()
