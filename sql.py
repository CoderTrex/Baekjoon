import mysql.connector

# MySQL 접속 정보
host = 'localhost'
port = 3306
database = 'webrtc'
username = 'root'
password = '1234'

# SQL 문장들
sql_commands = [
    "DROP TABLE IF EXISTS flight;",
    "DROP TABLE IF EXISTS attendance;",
    "DROP TABLE IF EXISTS lecture_users;",
    "DROP TABLE IF EXISTS lecture;",
    "DROP TABLE IF EXISTS users;"
]

try:
    # MySQL 데이터베이스에 연결
    conn = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=username,
        password=password
    )

    # 커서 생성
    cursor = conn.cursor()

    # SQL 문장 실행
    for sql_command in sql_commands:
        cursor.execute(sql_command)
    
    # 변경사항 저장
    conn.commit()

    print("SQL 문장 실행 완료")
    # 연결 종료
    if conn:
        conn.close()

except mysql.connector.Error as e:
    print(f"에러 발생: {e}")

