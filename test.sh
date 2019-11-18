#!/bin/bash

HTTP=$(which http)

if [ ! -x "$HTTP" ]; then
    echo 'You need HTTPie to run this script!'
    echo 'pipenv install httpie'
    exit 1
fi

URL=http://localhost:8080

# set -x

echo "Add 2 (types of) Pets..."
http PUT $URL/pets/1 name=Spot animal_type=dog
http PUT $URL/pets/2 name=Tiger animal_type=cat

echo "dump a Pet by ID..."
http $URL/pets/2

echo "dump all Pets..."
http $URL/pets

echo "add 1 more (type of) dog..."
http PUT $URL/pets/3 name=Bowser animal_type=dog tags:='{"color": "brown"}'

echo "dump Pets by ID or type..."
http $URL/pets/1
http $URL/pets animal_type==dog

echo "delete one Pet by ID..."
http DELETE $URL/pets/1

echo "dump all Pets..."
http $URL/pets
