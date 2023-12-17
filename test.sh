#!/bin/bash
echo "Running tests..."

./run.sh &
PID=$! # record the PID of the server process

# echo "Installing newman..."
# npm install -g newman
# exec newman run "./tests/forum- multiple posts.postman_collection.json" -n 10
# exec newman run "./tests/forum- post, read, delete.postman_collection.json" -n 10
# exec newman run "./tests/FullTextSearch.postman_collection.json" -n 5
# exec newman run "./tests/Users.postman_collection.json" -n 5