#Remove-STFStoreService
Remove a Store service
##Syntax
```
```
##Detailed Description
Removes a Store service, any Receiver for Web sites and if no other Stores are using it the associated Authentication service.
##Related Commands
*[Add-STFStoreService](Add-STFStoreService)
*[Set-STFStoreService](Set-STFStoreService)
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
##Return Values
##Examples
###EXAMPLE 1 Remove Store service
```
Remove-STFStoreService $storeService -Force
```
REMARKS
Remove the only Store including any associated Receiver for Web sites.
