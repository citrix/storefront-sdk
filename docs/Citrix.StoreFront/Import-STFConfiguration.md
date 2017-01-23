#Import-STFConfiguration
Imports a zip file containing configuration elements that form a Citrix StoreFront deployment. This zip file may be unencrypted in the form of a '.zip' file or encrypted in the form of a '.ctxzip'.
##Syntax
```Import-STFConfiguration -ConfigurationZip <String> [-Credential <PSCredential>] [-HostBaseUrl <String>] [-SiteId <Int64>] [<CommonParameters>]
```
##Detailed Description
Imports a zip file containing configuration elements that form a Citrix StoreFront deployment. This zip file may be unencrypted in the form of a '.zip' file or encrypted in the form of a '.ctxzip'.
##Related Commands
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||ConfigurationZip|The name of the backup archive WITH its correct file extension such as .ctxzip or .zip.|true|true (ByValue)||Credential|A predefined PowerShell credential object containing the same password that was used to export the backup archive.|false|false||HostBaseUrl|Specify if you wish to use a HostBaseURL other than the one contained in the configuration backup you are importing.|false|false||SiteId|The IIS SiteID for the Storefront website. Mandatory if importing onto a factory default Storefront installation. Typically 1.|false|true (ByValue)|##Input Type
###System.String
Parameter ConfigurationZip: The .NET 'System.String' reference type
###System.Management.Automation.PSCredential
Parameter Credential: The .NET 'System.Management.Automation.PSCredential' reference type
###System.String
Parameter HostBaseUrl: The .NET 'System.String' reference type
###System.Int64
Parameter SiteId: The .NET 'System.Int64' value type
##Return Values
##Examples
###EXAMPLE 1 Import Config to Configure an Unconfigured Machine
```Import-DSConfiguration -configurationZip '$env:userprofile\desktop\ConfigBackup.zip' -hostBaseUrl 'https://storefront.example.com' -siteId 1
```
REMARKS
Using the password supplied in $CredObject this cmdlet will decrypt and import
the ConfigBackup.ctxzip backup archive using the host base url and site id
from the exported configuration.
Example PSCredential:
$User = Any non empty string will suffice here. The exported configuration is
secured by only using the $Password.
$Password = 'Secret'
$Password = $Password | ConvertTo-SecureString -asPlainText -Force
$CredObject = New-Object
System.Management.Automation.PSCredential($User,$Password)
Create a PowerShell credential object containing a username and password for
symmetric encryption and decryption of configuration backup archives.
PowerShell credential objects store passwords as secure strings in memory.
The user is irrelevant but mandatory to create a PowerShell credential object.
The example code uses the currently logged in user.
The password is used for symmetric encryption/decryption of the backup
archive. NOTE: The password DOES NOT need to match the user's password to
create a valid credential object.
###EXAMPLE 2 Basic Config Import
```Import-DSConfiguration -configurationZip '$env:userprofile\desktop\ConfigBackup.zip'
```
REMARKS
This will import the ConfigBackup.zip configuration archive using the host
base url and site id from the exported configuration.
###EXAMPLE 3 Import Config to Configure an Unconfigured Machine
```Import-DSConfiguration -configurationZip '$env:userprofile\desktop\ConfigBackup.zip' -hostBaseUrl 'https://storefront.example.com' -siteId 1
```
REMARKS
This will import the ConfigBackup.zip configuration archive using the supplied
host base url and SiteId for the newly created deployment.
