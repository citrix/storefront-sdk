## Creating a PvD Desktop

This document provides an example of a script that creates a Delivery Group containing Personal
vDisk (PvD) desktops.

Before you begin, make sure you follow the steps detailed in the [Getting started guide](./getting-started.md), which shows you how to use Studio to perform the operation you want to script and collect the log of SDK operations that Studio made to perform the task. This output can then be customized to produce a script for automating the task.

!!! tip "Note"
    To ensure you always get the latest enhancements and fixes, Citrix recommends you follow the procedure described in this document, rather than copying and pasting the example script.

**Understand the script**

The following section explains what each part of the script produced by Studio is doing. This will help you with the customization of your own script. Line numbers and line breaks have been added to the script for readability.
```poweshell
1. Start-LogHighLevelOperation -AdminAddress 'test-ddc.mydomain.com:80'
-Source 'Studio' -StartTime 31/07/2013 10:08:58 -Text 'Create Delivery Group `'Win7 PvD
Desktops`''
```

Starts a logged operation and returns a log ID which is supplied to subsequent operations to associate them with the wider task.

```poweshell
2. New-BrokerDesktopGroup -AdminAddress 'test-ddc.mydomain.com:80' -ColorDepth 'TwentyFourBit' -DeliveryType 'DesktopsOnly' -DesktopKind 'Private' -InMaintenanceMode
$False -IsRemotePC $False -LoggingId 846f2d42-a994-4bce-ab58-be05c8d73b99 -MinimumFunctionalLevel 'L7' -Name 'Win7 PvD Desktops' -OffPeakBufferSizePercent 10 -PeakBufferSizePercent 10 -PublishedName 'Win7 PvD Desktops' -Scope @() -SecureIcaRequired \$False -SessionSupport 'SingleSession -ShutdownDesktopsAfterUse \$False -TimeZone 'GMT Standard Time'
```
Creates a new Delivery Group with options collected by the Studio wizard.
```poweshell
3. Add-BrokerMachinesToDesktopGroup -AdminAddress 'test-ddc.mydomain.com:80' -Catalog 'win7-pvd' -Count 2 -DesktopGroup 'Win7 PvD Desktops' -LoggingId 846f2d42-a994-4bce-ab58-be05c8d73b99
```
Adds the number of machines requested from the nominated catalog to the new Delivery Group.
```poweshell
4. Set-Variable -Name 'brokerUsers' -Value @('S-1-5-21-3291547628-200264090-930806513-1104','S-1-5-21-3291547628-200264090-930806513-1105') Get-BrokerUser -AdminAddress 'test-ddc.mydomain.com:80' -Filter {(SID -in $brokerUsers)} -MaxRecordCount 2147483647 Remove-Variable -Name 'brokerUsers' New-BrokerUser -AdminAddress 'test-ddc.mydomain.com:80' -Name
'MYDOMAIN\user1' New-BrokerUser -AdminAddress 'test-ddc.mydomain.com:80' -Name
'MYDOMAIN\user2'
```
The above commands are not required, Studio is verifying users.
```poweshell
5. Test-BrokerAssignmentPolicyRuleNameAvailable -AdminAddress 'test-ddc.mydomain.com:80' -Name @('Win7 PvD Desktops')
```
Studio checks that the policy assignment name is available to use.
```poweshell
6. New-BrokerAssignmentPolicyRule -AdminAddress 'test-ddc.mydomain.com:80' -DesktopGroupUid 41 -Enabled $True -IncludedUserFilterEnabled $False -LoggingId 846f2d42-a994-4bce-ab58-be05c8d73b99 -MaxDesktops 1 -Name 'Win7 PvD Desktops'
```
Create the new policy assignment rule for the Delivery Group. No users are specified here so
all control is through the access policy rule.
```poweshell
7. Set-Variable -Name 'brokerUsers' -Value @('S-1-5-21-3291547628-200264090-930806513-1104','S-1-5-21-3291547628-200264090-930806513-1105')
Get-BrokerUser -AdminAddress 'test-ddc.mydomain.com:80' -Filter {(SID -in \$brokerUsers)} -MaxRecordCount 2147483647

Remove-Variable -Name 'brokerUsers'

New-BrokerUser -AdminAddress 'test-ddc.mydomain.com:80' -Name 'MYDOMAIN\\user1'

New-BrokerUser -AdminAddress 'test-ddc.mydomain.com:80' -Name 'MYDOMAIN\\user2'
```

