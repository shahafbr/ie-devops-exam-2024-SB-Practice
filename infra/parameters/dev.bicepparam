using '../main.bicep'

param userAlias = 'sbrenner' //Replace sbrenner with your student alias, and use it in your main.bicep as part of the name of the module deployment to avoid deployment conflicts 
param appServiceContainerBackendName = 'sbrenner-asc-backend' 
param appServicePlanName = 'sbrenner-asp' 
param containerRegistryName = 'sbrenneracr' 
param postgreSQLDatabaseName = 'sbrenner-db'  
param postgreSQLServerName = 'sbrenner-dbsrv' 

