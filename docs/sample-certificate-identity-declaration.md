#Overview

##Introduction

This sample for the StoreFront Authentication SDK demonstrates how to create and add a new authentication protocol, CertificateIdentityDeclaration, to StoreFront.
This protocol allows a client to send a certificate to the server to identify a user, without providing proof that it has access to the associated private key. The service uses the built-in Kerberos S4U support to map this certificate to an account, verify the account, and extract the group information associated with the account. An identification-level token is then constructed that can be used to launch a session where the user has to fully authenticate to gain access.

##Installer

In common with the other samples, a pre-built installer is provided in addition to the source code.
Before attempting to deploy the pre-built sample installers, it is required to add the certificate at AuthSDK.zip/Certificates/YourCompany.cer to the Third-Party Root Certification Authorities store of the Local Computer account where StoreFront is installed. This is not required for the development machine. If this step is not completed, then the StoreFront Administration Console will display an error because the digital signature of the PowerShell modules associated with this customization will fail to verify.
The installer verifies that there is not an existing customization that implements CertificateIdentityDeclaration before deploying the StoreFront Feature package and the add-ins to the administration console. To actually deploy and enable a sample the “Add/Remove Methods” action from the “Authentication” node of the StoreFront Administration Console should be used.
Before attempting to uninstall a sample, the associated authentication method must first be removed using the “Add/Remove Methods” action. If this is not done, attempting to uninstall will result in a dialog informing the administrator that the feature should be removed using the StoreFront Administration Console first. The sample can then be removed by using the standard “Add/Remove Programs” control panel applet.

#Code Sample

## Visual Studio Solution Layout

The Certificate Identity Declaration solution is composed of five projects:

- Feature contains the code that will be added to the Authentication Service to control the authentication process, including the ASP.Net MVC Controller that manages the authentication protocol.
- Console.Extension contains the code for the administration console, including the data models, action handlers, business logic, and user interface elements.
- Installer is a WiX project to create an msi installer to deploy and remove the Certificate Identity Declaration Feature.
- Installer.CustomActions contains the msi custom actions required to deploy and remove the Certificate Identity Declaration Feature.
- UnitTests contains some simple unit tests to verify the merging of the code into the authentication service, and to verify the behavior of the Service Locator.

This sample does not require any configuration, and so does not contain a configuration project or a StoreFront Administration Console View Extension. It also requires no custom deployment steps or PowerShell commands and so does not have a Feature Installer project.
All the projects target the .NET Framework 4.5 and the MSIL platform, unless specifically stated. Projects that target .NET Framework 3.5 are either part of the StoreFront Administration Console, or loaded by the Console. The rationale behind this is discussed in the StoreFront Service Authentication SDK document.

## Feature Project

This C# class library project contains a new ASP.MVC Controller for handling the HTTP request and response. The protocol specifies a single request/response pattern that is handled by the Declare() method in the Controller, which performs the following:

- Verify that the HTTP verb is POST
- Verify that the request is an RST
- Verify that the client accepts an RSTR response
- Verify that the CertificateIdentityDeclaration protocol is enabled
- Verify that there is a token-issuing service to issue the token
- Verify that a certificate can be extracted from the required header
- Use the built-in Kerberos authenticator to validate the certificate
- Optionally, log the authentication result
- Create and return an RSTR message

In addition, there are classes following the standard pattern for logging and tracing to aid with diagnostics.

## Console.Extension Project

This C# class library project is responsible for:

- Providing the localized authentication method name in the StoreFront Administration Console
- Providing a single, fixed, status message in the StoreFront Administration Console

!!! info "Notes"
	This project is targeted at .NET Framework 3.5, because it will be loaded by the StoreFront Administration Console.

## Installer Project

This WiX project is responsible for the following:
- Creating the CertificateIdentityDeclaration StoreFront Feature Package
- Creating an installer to:
	- Deploy the Feature Package
	- Deploy the StoreFront Administration Console extension
	- Update the registry so that the StoreFront Administration Console will load the extension

!!! info "Notes"
	This project is targeted at the x64 platform

