from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# DBへのパスを定義
database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'trellolike.db')
# 定義したパスでDBを構築
engine = create_engine('sqlite:///' + database_file, convert_unicode=True)
# 接続インスタンスを生成
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Baseオブジェクトを生成
Base = declarative_base()
# DBの設定を注入
Base.query = db_session.query_property()

def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)
