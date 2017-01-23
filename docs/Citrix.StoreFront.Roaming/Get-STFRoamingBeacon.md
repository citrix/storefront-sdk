#Get-STFRoamingBeacon
Get roaming beacons
##Syntax
```Get-STFRoamingBeacon [-Internal] <SwitchParameter> [<CommonParameters>]
Get-STFRoamingBeacon [-External] <SwitchParameter> [<CommonParameters>]
```
##Detailed Description
Get the roaming beacons configured for the deployment.
##Related Commands
*[Set-STFRoamingBeacon](Set-STFRoamingBeacon)
*[Clear-STFRoamingBeacon](Clear-STFRoamingBeacon)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||Internal|Show internal beacon|true|true (ByValue)||External|Show external beacons|true|true (ByValue)|##Input Type
###System.Management.Automation.SwitchParameter
Parameter Internal: The .NET 'System.Management.Automation.SwitchParameter' value type
###System.Management.Automation.SwitchParameter
Parameter External: The .NET 'System.Management.Automation.SwitchParameter' value type
##Return Values
###String
The .NET 'System.String' reference type
##Examples
###EXAMPLE 1 Get internal beacon
```Get-STFRoamingBeacon -Internal
```
REMARKS
Gets the internal beacon
###EXAMPLE 2 Get external beacons
```Get-STFRoamingBeacon -External
```
REMARKS
Gets the external beacons
