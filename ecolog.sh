#!/bin/bash

echo "📡 Monitoraggio log EcoBlock (CTRL+C per uscire)"
echo "-----------------------------"

tail -n 20 -f node.log auth.log edit.log agent.log 2>/dev/null | awk '
  /node.log/ {print "\033[1;36m[NODE]\033[0m " $0; next}
  /auth.log/ {print "\033[1;33m[AUTH]\033[0m " $0; next}
  /edit.log/ {print "\033[1;32m[EDIT]\033[0m " $0; next}
  /agent.log/ {print "\033[1;35m[AGENT]\033[0m " $0; next}
  {print $0}
'
