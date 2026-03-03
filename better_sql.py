import sqlite3
class Advanced_SQL:
    def __init__(self, db):
        self.db = sqlite3.connect(db)
        self.cursor = self.db.cursor()
        self.col = {"A":"game.ID", "B":"game.name", "C":"main_genre.main_genre", "D":"game.price_NZD", "E":"game.released", "F":"studio.studio"}
        self.order = {"A":"game.ID", "B":"game.name", "C":"main_genre.main_genre", "D":"game.price_NZD", "E":"game.released", "F":"studio.studio"}

    def creating_query(self):
        col_list = list(self.col) + ["G"]
        col_func = ["ID of games", "Names of games", "Main genres", "Prices of games", "Release date games", "Studios of games", "End"]
        order_list = list(self.order)
        order_func = ["ID of games", "Names of games", "Main genres", "Prices of games", "Release date of games", "Studios of games"]
        query = "select"

        while True:
            print("Choose any of these to add to your column")
            for i in range(7):
                print(f'{col_list[i]}: {col_func[i]}')
            chosen = input("Type here: ").upper()
            if chosen == "G" or chosen not in col_list:
                break
            query += ' ' + self.col[chosen] + ','
            print(query)
        query = query[:len(query)-1]
        query += " from game join main_genre, studio on game.main_genre_ID = main_genre.ID and game.studio_ID = studio.ID order by"
        print(query)

        print("What do you want to sort it by?")
        for i in range(6):
            print(f'{order_list[i]}: {order_func[i]}')
        query += ' ' + self.order[input("Type here: ").upper()] + ';'

        return query
    
    def execute(self,query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return self.print_result(result)
    
    def print_result(self,result):
        sent = []
        for c in result:
            row = ''
            for r in c:
                row += f'{r} || '
            sent.append(row)
        return sent