## Installer.CustomActions Project

This C# class library project uses the standard pattern, as described in the StoreFront Authentication SDK document, with the Feature identifier and Authentication Protocol Name set to appropriate values for this customization.

!!! info "Notes"
	- This project is targeted at .NET Framework 3.5.
	- This project is targeted at the x64 platform to ensure that it has access to the correct registry locations.

## Unit Tests Project

This project contains standard: web.config merge and unmerge, route, and protocol choice tests, in addition to tests of the protocol in terms of HTTP request and responses.

# Protocol

This section describes the HTTP-based protocol to use to declare a user identity with a certificate.

## End Point

- URL: /CertificateIdentityDeclaration
- HTTP Method: POST
- Authentication: None
- Request Content-Type: application/vnd.citrix.requesttoken+xml
- Response Content-Type: application/vnd.citrix.requesttokenresponse+xml

The client presents the certificate associated with the user with the following header:
X-Citrix-AM-ClientCertificateDeclaration: <base64 Encoded Data>
The data is the result of exporting the public certificate in one of the following formats: Base64-encoded, DER-encoded X.509 certificate, or a PFX/PKCS12 certificate, before base-64 encoding the resulting data.

## Wire Level

The following  “wire-level” example shows all the HTTP requests and responses when a client attempts to access a protected service (the resources service) and has to obtain security tokens to be granted access.

***Request to Service Provider***

```
GET https://www.example.com/resources/v2 HTTP/1.1
Host: www.example.com
Accept: application/vnd.citrix.resources+xml
```

***Response from Service Provider***

```
HTTP/1.1 401 Unauthorized
Cache-Control: public, no-store, max-age=0
WWW-Authenticate: CitrixAuth realm="6b78ab94-a709-4e3a-8b9b-a49ca317c70c",
                             reqtokentemplate="", reason="notoken",
                             locations="https://www.example.com/Citrix/Authentication/auth/v1/token",
                             serviceroot-hint=https://www.example.com/Citrix/Store/resources/v2
```

At this point the client has to take the information provided in the CitrixAuth challenge and construct a Request for Security Token message to be POSTed to the URL specified in the challenge.

***Request to Authentication Service***

```
POST https://www.example.com/Citrix/Authentication/auth/v1/token HTTP/1.1
Content-Type: application/vnd.citrix.requesttoken+xml
Accept: application/vnd.citrix.requesttokenresponse+xml, application/vnd.citrix.requesttokenchoices+xml
Content-Encoding: utf-8
Host: www.example.com
Content-Length: xxx

<?xml version="1.0" encoding="utf-8"?>
<requesttoken xmlns="http://citrix.com/delivery-services/1-0/auth/requesttoken">
  <for-service>6b78ab94-a709-4e3a-8b9b-a49ca317c70c</for-service>
  <for-service-url>https://www.example.com/Citrix/Store/resources/v2</for-service-url>
  <reqtokentemplate />
  <requested-lifetime>1.06:00:00</requested-lifetime>
</requesttoken>
```

***Response from Service Provider***

```
HTTP/1.1 401 Unauthorized
Cache-Control: public, no-store, max-age=0
WWW-Authenticate: CitrixAuth realm="32f585f3-054d-4ee5-a714-b0e11e312308",
                     reqtokentemplate="", reason="notoken"   
                     locations="https://www.example.com/Citrix/Authentication/auth/v1/protocols",
                     serviceroot-hint="https://www.example.com/Citrix/Authentication/auth/v1/token"
```

Hence, the result of this sequence is another challenge, because the client has not presented the security token required to access the token issuing service. The client must therefore, again, parse the challenge to construct another Request Security Token message and POST it to the indicated Uri, as follows:

***Request to Authentication Service***

