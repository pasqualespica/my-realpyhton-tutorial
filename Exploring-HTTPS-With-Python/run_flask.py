

# Check parameter
if [ $# -lt 1 ]
then
   usage=NOK
else
   app_name=${1}.py
   echo "File ${app_name}"

   if [ -f "$app_name" ]; then
      echo "$app_name exist"
      usage=OK
   else 
      echo "$app_name does not exist"
      usage=NOK
   fi
fi

if [ "$usage" = "OK" ]
then
   echo "Start flask app  ${app_name}..."

   # ex. flask run --cert server-public-key.pem --key server-private-key.pem
   export FLASK_APP=$app_name
   export FLASK_ENV=development
   SERVER_CERT=${2}
   SERVER_KEY=${3}
   flask run --cert ${SERVER_CERT} --key ${SERVER_KEY}
   echo "running ... "   
else
   echo ""
   echo "Bad usage !!!"
   echo "  $0 [application name] [CERT SERVER - PUB KEY] [ PRIVATE KEY SERVER] "
   echo "  Ex. : $0 server server-public-key.pem server-private-key.pem "
   echo ""
fi

