#New-STFWebReceiverClientPlugin
Create a WebReceiver client plug-in
##Syntax
```New-STFWebReceiverClientPlugin [-Name] <String> [[-Source] <String>] [[-Scripts] <String[]>] [-Styles] <String[]> [[-Parameters] <Hashtable>] [<CommonParameters>]
```
##Detailed Description
Create WebReceiver script and branding customizations.
##Related Commands
*[Add-STFWebReceiverClientPlugin](Add-STFWebReceiverClientPlugin)
*[Set-STFWebReceiverClientPlugin](Set-STFWebReceiverClientPlugin)
*[Clear-STFWebReceiverClientPlugin](Clear-STFWebReceiverClientPlugin)
*[Remove-STFWebReceiverClientPlugin](Remove-STFWebReceiverClientPlugin)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||Name|Name of plug-in. This should be unique across all the plug-ins|true|true (ByValue)||Source|The script source location associated with the plug-in|false|false||Scripts|List of script locations|false|false||Styles|List of style locations|true|true (ByValue)||Parameters|This is a list of name value pair for passing parameter to the source script|false|true (ByValue)|##Input Type
###System.String
Parameter Name: The .NET 'System.String' reference type
###System.String
Parameter Source: The .NET 'System.String' reference type
###System.String[]
Parameter Scripts: The .NET 'System.String' reference type
###System.String[]
Parameter Styles: The .NET 'System.String' reference type
###System.Collections.Hashtable
Parameter Parameters: The .NET 'System.Collections.Hashtable' reference type
##Return Values
###ClientPlugin
The .NET 'Citrix.StoreFront.Model.ReceiverForWeb.ClientPlugin' reference type
##Examples
###EXAMPLE 1 Create a new client plugin
```$plugin = New-STFWebReceiverClientPlugin -Name "NetScaler" `
- Source "/plugins/netscalar/script1.js" `
-Scripts @("/ plugins/netscalar/script2.js", "/ plugins/netscalar/script1.js") `
-Styles @("/ plugins/netscalar/script2.css", "/ plugins/netscalar/script1.css") `
-Parameters @{"param1" = "value1";"param2" = "value2"}
```
REMARKS
Creates a new client plug-in for assignment to a WebReceiver.
