#Get-STFRoamingAccount
Get the Roaming account
##Syntax
```Get-STFRoamingAccount [-StoreService] <StoreService> [<CommonParameters>]
```
##Detailed Description
Get the Roaming account details for one or all Stores.
##Related Commands
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||StoreService|Store service to get the account record for|true|true (ByValue)|##Input Type
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
##Return Values
###Accounts
The .NET 'Citrix.StoreFront.Model.Roaming.Accounts' reference type
##Examples
###EXAMPLE 1 Get Roaming account for a specific Store
```$store = Get-STFStoreService
Get-STFRoamingAccount -StoreService $store
```
REMARKS
Get the Roaming account for the only configured Store service.
