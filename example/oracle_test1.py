from token import NAME
import oracledb

# 데이터베이스 접속 정보 설정
dsn = oracledb.makedsn("localhost", 1521, service_name="XE")
conn = oracledb.connect(user="c##mbc", password="qwer1234", dsn=dsn)

# 쿼리 실행을 위한 커서 생성
cursor = conn.cursor()

#테이블 생성
# try:
#     cursor.execute("""
#         CREATE TABLE test_table (
#             id NUMBER PRIMARY KEY,
#             data VARCHAR2(100)
#         )
#     """)
#     print("Table created successfully")
# except oracledb.DatabaseError as e:
#     print(f"Error creating table: {e}")

# INSERT 예제
# try:
#     cursor.execute("INSERT INTO test_table (id, data) VALUES (:1, :2)", [1, "Test data"])
#     conn.commit()
#     print("Data inserted successfully")
# except oracledb.DatabaseError as e:
#     print(f"Error inserting data: {e}")


# SELECT 예제
try:
    cursor.execute("SELECT * FROM test_table")
    for row in cursor:
        print(row)
except oracledb.DatabaseError as e:
    print(f"Error fetching data: {e}")


#select - emp table
name = input("input name...")
print(name) 

try:
    SELECT_QUERY = "SELECT * FROM EMP WHERE ENAME='" + name.upper() + "'"
    print(SELECT_QUERY)

    cursor.execute(SELECT_QUERY)
    for row in cursor:
        print(row)
except oracledb.DatabaseError as e:
    print(f"Error fetching data: {e}")

# 커서 및 커넥션 닫기
# cursor.close()
# conn.close()
