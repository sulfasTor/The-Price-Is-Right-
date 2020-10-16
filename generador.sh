#!/bin/bash

echo "Scrapping Amazon US...."

curl -s 'https://randomazonbackend.appspot.com/product/' > product.json

URL="https://www.amazon.com/dp/"`jq -r '.ASIN' product.json`

lynx -source $URL > innerHTML.html
PRICE=`xmllint --html --nowarning --xpath 'string(//*[@id="priceblock_ourprice"])' innerHTML.html 2>/dev/null`

if [ -z "$PRICE" ]
then
    echo "Empty price"
    exit
fi

xmllint --html --nowarning --xpath '//*[@id="productTitle"]' innerHTML.html 2>/dev/null > img_product.html
echo "</br></br>" >> img_product.html
xmllint --html --nowarning --xpath '//*[@id="landingImage"]' innerHTML.html 2>/dev/null >> img_product.html
xmllint --html --nowarning --xpath '//*[@id="feature-bullets"]' innerHTML.html 2>/dev/null >> img_product.html

/usr/bin/firefox --new-tab img_product.html &

./game.py "$PRICE" "$@"

/usr/bin/firefox --new-tab $URL &

rm img_product.html product.json innerHTML.html 2>/dev/null
