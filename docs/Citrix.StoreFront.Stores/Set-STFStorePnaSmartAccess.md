#Set-STFStorePnaSmartAccess
Set the SmartAccess settings
##Syntax
```
```
##Detailed Description
Configure the settings related to the verification of PNA SmartAccess HTTP headers.
##Related Commands
*[Grant-STFStorePnaSmartAccess](Grant-STFStorePnaSmartAccess)
*[Revoke-STFStorePnaSmartAccess](Revoke-STFStorePnaSmartAccess)
*[Get-STFStorePnaSmartAccess](Get-STFStorePnaSmartAccess)
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
###System.Int32
Parameter HeaderValidity: The .NET 'System.Int32' value type
##Return Values
##Examples
###EXAMPLE 1 Set SmartAccess trust settings
```
Set-STFStorePnaSmartAccess -StoreService $store -HeaderValidity 60
```
REMARKS
Sets the http headers to be trusted for up to 60 seconds after the current server date time.
