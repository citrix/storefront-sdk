#Enable-STFAuthenticationServiceProtocol
Enable an authentication protocol
##Syntax
```
```
##Detailed Description
Enable one or more authentication protocols on the specified Authentication service.
##Related Commands
*[Remove-STFAuthenticationServiceProtocol](Remove-STFAuthenticationServiceProtocol)
*[Disable-STFAuthenticationServiceProtocol](Disable-STFAuthenticationServiceProtocol)
*[Get-STFAuthenticationProtocolsAvailable](Get-STFAuthenticationProtocolsAvailable)
*[Add-STFAuthenticationServiceProtocol](Add-STFAuthenticationServiceProtocol)
##Parameters
|Name|Description|Required?|Pipeline Input|
###System.String[]
Parameter Name: The .NET 'System.String' reference type
###Citrix.StoreFront.Model.Authentication.AuthenticationService
Parameter AuthenticationService: A .NET class representing the configuration of a StoreFront Authentication service
##Return Values
##Examples
###EXAMPLE 1 Enable all authentication protocols
```
```
REMARKS
Enable all authentication protocols for the only configured Authentication
service.

```
```
REMARKS
Enable the HttpBasic authentication protocol.
