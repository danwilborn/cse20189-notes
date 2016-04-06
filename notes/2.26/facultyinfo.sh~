#!/bin/sh

curl -s "http://cse.nd,edu/people/faculty" | grep "Ph\.D\." | wc -l
# how many people have masters/doctors
curl -s "http://cse.nd.edu/people/faculty" | grep "M\.S\." | wc -l


curl -s "http://cse.nd.edu/people/faculty" | sed -rn 's/.*(Ph\.D|M\.S).*/\1/p' | sort | uniq -c 

#PhDs from Notre Dame
curl -s "http://cse.nd.edu/people/faculty" | sed -rn 's/.*(Ph\.D|M\.S).*Notre Dame.*/\1/p' | sort | uniq -c 

#What year did most of the professors graduate
curl -s "http://cse.nd.edu/people/faculty" | sed -rn 's/.*(Ph\.D|M\.S).*([0-9]{4}).*/\1/p' | sort | uniq -c | sort -rn

#Professional Specialists
curl -s "http://cse.nd.edu/people/faculty" | sed -rn 's/.*(Ph\.D|M\.S).*(Professional Specialist).*/\1/p' | sort | uniq -c | sort -rn
