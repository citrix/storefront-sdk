#Add-STFWebReceiverService
Create a new Receiver for Web service
##Syntax
```
```
##Detailed Description
Create and configure a new Receiver for Web service.
##Related Commands
*[Get-STFWebReceiverService](Get-STFWebReceiverService)
*[Remove-STFWebReceiverService](Remove-STFWebReceiverService)
##Parameters
|Name|Description|Required?|Pipeline Input|
###System.String
Parameter VirtualPath: The .NET 'System.String' reference type
###System.Int64
Parameter SiteId: The .NET 'System.Int64' value type
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
###System.Boolean
Parameter ClassicReceiverExperience: The .NET 'System.Boolean' value type
##Return Values
###WebReceiverService
A .NET class representing the configuration of a StoreFront Web Receiver service
##Examples
###EXAMPLE 1 Create new Receiver for Web service
```
$rfw = Add-STFWebReceiverService -VirtualPath /Citrix/Receiver -StoreService $store
```
REMARKS
Create a new Receiver for Web service at the virtual path /Citrix/Receiver
using the only configured Store service.
