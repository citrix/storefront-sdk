#Relying Party Authentication

##Scope

The purpose of this document is to describe the CitrixAuth authentication scheme used by the StoreFront Services Relying Parties to obtain user identity information.

##CitrixAuth Scheme

This section defines an RFC2617 [1] extension to support authentication to StoreFront Services Relying Parties, such as the resources service. The extension auth-scheme is CitrixAuth and is case-sensitive. It uses the standard HTTP Authorization and WWW-Authenticate HTTP headers as defined in RFC2617.

The headers have the following formats, in conformance with RFC2617:

`Authorization: CitrixAuth {security-token}`

If no valid Authorization header for the CitrixAuth scheme is found for the realm of the service it is sent to, then a challenge shall be issued as follows:

```
WWW-Authenticate: CitrixAuth realm="{service-id}" , reqtokentemplate="{template}", 
                             reason="{reason-description}",locations="{url-list}",
                             serviceroot-hint=”{service-root}”
```
The parameters are defined by the following:

|Parameter|Description|
|-|-|
|{service-id}|The unique identifier of the consuming service. With the hostname of the service being accessed it defines a Protection Space as per RFC2617 section 1.2|
|{security-token}|The serialized security token used to authenticate the user|
|{template}|This is a string that shall be passed by the client to the server when requesting a token for a specific service. The server can use this value to determine the token format to use. This value should be empty for current implementations, but must still be passed to the server.|
|{reason-description}|The reason why a challenge has been issued. This is to assist the client with managing cached tokens.|
|{url-list}|An ordered list of URLs separated by the ‘|’ or “pipe” character, to which a RequestToken message should be sent to obtain a token.|
|{serviceroot}|A hint for the client as to the root URL for the protection space associated with the current request. This simplifies the client decision-making regarding sending cached tokens to respond to the challenge.|

The reason-description may be one of the following values:

- notoken: No authentication token was supplied.
- expired: The supplied token is no longer valid.
- notforthisservice: The token is valid, but was not issued for the service trying to consume it.
- nottrusted: A valid token has been issued by a service that the consumer does not trust.
- invalidtoken: The token extracted from the Authorization header was invalid, for example it may be badly formed.
- passwordClaimNotFound: A required password claim was not found.
- badpassword: For a password-based token, the password has been changed or has expired since the token was issued and is no longer valid.
- badaccount: The account associated with the subject was invalid, for example it may be locked out.
- invalidAudience: The original token was not requested for a valid audience (see below).
- tokenSignatureNotVerified: The signature of the token could not be verified.
- wrongclaims: The token does not contain the required claims.
- gatewayclaimsinconsistent: The gateway identified in the supplied token does not match the gateway discovered by the relying party.

##Protection Space

RFC2617 section 1.2 defines a Protection Space as the domain over which credentials can be automatically applied. If a prior request has been authorized, the same credentials may be reused for all other requests within that protection space for a period of time determined by the authentication scheme, parameters, and/or user preference. The CitrixAuth scheme is consistent with other schemes in that a single protection space cannot extend outside the scope of its server. The CitrixAuth scheme uses both the service-id (Realm) and the audience to which the request is to be sent, to define a protection space, and the client should not automatically send credentials to services outside of the protection space defined for a particular credential. In this context, the audience is defined by the scheme, host name, and port associated with the original request.
The serviceroot-hint in the challenge provides the client with the root of the protection space for the current request. This enables a better caching strategy in the client, if the initial request is not to the root of the protection space.

##Example

The following illustrates a CitrixAuth challenge and response:

Request to the Relying Party

```
GET https://www.example.com/Citrix/Store/resources/v2/T2VvUndOMEZMM1VBK2NpYzY4PQ--/image/16 HTTP/1.1
Host: www.example.com
Accept: image/png
```

Response from the Relying Party

```
HTTP/1.1 401 Unauthorized
WWW-Authenticate: CitrixAuth realm="6b78ab94-a709-4e3a-8b9b-a49ca317c70c",
                             reqtokentemplate="", reason="notoken", 
                             locations="https://www.example.com/Citrix/Authentication/auth/v1/token",
                             serviceroot-hint="https://www.example.com/Citrix/Store2/resources/v2"
```

The client uses the information in the challenge to obtain an appropriate security token for the Service Provider, and then resends the original request with an attached Authorization header, as follows:

```
GET https://www.example.com/Citrix/Store/resources/v2/T2VvUndOMEZMM1VBK2NpYzY4PQ--/image/16 HTTP/1.1
Host: www.example.com
Accept: image/png
Authorization: CitrixAuth H4sIAAAAAAAEAO29B2AcSZYlJi9tynt/SvVK1+B0oQiAYBMk2JBAEOzBiM3mku…
```

Response from the Relying Party

```
HTTP/1.1 200 OK
Content-Type: image/png
Cache-Control: public, no-store, max-age=0
Content-Length: 773

<binary data>
```

##Client Processing of a Challenge

When a client receives a CitrixAuth challenge, it must respond by sending a Request Security Token message to the location specified in the challenge. For more information on the Request Security Token message see the StoreFront Security Token Services API document [2].
Consider the following example. The client has tried to access the URL: https://storefront.enterprise.com/Citrix/Store/resources/v2/launch
and received the following challenge:

```
WWW-Authenticate: CitrixAuth realm="d5c937a6-a09d-4805-adbb-ff92208f7466",
               reqtokentemplate="", reason="notoken",
               locations="https://storefront.enterprise.com/Citrix/Authentication/auth/v1/token"
               serviceroot-hint="https://storefront.enterprise.com/Citrix/Store/resources/v2"
```

The client should respond by sending the following message to the location specified in the challenge, that is https://storefront.enterprise.com/Citrix/Authentication/auth/v1/token.

```
POST /Citrix/Authentication/auth/v1/token HTTP/1.1
Content-Type: application/vnd.citrix.requesttoken+xml
Accept: application/vnd.citrix.requesttokenresponse+xml, application/vnd.citrix.requesttokenchoices+xml
Content-Encoding: utf-8
Host: storefront.enterprise.com

<?xml version="1.0" encoding="utf-8" ?>
<requesttoken xmlns="http://citrix.com/delivery-services/1-0/auth/requesttoken">
    <for-service>d5c937a6-a09d-4805-adbb-ff92208f7466</for-service>
    <for-service-url>
      https://storefront.enterprise.com/Citrix/Store/resources/v2/launch
    </for-service-url>
    <reqtokentemplate></reqtokentemplate>
    <requested-lifetime>01:00:00</requested-lifetime>
</requesttoken>
```

!!! info "Notes"
	1.The request is sent to the value specified by the locations part of the challenge. 
	
	2.The <for-service> element value is extracted from the realm value of the challenge.
	
	3.The <reqtokentemplate> element value is extracted from the reqtokentemplate value of the challenge. For current versions this is always empty.
	
	4.The <for-service-url> element value should be the URL that the client originally called. This should NOT be the value of the serviceroot-hint from the challenge.

##References

[1] HTTP Authentication: Basic and Digest Access Authentication: http://www.ietf.org/rfc/rfc2617.txt 

[2] StoreFront Security Token Services API v2.0

