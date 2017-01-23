#Add-STFUserFarmMapping
Add a new UserFarmMapping to a Store Service.
##Syntax
```
```
##Detailed Description
A UserFarmMapping is used to configure a specified group of users to use the EquivalentFarmSets defined within the UserFarmMapping. A UserFarmMapping can be used to partition users between defferent XenApp\XenDesktop servers.
##Related Commands
*[Clear-STFUserFarmMappings](Clear-STFUserFarmMappings)
*[Set-STFUserFarmMapping](Set-STFUserFarmMapping)
*[New-STFEquivalentFarmset](New-STFEquivalentFarmset)
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.Store.StoreService
Parameter StoreService: A .NET class representing the configuration of a StoreFront Store service
###System.String
Parameter Name: The .NET 'System.String' reference type
###System.Collections.Hashtable[]
Parameter GroupMembers: The .NET 'System.Collections.Hashtable' reference type
###Citrix.StoreFront.Model.Store.EquivalentFarmSet[]
Parameter EquivalentFarmSet: The .NET 'Citrix.StoreFront.Model.Store.EquivalentFarmSet' reference type
###System.Int32
Parameter IndexNumber: The .NET 'System.Int32' value type
###System.Management.Automation.SwitchParameter
Parameter PassThru: The .NET 'System.Management.Automation.SwitchParameter' value type
##Return Values
###UserFarmMapping
The .NET 'Citrix.StoreFront.Model.Store.UserFarmMapping' reference type
##Examples
###EXAMPLE 1 Add a new UserFarmMapping 3
```
$eu1Farmset = New-STFEquivalentFarmset -Name "EU1" -AggregationGroupName "EUUsers" -PrimaryFarms XenApp1, XenApp2 -BackupFarms XenAppBackup -LoadBalanceMode LoadBalanced
Add-STFUserFarmMapping -StoreService $store -Name "EUUsers" -GroupMembers (New-STFUserFarmMappingGroup -GroupName "EUGroup1" -AccountSid "S-1-5-21-7375663-6890924511-1272660413-2944159") -EquivalentFarmSet $eu1Farmset
```
REMARKS
Adds a new UserFarmMapping to the /Citrix/Store Store service for EUGroup1.

```
$eu1Farmset = New-STFEquivalentFarmset -Name "EU1" -AggregationGroupName "EUUsers" -PrimaryFarms XenApp1, XenApp2 -BackupFarms XenAppBackup -LoadBalanceMode LoadBalanced
Add-STFUserFarmMapping -StoreService $store -Name "EUUsers" -GroupMembers @{"EUGroup1" = "S-1-5-21-7375663-6890924511-1272660413-2944159"} -EquivalentFarmSet $eu1Farmset
```
REMARKS
Adds a new UserFarmMapping to the /Citrix/Store Store service for EUGroup1.

```
$eu1Farmset = New-STFEquivalentFarmset -Name "EU1" -AggregationGroupName "EUUsers" -PrimaryFarms XenApp1, XenApp2 -BackupFarms XenAppBackup -LoadBalanceMode LoadBalanced
Add-STFUserFarmMapping -StoreService $store -Name "EUUsers" -GroupMembers (New-STFUserFarmMappingGroup -AllUsers) -EquivalentFarmSet $eu1Farmset
```
REMARKS
Adds a new UserFarmMapping to the /Citrix/Store Store service for all users.
