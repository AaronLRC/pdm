import psycopg2

host = "104.154.246.252"
database = "django"
user = "postgres"
pwd = "postgres"


def make_connection():

    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=pwd,
                            port="5432")
    print(conn)
    return conn


def execute_query(conn, c):

    query = ["""INSERT INTO api_medic_hypertable(time, kit_id, pres_card, frec_resp, temp_corp, caidas) VALUES (NOW(), '{}', {}, {}, {}, {}) ;""".format('AA0001', a1, a2, a3, a4),
             ]
    for m in range(len(query)):
        print(query[m])
        c.execute(query[m], vars=None)
        conn.commit()



def close_connection(conn):
    conn.close()


if __name__ == "__main__":
    conn = make_connection()
    c = conn.cursor()
    close_connection(conn)
