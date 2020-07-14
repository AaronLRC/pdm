import psycopg2
import random
import time

host = "104.154.246.252"
database = "django"
user = "postgres"
pwd = "postgres"


kit_id_value=input('Ingrese código del kit: ')

def make_connection():

    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")
    print(conn)
    return conn


def execute_query(conn, c, a1, a2, a3, a4):


    query = ["""INSERT INTO api_medic_hypertable(time, kit_id, pres_card, frec_resp, temp_corp, caidas) VALUES (NOW(), '{}', {}, {}, {}, {}) ;""".format(kit_id_value, a1, a2, a3, a4),
             ]
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()


def generate_random_data(conn, c):

    a1 = 85
    a2 = 15
    a3 = 40
    a4 = 1

    iterations = int((1/0.05)*60*10*100000)
    print(iterations, end="\n")

    for i in range(iterations):
        a1 += random.uniform(-1, 1)
        a2 += random.uniform(-0.1, 0.1)
        a3 += random.uniform(-0.1, 0.1)
        a4 += random.randint(-1, 1)
        execute_query(conn, c, a1, a2, a3, a4)

        if ((i % 15 == 0) and (i != 0)):

            close_connection(conn)            
            conn = make_connection()
            c = conn.cursor()

        time.sleep(1)
        # print(i)


def close_connection(conn):
    conn.close()


if __name__ == "__main__":

    conn = make_connection()
    c = conn.cursor()
    generate_random_data(conn, c)
    close_connection(conn)
