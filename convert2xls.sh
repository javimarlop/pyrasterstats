awk '{print "csv2xls "$1".csv -o "$1".xls -d \";\""}' list.txt|sh
