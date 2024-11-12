for file in *.json; do
    mongoimport --config ../mongo-config.yml --collection patients --file "$file"
done
