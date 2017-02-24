#Import-STFSamlEncryptionCertificate
Import the encryption certificate to be used by the SAML Service Provider
##Syntax
```
```
##Detailed Description
Import, for the specified authentication service, the encryption certificate to be used by SAML Service Provider
##Related Commands
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.Authentication.AuthenticationService
Parameter AuthenticationService: A .NET class representing the configuration of a StoreFront Authentication service
###System.String
Parameter FilePath: The .NET 'System.String' reference type
###System.String
Parameter Password: The .NET 'System.String' reference type
##Return Values
##Examples
###EXAMPLE 1 Import the encryption certificate to be used by the SAML Service Provider, when a password is not required.
```
Import-STFSamlEncryptionCertificate -AuthenticationService $authentication -FilePath C:\windows\temp\EncryptionCertificate.pfx
```
REMARKS
Import the encryption certificate to be used by the SAML Service Provider, when no password is required for the
private key.
