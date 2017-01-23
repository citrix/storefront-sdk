#Get-STFRoamingServiceRecord
Get the Service Record
##Syntax
```Get-STFRoamingServiceRecord [-StoreService] <StoreService> [<CommonParameters>]
```
##Detailed Description
Get the Service record for a specific or all Stores.
##Related Commands
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||StoreService|Store service to get the account record for|true|true (ByValue)|##Input Type
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
##Return Values
###ServiceRecords
The .NET 'Citrix.StoreFront.Model.Roaming.ServiceRecords' reference type
##Examples
###EXAMPLE 1 Get Service record for a specific Store
```$store = Get-STFStoreService
Get-STFRoamingServiceRecord -StoreService $store
```
REMARKS
Get the service record used for accessing the specified Store service
