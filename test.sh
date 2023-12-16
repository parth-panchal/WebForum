#!/bin/bash
npm install -g newman
newman run "./tests/forum- multiple posts.postman_collection.json" -n 10
newman run "./tests/forum- post, read, delete.postman_collection.json" -n 10
newman run "./tests/FullTextSearch.postman_collection.json" -n 5
newman run "./tests/Users.postman_collection.json" -n 5