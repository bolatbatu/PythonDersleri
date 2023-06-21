from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///Örnekler/38.2.example.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    posts = relationship("BlogPost", back_populates="user")


class BlogPost(Base):
    __tablename__ = "blog_post"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    create_date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="posts")


Base.metadata.create_all(engine)


def register_user(username, password):
    user = User(username=username, password=password)
    session.add(user)
    session.commit()


def login_user(username, password):
    user = session.query(User).filter_by(username=username).first()
    if user and user.password == password:
        return user
    return None


register_user("john_doe", "password123") 
 

user = login_user("john_doe", "password123") 
if user:
    print("Login successful!")
else:
    print("Invalid username or password.")
