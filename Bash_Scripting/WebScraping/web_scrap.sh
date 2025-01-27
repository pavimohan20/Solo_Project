#!/bin/bash

# Step 1: Fetch the webpage HTML
curl -s "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops" > page.html

# Debug: Check the content of the fetched HTML
echo "Content of page.html:"
head -n 20 page.html

# Step 2: Parse the HTML to extract laptop details (name, price, description)

# Extract laptop names
names=$(awk -F 'title="' '/<a class="title"/ {print $2}' page.html | awk -F '"' '{print $1}')
echo "Extracted names: $names"  # Debug statement

# Extract laptop prices
prices=$(awk -F '>' '/<h4 class="pull-right price"/ {print $2}' page.html | awk -F '<' '{print $1}')
echo "Extracted prices: $prices"  # Debug statement

# Extract laptop descriptions
descriptions=$(awk -F '>' '/<p class="description"/ {print $2}' page.html | awk -F '<' '{print $1}')
echo "Extracted descriptions: $descriptions"  # Debug statement

# Combine the extracted details and print them
paste <(echo "$names") <(echo "$descriptions") <(echo "$prices") | while IFS=$'\t' read -r name description price; do
    if [ -n "$name" ] && [ -n "$description" ] && [ -n "$price" ]; then
        echo "$name | $description | $price"
    fi
done

read -p "Press any key to continue..."