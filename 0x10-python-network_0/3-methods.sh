#!/bin/bash
#Script that takes in a URL and displays all HTTP methods the server will accept
curl "$1" -sX POST -d "email=calebrori@gmail.com&subject=This is a test email"
