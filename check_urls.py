import requests
import mysql.connector

def verify_urls():
    conn = mysql.connector.connect(
        host='localhost',
        user='sujeesh_usr',
        password='Mysql@121212',
        database='wegmans'
    )
    cursor = conn.cursor()

    cursor.execute('SELECT id, url FROM product')
    products = cursor.fetchall()

    for product in products:
        product_id, url = product
        try:
            response = requests.get(url)
            if response.status_code == 200:
                is_active = True
            else:
                is_active = False
        except requests.exceptions.RequestException:
            is_active = False

        cursor.execute('UPDATE product SET active = %s WHERE id = %s', (is_active, product_id))
        conn.commit()

    conn.close()

if __name__ == "__main__":
    verify_urls()
