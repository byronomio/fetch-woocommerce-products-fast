# Fetch WooCommerce Products Fast

A streamlined approach to fetch all parent and simple WooCommerce products directly from the MySQL database. Designed for sites where the WooCommerce API may be slower, and particularly effective when variable products contain dashes in their SKUs.

## Features

- Direct database connection for faster fetching.
- Filters out duplicate SKUs.
- Outputs a neatly formatted JSON file with product details.

## Requirements

- Python 3.x
- `mysql-connector-python` package. Install via pip: 
	pip install mysql-connector-python

## Usage

1. Fill in the database connection details (host, user, password, database) in the script.
2. Run the script:
	python fetch-woocommerce-products-fast.py
3. Check the `products.json` file in the script's directory for the fetched product details.

## Note

Ensure that the database user has read permissions for the `wp_wc_product_meta_lookup` table. Always backup your database before running scripts that interact with it.

## Contributing

Pull requests are welcome. 