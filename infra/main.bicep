// Exercise II: Configure the input parameters to set up your development environment
param userAlias string = 'sbrenner'
param keyVaultName string = '${userAlias}kv'
param appServiceContainerBackendName string
param appServicePlanName string
param containerRegistryName string
param postgreSQLServerName string
param postgreSQLDatabaseName string
param location string = resourceGroup().location
@secure()
param administratorLogin string
@secure()
param administratorPassword string



//Deploy Key VaulT:
module keyVault 'modules/key-vault.bicep' = {
  name: 'keyVault'
  params: {
    location: location
    name: keyVaultName
  }
}

//Deploy App Service Plan:
module appServicePlan 'modules/app-service-plan.bicep' = {
  name: 'appServicePlan'
  params: {
    location: location
    appServicePlanName: appServicePlanName
    skuName: 'B1'
  }
}

//Deploy Container Registry
module containerRegistry 'modules/container-registry.bicep' = {
  name: 'containerRegistry'
  params: {
    location: location
    name: containerRegistryName
  }
}

//Deploy PostgreSQL Server
module postgreSQLServer 'modules/postgre-sql-server.bicep' = {
  name: 'postgreSQLServer'
  params: {
    location: location
    name: postgreSQLServerName
    administratorLogin: administratorLogin
    administratorPassword: administratorPassword
  }
}

//Deploy PostgreSQL Database
module postgreSQLDatabase 'modules/postgre-sql-db.bicep' = {
  name: 'postgreSQLDatabase'
  params: {
    name: postgreSQLDatabaseName
    postgreSqlServerName: postgreSQLServerName
  }
}

//Deploy App Service Container
module appServiceContainer 'modules/app-service-container.bicep' = {
  name: 'appServiceContainer'
  params: {
    location: location
    name: appServiceContainerBackendName
    appServicePlanId: appServicePlan.outputs.id
    dockerRegistryName: containerRegistryName
    dockerRegistryServerUserName: containerRegistry.outputs.acrUsername
    dockerRegistryServerPassword: containerRegistry.outputs.acrPassword0
    dockerRegistryImageName: 'backend'
    dockerRegistryImageVersion: 'latest'
    appSettings: [
      {
        name: 'WEBSITES_PORT'
        value: '8080'
      }, {
        name: 'ENV'
        value: 'development'
      }, {
        name: 'DBUSER'
        value: administratorLogin
      }, {
        name: 'DBPASS'
        value: administratorPassword
      }, {
        name: 'DBHOST'
        value: '${postgreSQLServerName}.postgres.database.azure.com'
      }, {
        name: 'DBNAME'
        value: postgreSQLDatabaseName
      }
    ]
  }
}
