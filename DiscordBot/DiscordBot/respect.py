import WorkWithSQLite
import datetime

def add_respect(user_id: int) -> bool:
    data = WorkWithSQLite.user_info(user_id)

    if data[3] < int((datetime.datetime.now() - datetime.timedelta(minutes=60)).timestamp()):
        data = (data[0], data[1]+1, data[2], int((datetime.datetime.now()).timestamp()))
        WorkWithSQLite.write_user_info(data)
        print(data)
        return True
    else:
        return False

def get_respect(user_id: int) -> int:
    return WorkWithSQLite.user_info(user_id)[1]


