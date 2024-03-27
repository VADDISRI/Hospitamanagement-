import pyodbc


class DBConnection:
    con = None

    @staticmethod
    def getConnection():
        if DBConnection.con is None:
            try:
                DBConnection.con = pyodbc.connect(
                    'Driver={SQL Server};'
                    'Server=LAPTOP-M33JLBTA\SQLEXPRESS;'
                    'Database=hospital;'
                )
                print("DB Connected !!!")
            except pyodbc.Error as err:
                print(f"Error connecting DB: {err}")

        return DBConnections