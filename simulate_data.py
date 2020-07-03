import psycopg2
import random
import time

host="104.154.246.252"
database="datadb"
user="postgres"
pwd="postgres"


def make_connection():

    conn = psycopg2.connect(database=database,
                            user=user, 
                            password=pwd,
                            host=host, 
                            port="5432")
    print(conn)
    return conn                            

def execute_query(conn,c,a1,a2,a3,a4):

    query=["""INSERT INTO conditions(time, location, temperature, humidity) VALUES (NOW(), 'kit#1', {}, {}) ;""".format(a1,a2),
            """INSERT INTO conditions(time, location, temperature, humidity) VALUES (NOW(), 'kit#2', {}, {});""".format(a3,a4)]
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()

def generate_random_data(conn,c):
    
    a1=20
    a2=45
    a3=58
    a4=70

    iterations=int((1/0.05)*60*10*100000)
    print(iterations, end="\n")

    for i in range(iterations):
        a1+=random.uniform(-1, 1)
        a2+=random.uniform(-2, 2)
        a3+=random.uniform(-3, 3)
        a4+=random.uniform(-4, 4)
        execute_query(conn,c,a1,a2,a3,a4)

        if ((i%200==0) and (i!=0)):

            close_connection(conn)
            conn=make_connection()
        
        
        # time.sleep(0.05)
        # print(i)



    

def close_connection(conn):
    conn.close() 

if __name__ == "__main__":
    conn=make_connection()
    c = conn.cursor()
    generate_random_data(conn,c)
    close_connection(conn)
