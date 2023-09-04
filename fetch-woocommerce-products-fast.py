import mysql.connector
import json

# Define a function to fetch products
def fetch_products():
    # Connect to MySQL
    connection = mysql.connector.connect(
        host='',
        user='',
        password='',
        database=''
    )

    # Create a cursor object to interact with the MySQL server
    cursor = connection.cursor()

    # Define SQL query to fetch all rows
    query = "SELECT product_id, sku FROM wp_wc_product_meta_lookup WHERE sku != ''"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    connection.close()

    # Extract base SKUs (before any hyphen)
    base_skus = [row[1].split('-')[0] for row in rows]

    # Identify distinct base SKUs
    distinct_skus = set(base_skus)

    # Filter rows by distinct base SKUs and avoid duplicate SKUs
    filtered_rows = []
    seen_skus = set()
    for row in rows:
        sku_base = row[1].split('-')[0]
        if sku_base in distinct_skus and sku_base not in seen_skus:
            seen_skus.add(sku_base)
            filtered_rows.append({
                "id": row[0],
                "sku": row[1]
            })

    return filtered_rows

# Fetch the products
products = fetch_products()

# Save the results to a JSON file
with open('products.json', 'w') as file:
    json.dump({"products": products}, file, indent=4)  # Added indentation for better readability

print("Data saved to products.json!")
