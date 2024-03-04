from sqlalchemy import select, and_
from database.models import CodeTable
from database.database import Base, session_maker, engine
import datetime


class ORM:
    @staticmethod
    def create_table():
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_data_unique_code(code: str, user: str):

        with session_maker() as session:

            today = str(datetime.date.today().strftime('%d_%m_%y'))
            existing_code = session.query(CodeTable).filter_by(code=code).first()
            if existing_code:
                print(f"Код {code} уже существует.")
                return False

            code_table = CodeTable(code=code, user=user, date=today)
            session.add(code_table)
            session.commit()
            return True

    @staticmethod
    def select_data():
        with session_maker() as session:
            query = select(CodeTable)
            result = session.execute(query)
            everithing = result.scalars().all()
            print(f'{everithing}')

    @staticmethod
    def select_today_codes(user: str):
        with session_maker() as session:

            today = str(datetime.date.today().strftime('%d_%m_%y'))

            query = (
                select(CodeTable.code)
                .where(
                    and_(
                        CodeTable.user == user,
                        CodeTable.date == today
                    )
                )
            )

            result = session.execute(query)
            codes = [row[0] for row in result.fetchall()]
            # print(codes)
            return codes
