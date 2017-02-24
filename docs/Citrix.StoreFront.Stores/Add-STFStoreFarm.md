#Add-STFStoreFarm
Add a farm to a Store
##Syntax
```Add-STFStoreFarm [-Farm] <Farm> [-StoreService] <StoreService> [[-Product] <String>] [[-RestrictPoPs] <String>] [[-FarmGuid] <String>] [<CommonParameters>]
Add-STFStoreFarm [-FarmName] <String> [-FarmType] <XenApp | XenDesktop | AppController | VDIinaBox | Store> [[-Servers] <String[]>] [[-ServiceUrls] <String[]>] [[-Port] <Int32>] [[-TransportType] <HTTP | HTTPS | SSL>] [[-SSLRelayPort] <Int32>] [[-LoadBalance] <Boolean>] [[-AllFailedBypassDuration] <Int32>] [[-BypassDuration] <Int32>] [[-TicketTimeToLive] <Int32>] [[-RadeTicketTimeToLive] <Int32>] [[-MaxFailedServersPerRequest] <Int32>] [[-Zones] <String[]>] [[-PassThru] <SwitchParameter>] [-StoreService] <StoreService> [[-Product] <String>] [[-RestrictPoPs] <String>] [[-FarmGuid] <String>] [<CommonParameters>]
```
##Detailed Description
Add a XenApp \ XenDesktop farm to the specified Store service.
##Related Commands
*[Remove-STFStoreFarm](Remove-STFStoreFarm)
*[Get-STFStoreFarm](Get-STFStoreFarm)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||Farm|The Farm object to add to the Store service|true|true (ByValue)||StoreService|Store service the farm will be added to|true|false||FarmName|The friendly name of the farm|true|false||FarmType|The type of farm to be added. XenDesktop or XenApp for example|true|false||Servers|The hostnames or IP addresses of the xml services|false|false||ServiceUrls|The url to the service location used to provide web and SaaS apps via this farm.|false|false||Port|Service communication port|false|false||TransportType|Type of transport to use. Http, Https, SSL for example|false|false||SSLRelayPort|The SSL Relay port|false|false||LoadBalance|Round robin load balance the xml service servers|false|false||AllFailedBypassDuration|Period of time to skip all xml service requests should all servers fail to respond|false|false||BypassDuration|Period of time to skip a server when is fails to respond|false|false||TicketTimeToLive|Period of time an ICA launch ticket is valid once requested on pre 7.0 XenApp and XenDesktop farms|false|false||RadeTicketTimeToLive|Period of time a RADE launch ticket is valid once requested on pre 7.0 XenApp and XenDesktop farms|false|false||MaxFailedServersPerRequest|Maximum number of servers within a single farm that can fail before aborting a request|false|false||Zones|The list of Zone names associated with the farm|false|false||Product|Cloud deployments only otherwise ignored. The product name of the farm configured|false|false||RestrictPoPs|Cloud deployments only otherwise ignored. Restricts GWaaS traffic to the specified POP|false|false||FarmGuid|Cloud deployments only otherwise ignored. A tag indicating the scope of the farm|false|false||PassThru|The resulting Store service|false|false|##Input Type
###Citrix.StoreFront.Model.Store.Farm
Parameter Farm: A .NET class representing the configuration of a Farm in StoreFront Store service
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
###System.String
Parameter FarmName: The .NET 'System.String' reference type
###Citrix.StoreFront.Model.Store.FarmType
Parameter FarmType: The .NET 'Citrix.StoreFront.Model.Store.FarmType' value type
###System.String[]
Parameter Servers: The .NET 'System.String' reference type
###System.String[]
Parameter ServiceUrls: The .NET 'System.String' reference type
###System.Int32
Parameter Port: The .NET 'System.Int32' value type
###Citrix.StoreFront.Model.Store.TransportType
Parameter TransportType: The .NET 'Citrix.StoreFront.Model.Store.TransportType' value type
###System.Int32
Parameter SSLRelayPort: The .NET 'System.Int32' value type
###System.Boolean
Parameter LoadBalance: The .NET 'System.Boolean' value type
###System.Int32
Parameter AllFailedBypassDuration: The .NET 'System.Int32' value type
###System.Int32
Parameter BypassDuration: The .NET 'System.Int32' value type
###System.Int32
Parameter TicketTimeToLive: The .NET 'System.Int32' value type
###System.Int32
Parameter RadeTicketTimeToLive: The .NET 'System.Int32' value type
###System.Int32
Parameter MaxFailedServersPerRequest: The .NET 'System.Int32' value type
###System.String[]
Parameter Zones: The .NET 'System.String' reference type
###System.String
Parameter Product: The .NET 'System.String' reference type
###System.String
Parameter RestrictPoPs: The .NET 'System.String' reference type
###System.String
Parameter FarmGuid: The .NET 'System.String' reference type
###System.Management.Automation.SwitchParameter
Parameter PassThru: The .NET 'System.Management.Automation.SwitchParameter' value type
##Return Values
###Farm
A .NET class representing the configuration of a Farm in StoreFront Store service
##Examples
###EXAMPLE 1 Add a farm to the only Store service
```$store = Get-STFStoreService
Add-STFStoreFarm -StoreService $store -FarmName "XenDesktop75" -FarmType XenDesktop -Port 80 -TransportType HTTP -Servers Xen1
```
REMARKS
Adds the Xen1 XenDesktop server to the XenDesktop75 farm
###EXAMPLE 2 Add a farm to the Store service at /Citrix/Store
```$store = Get-STFStoreService -VirtualPath /Citrix/Store
Add-STFStoreFarm -StoreService $store -FarmName "XenDesktop75" -FarmType XenDesktop -Port 80 -TransportType HTTP -Servers Xen1
```
REMARKS
Adds the Xen1 XenDesktop server to the XenDesktop75 farm
###EXAMPLE 3 Copy a farm from the Store service at /Citrix/Store1 to the Store service at /Citrix/Store2
```$store1 = Get-STFStoreService -VirtualPath /Citrix/Store1
$farm = $store1.FarmsConfiguration.Farms[0]
$store2 = Get-STFStoreService -VirtualPath /Citrix/Store2
Add-STFStoreFarm -StoreService $store2 -Farm $farm
```
REMARKS
Adds a new farm to $store2 with the same properties as the first farm from $store1. The farm object ($farm) is not
changed by this operation.
