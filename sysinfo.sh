!/bin/bash
"This script will email us our user, IP, hostnam and today's date."
emailaddress=wirtdn@mail.uc.edu
today=(echo (date +"%mm-%dd-%yyyy"))
ip= (echo (ip a | grep 'dynamic ens192' | awk |'{print$2}'
content"wirtdn: \t $USER \n"
mail -s "IT3038C Linux IP" $emailaddress <<<
(echo -e $content)
