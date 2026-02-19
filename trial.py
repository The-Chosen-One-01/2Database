#Importing SQLite
import sqlite3

#Connecting database
db = sqlite3.connect("games.db")

#Adding cursor
cursor = db.cursor()

#Adding query
col = {"A":"game.ID", "B":"game.name", "C":"main_genre.main_genre", "D":"game.price_NZD", "E":"game.released", "F":"studio.studio"}
order = {"A":"game.ID", "B":"game.name", "C":"main_genre.main_genre", "D":"game.price_NZD", "E":"game.released", "F":"studio.studio"}
#Creating query
def creating_query(col, order, cursor):
    col_list = list(col) + ["G"]
    col_func = ["ID of games", "Names of games", "Main genres", "Prices of games", "Release date of games", "Studios of games", "End"]
    order_list = list(order)
    order_func = ["ID of games", "Names of games", "Main genres", "Prices of games", "Release date of games", "Studios of games"]
    query = "select"

    while True:
        print("Choose any of these to add to your column")
        for i in range(7):
            print(f'{col_list[i]}: {col_func[i]}')
        chosen = input("Type here: ").upper()
        if chosen == "G" or chosen not in col_list:
            break
        query += ' ' + col[chosen] + ','
        print(query)
    query = query[:len(query)-1]
    query += " from game join main_genre, studio on game.main_genre_ID = main_genre.ID and game.studio_ID = studio.ID order by"
    print(query)

    print("What do you want to sort it by?")
    for i in range(6):
        print(f'{order_list[i]}: {order_func[i]}')
    query += ' ' + order[input("Type here: ").upper()] + ';'

    cursor.execute(query)
    return cursor.fetchall()

#Executing query
result = creating_query(col, order, cursor)

#Returning results
for column in result:
    out = ''
    for row in column:
        out += f'| {row} |'
    print(out)


#Closing database
db.close()


    
