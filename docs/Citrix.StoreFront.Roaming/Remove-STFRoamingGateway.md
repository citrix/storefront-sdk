#Remove-STFRoamingGateway
Remove a Gateway used for remote access and authentication
##Syntax
```Remove-STFRoamingGateway [-Gateway] <RoamingGateway> [<CommonParameters>]
Remove-STFRoamingGateway [-Name] <String> [<CommonParameters>]
```
##Detailed Description
Remove a Gateway from the global list of Gateways and from any Stores that are configured to use it for remote access or authentication.
##Related Commands
*[Add-STFRoamingGateway](Add-STFRoamingGateway)
*[Get-STFRoamingGateway](Get-STFRoamingGateway)
*[Set-STFRoamingGateway](Set-STFRoamingGateway)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||Gateway|Remove the Gateway supplied from the global list|true|true (ByValue)||Name|Remove the Gateway named from the global list|true|true (ByValue)|##Input Type
###Citrix.StoreFront.Model.Roaming.RoamingGateway
Parameter Gateway: The .NET 'Citrix.StoreFront.Model.Roaming.RoamingGateway' reference type
###System.String
Parameter Name: The .NET 'System.String' reference type
##Return Values
##Notes
Any existing Store Service objects may be invalidated by this operation and should not be used after calling this Cmdlet.
##Examples
###EXAMPLE 1 Remove Gateway by name
```Remove-STFRoamingGateway -Gateway "Netscaler10x"
```
REMARKS
Removes the Gateway with the matching name.
###EXAMPLE 2 Remove Gateway
```$gateway = Get-STFRoamingGateway -Name "Netscaler10x"
          Remove - STFRoamingGateway - Gateway $gateway
```
REMARKS
Gets the Gateway named "Netscaler10x" from the global list and removes it.
