import UserI
import databaseI

if __name__ == "__main__":
    databaseT = r"C:\Users\danis\PycharmProjects\5AHW\SteinScherePapierEchseSpock\StScPaLiSp_Python.db"
    databaseI.create_database(databaseT)
    UserI.mainmenu()

