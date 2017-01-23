#New-STFEquivalentFarmset
Create a new EquivalentFarmSet for a UserFarmMapping.
##Syntax
```New-STFEquivalentFarmset [-Name] <String> [-AggregationGroupName] <String> [-PrimaryFarms] <String[]> [[-BackupFarms] <String[]>] [-LoadBalanceMode] <Failover | LoadBalanced> [<CommonParameters>]
```
##Detailed Description
An EquivalentFarmSet is a set of PrimaryFarms that are considered to be identical. The applications and desktops available are equivalent so the experience of using any of the PrimaryFarms would be identical to an end user.If a farm is not identical then the applications and desktops available during enumeration and launch may vary as requests are load balanced or failed over between farms. If this is the case consider creating a second EquivalentFarmSet and give them both the same AggregationGroupName to remove any duplicate (or overlapping) applications and desktops.EquivalentFarmSets also define BackupFarms, they will only be used should all PrimaryFarms and EquivalentFarmsSets with identical AggregationGroupName become unavailable.
##Related Commands
*[New-STFEquivalentFarmset](New-STFEquivalentFarmset)
*[Get-STFUserFarmMapping](Get-STFUserFarmMapping)
*[Clear-STFUserFarmMappings](Clear-STFUserFarmMappings)
*[New-STFUserFarmMappingGroup](New-STFUserFarmMappingGroup)
*[Set-STFUserFarmMapping](Set-STFUserFarmMapping)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||Name|The unique Name used to identify the EquivalentFarmSet.|true|false||AggregationGroupName|The AggregationGroupName used to de-duplicate applications and desktops that are available on multiple EquivalentFarmSets. Where multiple EquivalentFarmSets are defined the AggregationGroup will prevent the user seeing the application multiple times if it exists in both places.|true|false||PrimaryFarms|The PrimaryFarms. The farm names should matched those defined in the Store service.|true|false||BackupFarms|The BackupFarms. The farm names should matched those defined in the Store Service.|false|false||LoadBalanceMode|The load balance mode either Failover or LoadBalanced.|true|false|##Input Type
###System.String
Parameter Name: The .NET 'System.String' reference type
###System.String
Parameter AggregationGroupName: The .NET 'System.String' reference type
###System.String[]
Parameter PrimaryFarms: The .NET 'System.String' reference type
###System.String[]
Parameter BackupFarms: The .NET 'System.String' reference type
###Citrix.StoreFront.Model.Store.LoadBalanceMode
Parameter LoadBalanceMode: The .NET 'Citrix.StoreFront.Model.Store.LoadBalanceMode' value type
##Return Values
###EquivalentFarmSet
The .NET 'Citrix.StoreFront.Model.Store.EquivalentFarmSet' reference type
##Notes
Must be added to a UserFarmMapping via the Set-STFUserFarmMapping cmdlet before it can be used.
##Examples
###EXAMPLE 1 Create a new EquivalentFarmSet
```$eu1Farmset = New-STFEquivalentFarmset -Name "EU1" -AggregationGroupName "EUUsers" -PrimaryFarms XenApp1, XenApp2 -BackupFarms XenAppBackup -LoadBalanceMode LoadBalanced
```
REMARKS
Creates a new EquivalentFarmSet with two servers XenApp1 and XenApp2 that will
be load balanced. Should the primary server fail XenAppBackup will be used.
