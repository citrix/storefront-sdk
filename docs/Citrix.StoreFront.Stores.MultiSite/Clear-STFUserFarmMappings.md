#Clear-STFUserFarmMappings
Clear the UserFarmMappings for a Store
##Syntax
```Clear-STFUserFarmMappings [-StoreService] <StoreService> [<CommonParameters>]
```
##Detailed Description
Clear all of the UserFarmMappings configured for or Store.
##Related Commands
*[Set-STFUserFarmMapping](Set-STFUserFarmMapping)
*[Get-STFUserFarmMapping](Get-STFUserFarmMapping)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||StoreService|The Store service output the UserFarmMappings from.|true|true (ByValue)|##Input Type
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
##Return Values
##Examples
###EXAMPLE 1 Clear all UserFarmMappings
```Clear-STFUserFarmMappings -StoreService $store
```
REMARKS
Clears all existing UserFarmMappings from the Store service $store.
