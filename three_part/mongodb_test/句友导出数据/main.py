from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient()
    db = client.ju_friends

    table = db['book']
    book_list = table.find()
    count = 0
    for book in book_list:
        file_name = "data/{}-{}-{}-1.csv".format(book["name"],book["author"],"句友官方")
        with open(file_name, "w+", encoding='utf-8') as f:
            sentences = book['sentence']
            for sentence in sentences:
                f.write(sentence)

        f.close()