The above commands are not required, Studio is performing further checks.
```poweshell
8. Test-BrokerAccessPolicyRuleNameAvailable -AdminAddress 'test-ddc.mydomain.com:80' -Name @('Win7 PvD Desktops\_Direct')
```
Studio tests that the access policy rule name is available to use.
```poweshell
9. New-BrokerAccessPolicyRule -AdminAddress 'test-ddc.mydomain.com:80' -AllowedConnections 'NotViaAG' -AllowedProtocols @('HDX','RDP') -AllowRestart $True -DesktopGroupUid
41 -Enabled \$True -IncludedSmartAccessFilterEnabled $True -IncludedUserFilterEnabled $True -IncludedUsers @('MYDOMAIN\user1','MYDOMAIN\user2') -LoggingId 846f2d42-a994-4bce-ab58-be05c8d73b99 -Name 'Win7 PvD Desktops_Direct'
```
Creates the access policy rule for the new desktop for non-NetScaler Gateway connections.
```poweshell
10. Test-BrokerAccessPolicyRuleNameAvailable -AdminAddress 'test-ddc.mydomain.com:80' -Name @('Win7 PvD Desktops_AG') New-BrokerAccessPolicyRule -AdminAddress 'test-ddc.mydomain.com:80' -AllowedConnections 'ViaAG' -AllowedProtocols @('HDX','RDP') -AllowRestart $True -DesktopGroupUid 41 -Enabled $True -IncludedSmartAccessFilterEnabled $True -IncludedSmartAccessTags @() -IncludedUserFilterEnabled $True -IncludedUsers
@('MYDOMAIN\user1','MYDOMAIN\user2') -LoggingId 846f2d42-a994-4bce-ab58-be05c8d73b99 -Name 'Win7 PvDDesktops_AG'
```
Studio repeats this process for NetScaler Gateway connections.
```poweshell
11. Test-BrokerPowerTimeSchemeNameAvailable -AdminAddress 'test-ddc.mydomain.com:80' -Name @('Win7 PvD Desktops_Weekdays') New-BrokerPowerTimeScheme -AdminAddress 'test-ddc.mydomain.com:80' -DaysOfWeek 'Weekdays' -DesktopGroupUid 41 -DisplayName 'Weekdays' -LoggingId 846f2d42-a994-4bce-ab58-be05c8d73b99 -Name 'Win7 PvD Desktops_Weekdays' -PeakHours @($False,$False,$False,$False,$False,$False,$False,$True,$True,$True,$True,$True,$True,$True,$True, $True,$True,$True,$True,$False,$False,$False,$False,$False) -PoolSize @(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) Test-BrokerPowerTimeSchemeNameAvailable -AdminAddress 'test-ddc.mydomain.com:80' -Name @('Win7 PvD Desktops_Weekend') New-BrokerPowerTimeScheme -AdminAddress 'test-ddc.mydomain.com:80' -DaysOfWeek 'Weekend' -DesktopGroupUid 41 -DisplayName 'Weekend' -LoggingId 846f2d42-a994-4bce-ab58-be05c8d73b99 -Name 'Win7 PvD Desktops_Weekend' -PeakHours @($False,$False,$False,$False,$False,$False,$False,$True,$True,$True,$True,$True,$True,$True,$True,$True,$True,$True,$True,$False,$False,$False,$False,$False) -PoolSize @(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
```
Studio checks that the names for the (optional) weekday and weekend power schemes are
available, and adds these.
```poweshell
12. Stop-LogHighLevelOperation -AdminAddress 'test-ddc.mydomain.com:80' -EndTime 31/07/2013 10:09:05 -HighLevelOperationId '846f2d42-a994-4bce-ab58-be05c8d73b99' -IsSuccessful $True
```
Stops the logged operation begun in step 1 and indicates it was successful.

**Customize the script**

This section shows how to convert and adapt the Studio output into a script that is more consumable.

The script creates a Delivery Group containing PvD desktops. The catalog specified in the parameters must exist already and be populated appropriately (with an allocation type of static and a PvD disk). The script is designed to be run from a Powershell command line logged on as a Citrix administrator. No checks are made for permissions; the script will fail if the user does not have the appropriate permissions.
```poweshell
&lt;\#

Sample usage:

.\CreatePvDGroup.ps1 `

-GroupName "Win7 PvD Desktops" `

-SrcCatalog "win7-pvd" `

-NumDesktops 2 `

-Users @('mydomain\user1','mydomain\user2') `

\#&gt;

