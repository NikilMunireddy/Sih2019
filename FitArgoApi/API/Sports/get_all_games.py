try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json
import time

def get_all_games():
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="SELECT * FROM games"
        cursor.execute(SQL_QUERY,)
        result=cursor.fetchall()
        result_dict={}
        res=[]
        if(len(result)>0):
            try:
                for row in result:
                    result_dict={
                        "gid":row[0],
                        "uid":row[8],
                        "location_lat":row[1],
                        "location_long":row[2],
                        "pdate":str(row[3]),
                        "stime":str(row[4]),
                        "etime":str(row[5]),
                        "level":row[6],
                        "participants":row[7],
                        "address":row[9],
                        "gname":row[10]
                    }
                    res.append(result_dict)
            except IndexError as e:
                print(str(e))
                raise Exception


    except (Exception,psycopg2.Error) as error:
        print(error)
        raise Exception
    return res