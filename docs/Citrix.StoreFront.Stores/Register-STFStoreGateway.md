#Register-STFStoreGateway
Register an authentication Gateway with a Store
##Syntax
```
```
##Detailed Description
Register an authentication Gateway with the Store for use when users access StoreFront from the internet.
##Related Commands
*[Register-STFStoreOptimalLaunchGateway](Register-STFStoreOptimalLaunchGateway)
*[Unregister-STFStoreOptimalLaunchGateway](Unregister-STFStoreOptimalLaunchGateway)
*[Unregister-STFStoreGateway](Unregister-STFStoreGateway)
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.Roaming.RoamingGateway
Parameter Gateway: The .NET 'Citrix.StoreFront.Model.Roaming.RoamingGateway' reference type
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
###System.Management.Automation.SwitchParameter
Parameter DefaultGateway: The .NET 'System.Management.Automation.SwitchParameter' value type
###System.Management.Automation.SwitchParameter
Parameter UseFullVpn: The .NET 'System.Management.Automation.SwitchParameter' value type
##Return Values
##Examples
###EXAMPLE 1 Register a gateway
```
$storeService = Get-STFStoreService
Register-STFStoreGateway -Gateway $gateway9 -StoreService $storeService -DefaultGateway -UseFullVpn
```
REMARKS
Get the Gateway "Netscaler9" from the global list and register it to the only
Store for full VPN access.
