#!/bin/bash

function testsite(){
    regexd='http(s)?://www\.[a-zA-Z]+\.(com|ca)$'
    if [[ $1 =~ $regexd ]]
    then 
        rCode=$(curl -o /dev/null -s -w "%{http_code}\n" $1)
        echo "($1) returned $rCode"
    else
        echo "($1) is invalid url"
    fi
}    


read -p "enter a url: " var

testsite $var