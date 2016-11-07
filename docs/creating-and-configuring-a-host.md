## Creating and configuring a host

The following example shows how to create and configure a host.

Before you begin, make sure you follow the steps detailed in the [Getting started guide](./getting-started.md), which tells you how to use Studio to perform the operation you want to script (in this case, to create a host) and collect the log of SDK operations that Studio made to perform the task. This output can then be customized to produce a script for automating host creation.

!!! tip "Note"
    To ensure you always get the latest enhancements and fixes, Citrix recommends you follow the procedure described in this document, rather than copying and pasting the example script. Line numbers and line breaks have been added to the script for readability.

**Understand the script**

The following section explains what each part of the script produced by Studio is doing. This will help you with the customization of your own script. Line numbers have been added for readability.

```powershell
1. Get-LogSite -AdminAddress 'mycontroller.example.com:80'
```
Queries the configuration logging service to retrieve information about the site
configuration.

```powershell
2. Start-LogHighLevelOperation -AdminAddress 'mycontroller.example.com:80'
-Source 'Studio' -StartTime 14/08/2013 14:30:28 -Text 'Create Connection `'Example XenServer`''
```
Starts a high-level logging operation with the configuration logging operation within which the rest of the commands will exist. Returns a log ID which is supplied to subsequent operations.

```powershell
3. Set-HypAdminConnection -AdminAddress 'mycontroller.example.com:80'
```

Sets the location of the Host Service that will be used by the configuration cmdlets. Because the Host Service exposes a PowerShell provider, not all of the cmdlets can take an address for the service so this cmdlet sets a default location.

```powershell
4. New-Item -ConnectionType 'XenServer' -HypervisorAddress @('http://xenhost1.example.com') -LoggingId e355ce51-8cbb-400a-ae81-1fdc567239cb -Path @('XDHyp:\Connections\Example XenServer') -Scope @() -Password ******** -UserName 'root'
```

Creates a connection to a XenServer (xenhost1.example.com). This is a non-persistent connection
and is available only to this PowerShell runspace.

```powershell
5. Stop-LogHighLevelOperation -AdminAddress 'mycontroller.example.com:80' -EndTime 14/08/2013 14:30:29 -HighLevelOperationId 'e355ce51-8cbb-400a-ae81-1fdc567239cb' -IsSuccessful $True
```

Stops the logged operation begun previously and indicates it was successful.
```powershell
6. Get-LogSite -AdminAddress 'mycontroller.example.com:80'
```
Queries the configuration logging service to retrieve information about the site configuration.

```powershell
7. Start-LogHighLevelOperation -AdminAddress 'mycontroller.example.com:80' -Source 'Studio' -StartTime 14/08/2013 14:30:30 -Text 'Update Connection `'Example XenServer`''
```
Starts a new high-level logging operation.
```powershell
8. Set-HypAdminConnection -AdminAddress 'mycontroller.example.com:80'
```
Sets the Host Service address details again (note that this repetition is removed in the optimized script below).
```powershell
9. Set-Item -HypervisorAddress @('http://xenhost1.example.com','http://xenhost2.example.com') -LoggingId 44e15629-6906-4840-a36c-984aaf67be6d -PassThru -Path @('XDHyp:\\Connections\\Example XenServer') -Password ******** -UserName 'root'
```
Updates the connection created in step 4. Because there is more than one XenServer in the pool, it supplies all the addresses to enable High Availability.
```powershell
10. Stop-LogHighLevelOperation -AdminAddress 'mycontroller.example.com:80' -EndTime 14/08/2013 14:30:31 -HighLevelOperationId '44e15629-6906-4840-a36c-984aaf67be6d' -IsSuccessful \$True
```
Stops the logging operation begun in step 7.
```powershell
11. Get-LogSite -AdminAddress 'mycontroller.example.com:80'
```
Queries the configuration logging service to retrieve information about the site configuration.
```powershell
12. Start-LogHighLevelOperation -AdminAddress 'mycontroller.example.com:80' -Source 'Studio'
-StartTime 14/08/2013 14:31:03 -Text 'Create Resources `'Example Resources`' and Persist Connection `'Example XenServer`''
```
Starts a new logging operation.
```powershell
13. Set-HypAdminConnection -AdminAddress 'mycontroller.example.com:80'
```
Sets the Host Service address details again.
```powershell
14. Get-ChildItem -Path @('XDHyp:\Connections')
```
Gets the contents of the host connection to populate the wizard dialogs.
```powershell
15. Set-HypAdminConnection -AdminAddress 'mycontroller.example.com:80'
```
Sets the Host Service address details again.
```powershell
16. Remove-Item -LoggingId 76caa3f4-df93-4cb2-b78d-6a8824766314 -Path @('XDHyp:\Connections\Example XenServer')
```
Removes the temporary connection created in the wizard.
```powershell
17. Set-HypAdminConnection -AdminAddress 'mycontroller.example.com:80'
```
Sets the Host Service address details again.
```powershell
18. New-Item -ConnectionType 'XenServer' -HypervisorAddress @('http://xenhost1.example.com','http://xenhost2.example.com') -LoggingId 76caa3f4-df93-4cb2-b78d-6a8824766314 -Path @('XDHyp:\\Connections\\Example XenServer') -Persist -Scope @() -Password ******** -UserName 'root'
```

Recreates the connection as a persistent connection which is written to the database and available to other PowerShell runspaces.

```powershell
19. New-BrokerHypervisorConnection -AdminAddress 'mycontroller.example.com:80' -HypHypervisorConnectionUid a14096ba-5074-44ff-b596-371e345c0449 -LoggingId 76caa3f4-df93-4cb2-b78d-6a8824766314
```
Adds the host connection to the Broker Service.
```powershell
20. Set-HypAdminConnection -AdminAddress 'mycontroller.example.com:80'
```
Sets the Host Service address details again.
```powershell
21. New-Item -HypervisorConnectionName 'Example XenServer' -LoggingId 76caa3f4-df93-4cb2-b78d-6a8824766314 -NetworkPath @('XDHyp:\Connections\Example XenServer\Network0.network') -Path @('XDHyp:\HostingUnits\Example Resources') -PersonalvDiskStoragePath @('XDHyp:\Connections\Example XenServer\PvdStorage.storage') -RootPath 'XDHyp:\Connections\Example XenServer' -StoragePath
@('XDHyp:\Connections\Example XenServer\Primary OS.storage')
```
Creates the HostingUnit (referred to as Resources in Studio) using the information gathered in
step 14.
```powershell
22. Set-HypAdminConnection -AdminAddress 'mycontroller.example.com:80'
```
Sets the Host Service address details again.
```powershell
23. Get-Item -Path @('XDHyp:\Connections\Example XenServer')
```
Retrieves the newly created object.

```powershell
Stop-LogHighLevelOperation -AdminAddress 'mycontroller.example.com:80' -EndTime 14/08/2013 14:31:07 -HighLevelOperationId '76caa3f4-df93-4cb2-b78d-6a8824766314' -IsSuccessful $True
```
Stops the logged operation begun previously and indicates if it was successful.

**Customize the script**

The following section shows how to convert and adapt the Studio output into a script that is more consumable. The following script has been simplified so that, instead of creating a temporary host connection in the process of acquiring information in the wizards as in the Studio script above, a persistent connection is created. Information is then queried from within this to create the HostingUnit (Resources). Note that the LoggingId and HypHyperConnectionUid details are different.

Line numbers have been added for readability; each numbered item is a single PowerShell command.
```powershell
1. Start-LogHighLevelOperation -AdminAddress 'mycontroller.example.com:80' -Source 'Studio' -Text 'Create Connection \`'Example XenServer\`''

2. Set-HypAdminConnection -AdminAddress 'mycontroller.example.com:80'

3. New-Item -ConnectionType 'XenServer' -HypervisorAddress @('http://xenhost1.example.com','http://xenhost2.example.com')-LoggingId
76caa3f4-df93-4cb2-b78d-6a8824766314 -Path @('XDHyp:\\Connections\\Example XenServer') -Persist -Scope @() -Password \*\*\*\*\*\*\*\* -UserName 'root'

4. Get-ChildItem -Path @('XDHyp:\Connections')

5. New-BrokerHypervisorConnection -AdminAddress 'mycontroller.example.com:80' -HypHypervisorConnectionUid a14096ba-5074-44ff-b596-371e345c0449 -LoggingId
76caa3f4-df93-4cb2-b78d-6a8824766314

6. New-Item -HypervisorConnectionName 'Example XenServer' -LoggingId
76caa3f4-df93-4cb2-b78d-6a8824766314 -NetworkPath @('XDHyp:\Connections\Example XenServer\Network
0.network') -Path @('XDHyp:\HostingUnits\Example Resources') -PersonalvDiskStoragePath @('XDHyp:\Connections\Example XenServer\Pvd Storage.storage') -RootPath 'XDHyp:\Connections\Example XenServer' -StoragePath @('XDHyp:\Connections\Example XenServer\PrimaryOS.storage')

7. Stop-LogHighLevelOperation -AdminAddress 'mycontroller.example.com:80' -HighLevelOperationId '76caa3f4-df93-4cb2-b78d-6a8824766314 -IsSuccessful $True
```
