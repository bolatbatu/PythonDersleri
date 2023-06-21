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

engine = create_engine('sqlite:///Örnekler/37.2.example.db')



# declarative base class
class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employee"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    fullname: Mapped[str]
    nickname: Mapped[str] = mapped_column(String(64))
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    addresses: Mapped[list["Address"]] = relationship(back_populates="employee")


class Address(Base):
    __tablename__ = "address"

    id = mapped_column(Integer, primary_key=True)
    employee_id = mapped_column(ForeignKey("employee.id"))
    email_address: Mapped[str]

    employee: Mapped["Employee"] = relationship(back_populates="addresses")

Base.metadata.create_all(engine)

session = Session(engine) 

# Çalışan  ve adres ekleme
def employee_add(name, fullname, nickname, email_address):
    employee = Employee(name=name, fullname=fullname, nickname=nickname)
    address = Address(email_address=email_address)
    employee.addresses.append(address)
    session.add(employee)
    session.commit()



def employee_query(name):
    employee = session.query(Employee).filter_by(name=name).first()
    print(f"{employee.fullname} eposta adresi : {employee.addresses[0].email_address}")
