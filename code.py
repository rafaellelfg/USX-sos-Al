import psycopg2

def bug_found(cursor,conn):
    tester_id = input("\n Ur tester id ")
    desricption = input ("\n give a description")
    sql_command = """
    insert into report(tester_id,description,status)
    values(%s,%s,'start')
    """
    cursor.execute(sql_command,(tester_id,desricption))
    conn.commit()
    print ("\n bug sended")

def bug_in_process (cursor,conn) :
    dev_id = input("\n Ur dev id ")
    bug_number = input ("\n Enter the bug number ")
    sql_command = """
    update report set status = 'in process' , dev_id = %s   where rep_id = %s
    """
    cursor.execute(sql_command,(dev_id,bug_number))
    conn.commit()
    print ("\n debugging started")
    
    
def resolve (cursor , conn):
    dev_id = input("\n Ur dev id ")
    bug_number = input ("\n Enter the bug number ")
    sql_command = """
    update report set status = 'resolved' , dev_id = %s   where rep_id = %s
    """
    cursor.execute(sql_command,(dev_id,bug_number))
    conn.commit()
    print ("\n debugging finished")

def tester_mode(cursor,conn):
    while True :
        action = input("\n 1. record_bug 2. exit ")
        if action == "1":
            bug_found(cursor,conn)
        elif action == "2":
            break
        else :
            print ("fuck off")

def dev_mode(cursor,conn):
    while True :
        action = input("\n 1. fix bug 2. finished bug 3. exit ")
        if action == "1":
            bug_in_process(cursor,conn)
        elif action == "2":
            resolve(cursor,conn)
        elif action == "3" :
            break
        else :
            "wrong command"

def main():
    conn = psycopg2.connect(dbname ="test_db", user = "postgres", password = "sosal1337")
    cursor = conn.cursor()
    while True :
        role = input("\n 1.Tester 2.Dev or exit " )
        if role == "exit":
            break
        elif role == "1":
            tester_mode(cursor,conn)
        elif role == "2":
            dev_mode(cursor,conn)
        else :
            "man fuck up urself"
    cursor.close()
    conn.close()
    
if __name__ == "__main__":
    main()
    