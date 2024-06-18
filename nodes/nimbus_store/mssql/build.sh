#!/bin/bash
# Wait for SQL to start.
sleep 35s
# Connect to SQL and run our script.
/opt/mssql-tools/bin/sqlcmd -S localhost,1433 -U SA -P $MSSQL_SA_PASSWORD -i /usr/init/setup.sql