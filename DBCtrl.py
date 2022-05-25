import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.2.3",
  user="DT001",
  password="Teleport1536!",
  database="INQNET_GUI"
)

cur = mydb.cursor()
cur.execute("create table if not exists ExfoJSI (wavelengthA1 float, bandwidthA1 float, wavelengthB2 float, bandwidthB2 float, wavelengthA2 float, bandwidthA2 float, wavelengthB1 float, bandwidthB1 float, datetime datetime)")

def recFilter(WLA1, BWA1, WLB2, BWB2, WLA2, BWA2, WLB1, BWB1):
    querr="insert into ExfoJSI (wavelengthA1, bandwidthA1, wavelengthB2, bandwidthB2, wavelengthA2, bandwidthA2, wavelengthB1, bandwidthB1, datetime) values ("+str(WLA1)+", "+str(BWA1)+", "+str(WLB2)+", "+str(BWB2)+", "+str(WLA2)+", "+str(BWA2)+", "+str(WLB1)+", "+str(BWB1)+", NOW())"
    cur.execute(querr)
    mydb.commit()
    print(querr)
