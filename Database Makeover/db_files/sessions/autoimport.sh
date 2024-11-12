for file in *.json; do
    mongoimport --config ../mongo-config.yml --collection sessions --file "$file"
done
