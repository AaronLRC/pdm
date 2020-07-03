import time
import psycopg2
import psycopg2.extras
import random

TABLE_NAME = 'conditions'


# def measure_time(func):
#     def time_it(*args, **kwargs):
#         time_started = time.time()
#         func(*args, **kwargs)
#         time_elapsed = time.time()
#         print("{execute} running time is {sec} seconds for inserting {rows} rows.".format(execute=func.__name__,
#                                                                                           sec=round(
#                                                                                               time_elapsed - time_started,
#                                                                                               4), rows=len(kwargs.get('values'))))

#     return time_it


class PsycopgTest():

    def __init__(self, num_rows):
        self.num_rows = num_rows

    # def create_dummy_data(self):
    #     values = []
    #     for i in range(self.num_rows):
    #         values.append((i + 1, 'test'))
    #     return values

    def connect(self):
        conn_string = "host={0} user={1} dbname={2} password={3}".format('104.154.246.252',
                                                                         'postgres',
                                                                         'datadb',
                                                                         'postgres')
        self.connection = psycopg2.connect(conn_string)
        self.cursor = self.connection.cursor()

    # def create_table(self):
    #     self.cursor.execute(
    #         "CREATE TABLE IF NOT EXISTS {table} (id INT PRIMARY KEY, NAME text)".format(table=TABLE_NAME))
    #     self.connection.commit()

    # def truncate_table(self):
    #     self.cursor.execute("TRUNCATE TABLE {table} RESTART IDENTITY".format(table=TABLE_NAME))
    #     self.connection.commit()

    # @measure_time
    def method_execute(self, kit, a1, a2):
        """Loop over the dataset and insert every row separately"""

        self.cursor.execute("INSERT INTO {table}(time, location, temperature, humidity) VALUES (NOW(),\
             '{kit}', {a1}, {a2}) ;".format(table=TABLE_NAME, kit=kit, a1=a1, a2=a2))
        self.connection.commit()

    # @measure_time
    # def method_execute_many(self, values):
    #     self.cursor.executemany("INSERT INTO {table} VALUES (%s, %s)".format(table=TABLE_NAME), values)
    #     self.connection.commit()

    # @measure_time
    def method_execute_batch(self,  kit, a1, a2):
        values = []
        values.append((1, 'NOW()'))
        values.append((2, kit))
        values.append((3, a1))
        values.append((4, a2))
        psycopg2.extras.execute_batch(
            self.cursor, "INSERT INTO {table} VALUES ('%s','%s',%f, %f) ;".format(table=TABLE_NAME), values)
        self.connection.commit()

    # @measure_time
    # def method_string_building(self, kit, a1,a2):
    #     argument_string = ",".join("('%s', '%s')" % (x, y) for (x, y) in values)
    #     self.cursor.execute("INSERT INTO {table} VALUES".format(table=TABLE_NAME) + argument_string)
    #     self.connection.commit()


def main():
    psyco = PsycopgTest(10000)
    psyco.connect()
    # values = psyco.create_dummy_data()
    # psyco.create_table()
    # psyco.truncate_table()
    kits = ['kit#1', 'kit#2', 'kit#3']

    a1 = 20
    a2 = 45
    a3 = 58
    a4 = 70

    iterations = int((1/0.05)*60*10*100000)
    print(iterations, end="\n")

    for i in range(iterations):
        a1 += random.uniform(-1, 1)
        a2 += random.uniform(-2, 2)
        a3 += random.uniform(-3, 3)
        a4 += random.uniform(-4, 4)

        psyco.method_execute_batch(kits[0], a1, a2)
        psyco.method_execute_batch(kits[1], a3, a4)
        print(i, end=',')
    # psyco.method_execute_many(values=values)
    # psyco.method_execute_batch(values=values)
    # psyco.method_string_building(values=values)


if __name__ == '__main__':
    main()
