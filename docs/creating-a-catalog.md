##Creating a Catalog

The following example shows how to create a catalog for a set of Machine Creation Services
(MCS) machines.

Before you begin, make sure you follow the steps detailed in [Get started with the
SDK](./getting-started.md).

This document tells you how to use Studio to perform the operation you want to script (in this case, to create a catalog for a set of Machine Creation Services machines) and collect the log of SDK operations that Studio made to perform the task. This output can then be customized to produce a script for automating catalog creation.

!!! tip "Note"
    To ensure you always get the latest enhancements and fixes, Citrix recommends you follow the procedure described in this document, rather than copying and pasting the example script. Line numbers and line breaks have been added to the script for readability.

**Understand the script**

The following section explains what each part of the script produced by Studio is doing. This
will help you with the customization of your own script. Line numbers have been added for readability.
```PowerShell
1. Start-LogHighLevelOperation -AdminAddress
'ddc.dumdev.internal.citrix.com:80' -Source 'Studio' -StartTime 29/05/2013 14:43:08 -Text 'Create Machine Catalog `'ExampleMachines`''
```
Starts a logged operation and returns a log ID which is supplied to subsequent
operations to associate them with the larger task.
```PowerShell
2. New-BrokerCatalog
-AdminAddress 'ddc.dumdev.internal.citrix.com:80' -AllocationType 'Permanent' -Description 'Example Machines' -IsRemotePC $False -LoggingId
f39a2792-064a-43eb-97c7-397cc1238e46 -MinimumFunctionalLevel 'L7' -Name 'ExampleMachines' -PersistUserChanges 'OnPvd' -ProvisioningType 'MCS' -Scope @()
-SessionSupport 'SingleSession'
```

Creates a Broker
catalog. This catalog is populated with machines which are about to be
created.
```PowerShell
3. New-AcctIdentityPool -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -AllowUnicode -Domain 'dumdev.internal.citrix.com'
   -IdentityPoolName 'ExampleMachines' -LoggingId f39a2792-064a-43eb-97c7-397cc1238e46 -NamingScheme 'Example-####' -NamingSchemeType 'Numeric'
   -OU 'OU=DUMVMs,DC=dumdev,DC=internal,DC=citrix,DC=com' -Scope @()
```

Creates an Identity Pool. This defines the mechanism for creating AD computer accounts. This
becomes a container for AD accounts created for the machines that are to be created.
```PowerShell
4. Set-BrokerCatalogMetadata -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -CatalogId 1 -LoggingId f39a2792-064a-43eb-97c7-397cc1238e46 -Name
'Citrix_DesktopStudio_IdentityPoolUid' -Value 'b99aee6d-8772-4dbc-978b-8eb9a26e2407'
```
Sets metadata on the Broker catalog with details of the Identity Pool. This is not essential.
```PowerShell
5. Test-ProvSchemeNameAvailable -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -ProvisioningSchemeName @('ExampleMachines')
```
Checks that the requested name is available. This is not essential.
```PowerShell
6. New-ProvScheme -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -CleanOnBoot -HostingUnitName 'SharedNFS' -IdentityPoolName 'ExampleMachines' -LoggingId
f39a2792-064a-43eb-97c7-397cc1238e46 -MasterImageVM 'XDHyp:\hostingunits\SharedNFS\BaseVM.vm\Base OS,
domain joined and activated.snapshot \Pre-reqs installed.snapshot\\Updates Applied.snapshot\VDA75-no agent.snapshot\Updated Agent.snapshot'
-NetworkMapping @{0='xdhyp:\hostingunits\SharedNFS\Network0.network'} -PersonalVDiskDriveLetter P -PersonalVDiskDriveSize 10 -ProvisioningSchemeName 'ExampleMachines'
-RunAsynchronously -Scope @() -UsePersonalVDiskStorage -VMCpuCount 1 -VMMemoryMB 1024
```

Creates a provisioning scheme object. This is a template for the machines that are to be created. It specifies the hypervisor, network, storage, memory, number of CPUs to be used etc. It takes parameters from the system already set up, such as the HostingUnit name and the path to the VM snapshot to be used for the machines to be created. This command makes a 'consolidated' copy of the VM snapshot being used and, as a result, the process can take time to complete.

In this example, the Studio script specified the -RunAsyncronous flag on this command. This means the command will return control to the administrator before it has completed, so you must wait for it to finish before performing any operations that require it to be complete. If this flag is not specified, the command runs synchronously in-line and control is not returned until the command completes (successfully or otherwise). You can check the status of an asynchronous task using the Get-ProvTask cmdlet. Supply the task ID returned from the operation that started the task; in this case, the New-ProvScheme cmdlet.
```PowerShell
7. Set-BrokerCatalog -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -LoggingId f39a2792-064a-43eb-97c7-397cc1238e46 -Name 'ExampleMachines'
   -ProvisioningSchemeId 76125e3a-9001-4993-86b6-eefc85c87880
