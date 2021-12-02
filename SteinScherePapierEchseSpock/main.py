import UserI
import databasehandler

if __name__ == "__main__":
    dbPath = r"C:\Users\Michi\Desktop\Schule\5AHWII\Python\SWP_PY\SteinScherePapierEchseSpock\StScPaLiSp_Python.db"
    databasehandler.create_database(dbPath)
    UserI.mainmenu()

