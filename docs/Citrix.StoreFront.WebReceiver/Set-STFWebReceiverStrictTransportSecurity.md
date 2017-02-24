#Set-STFWebReceiverStrictTransportSecurity
Set the WebReceiver HTTP Strict Transport Security options
##Syntax
```
```
##Detailed Description
Set the WebReceiver HTTP Strict Transport Security options.
##Related Commands
*[Get-STFWebReceiverStrictTransportSecurity](Get-STFWebReceiverStrictTransportSecurity)
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.ReceiverForWeb.WebReceiverService
Parameter WebReceiverService: A .NET class representing the configuration of a StoreFront Web Receiver service
###System.Boolean
Parameter Enabled: The .NET 'System.Boolean' value type
###System.TimeSpan
Parameter PolicyDuration: The .NET 'System.TimeSpan' value type
##Return Values
##Examples
###EXAMPLE 1 Enable WebReceiver HTTP Strict Transport Security
```
Set-STFWebReceiverStrictTransportSecurity -WebReceiverService $receiver -Enabled $true
```
REMARKS
Enable the HTTP Strict Transport Security feature on the only WebReceiver service.