```

Updates the BrokerCatalog with the unique Id of the provisioning scheme created above.
```PowerShell
8. Add-ProvSchemeControllerAddress -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -ControllerAddress @('DDC.dumdev.internal.citrix.com')
-LoggingId f39a2792-064a-43eb-97c7-397cc1238e46 -ProvisioningSchemeName 'ExampleMachines'
```

Adds a set of controller addresses to the provisioning scheme object. This is a list of addresses that the machines created can use to register with a Controller (broker) when deployed. The machines' registration addresses can be supplied in many ways; however, this information is required if the administrator wants to use the 'Allow Machine Creation Service to supply this' in the VDA installer. Changes to this list affect only machines created after the change, not existing machines.
```PowerShell
9. Get-AcctADAccount -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -IdentityPoolUid b99aee6d-8772-4dbc-978b-8eb9a26e2407 -Lock $False -MaxRecordCount 2147483647 -State 'Available'
```
Studio gets a list of available Machine Identities from the Identity Pool so that, if existing accounts have been created in the past but are unused, these can be consumed instead of creating new accounts. Note that this is not required in a script because new accounts can be created instead, provided the script is running in a context that has permissions to do this. However, if the script does not have permissions to create accounts, change the script to consume available accounts (a separate process will be required to provide a pool of accounts into the Identity Pool, before running the script).

```PowerShell
10. New-AcctADAccount -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -Count 2 -IdentityPoolUid b99aee6d-8772-4dbc-978b-8eb9a26e2407 -LoggingId
f39a2792-064a-43eb-97c7-397cc1238e46
```

Creates the required AD computer accounts in Active Directory. The script creates one account
but, if required, it can create more using the 'Count' parameter of the command. The accounts are created into the OU defined in the provisioning scheme created above.

```PowerShell
11. New-ProvVM -ADAccountName @('DUMDEV\Example-0001\$','DUMDEV\Example-0002\$') -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -LoggingId
f39a2792-064a-43eb-97c7-397cc1238e46 -ProvisioningSchemeName 'ExampleMachines' -RunAsynchronously
```

Creates virtual machines, based on the template definition in the provisioning scheme
created above. This process may take time to complete.
```PowerShell
12. Lock-ProvVM -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -LoggingId f39a2792-064a-43eb-97c7-397cc1238e46
    -ProvisioningSchemeName 'ExampleMachines' -Tag 'Brokered' -VMID @('0710bb77-d01f-d006-4d67-5472e5cd349f')
```
Locks the provisioned virtual machines and prevents accidental modification of the virtual
machine. Consumers of the SDK can use this to indicate that the virtual machine is in use and why it is locked. The script locks the VM with a tag of 'Brokered' to indicate the virtual machine is created and added to a Broker catalog and must not be deleted without first being removed from the catalog. You can set the Tag name to whatever is required.
```PowerShell
13. New-BrokerMachine -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -CatalogUid 1 -HostedMachineId '0710bb77-d01f-d006-4d67-5472e5cd349f' -HypervisorConnectionUid 1
-LoggingId f39a2792-064a-43eb-97c7-397cc1238e46 -MachineName 'S-1-5-21-3918710733-2340574387-1999698698-109114'
```
Creates a Broker Machine object. These are objects stored in the catalog which join the
provisioned machine with the catalog.

```PowerShell
14. Start-BrokerMachinePvdImagePrepare -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -InputObject @(2) -LoggingId f39a2792-064a-43eb-97c7-397cc1238e46
```
Requests the Broker Service to initiate a preparation operation for Personal vDisk. This is required to allow the machine to initialize the storage for Personal vDisk.
```PowerShell
15. Stop-LogHighLevelOperation -AdminAddress 'ddc.dumdev.internal.citrix.com:80' -HighLevelOperationId f39a2792-064a-43eb-97c7-397cc1238e46 -IsSuccessful $true
```

Stops the logged operation begun in the first step and indicates it was successful.

**Customize the script**

The following section shows how to convert and adapt the Studio output into a script that is
more consumable. In addition to using variables and removing commands that are not required, it shows how to add machine creation into a loop so that you can control the number of machines created. Line numbers have been added for readability.

```PowerShell
1[CmdletBinding()]

param

(

[Parameter(Mandatory=$true)] [string] $hostingUnitPath,

[Parameter(Mandatory=$true)] [string] $catalogName,

[string] $catalogDescription,

[Parameter(Mandatory=$true)] [int] $numVmsToCreate,

[string] $adminAddress,

[Parameter(Mandatory=$true)] [string] $namingScheme,

[string] $OU,

[Parameter(Mandatory=$true)] [string] $domain,

[Parameter(Mandatory=$true)] [string] $masterImagePath

)

2. Set-HypAdminConnection -AdminAddress $adminAddress

3. $hostingUnit = get-item $hostingUnitPath

4. $hostConnection = $hostingUnit.hypervisorConnection

5. $brokerHypConnection = Get-BrokerHypervisorConnection -HypHypervisorConnectionUid $hostConnection.HypervisorConnectionUid

6. # Start logged operation

7. $loggingOp = Start-LogHighLevelOperation -AdminAddress $adminAddress -Source 'Scripted' -Text "Create Machine Catalog `'$catalogName`'"

8. $loggingId = $loggingOp.Id

