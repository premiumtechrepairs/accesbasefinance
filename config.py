import pymysql

connexion = pymysql.connect(
    host="localhost",
    user="app_finance",
    password="Finance2026!",
    database="societytracker",
    cursorclass=pymysql.cursors.DictCursor
)