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
    with open('users.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    user = User(username=username, password=password)
    session.add(user)
    session.commit()


def login_user(username, password):
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                return User(username=username, password=password)
    return None


# Usage examples:
def main():
    register_user("john_doe", "password123")  # Register a new user
    register_user("jane_smith", "p@ssw0rd")  # Register another user

    user = login_user("john_doe", "password123")  # Login with username and password
    if user:
        print("Login successful!")
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    main()
