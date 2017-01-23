#Set-STFCitrixAGBasicOptions
Set the CitrixAGBasic protocol options
##Syntax
```
Set-STFCitrixAGBasicOptions [-PasswordRequired] <Boolean> [-AuthenticationService] <AuthenticationService> [<CommonParameters>]
```
##Detailed Description
Set the CitrixAGBasic Authentication service protocol options.
##Related Commands
*[Set-STFCitrixAGBasicOptions](Set-STFCitrixAGBasicOptions)
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.Authentication.AuthenticationService
Parameter AuthenticationService: A .NET class representing the configuration of a StoreFront Authentication service
###Citrix.StoreFront.Model.Authentication.CredentialValidationMode
Parameter CredentialValidationMode: The .NET 'Citrix.StoreFront.Model.Authentication.CredentialValidationMode' value type
###System.Boolean
Parameter PasswordRequired: The .NET 'System.Boolean' value type
##Return Values
##Examples
###EXAMPLE 1 Set CredentialValidationMode to password
```
Set-STFCitrixAGBasicOptions -AuthenticationService $authentication -CredentialValidationMode Password
```
REMARKS
Sets the CitrixAGBasic CredentialValidationMode to password on the only
configured authentication service.
