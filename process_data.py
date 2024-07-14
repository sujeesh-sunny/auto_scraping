import json
import mysql.connector

def process_and_store_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    products = data['items']
    product_data = [(product['name'], product['base_price'], product['href']) for product in products]

    conn = mysql.connector.connect(
        host='localhost',
        user='sujeesh_usr',
        password='Mysql@121212',
        database='wegmans'
    )
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            price DECIMAL(10, 2),
            url TEXT,
            active BOOLEAN
        )
    ''')

    cursor.executemany('''
        INSERT INTO product (name, price, url, active)
        VALUES (%s, %s, %s, %s)
    ''', [(name, price, url, None) for name, price, url in product_data])

    conn.commit()
    conn.close()

    check_urls()

def check_urls():
    import check_urls
    check_urls.verify_urls()

if __name__ == "__main__":
    import sys
    process_and_store_data(sys.argv[1])
