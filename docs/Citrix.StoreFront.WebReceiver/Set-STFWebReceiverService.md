#Set-STFWebReceiverService
Configure Receiver for Web
##Syntax
```Set-STFWebReceiverService [-WebReceiverService] <WebReceiverService> [[-ClassicReceiverExperience] <Boolean>] [[-DefaultIISSite] <SwitchParameter>] [[-PassThru] <SwitchParameter>] [<CommonParameters>]
```
##Detailed Description
Configure Receiver for Web service options.
##Related Commands
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||WebReceiverService|Receiver for Web service|true|true (ByValue)||ClassicReceiverExperience|Enable or disable the classic or unified Receiver experience|false|false||DefaultIISSite|Make the Receiver for Web the default IIS site|false|false||PassThru|Output the updated WebReceiver object|false|false|##Input Type
###Citrix.StoreFront.Model.ReceiverForWeb.WebReceiverService
Parameter WebReceiverService: A .NET class representing the configuration of a StoreFront Web Receiver service
###System.Boolean
Parameter ClassicReceiverExperience: The .NET 'System.Boolean' value type
###System.Management.Automation.SwitchParameter
Parameter DefaultIISSite: The .NET 'System.Management.Automation.SwitchParameter' value type
###System.Management.Automation.SwitchParameter
Parameter PassThru: The .NET 'System.Management.Automation.SwitchParameter' value type
##Return Values
##Examples
###EXAMPLE 1 Set Receiver for Web options
```$rfw = Get-STFWebReceiverService
Set-STFWebReceiverService $rfw -CommunicationAttempts 2 -ShowDesktopViewer $false
```
REMARKS
Configure the number of communication attempts to two and disable the desktop
viewer on the only configured Receiver for Web service.