Param(

[Parameter(Mandatory=\$true)\] \[string\] \$GroupName,

\[Parameter(Mandatory=\$true)\] \[string\] \$SrcCatalog,

\[Parameter(Mandatory=\$true)\] \[int\] \$NumDesktops,

\[Parameter(Mandatory=\$true)\] \[array\] \$Users

\[string\] \$AdminAddress

)
```

The table explains the parameters used in the script.

| Parameter   |                                                                           Description                                                                           |
|-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| SrcCatalog  | The name of the catalog to be used to create the PvD desktop. Create the catalog by specifying an allocation type of static. Machines must also have PvD disks. |
| GroupName   | The name of the catalog to be used to create the PvD desktop. Create the catalog by specifying an allocation type of static. Machines must also have PvD disks. |
| NumDesktops | The number of machines to add to the PvD desktop group. If insufficient machines are available, as many as possible are added.                                  |
| Users       | Which users can access the group. This is a list of users or groups; for example, @('mydomain\Domain Users') or @('mydomain\user1','mydomain\user2')            |

```powershell
Set-HypAdminConnection -AdminAddress $adminAddress
```
Specify the hypervisor admin connection to use. Removes the need for the -AdminAddress for some
of the commands.

```powershell
$peakPoolSize = 2

$weekendPoolSizeByHour = new-object int[] 24

$weekdayPoolSizeByHour = new-object int[] 24

9..17 | %{ $weekdayPoolSizeByHour[$_] = $peakPoolSize }

$peakHours = (0..23 | %{ $_ -ge 9 -and $_ -le 17 })
```
This creates 24 element arrays with a 1 or a 0 in each entry. Use these to specify when peak
hours are for the power schedules for the Delivery Groups. Elements 9 to 17 (hours starting 09:00 to 17:00) for weekdays are set to 1, others are left at 0. Two unassigned machines are powered up during peak times, if available.
```powershell
$logId = Start-LogHighLevelOperation` -Text "Create PvD desktop group" `
-Source "Create PvD Desktop Group Script"
```
Start a new logged operation. This returns a log ID which is passed into subsequent
operations to associate them with the create group task.
```powershell
$grp = New-BrokerDesktopGroup `

-DesktopKind 'Private' `

-DeliveryType 'DesktopsOnly' `

-LoggingId $logId.Id `

-Name $GroupName `

-PublishedName $GroupName `

-SessionSupport 'SingleSession' `

-ShutdownDesktopsAfterUse $False

$count = Add-BrokerMachinesToDesktopGroup `

-Catalog $SrcCatalog `

-Count $NumDesktops `

-DesktopGroup \$GroupName `

-LoggingId $logId.Id

"$count machines added to the PvD desktop group"
```
Create the new Delivery Group, delivering private desktops. The catalog used must have been
populated with suitable machines (permanent with a PvD disk). PublishedName is the name seen by end users; the following uses the same name as the group name.
```powershell
New-BrokerAssignmentPolicyRule \`

-DesktopGroupUid \$grp.Uid \`

-IncludedUserFilterEnabled \$False \`

-LoggingId \$logId.Id \`

-MaxDesktops 1 \`

-Name (\$GroupName + '\_AssignRule') \`

| Out-Null
```
Assigned desktops need an assignment policy. Disable user filter so that access is controlled
entirely by access policy rules.
```powershell
New-BrokerAccessPolicyRule `

-AllowedConnections 'NotViaAG' `

-AllowedProtocols @('HDX','RDP') `

-AllowRestart $True `

-DesktopGroupUid $grp.Uid `

-IncludedSmartAccessFilterEnabled $True `

-IncludedUserFilterEnabled $True `

-IncludedUsers $Users `

-LoggingId $logId.Id `

-Name ($GroupName + '_Direct') `

| Out-Null

New-BrokerAccessPolicyRule `

-AllowedConnections 'ViaAG' `

-AllowedProtocols @('HDX','RDP') `

-AllowRestart $True `

-DesktopGroupUid $grp.Uid `

-IncludedSmartAccessFilterEnabled $True `

-IncludedSmartAccessTags @() `

-IncludedUserFilterEnabled $True `

-IncludedUsers $Users `

-LoggingId $logId.Id `

-Name ($GroupName + '_AG') `

| Out-Null
```
Specify any access restrictions: allow direct access using NetScaler Gateway, using HDX &
RDP protocols. The user can request the desktop be restarted, if necessary.

```poweshell
New-BrokerPowerTimeScheme `

-DaysOfWeek 'Weekdays' `

-DesktopGroupUid $grp.Uid `

-DisplayName 'Weekdays' `

-LoggingId $logId.Id `

-Name ($GroupName + '_Weekdays') `

-PeakHours $peakHours `

-PoolSize $weekdayPoolSizeByHour `

| Out-Null

New-BrokerPowerTimeScheme `

-DaysOfWeek 'Weekend' `

-DesktopGroupUid $grp.Uid `

-DisplayName 'Weekend' `

-LoggingId $logId.Id `

-Name ($GroupName + '_Weekend') `

-PeakHours $peakHours `

-PoolSize $weekendPoolSizeByHour `

| Out-Null
```
Optional: Specify power schedules.

```powershell
Stop-LogHighLevelOperation -HighLevelOperationId
$logId.Id -IsSuccessful $True
```
Stop configuration logging and indicate if successful or not.
