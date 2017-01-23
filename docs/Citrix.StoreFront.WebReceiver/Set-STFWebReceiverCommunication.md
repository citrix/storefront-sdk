#Set-STFWebReceiverCommunication
Set the WebReceiver communication settings
##Syntax
```
```
##Detailed Description
Set the communication settings used for the WebReceiver proxy.
##Related Commands
*[Get-STFWebReceiverAuthenticationMethods](Get-STFWebReceiverAuthenticationMethods)
*[Get-STFWebReceiverAuthenticationMethodsAvailable](Get-STFWebReceiverAuthenticationMethodsAvailable)
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.ReceiverForWeb.WebReceiverService
Parameter WebReceiverService: A .NET class representing the configuration of a StoreFront Web Receiver service
###System.Int32
Parameter Attempts: The .NET 'System.Int32' value type
###System.TimeSpan
Parameter Timeout: The .NET 'System.TimeSpan' value type
###Citrix.StoreFront.Model.ReceiverForWeb.LoopbackOption
Parameter Loopback: The .NET 'Citrix.StoreFront.Model.ReceiverForWeb.LoopbackOption' value type
###System.Int32
Parameter LoopbackPortUsingHttp: The .NET 'System.Int32' value type
###System.Boolean
Parameter ProxyEnabled: The .NET 'System.Boolean' value type
###System.Int32
Parameter ProxyPort: The .NET 'System.Int32' value type
###System.String
Parameter ProxyProcessName: The .NET 'System.String' reference type
##Return Values
##Examples
###EXAMPLE 1 Configure the communication timeout
```
Set-STFWebReceiverCommunication -WebReceiverService $webReceiver -Timeout 240
```
REMARKS
Set the current WebReceiver communication timeout to four minutes for
/Citrix/StoreWeb.