9. # Create the broker catalog and the AD Identity account pool

10. $catalog = New-BrokerCatalog -AllocationType 'Permanent' -Description $catalogDescription -IsRemotePC $False

-MinimumFunctionalLevel 'L7' -Name $catalogName -PersistUserChanges
'OnPvd' -ProvisioningType 'MCS' -Scope @() -SessionSupport 'SingleSession' -LoggingId $loggingId -AdminAddress
$adminAddress

11. $adPool = New-AcctIdentityPool -IdentityPoolName $catalogName
-NamingScheme $namingScheme

-NamingSchemeType 'Numeric' -OU $OU -Domain $domain -AllowUnicode
-LoggingId $loggingId -AdminAddress $adminAddress

12. Set-BrokerCatalogMetadata -CatalogId $catalog.Uid -Name
'Citrix_DesktopStudio_IdentityPoolUid' -Value $adPool.IdentityPoolUid -LoggingId $loggingId -AdminAddress
$adminAddress

13. ###################################################################

14. #create the ProvisioningScheme and wait for it to complete (reporting progress)

15. $provSchemeTaskID = New-ProvScheme -ProvisioningSchemeName
$catalogName -HostingUnitUID $hostingUnit.HostingUnitUID

-IdentityPoolUID $adpool.IdentityPoolUid -CleanOnBoot -MasterImageVM
$masterImagePath -UsePersonalVDiskStorage

-PersonalVDiskDriveLetter P -PersonalVDiskDriveSize 10 -RunAsynchronously
-LoggingId $loggingId -AdminAddress $adminAddress

16. $ProvTask = get-provTask -TaskID $provSchemeTaskID -AdminAddress $adminAddress

17. $taskProgress = 0

18. write-host "Creating New ProvScheme"

19. while ($provTask.Active -eq $true)

20. {

21. # catch an uninitialized task progress, this occurs until the product initialized the value

22. try {$totalPercent = if ($provTask.TaskProgress){$provTask.TaskProgress} else {0}} catch {}

23. Write-Progress -activity "Creating Provisioning Scheme:" -status "$totalPercent% Complete:" -percentcomplete $totalPercent

24. sleep 30

25. $ProvTask = get-provTask -TaskID $provSchemeTaskID -AdminAddress $adminAddress

26. }

27. write-host "New ProvScheme Creation Finished"

28. $provScheme = get-provScheme -ProvisioningSchemeUID $provTask.ProvisioningSchemeUid

29. $controllers = Get-BrokerController | select DNSName

30. Add-ProvSchemeControllerAddress -ProvisioningSchemeUID $provScheme.ProvisioningSchemeUID -ControllerAddress $controllers -LoggingId $loggingId -AdminAddress $adminAddress

31. ###################################################################

32. # Set the provisioning scheme id for the broker catalog

33. Set-BrokerCatalog -InputObject $catalog -ProvisioningSchemeId $provTask.ProvisioningSchemeUid -LoggingId $loggingId -AdminAddress $adminAddress

34. ###################################################################

35. # create the AD accounts required and then create the Virtual machines (reporting progress)

36. $accts = New-AcctADAccount -IdentityPoolUid $adPool.IdentityPoolUid -Count $numVMsToCreate -LoggingId $loggingId -AdminAddress $adminAddress

37. $provVMTaskID = New-ProvVM -ProvisioningSchemeUID $provScheme.ProvisioningSchemeUID

-ADAccountName $accts.SuccessfulAccounts -RunAsynchronously -LoggingId $loggingId -AdminAddress $adminAddress

38. # wait for the VMS to finish Provisioning

39. $ProvTask = get-provTask -TaskID $provVMTaskID -AdminAddress $adminAddress

40. while ($provTask.Active -eq $true)

41. {

42. # catch an uninitialized task progress, this occurs until the product initialized the value

43. try {$totalPercent = if ($provTask.TaskProgress){$provTask.TaskProgress} else {0}} catch {}

44. Write-Progress -activity "Creating Machines:" -status "$totalPercent% Complete:" -percentcomplete $totalPercent

45. sleep 5

46. $ProvTask = get-provTask -TaskID $provVMTaskID -AdminAddress $adminAddress

47. }

48. write-host "VM Creation Finished"

49. # Lock the VMs and add them to the broker Catalog

50. $provisionedVMs = get-ProvVM -ProvisioningSchemeUID
$provScheme.ProvisioningSchemeUID -AdminAddress $adminAddress

51. $provisionedVMs | Lock-ProvVM -ProvisioningSchemeUID $provScheme.ProvisioningSchemeUID
-Tag 'Brokered' -LoggingId $loggingId -AdminAddress $adminAddress

52. $provisionedVMs | ForEach-Object {New-BrokerMachine -CatalogUid $catalog.UID -HostedMachineId $_.VMId

-HypervisorConnectionUid $brokerHypConnection.UID -MachineName $_.ADAccountSid -LoggingId $loggingId -AdminAddress $adminAddress}

53. Stop-LogHighLevelOperation -IsSuccessful $true -HighLevelOperationId $loggingId -AdminAddress $adminAddress
```
