param userAlias string
param appServiceContainerBackendName string
param appServicePlanName string
param containerRegistryName string
param keyVaultName string
param postgreSQLServerName string
param administratorLogin string
@secure()
param administratorPassword string
param postgreSQLDatabaseName string
param location string = resourceGroup().location

module keyVault 'modules/key-vault.bicep' = {
  name: 'keyVault'
  params: {
    location: location
    name: keyVaultName
  }
}

module appServicePlan 'modules/app-service-plan.bicep' = {
  name: 'appServicePlan'
  params: {
    location: location
    appServicePlanName: appServicePlanName
    skuName: 'B1'
  }
}

module containerRegistry 'modules/container-registry.bicep' = {
  name: 'containerRegistry'
  params: {
    location: location
    name: containerRegistryName
  }
}
module postgreSQLServer 'modules/postgre-sql-server.bicep' = {
  name: 'postgreSQL'
  params: {
    location: location
    name: postgreSQLServerName
    administratorLogin: administratorLogin
    administratorPassword: administratorPassword
  }
}

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
      }
    ]
  }
}
