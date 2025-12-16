import streamlit as st
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import pandas as pd
from faker import Faker

# SQLite 데이터베이스 연결
engine = create_engine('sqlite:///users.db')
metadata = MetaData()

# 테이블 정의
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('email', String),
                    Column('address', String))

# 테이블 생성
metadata.create_all(engine)

# Faker를 사용해서 가짜 데이터 생성
fake = Faker()

def generate_fake_data(n=10):
    with engine.connect() as conn:
        # 기존 데이터 삭제
        conn.execute(users_table.delete())
        # 가짜 데이터 삽입
        for _ in range(n):
            # Object Relation Mapping(ORM)
            # 파이썬 object를 db의 relation으로 mapping해주는 것
            # SQL문으로 바꿔주는 기능이 들어가 있다.
            conn.execute(users_table.insert().values(
                name=fake.name(),
                email=fake.email(),
                address=fake.address()
            ))
        conn.commit()

# 가짜 데이터 생성 버튼
if st.button('Generate Fake Data'):
    generate_fake_data(20)
    st.success('Fake data generated!')

# 데이터 조회
def load_data():
    with engine.connect() as conn:
        query = "SELECT * FROM users"
        # return pd.read_sql(users_table.select(), conn)로도 쓸 수 있음
        return pd.read_sql(query, conn)

# 데이터 로드 및 표시
data = load_data()
st.write(data)