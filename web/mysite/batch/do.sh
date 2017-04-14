bindir=$(dirname $0)
jsondir=$(../manage.py shell -c 'import mysite; print (mysite.settings.jsondir)')
logdir=$(../manage.py shell -c 'import mysite; print (mysite.settings.logdir)')

cd ${bindir} # fabfile is there
while true
do
 date
 for jsonfile in $jsondir/*json
 do
  jsonname=$(basename ${jsonfile})
  if [[ ! -f ${jsonfile}.state  ]]
  then
   echo "exec:" ${jsonfile}
   applcode=$(grep jobapplcode ${jsonfile} | awk -F: '{print $2}' | awk -F\" '{print $2}' )
   if [[ -n ${applcode} ]]
   then
    appl_logdir=${logdir}/${applcode}
    if [[ ! -d ${appl_logdir} ]]
    then
     mkdir ${appl_logdir}
    fi
   else
    appl_logdir=${logdir}
   fi
   echo logdir: $appl_logdir
   logpath=${appl_logdir}/${jsonname}.txt
   echo logpath: ${logpath}
   ${bindir}/do.py ${jsonfile} > ${logpath} 2>&1 &
  fi
 done
 echo ""
 sleep 15
done