```
POST https://www.example.com/Citrix/Authentication/auth/v1/protocols HTTP/1.1
Content-Type: application/vnd.citrix.requesttoken+xml
Accept: application/vnd.citrix.requesttokenresponse+xml, application/vnd.citrix.requesttokenchoices+xml
Content-Encoding: utf-8
Host: www.example.com
Content-Length: xxx

<?xml version="1.0" encoding="utf-8"?>
<requesttoken xmlns="http://citrix.com/delivery-services/1-0/auth/requesttoken">
  <for-service>32f585f3-054d-4ee5-a714-b0e11e312308</for-service>
  <for-service-url>https://www.example.com/Citrix/Authentication/auth/v1/token</for-service-url>
  <reqtokentemplate />
  <requested-lifetime>1.06:00:00</requested-lifetime>
</requesttoken>
Response from Service Provider
HTTP/1.1 300 Multiple Choices
Cache-Control: public, no-store, max-age=0
Content-Type: application/vnd.citrix.requesttokenchoices+xml
Content-Length: xxx

<?xml version="1.0" encoding="utf-8"?>
<requesttokenchoices xmlns="http://citrix.com/delivery-services/1-0/auth/requesttokenchoices">
  <choices>
    <choice>
      <protocol>ExplicitForms</protocol>
      <location>https://www.example.com/Citrix/Authentication/ExplicitForms/Authenticate</location>
    </choice>
    <choice>
      <protocol>CertificateIdentityDeclaration</protocol>
      <location>
           https://www.example.com/Citrix/Authentication/CertificateIdentityDeclaration
      </location>
    </choice>
  </choices>
</requesttokenchoices>
```

In this case the authentication service has responded with a HTTP 300 (Multiple Choices) response, indicating that the security token can be obtained from a choice of URIs. In this case, each choice represents a different authentication protocol.
The client has been configured with a plug-in that knows how to perform CertificateIdentityDeclaration authentication, and so chooses that method by sending the RST to the specified endpoint, as illustrated below:

***Request to Certificate Identity Declaration End-point***

```
POST https://www.example.com/Citrix/Authentication/CertificateIdentityDeclaration HTTP/1.1
Content-Type: application/vnd.citrix.requesttoken+xml
Accept: application/vnd.citrix.requesttokenresponse+xml
X-Citrix-AM-ClientCertificateDeclaration: <Base64EncodedData>
Host: www.example.com
Content-Length: xxx

<?xml version="1.0" encoding="utf-8"?>
<requesttoken xmlns="http://citrix.com/delivery-services/1-0/auth/requesttoken">
  <for-service>32f585f3-054d-4ee5-a714-b0e11e312308</for-service>
  <for-service-url>https://www.example.com/Citrix/Authentication/auth/v1/token</for-service-url>
  <reqtokentemplate />
  <requested-lifetime>1.06:00:00</requested-lifetime>
</requesttoken>
```

If the certificate represents a valid user, then the server responds with a Request Token Response, as follows:

```
HTTP/1.1 200 OK
Cache-Control: no-cache; private; no-store; must-revalidate; max-stale=0; post-check=0;
               pre-check=0; max-age=0
Content-Type: application/vnd.citrix.requesttokenresponse+xml
Content-Length: xxx

<?xml version="1.0" encoding="utf-8"?>
<requesttokenresponse xmlns="http://citrix.com/delivery-services/1-0/auth/requesttokenresponse">
  <for-service>32f585f3-054d-4ee5-a714-b0e11e312308</for-service>
  <issued>2012-06-12T09:50:53.8436039Z</issued>
  <expiry>2012-06-13T05:50:53.8436039Z</expiry>
  <lifetime>0.20:00:00</lifetime>
  <token-template />
  <token>H4sIAAAAAAAEAO29B2AcSZYlJi9tynt/Sv8Id/T8DXarOsQ4AAA==</token>
  <CredentialUpdateInformationList xmlns="http://citrix.com/authentication/response/1">
    <CredentialUpdateInformation>
      <CredentialDisplayName>example.com</CredentialDisplayName>
      <AuthenticationInfoId>Citrix Common Forms 1.0</AuthenticationInfoId>
      <CredentialUpdateService />
    </CredentialUpdateInformation>
  </CredentialUpdateInformationList>
</requesttokenresponse>
```

The client can then use this token to obtain a token to gain access for the resources service.

