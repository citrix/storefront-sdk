#Get-STFAuthenticationServiceProtocol
Get authentication protocols
##Syntax
```
```
##Detailed Description
Gets the authentication protocols configured for a specified Authentication service.
##Related Commands
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFront.Model.Authentication.AuthenticationService
Parameter AuthenticationService: A .NET class representing the configuration of a StoreFront Authentication service
##Return Values
###AuthenticationProtocolChoice
A .NET class representing an Authentication protocol offered by an Authentication service
##Examples
###EXAMPLE 1 Get the authentication protocols
```
```
REMARKS
Get the protocols configured for the only Authentication service.
OUTPUT
```
Enabled ChoiceProperties
----                                                                    
------- ----------------
Certificate                                                               
False {}
CitrixAGBasic                                                             
False {[requestFilter, CitrixAGBasicReques...
CitrixFederation                                                           
True {}
ExplicitForms                                                              
True {}
HttpBasic                                                                 
False {}
IntegratedWindows                                                         
False {}
```