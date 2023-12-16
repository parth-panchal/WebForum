#!/bin/bash
newman run ./tests/forum_multiple_posts.postman_collection.json -n20
newman run ./tests/forum_post_read_delete.postman_collection.json -n20
newman run ./tests/FullTextSearch.postman_collection.json -n20
newman run ./tests/Users.postman_collection.json -n20