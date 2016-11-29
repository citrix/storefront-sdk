# Requests
The following topics describe the requests available using the API. Each request is described, together with possible response codes and examples.

!!! tip "Note"
	In some examples, line breaks and white space have been added for readability.

## Client Configuration
Use this request to obtain the client configuration settings for the site. These settings define the behavior of the client and provide Web Proxy URLs for other services such as authentication and resource enumeration.This request can be performed before authentication has taken place and before a web session has been established.

### Request

| URL                 | Method | Description                                                             |
|---------------------|--------|-------------------------------------------------------------------------|
| /Home/Configuration | GET    | Requests the client configuration, which is returned as an XML document |

| Response Code | Description                                     |
|---------------|-------------------------------------------------|
| 200           | Success                                         |
| 403           | Forbidden, due to one of the following reasons: |
|               |- Invalid CSRF token                             |             
|               |- Invalid X-Citrix-IsUsingHTTPS header           |

### Success Response Content
If a successful response (HTTP status code 200 OK) is returned, the response body contains an XML document describing the Citrix Receiver for Web configuration settings for the client, with root node `clientSettings`. For more information about the various configuration elements and attributes, see Using configuration elements on page 81.### Example: Client Configuration 
####Request```curlPOST http://webserver/Citrix/StoreWeb/Home/Configuration HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: 4F4F307CAEAB89EEA86EF511788B1BB1X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Connection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0```
####Response

```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0Set-Cookie: CsrfToken=597E2BAC2A18AF3816B229D5022B6E2A; path=/Citrix/StoreWeb/X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 20 Sep 2013 15:03:40 GMT
Content-Length: 1592<clientSettings>  <session timeout="20" userLanguages="en-US,en;q=0.5" />  <authManager getUsernameURL="Authentication/GetUserName"               changeCredentialsURL="Authentication/GetChangeCredentialForm"               logoffURL="Authentication/Logoff"loginFormTimeout="5" />  <storeProxy keepAliveURL="Home/KeepAlive">    <resourcesProxy listURL="Resources/List"resourceDetails="default" />    <sessionsProxy listAvailableURL="Sessions/ListAvailable"                   disconnectURL="Sessions/Disconnect"                   logoffURL="Sessions/Logoff" />  </storeProxy>  <pluginAssistant enabled="true" upgradeAtLogin="true">    <win32 path="http://downloadplugins.citrix.com.edgesuite.net/Windows/CitrixReceiverWeb.exe" />    <macOS path=http://downloadplugins.citrix.com.edgesuite.net/Mac/CitrixReceiverWeb.dmg           minimumSupportedOSVersion="10.6" />    <html5 enabled="Off"           platforms="Firefox;Chrome;Version/([6-9]|\d\d).*Safari;MSIE \d\d;Trident;"           launchURL="clients/HTML5Client/src/SessionWindow.html"           preferences="" singleTabLaunch="false"chromeAppOrigins="chrome-extension://haiffjcadagjlijoggckpgfnoeiflnem|chrome-extension://bgiigkppjadidglloadcadeihlnbpagp" />  </pluginAssistant>  <userInterface frameOptions="deny" autoLaunchDesktop="true">    <workspaceControl enabled="true"autoReconnectAtLogon="true" logoffAction="disconnect"                      showReconnectButton="true"showDisconnectButton="true" />    <receiverConfiguration enabled="true"                           downloadURL="ServiceRecord/GetDocument/receiverconfig.cr" />    <uiViews showDesktopsView="true" showAppsView="true"defaultView="desktops" />    <appShortcuts enabled="false"allowSessionReconnect="false" />  </userInterface></clientSettings>
```
##Session Keep AliveUse this request to extend the duration of a session. The request can be performed before authentication takes place and before a web session is established. Simply contacting the server keeps the server-side session alive and resets the ASP.NET session idle timer. For example, if the session timeout is 20 minutes and this call is made after 15 minutes of idle time, the user is allowed a further 20 minutes before the session times out.
###Request
|URL|Method|Description|
|---|---|----||/Home/KeepAlive|HEAD|Returns an empty response with an HTTP 200 status code. This is used by the client to extend the life of the HTTP session, which by default times out if no requests are received within a period of 20 minutes.|
###Response
|Response Code|Description|
|---|----||200|Success||403|Forbidden, due to one of the following reasons:|| |* Invalid CSRF token|| |* Invalid X-Citrix-IsUsingHTTPS header|
###Success Response ContentIf a successful response (HTTP status code 200 OK) is returned, the response body is empty.###Example: Session Keep Alive 
####Request
```curl
HEAD http://webserver/Citrix/StoreWeb/Home/KeepAlive HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0Accept: text/plain, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: 4DE109CB32EBE310E1902D05D8DD5BDFX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/CsrfToken=4DE109CB32EBE310E1902D05D8DD5BDF;CtxsAuthId=B3C9A3C0D34C04EE7CC7C0C6B94A509D;ASP.NET_SessionId=jti1oxzixf5pvwisz5zw05wg; AGSSOHasOccurred=;
PasswordChangeAllowed=Connection: keep-alive
```
####Response
```curl
HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Length: 0Content-Type: text/htmlExpires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Mon, 23 Sep 2013 09:16:35 GMT
```
##Authentication MethodsUse the following URL to determine which authentication methods are available, prior to initiating authentication.###Request

|URL (indicative only)|Method|Description|
|---|----|---||/Authentication/ GetAuthMethods|POST|Returns a list of available authentication methods in XML format.|
!!! tip "Note"
	* The client must first make a POST request to /Resources/List. Since the user is not yet 	authenticated, this returns a challenge in the form of a CitrixWebReceiver- Authenticate 	header with the GetAuthMethods URL in the location field.
For example:
```curl
CitrixWebReceiver-Authenticate:reason="TokenRequired",location="Authentication/GetAuthMethods"`
```
!!! tip "Note"	* The client must not skip this request by hard-coding any of the authentication URLs, as 	these may change from release to release.	* The available authentication methods are specified in the Citrix Receiver for Web 	configuration file. The list of methods returned is the intersection of those configured 	for the Citrix Receiver for Web site and those configured for the StoreFront 	Authentication service.	* When Gateway authentication is available, use this in preference to (and to the 	exclusion of) all other authentication methods. This is because Gateway authentication is 	available only when the user is connecting to Citrix Receiver for Web externally through a 	NetScaler Gateway, while the other authentication methods are intended only for intranet 	use.
###Response
|Response Code|Description|
|----|----||200|Success||403|Forbidden, due to one of the following reasons:|| |* Invalid CSRF token|| |* Invalid X-Citrix-IsUsingHTTPS header|
|Response Format|Request Accept/Response Content-Type Header|
|---|----||XML|application/xml|###Success Response Content
When a successful response (HTTP status code 200) is returned, the response body contains an XML document with root node authMethods and zero or more method child elements. Each method child element contains a name attribute identifying the authentication method and a url attribute that the client uses to initiate authentication using the given method. The possible authentication method names are:
|Method name|Typical URL (indicative only)|Description|
|----|----|----||ExplicitForms|ExplicitAuth/Login|Explicit authentication with user-supplied credentials such as username, domain and password.||IntegratedWindows|DomainPassthroughAuth/ Login|Domain pass-through authentication||Certificate|SmartcardAuth/Login|Smart card (client certificate) authentication||CitrixAGBasic|GatewayAuth/Login|Automatic authentication ("single-sign-on") to NetScaler Gateway||PostCredentials|PostCredentialsAuth/Login|Authentication achieved by posting user credentials directly to the Web Proxy.| 

###Example: Get Auth Methods####Request
```curl
POST http://webserver/Citrix/StoreWeb/Authentication/GetAuthMethods HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateCsrf-Token: EE87320F00C8694137FBB9319DE3EE80X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=EE87320F00C8694137FBB9319DE3EE80;ASP.NET_SessionId=vo0ii2tbv2oaqcrko5zjjjlxConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response
```curl
HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Wed, 15 Jan 2014 13:17:19 GMTContent-Length: 282<?xml version="1.0" encoding="UTF-8"?><authMethods>    <method name="IntegratedWindows"url="DomainPassthroughAuth/Login"/>    <method name="Certificate" url="SmartcardAuth/Login"/>    <method name="ExplicitForms" url="ExplicitAuth/Login"/></authMethods>
```
##Domain Pass-Through and Smart Card AuthenticationUse these requests to authenticate a user either using pass through authentication or a smart card device.###Request|URL (indicative only)|Method|Description||----|----|----|
|/DomainPassthroughAuth/ Login|POST|Authenticates the user using the credentials with which he or she logged on to the computer.||/SmartcardAuth/Login|POST|Authenticates the user using a smart card connected to the user's client computer.|
!!! tip "Notes"
	* Domain pass-through authentication requires the client browser to be running on 	Microsoft Windows. The caller must check the client platform OS prior to initiating pass-	through authentication.	* The pass-through URL is configured in IIS to be protected by Integrated Windows 	Authentication (IWA). The actual authentication takes place between the browser and IIS, 	transparently to Citrix Receiver for Web.	* The smart card URL is configured in IIS to be accessible only via HTTPS and to require a 	client certificate to be supplied by the browser.	* Both pass-through and smart card authentication require that the option 'Trust requests 	to the XML Service' is enabled on the back-end XenDesktop/XenApp server.	* When pass-through authentication is used to authenticate to Citrix Receiver for Web, the 	user's password is not available to StoreFront. For launches to work without the user 	being prompted for credentials, configure Citrix Receiver as described in [http://	support.citrix.com/article/CTX133855](http://support.citrix.com/article/CTX133855).	* Smart card authentication requires two PIN prompts, one to authenticate to the web site 	and another to authenticate to the remote session.	* If authentication fails, check the StoreFront event logs which may reveal further 	information to assist with diagnosing the failure.

###Response

|Response Code|Description||----|----|
|200|Success or failure.||401|Unauthorized. Returned in the following situations:|| |* The user attempts pass-through authentication from a computer not joined to the StoreFront domain, and cancels the browser dialog prompting for domain credentials|
| |* The user attempts smart card authentication and cancels one of the browser prompts to insert a card, select a certificate, or enter a PIN.|
|403|Forbidden, due to one of the following reasons:|| |* Invalid CSRF token|| |* Invalid X-Citrix-IsUsingHTTPS header|

|Response Format|Request Accept/Response Content-Type Header|
|---|----||XML|application/xml|

###Success Response ContentWhen a successful response (HTTP status code 200) is returned, the response body contains an XML document with root node `AuthenticationStatus` and the following child elements:
|Element name|Required|Description||----|----|----|
|Result|Yes|Value "success" or "failure".||AuthType|No|The authentication type, one of the authentication method strings "ExplicitForms", "IntegratedWindows", "Certificate", "CitrixAGBasic", "PostCredentials". Only sent when authentication succeeds.||LogMessage|No|An error id indicating the reason for the authentication failure. Typically the generic value "fatalerror" is returned, but "sessiontimeout" is returned if the Citrix Receiver for Web session has timed out. Only sent when authentication fails.|
###Example: Successful smart card authentication 
####Request
```curlPOST https://webserver.domain.com/Citrix/StoreWeb/SmartcardAuth/Login HTTP/1.1Csrf-Token: C34A98583E032C5D26D4332A54738447Accept: application/xml, text/xml, */*; q=0.01X-Citrix-IsUsingHTTPS: YesX-Requested-With: XMLHttpRequestReferer: https://webserver.domain.com/Citrix/StoreWeb/Accept-Language: en-GBAccept-Encoding: gzip, deflateUser-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3;WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.3)Host: webserver.domain.comContent-Length: 0DNT: 1Connection: Keep-AliveCache-Control: no-cacheCookie: CsrfToken=C34A98583E032C5D26D4332A54738447;ASP.NET_SessionId=aisncy3nsdcz2snnpc045y1h```####Response
```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/xml; charset=utf-8Expires: -1Server: Microsoft-IIS/7.5Set-Cookie: CtxsAuthId=5989E6314A2ADEB10D4F4A71093CAF6D; path=/Citrix/StoreWeb/; secure; HttpOnlyX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 17 Jan 2014 17:39:44 GMTContent-Length: 255<?xml version="1.0" encoding="UTF-8"?><AuthenticationStatus">  <Result>success</Result>  <AuthType>Certificate</AuthType></AuthenticationStatus>```
###Example: Failed pass-through authenticationIn this example, the computer is off-domain, and the user cancels the browser prompt for domain credentials.####Request
```curl
POST http://webserver/Citrix/StoreWeb/DomainPassthroughAuth/Login HTTP/1.1Host: webserverUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/
20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateCsrf-Token: 74F22328CCE9A0C62097A5A77FC7D58BX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=74F22328CCE9A0C62097A5A77FC7D58B;ASP.NET_SessionId=flz4othwj5g5sc0fw3ywtzosConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response
```curl
HTTP/1.1 401 UnauthorizedContent-Type: text/html; charset=utf-8Server: Microsoft-IIS/7.5WWW-Authenticate: NegotiateWWW-Authenticate: NTLMX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 17 Jan 2014 17:44:14 GMTContent-Length: 1293Proxy-Support: Session-Based-Authentication<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html;charset=iso-8859-1"/><title>401 - Unauthorized: Access is denied due to invalidcredentials.</title><style type="text/css"><!--body{margin:0;font-size:.7em;font-family:Verdana, Arial,Helvetica, sans-serif;background:#EEEEEE;}fieldset{padding:0 15px 10px 15px;}h1{font-size:2.4em;margin:0;color:#FFF;}h2{font-size:1.7em;margin:0;color:#CC0000;}h3{font-size:1.2em;margin:10px 0 0 0;color:#000000;}#header{width:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:"trebuchet MS", Verdana, sans-serif;color:#FFF;background-color:#555555;}#content{margin:0 0 0 2%;position:relative;}.content-container{background:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;}--></style></head><body><div id="header"><h1>Server Error</h1></div><div id="content"> <div class="content-container"><fieldset>
 <h2>401 - Unauthorized: Access is denied due to invalidcredentials.</h2>  <h3>You do not have permission to view this directory orpage using the credentials that you supplied.</h3> </fieldset></div></div></body></html>
```
##Explicit Forms Authentication
Use this request to authenticate a user using explicit forms authentication. Explicit authentication, where the user enters credentials manually, is performed using the Citrix Common Forms Protocol. See the Citrix StoreFront API documentation for more information about Common Forms authentication.
The client initiates a forms conversation by making a request to the Web Proxy Explicit Forms URL (returned by /Authentication/GetAuthMethods) to get the first form in a possible series of forms. The Web Proxy forwards form requests to the StoreFront Authentication service and relays replies back to the client. All forms are unmodified by the Web Proxy, with the sole exception that any post-back URLs are modified to point to Web Proxy URLs, so that the client never contacts the Authentication service directly.
The forms are always returned as XML, which must be parsed by the client, transformed into corresponding HTML and displayed to the user. Once the user completes and submits a form, the client posts the form data back to a post-back URL provided in the original form XML. This may result in further forms being sent to the client to solicit additional information from the user. The client continues the process of rendering and submitting forms until either an authentication success or failure response is received.
The client must not assume that the initial form returned represents a logon form. Typically, this is the case, but another form may be returned in certain circumstances; for example, a change password form is returned if password expiry is configured and the user's password has expired. Third parties may also use the StoreFront Authentication SDK to inject custom forms into the authentication process.###Request

|URL (indicative only)|Method|Accepts POST data|Description|
|-----|-----|----|----||/ExplicitAuth/Login|POST|No|Requests the first form in an explicit forms conversation. The URL is returned by / Authentication/ GetAuthMethods.||/ExplicitAuth/ LoginAttempt|POST|Yes|Attempts an explicit logon. The URL is returned as the PostBack element in a login form.||/ExplicitAuth/ SendForm|POST|Yes|Proxies a form back to the StoreFront Authentication service. The URL is returned as the PostBack element in a form.||/ExplicitAuth/ GetChangeCredentialForm|POST|No|Requests a change credential form. Used when elective change password support is enabled in the StoreFront Authentication service. The URL is supplied in the RfWeb configuration.||/ExplicitAuth/ CancelForm|POST|No|Cancels the current form. The URL is returned as the CancelPostBack element in a form.| When the user submits a form (for example, by activating a Logon button), the client must process the user-supplied data as described in the section Processing Form Data of the document "Citrix Receiver Common Authentication Forms Language v2.0" in the Citrix StoreFront API documentation.
!!! tip "Notes"
	* If the client omits to post any of the required data, the Authentication service rejects 	the form, resulting in a failed logon.	* Once the user submits a form that results in successful authentication, the StoreFront 	Authentication service returns a primary authentication token for the user. All tokens, 	including the primary token plus any secondary tokens that are subsequently acquired for 	other StoreFront services (for example, Resources service), are held at the Web Proxy on 	behalf of the user, so that the client does not need to deal with the complexities of the 	authentication system.	* Tokens are maintained in the Web Proxy in an ASP.NET session object, which is bound to 	the user's browser session via the ASP.NET_SessionId cookie.###Response

|Response Code|Description|
|---|----||200|Success or failure or an XML form||403|Forbidden, due to one of the following reasons:|| |* Invalid CSRF token|| |* Invalid X-Citrix-IsUsingHTTPS header|
|Response Format|Request Accept/Response Content-Type Header||---|----|
|XML|application/xml|###Success Response Content
When a successful response (HTTP status code 200) is returned, the response body contains an XML document where the root node is either AuthenticationStatus or AuthenticateResponse.An AuthenticationStatus response indicates either success or failure and contains the following child elements:
|Element name|Required|Description|
|-----|----|-----||Result|Yes|Value "success" or "failure".||AuthType|No|The authentication type, indicated by one of the authentication method strings "ExplicitForms", "IntegratedWindows", "Certificate", "CitrixAGBasic", "PostCredentials". Only sent when authentication succeeds.||LogMessage|No|An error id indicating the reason for the authentication failure. Typically, the generic value "fatalerror" is returned, but "sessiontimeout" is returned if the Citrix Receiver for Web session has timed out. Only sent when authentication fails.||IsChangePasswordEnabled|No|Value "true". Only sent when authentication succeeds and elective change password is enabled.||IsExpiryNotificationEnabled|No|Value "true". Only sent when authentication succeeds, password expiry notification is enabled, and the user's password is due to expire within the configured time.|
|TimeRemaining|No|The time remaining (in minutes) until the user's password expires. Only sent when authentication succeeds, password expiry notification is enabled and the user's password is due to expire within the configured time.|

`AuthenticateResponse` is an XML description of a form that is displayed to the user to collect additional information required for the authentication operation (typically, logon on change password). See the Common Forms Authentication documentation for information about the various form elements.

###Example: Explicit Authentication—Logon Form Returned 
####Request```curlPOST http://webserver/Citrix/StoreWeb/ExplicitAuth/Login HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateCsrf-Token: 23E18D9002817048C931EA636E0D5C81X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/
Cookie: CtxsAuthMethod=ExplicitForms;CsrfToken=23E18D9002817048C931EA636E0D5C81;ASP.NET_SessionId=hdqnxu21dz3p2nb2zcfo2sfsConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response
```curl
HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/vnd.citrix.authenticateresponse-1+xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5X-Citrix-ExplicitAuthProtocol: ExplicitFormsX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 17 Jan 2014 16:25:09 GMTContent-Length: 1555<?xml version="1.0" encoding="UTF-8"?><AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">  <Status>success</Status>  <Result>more-info</Result>  <StateContext />  <AuthenticationRequirements>    <PostBack>ExplicitAuth/LoginAttempt</PostBack>    <CancelPostBack>ExplicitAuth/CancelForm</CancelPostBack>    <CancelButtonText>Cancel</CancelButtonText>    <Requirements>      <Requirement>    <Credential>      <ID>username</ID>      <SaveID>ExplicitForms-Username</SaveID>      <Type>username</Type>    </Credential>    <Label>      <Text>User name:</Text>      <Type>plain</Type>    </Label>    <Input>      <AssistiveText>domain\user or user@domain.com</AssistiveText>      <Text>        <Secret>false</Secret>        <ReadOnly>false</ReadOnly>        <InitialValue>        </InitialValue>        <Constraint>.+</Constraint>      </Text>    </Input>      </Requirement>      <Requirement><Credential>      <ID>password</ID>      <SaveID>ExplicitForms-Password</SaveID>      <Type>password</Type>    </Credential>    <Label>      <Text>Password:</Text>      <Type>plain</Type>    </Label>    <Input>      <Text>        <Secret>true</Secret>        <ReadOnly>false</ReadOnly>        <InitialValue>        </InitialValue>        <Constraint>.+</Constraint>      </Text>    </Input>      </Requirement>      <Requirement>    <Credential>      <ID>saveCredentials</ID>      <Type>savecredentials</Type>    </Credential>    <Label>      <Text>Remember my password</Text>      <Type>plain</Type>    </Label>    <Input>      <CheckBox>        <InitialValue>false</InitialValue>      </CheckBox>    </Input>      </Requirement>      <Requirement>    <Credential>      <ID>loginBtn</ID>      <Type>none</Type>    </Credential>    <Label>      <Type>none</Type>    </Label>    <Input>      <Button>Log On</Button>    </Input>      </Requirement>    </Requirements>  </AuthenticationRequirements></AuthenticateResponse>
```
The client transforms the XML form description into an HTML representation, which is then dynamically added to the web page DOM. The above XML results in an HTML form consisting of a **User name** label and text input field, a **Password** label and password input field, and a **Log On** button.

The user types his or her credentials in the input fields and submits the form by clicking the **Log On** button.

The client intercepts the form submission and follows the Common Forms Authentication rules to build the form data to send back to the Web Proxy (to be forwarded to the Authentication service). The form is submitted to the PostBack URL; in this case Authentication/LoginAttempt. However, the user mistypes their password which results in the Authentication service returning another logon form XML document, this time highlighting the error with an additional Requirements node.
###Example: Explicit Authentication—Incorrect Credentials Submitted 
####Request```curl POST http://webserver/Citrix/StoreWeb/ExplicitAuth/LoginAttempt HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: E2FF5D342BA9193DF707062EA7A31C54X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 72Cookie: CtxsAuthMethod=ExplicitForms;CsrfToken=E2FF5D342BA9193DF707062EA7A31C54;ASP.NET_SessionId=1zfyotwrcjr3uzry3jbqcpvgConnection: keep-alivePragma: no-cacheCache-Control: no-cacheusername=acmecorp%5Cuser1&password=rubbish&loginBtn=Log+On&StateContext=
```
####Response
```curl
HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5Set-Cookie: CtxsAuthId=22BE25569A283D63B1C5668580119320; path=/Citrix/StoreWeb/; HttpOnlyX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 17 Jan 2014 16:42:49 GMTContent-Length: 157<?xml version="1.0" encoding="UTF-8"?><AuthenticationStatus>  <Result>success</Result>  <AuthType>ExplicitForms</AuthType></AuthenticationStatus>
```

###Example: Explicit Authentication—Password ExpiredIf StoreFront is configured to allow users to change an expired password and a user attempts to log on when their password has expired, a change password XML form is returned when the user submits their credentials. This form includes a label to inform the user that their password must be changed, and text input fields (plus corresponding labels) for the user to enter the old password and to enter and confirm a new password. Note that the post-back URL is also updated to point back to the Web Proxy URL Authentication/ChangePassword.####Request
```curlPOST http://webserver/Citrix/StoreWeb/ExplicitAuth/LoginAttempt HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: A75AC234CA8C565EEEBE96FF81E495BAX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 70Cookie: CtxsAuthMethod=ExplicitForms;CsrfToken=A75AC234CA8C565EEEBE96FF81E495BA;ASP.NET_SessionId=ulemrewlolkvhallkgcbwm3lConnection: keep-alivePragma: no-cacheCache-Control: no-cacheusername=acmecorp%5Cuser1&password=mypassword&loginBtn=Log+On&StateContext=
```
####Response
```curl
HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/vnd.citrix.authenticateresponse-1+xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5X-Citrix-ExplicitAuthProtocol: ExplicitFormsX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Mon, 20 Jan 2014 10:53:59 GMTContent-Length: 2111<?xml version="1.0" encoding="UTF-8"?><AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">  <Status>success</Status>  <Result>update-credentials</Result>  <StateContext />  <AuthenticationRequirements>    <PostBack>ExplicitAuth/SendForm</PostBack>    <CancelPostBack>ExplicitAuth/CancelForm</CancelPostBack>    <CancelButtonText>Cancel</CancelButtonText>    <Requirements>      <Requirement>    <Credential>      <Type>none</Type>    </Credential>    <Label>      <Text>Change Password</Text>      <Type>heading</Type>    </Label>    <Input />      </Requirement>      <Requirement>    <Credential>      <Type>none</Type>    </Credential>    <Label>      <Text>Your password has expired and must be changed.</Text>      <Type>information</Type>    </Label>    <Input />      </Requirement>      <Requirement>    <Credential>
  <Type>username</Type></Credential><Label>  <Text>User name:</Text>  <Type>plain</Type></Label><Input>  <Text>    <Secret>false</Secret>    <ReadOnly>true</ReadOnly>    <InitialValue>acmecorp\user1</InitialValue>    <Constraint>.+</Constraint>  </Text></Input>  </Requirement>  <Requirement><Credential>  <ID>oldPassword</ID>  <Type>password</Type></Credential><Label>  <Text>Old password:</Text>  <Type>plain</Type></Label><Input>  <Text>    <Secret>true</Secret>    <ReadOnly>false</ReadOnly>    <InitialValue>    </InitialValue>    <Constraint>.+</Constraint>  </Text></Input>  </Requirement>  <Requirement><Credential>  <ID>newPassword</ID>  <SaveID>ExplicitForms-Password</SaveID>  <Type>newpassword</Type></Credential><Label>  <Text>New password:</Text>  <Type>plain</Type></Label><Input>  <Text>    <Secret>true</Secret>    <ReadOnly>false</ReadOnly>    <InitialValue>    </InitialValue>    <Constraint>.+</Constraint>  </Text></Input>  </Requirement>  <Requirement><Credential>  <ID>confirmPassword</ID>
<Type>newpassword</Type>    </Credential>    <Label>      <Text>Confirm password:</Text>      <Type>plain</Type>    </Label>    <Input>      <Text>        <Secret>true</Secret>        <ReadOnly>false</ReadOnly>        <InitialValue>        </InitialValue>        <Constraint>.+</Constraint>      </Text>    </Input>      </Requirement>      <Requirement>    <Credential>      <ID>changePasswordBtn</ID>      <Type>none</Type>    </Credential>    <Label>      <Type>none</Type>    </Label>    <Input>      <Button>OK</Button>    </Input>      </Requirement>    </Requirements>  </AuthenticationRequirements></AuthenticateResponse>
```
When the user enters the requested information and submits the form, a further form is returned by the Authentication service for the user to confirm that their password has been successfully changed. Note that the request specifies the button id changePasswordBtn specified in the form above; failing to specify the correct button id results in the form being rejected. The confirmation form comprises simply of a text label and OK button.####Request
```curl
POST http://webserver/Citrix/StoreWeb/ExplicitAuth/SendFormHTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: 94FEF17799905C51ADD4599AC0056209X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 95Cookie: CtxsAuthMethod=ExplicitForms;
CsrfToken=94FEF17799905C51ADD4599AC0056209;ASP.NET_SessionId=01omrcuoenllin1eugyr142jConnection: keep-alivePragma: no-cacheCache-Control: no-cacheoldPassword=mypassword&newPassword=newpassword&confirmPassword=newpassword&changePasswordBtn=OK&StateContext=
```
####Response
```curl
HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/vnd.citrix.authenticateresponse-1+xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5X-Citrix-ExplicitAuthProtocol: ExplicitFormsX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Mon, 20 Jan 2014 11:13:18 GMTContent-Length: 720<?xml version="1.0" encoding="UTF-8"?><AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">  <Status>success</Status>  <Result>more-info</Result>  <StateContext />  <AuthenticationRequirements>    <PostBack>ExplicitAuth/SendForm</PostBack>    <CancelPostBack>    </CancelPostBack>    <Requirements>      <Requirement>    <Credential>      <Type>none</Type>    </Credential>    <Label>      <Text>Your password has been changed successfully.</Text>      <Type>confirmation</Type>    </Label>    <Input />      </Requirement>      <Requirement>    <Credential>      <ID>changePasswordConfirmBtn</ID>      <Type>none</Type>    </Credential>    <Label>      <Type>none</Type>    </Label>    <Input>      <Button>OK</Button>    </Input>      </Requirement>
	nticationRequirements></AuthenticateResponse>
```
After the user clicks the OK button, the confirmation form is submitted and a successful authentication response is obtained.####Request```curl POST http://webserver/Citrix/StoreWeb/ExplicitAuth/SendFormHTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: 94FEF17799905C51ADD4599AC0056209X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 41Cookie: CtxsAuthMethod=ExplicitForms;CsrfToken=94FEF17799905C51ADD4599AC0056209;ASP.NET_SessionId=01omrcuoenllin1eugyr142jConnection: keep-alivePragma: no-cacheCache-Control: no-cachechangePasswordConfirmBtn=OK&StateContext=
```
####Response
```curl
HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5Set-Cookie: CtxsAuthId=7BFB98069F1D33A0FB4268F702B0C983; path=/Citrix/StoreWeb/; HttpOnlyX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Mon, 20 Jan 2014 11:13:24 GMTContent-Length: 157<?xml version="1.0" encoding="UTF-8"?><AuthenticationStatus>  <Result>success</Result>  <AuthType>ExplicitForms</AuthType></AuthenticationStatus>
```

###Example: Explicit Authentication—Elective Change PasswordIf StoreFront is configured to allow users to change their password at any time and a user attempts to log on when their password is due to expire within the configured expiry period, a successful authentication response is returned. This response includes additional elements indicating that expiry notification is enabled and the number of days remaining until the password expires.####Request```curlPOST http://webserver/Citrix/StoreWeb/ExplicitAuth/LoginAttempt HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: 94FD74E2F4DF05D6B0642D25021F632AX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 70Cookie: CtxsAuthMethod=ExplicitForms;CsrfToken=94FD74E2F4DF05D6B0642D25021F632A;ASP.NET_SessionId=mgucndg5j24cgvymxgrjblr4Connection: keep-alivePragma: no-cacheCache-Control: no-cacheusername=acmecorp%5Cuser1&password=mypassword&loginBtn=Log+On&StateContext=
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5Set-Cookie: CtxsAuthId=F431D32D995E3CF6A59F5728A0F54085; path=/Citrix/StoreWeb/; HttpOnlyX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Mon, 20 Jan 2014 11:25:46 GMTContent-Length: 320<?xml version="1.0" encoding="UTF-8"?><AuthenticationStatus>  <Result>success</Result>  <AuthType>ExplicitForms</AuthType>  <IsChangePasswordEnabled>true</IsChangePasswordEnabled>  <IsExpiryNotificationEnabled>true</IsExpiryNotificationEnabled>
  TimeRemaining>89</TimeRemaining></AuthenticationStatus>```
The client may then provide an interface for the user to initiate an elective change password request at any time using the changeCredentials URL obtained from the Citrix Receiver for Web configuration at XPath /clientSettings/authManager. Requesting this URL initiates a Common Forms protocol conversation, in a similar way to /ExplicitAuth/ Login. If the user submits the form after entering invalid data (or omitting required data), further forms may be generated. The client must be prepared to receive multiple forms in succession and process these until either a success or failure response is received. If the password change is successful, a password confirmation form is returned; when the confirmation form is submitted a successful AuthenticationStatus response is returned. In other words, the change password conversation proceeds exactly as described in the example for the case where the user's password has expired at logon time.####Request
```curl
POST http://webserver/Citrix/StoreWeb/Authentication/GetChangeCredentialForm HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateCsrf-Token: A4BF7CB3334846575421F41AD44EBA67X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CtxsAuthMethod=ExplicitForms;CsrfToken=A4BF7CB3334846575421F41AD44EBA67;CtxsAuthId=910C6BFC2C98184CA57F77556041E0D3;ASP.NET_SessionId=cxd25yc3xwq10qevwpxywyxuConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/vnd.citrix.authenticateresponse-1+xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5X-Citrix-ExplicitAuthProtocol: ExplicitFormsX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Mon, 20 Jan 2014 11:48:00 GMTContent-Length: 2097<?xml version="1.0" encoding="UTF-8"?>
<AuthenticateResponse xmlns="http://citrix.com/authentication/response/1">  <Status>success</Status>  <Result>update-credentials</Result>  <StateContext />  <AuthenticationRequirements>    <PostBack>ExplicitAuth/SendForm</PostBack>    <CancelPostBack>ExplicitAuth/CancelForm</CancelPostBack>    <CancelButtonText>Cancel</CancelButtonText>    <Requirements>      <Requirement>    <Credential>      <Type>none</Type>    </Credential>    <Label>      <Text>Change Password</Text>      <Type>heading</Type>    </Label>    <Input />      </Requirement>      <Requirement>    <Credential>      <Type>none</Type>    </Credential>    <Label>      <Text>Enter your old and new passwords</Text>      <Type>information</Type>    </Label>    <Input />      </Requirement>      <Requirement>    <Credential>      <Type>username</Type>    </Credential>    <Label>      <Text>User name:</Text>      <Type>plain</Type>    </Label>    <Input>      <Text>        <Secret>false</Secret>        <ReadOnly>true</ReadOnly>        <InitialValue>acmecorp\user1</InitialValue>        <Constraint>.+</Constraint>      </Text>    </Input>      </Requirement>      <Requirement>    <Credential>      <ID>oldPassword</ID>      <Type>password</Type>    </Credential>    <Label>      <Text>Old password:</Text>      <Type>plain</Type>    </Label><Input>
<Text>    <Secret>true</Secret>    <ReadOnly>false</ReadOnly>    <InitialValue>    </InitialValue>    <Constraint>.+</Constraint>  </Text></Input>  </Requirement>  <Requirement><Credential>  <ID>newPassword</ID>  <SaveID>ExplicitForms-Password</SaveID>  <Type>newpassword</Type></Credential><Label>  <Text>New password:</Text>  <Type>plain</Type></Label><Input>  <Text>    <Secret>true</Secret>    <ReadOnly>false</ReadOnly>    <InitialValue>    </InitialValue>    <Constraint>.+</Constraint>  </Text></Input>  </Requirement>  <Requirement><Credential>  <ID>confirmPassword</ID>  <Type>newpassword</Type></Credential><Label>  <Text>Confirm password:</Text>  <Type>plain</Type></Label><Input>  <Text>    <Secret>true</Secret>    <ReadOnly>false</ReadOnly>    <InitialValue>    </InitialValue>    <Constraint>.+</Constraint>  </Text></Input>  </Requirement>  <Requirement><Credential>  <ID>changePasswordBtn</ID>  <Type>none</Type></Credential><Label>  <Type>none</Type></Label><Input> <Button>OK</Button>    </Input>      </Requirement>    </Requirements>  </AuthenticationRequirements></AuthenticateResponse>
```
With elective change password the user has already authenticated to Citrix Receiver for Web. Since the change password request is not essential to access the site, the client UI should provide a Cancel button on the form. If the user chooses to cancel, the Web Proxy cancel post-back URL in the above form must be used to relay to the Authentication service that the request has been cancelled.####Request
```curl
POST http://webserver/Citrix/StoreWeb/ExplicitAuth/CancelFormHTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: 3E5784A870D03FF16BF7A37415F9E0ABX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 73Cookie: CtxsAuthMethod=ExplicitForms;CsrfToken=3E5784A870D03FF16BF7A37415F9E0AB;CtxsAuthId=C389FA6A3BD8E1E3811C184C01918411;ASP.NET_SessionId=chgeeknlk5aiewkyyqfwp43pConnection: keep-alivePragma: no-cacheCache-Control: no-cacheoldPassword=&newPassword=&confirmPassword=&cancelBtn=Cancel&StateContext=
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/vnd.citrix.authenticateresponse-1+xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Mon, 20 Jan 2014 12:02:33 GMTContent-Length: 201<?xml version="1.0" encoding="UTF-8"?><AuthenticateResponse xmlns="http://citrix.com/authentication/
response/1">  <Status>success</Status>  <Result>cancelled</Result>  <StateContext /></AuthenticateResponse>
```
##Post Credentials AuthenticationWith post credentials authentication, the client supplies the user's credentials directly using HTTP POST. This provides a simpler authentication mechanism than Explicit Forms because the client does not need to parse XML forms and handle the forms conversation. However, this method is less flexible than Explicit Forms authentication and does not support change password functionality, which uses the Common Forms protocol.###Request| URL (indicative only)       | Method | Description                                                                                                                      |
|-----------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------|
| /PostCredentialsAuth/ Login | POST   | Authenticates the user using the credentials supplied in the POST body. The URL is returned by / Authentication/ GetAuthMethods. |

| POST parameter | Description                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| username       | The username, including a domain specification if required, in either SAM or UPN format. For example, domain\fred or fred@some.domain |
| password       | The password.                                                                                                                         |

!!! tip "Note"
	* The Http Basic authentication method must be enabled for the Authentication service 	because the Web Proxy internally uses HttpBasic to authenticate the user to StoreFront.	* A non-empty username string value must be supplied, but the password may be supplied 	with an empty value.
| Response Code | Description                                     |
|---------------|-------------------------------------------------|
| 200           | Success or failure                              |
| 400           | The username or password was not supplied.      |
| 403           | Forbidden, due to one of the following reasons: |
|               | * Invalid CSRF token                            |
|               | * Invalid X-Citrix-IsUsingHTTPS header          |

| Response Format | Request Accept/Response Content-Type Header |
|-----------------|---------------------------------------------|
| XML             | application/xml                             |

###Success Response ContentWhen a successful response (HTTP status code 200) is returned, the response body contains an XML document with root node AuthenticationStatus and the following child elements:

| Element name | Required | Description |
|--------------|----------|------------ |
| Result       | Yes      |Value "success" or "failure".|
| AuthType	   | No | The authentication type, as indicated by one of the authentication method strings: "ExplicitForms", "IntegratedWindows", "Certificate", "CitrixAGBasic", "PostCredentials". Only sent when authentication succeeds.|
| LogMessage | No | An error id indicating the reason for the authentication failure. Typically the generic value "fatalerror" is returned, but "sessiontimeout" is returned if the Citrix Receiver for Web session has timed out. When the credentials are rejected by the Authentication service, "loginfailed" is returned. Only sent when authentication fails. |

###Example: Successful Post Credentials Authentication 
####Request
```curl
POST http://webserver/Citrix/StoreWeb/PostCredentialsAuth/Login HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: 04416E5028580B5783E1A051732214B4X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/ApiExample.htmlContent-Length: 42Cookie: CsrfToken=04416E5028580B5783E1A051732214B4;ASP.NET_SessionId=m5utlgwykupmhhbq11c2gt0sConnection: keep-alivePragma: no-cacheCache-Control: no-cacheusername=acmecorp%5Cuser1&password=mypassword
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5Set-Cookie: CtxsAuthId=488731E2C57EF91E84729A3ECB3E5CAF; path=/Citrix/StoreWeb/; HttpOnlyX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Tue, 28 Jan 2014 13:44:18 GMTContent-Length: 159<?xml version="1.0" encoding="UTF-8"?><AuthenticationStatus>  <Result>success</Result>  <AuthType>PostCredentials</AuthType></AuthenticationStatus>	```
##NetScaler Gateway Single Sign-OnUse this request to automatically authenticate a user who has authenticated to NetScaler Gateway.###Request
| URL                | Method | Description                                                    |
|--------------------|--------|----------------------------------------------------------------|
| /GatewayAuth/Login | POST   | Authenticates the user using NetScaler Gateway single sign-on. |

!!! tip "Notes"
 	* When Citrix Receiver for Web is accessed through NetScaler Gateway, changing an expired 	password during logon is dealt with by the Gateway.	* Since Citrix Receiver for Web is not involved in the explicit forms authentication, it 	does not provide password expiry notification when a user's password expires soon.	* When elective change password is enabled and a user successfully changes their password, 	the client must log the user off because there is no way to sync up with NetScaler 	Gateway. The user then has to log onto the Gateway again.	* When authentication fails, the StoreFront event logs may reveal further information to 	assist with diagnosing the failure.
###Response
| Response Code | Description                                     |
|---------------|-------------------------------------------------|
| 200           | Success or failure                              |
| 403           | Forbidden, due to one of the following reasons: |
|               | * Invalid CSRF token                            |
|               | * Invalid X-Citrix-IsUsingHTTPS header          |

| Response Format | Request Accept/Response Content-Type Header |
|-----------------|---------------------------------------------|
| XML             | application/xml                             |

###Success Response ContentWhen a successful response (HTTP status code 200) is returned, the response body contains an XML document with root node AuthenticationStatus with the same child elements as described for Explicit Authentication.###Example: Successful NetScaler Gateway Authentication 
####Request
```curl
POST https://gateway.acme.com/Citrix/StoreWeb/GatewayAuth/Login HTTP/1.1Host: gateway.acme.comUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0
Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-us,en;q=0.7,fr;q=0.3Accept-Encoding: gzip, deflateCsrf-Token: AD11BBE759D84186CE8753ABA4246FDDX-Citrix-IsUsingHTTPS: YesX-Requested-With: XMLHttpRequestReferer: https://gateway.acme.com/Citrix/StoreWebCookie: CsrfToken=AD11BBE759D84186CE8753ABA4246FDD;NSC_AAAC=84dc5a2985fe2cdddcb18697f37d49ec0094e9e2145525d5f4f58455e445a4a42; ASP.NET_SessionId=rozslfqggjk32jbjggkwptpjConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response
```curl
ResponseHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/xml; charset=utf-8Expires: -1Server: Microsoft-IIS/8.5Set-Cookie: CtxsAuthId=9ADB4CFDA7CE38BEA0C64A64C5914145; path=/Citrix/StoreWeb/; secure; HttpOnlyX-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Mon, 20 Jan 2014 15:27:41 GMTContent-Length: 216<?xml version="1.0" encoding="UTF-8"?><AuthenticationStatus>  <Result>success</Result>  <AuthType>CitrixAGBasic</AuthType>  <IsChangePasswordEnabled>true</IsChangePasswordEnabled></AuthenticationStatus>
```
##Get User NameUse this request to obtain the full user name, as configured in Active Directory. If the full user name is unavailable, the user's logon name is returned instead.###Request
| URL                          | Method | Description                                                                                                                |
|------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------|
| /Authentication/ GetUserName | POST   | Returns the user name. Obtain the URL from the Citrix Receiver for Web configuration using the getUsernameURL attribute at XPath /clientSettings/ authManager|

!!! tip "Notes"
	* This request requires an authenticated session, indicated by the cookies 	ASP.NET_SessionId and CtxsAuthId. When using an unauthenticated Store, no user has 	actually logged on and an HTTP 403 response is returned.	* The Web Proxy uses the StoreFront Token Validation service to obtain the user name from 	the authentication token.###Response
| Response Code | Description                                                                           |
|---------------|---------------------------------------------------------------------------------------|
| 200           | Success or authentication challenge                                                   |
| 403           | Forbidden, due to one of the following reasons:                                       |
|               | * Invalid CSRF token                                                                  |
|               | * Invalid X-Citrix-IsUsingHTTPS header w Invalid CtxsAuthId cookie                    |
|               | * Missing authentication token in server session, when the user has not yet logged on |

###Success Response ContentIf a successful response (HTTP status code 200 OK) is returned, the response body contains the user name as a string in plain text format, encoded as UTF-8.###Example: Get User Name 
####Request
```curlPOST http://webserver/Citrix/StoreWeb/Authentication/GetUserName HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: text/plain, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: 128B2AA41FE56F42CA4550FEE88198CBX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=128B2AA41FE56F42CA4550FEE88198CB;CtxsAuthId=82221BEE46C4C14CAFD2405F9A3C600F;ASP.NET_SessionId=5cfuoz0dc0p3y0o2nidhglkhConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0```
####Response
```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: text; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 18 Oct 2013 13:43:17 GMTContent-Length: 9Joe Blogs
```
##Log OffUse this request to log off a user's web session.###Request
| URL                    | Method | Description                                                                                                                        |
|------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------|
| /Authentication/Logoff | POST   | Terminates the user's web session. Obtain the URL from the Citrix Receiver for Web configuration using the logoffURL attribute at: XPath /clientSettings/ authManager.                                                                                                |

!!! tip "Notes"
	* This request requires an authenticated session, indicated by the cookies 	ASP.NET_SessionId and CtxsAuthId.	* The StoreFront Authentication service is called to destroy the user's primary token.	* The Web session is terminated and the following cookies are cleared: ASP.NET_SessionId, 	CtxsAuthId, CsrfToken.
###Response
| Response Code | Description                                                        |
|---------------|--------------------------------------------------------------------|
| 200           | Success                                                            |
| 403           | Forbidden, due to one of the following reasons:                    |
|               | * Invalid CSRF token                                               |
|               | * Invalid X-Citrix-IsUsingHTTPS header w Invalid CtxsAuthId cookie |

###Success Response ContentIf a successful response (HTTP status code 200 OK) is returned, the response body is empty.###Example: Log Off 

####Request
```curl
POST http://webserver/Citrix/StoreWeb/Authentication/LogoffHTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: application/xml, text/xml, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: 128B2AA41FE56F42CA4550FEE88198CBX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=128B2AA41FE56F42CA4550FEE88198CB;CtxsAuthId=82221BEE46C4C14CAFD2405F9A3C600F;ASP.NET_SessionId=5cfuoz0dc0p3y0o2nidhglkh; AGSSOHasOccurred=;PasswordChangeAllowed=Connection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/vnd.citrix.webreceiver.authenticationlogoffresponse+xmlExpires: -1Server: Microsoft-IIS/8.0Set-Cookie: CsrfToken=128B2AA41FE56F42CA4550FEE88198CB;expires=Tue, 18-Oct-1983 13:43:23 GMT; path=/Citrix/StoreWeb/Set-Cookie: CtxsAuthId=82221BEE46C4C14CAFD2405F9A3C600F;expires=Tue, 18-Oct-1983 13:43:23 GMT; path=/Citrix/StoreWeb/Set-Cookie: ASP.NET_SessionId=; path=/X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 18 Oct 2013 13:43:22 GMTContent-Length: 0
```
##Resource EnumerationUse this request to get a list of all the resources available for a user. 
###Request
| URL (indicative only) | Method | Description                                                           |
|-----------------------|--------|-----------------------------------------------------------------------|
| /Resources/List       | POST   | Returns a list of all resources available for the user in JSON format |

| POST parameters | Description                                                        |
|---------------|--------------------------------------------------------------------|
| resourcesDetails           | The resource details to include in the response. Use one of the following supported values: ||  | * Default—a default set of resource details (see below). ||  | * Full—an extended set of resource details (see below). ||  | If you do not specify the parameter, "Default" is assumed.                                                           |
!!! tip "Notes"
	* Typically, this request requires an authenticated session, indicated by the cookies 	ASP.NET_SessionId and CtxsAuthId. However, when the Web Proxy is configured to use an 	unauthenticated Store, an authenticated session is not required.	* The Web Proxy always performs a fresh enumeration for the user by communicating with the 	StoreFront Store service to pick up any changes that may have occurred.
###Response
| Response Code | Description                                                          |
|---------------|----------------------------------------------------------------------|
| 200           | Success or authentication challenge                                  |
| 403           | Forbidden, due to one of the following reasons: w Invalid CSRF token |
|               | * Invalid X-Citrix-IsUsingHTTPS header w Invalid CtxsAuthId cookie   |
|               | * Invalid CtxsAuthId cookie                                          |

| Response Format | Request Accept/Response Content-Type Header |
|-----------------|---------------------------------------------|
| JSON             | application/json                            |

###Success Response ContentWhen a successful response (HTTP status code 200) is returned, the response body contains a JSON object describing the resources that are available for the authenticated user. This object contains the following fields:
| Field                   | JavaScript Type | Description                                                                                                                                                           |
|-------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resources               | Object Array    | Details of each published resource available to the user. Each object in the array corresponds to a single resource and contains a set of fields, as described below. |
| isSubscriptionEna bled  | Boolean         | Whether subscription operations are enabled for the Store or not.                                                                                                     |
| isUnauthenticated Store | Boolean         | Whether or not the Store is accessible only without first authenticating.                                                                                             |

The resources field in the table above is an array of resource objects. Each resource object always contains the following set of fields:

| Field | JavaScript Type | Description                          |
|-------|-----------------|--------------------------------------|
| clienttypes| String Array | An array of string values identifying the clients supported for launches. Known values include **ica30**, **rade**, **rdp** (XenApp/XenDesktop), **application/ios**, **application/android** (AppController), **g2m**, **g2t** etc. (Citrix Online Integration using Generic applications). |
|iconurl | String | The URL to request the resource's icon image data. |
| id | String | Unique resource identifier, created by the Web Proxy. |
| launchstatusurl | String | The URL to determine whether a resource is ready to launch or not (see ICA Launch). |
| launchurl | String | The URL to make a launch request (see ICA Launch). |
| name | String | The user-friendly name of the resource. |
| path | String | The path defined in the XenApp/XenDesktop site (farm) for the resource. |
| shortcutvalidation url | String | The app shortcut validation URL, to confirm that an app may be launched using a shortcut. | 
| subscriptionstatus | String | The subscription status (see Resource Subscription).|

In addition, each resource object may contain the following optional fields:

| Field | JavaScript Type | Description |
|-------|-----------------|-------------|
|assigndesktopurl| String |Call this URL to assign a desktop to the user. Supplied only for XenDesktop assign-on-first-use desktops.|
|content | Boolean | Supplied with value *true* if the resource represents a document as opposed to a published application/desktop, otherwise omitted.|
| description | String | A longer text description of the resource.|
| desktopassignmenttype| String | The desktop assignment type: one of the values *shared*, *assign-on-first-use* or *assigned*. Supplied only for XenDesktop resources.|
|desktophostname| String| The desktop host name, if known. Supplied only for XenDesktop assigned desktops.|
| disabled | Boolean | Supplied with value *true* if the resource is not enabled, otherwise omitted.|
| isdesktop| Boolean | Supplied with value *true* if the resource is a desktop, otherwise omitted.|
| keywords| String Array | An array of string values identifying keywords associated with the resource.|
| mandatory| Boolean | Supplied with value true if the resource is tagged by the back-end resource provider as mandatory, otherwise omitted.|
|position|String|A string representing the relative position of a subscribed resource in the Citrix Receiver for Web UI. Only generated for resources for which a position has already been defined.|
|poweroffurl|String|The URL to make a machine power-off request. Only supplied if the resource can be powered- off, as reported by the StoreFront Resources service.|
|prelaunchurl |String|The URL to call to contact the AppController pre-launch service to obtain an updated content URL for single sign-on.|
|recommended|Boolean|Supplied with value true if the resource is tagged by the back-end resource provider as **featured** or **recommended**, otherwise omitted.|
|requiresvpn|Boolean| Supplied with value true if the resource is marked (using the Resources Service VPN keyword,) as launchable remotely (with NetScaler Gatway) only when using a VPN, otherwise omitted.|
|requiresworkflow|Boolean| Supplied with value true if workflow is enabled for the resource (typically due to the presence of the **WFS** keyword).|
|subscriptionurl|String|The URL to make a subscription request (see Resource Subscription).|

When the `resourceDetails` request parameter specifies that a "Full" enumeration should be performed, the following additional, and optional fields may be returned:

| Field | JavaScript Type | Description |
|-------|-----------------|-------------|
| images | Object Array | An array of objects identifying the image sizes and color depths of the resource icon held by the StoreFront Services server (may be used to determine which image sizes are likely to give good results when requested by the client). Each object in the array contains a pair of integer fields named **size** and **depth**.|
| playsfiletypes | Object Array | An array of objects describing the file extensions supported by the resource [Application only]. Each object in the array may contain the following fields:|
| | | *name* (String): file type association name |
| | | *description* (String): file type association description |
| | | *isdefault* (Boolean): whether this is the default file type association or not |
| | | *fileextensions* (String Array): array of file extensions that can be opened by this resource |
| | | *mimetypes* (String Array): array of mime types supported by the resource |
| | | *parameters* (String Array): array of parameters used for launching the resource |
| properties | Object Array | Resource properties—an array of name value pairs associated with the resource and ultimately supplied by the resource provider. Each object in the array contains a string field name describing the property *name* and a string array field *values* describing a list of property values.|
| publishername | String| The name of the publisher (the farm name for XenApp).|
| shortcuturl | String | The app shortcut URL, to use when embedding a link to the resource in a portal page.|
| subscriptionproperties | Object Array | Subscription properties — an array of name value pairs associated with the resource subscription and stored in the subscription database. Each object in the array contains a string field name for the property *name* and an optional string array field *values* for the list of property values. For more information, see Resource Subscription. |
| type | String |The resource type, typically one of the following values:|
| | | * Citrix.MPS.Application| 
| | | * Citrix.MPS.Desktop|
| | | * Citrix.MPS.Document|

!!! tip "Notes"
	* The iconurl value encodes a particular icon size, as configured in the Web.config site 	configuration file (resourcesService section, within serverSettings). The StoreFront Store 	service returns the icon that best matches the requested size.	* The iconurl represents image data at the point that the enumeration was performed. If 	the icon for a resource subsequently changes, the URL will not point to the updated image. 	However, the URL is persistent because it always points to the same icon, although it may 	return 404 after the icon has been updated on the XenApp/XenDesktop server.	* The subscriptionUrl is used for both subscribing to and unsubscribing from a resource, 	with the operation selected by a POST parameter.###Example: Request all resources 
####Request
```curl
POST http://webserver/Citrix/StoreWeb/Resources/List HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: EC8A9490C8D32616B21C3EED398FE9EEX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 32Cookie: CsrfToken=EC8A9490C8D32616B21C3EED398FE9EE;CtxsAuthId=BB8B836131AA35C54DF588E631838946;ASP.NET_SessionId=jel5evcolmhl4bcm1i31exqo; AGSSOHasOccurred=;PasswordChangeAllowed=Connection: keep-alivePragma: no-cacheCache-Control: no-cacheformat=json&resourceDetails=Default
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cache
Content-Type: application/json; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Tue, 24 Sep 2013 11:03:37 GMTContent-Length: xxxxx{"resources":[  {"clienttypes":["ica30","rdp"],   "description":"",   "iconurl":"Resources\/Icon\/NUM2RDNDRDU1QzdBMUE0RjU0NjA4NjRBNTkwMzY0NzQyMEM2OTQ3QQ--\/48",   "id":"Q29udHJvbGxlci4hJCVeJl8rLQ--",   "launchurl":"Resources\/LaunchIca\/Q29udHJvbGxlci4hJCVeJl8rLQ--",   "name":"Microsoft Word",   "path":"\\Office Apps\\",   "shortcutvalidationurl":"Resources\/ValidateAppShortcutLaunch\/Q29udHJvbGxlci4hJCVeJl8rLQ--",   "subscriptionstatus":null,   "subscriptionurl":"Resources\/Subscription\/Q29udHJvbGxlci4hJCVeJl8rLQ--"  },  {"clienttypes":["ica30","rdp"],   "description":"",   "disabled":true,   "iconurl":"Resources\/Icon\/NUM2RDNDRDU1QzdBMUE0RjU0NjA4NjRBNTkwMzY0NzQyMEM2OTQ3QQ--\/48",   "id":"Q29udHJvbGxlci4hJF4kJV4-",   "launchurl":"Resources\/LaunchIca\/Q29udHJvbGxlci4hJF4kJV4-",   "name":"!$^$%^",   "path":"\\Yabba\\",   "shortcutvalidationurl":"Resources\/ValidateAppShortcutLaunch\/Q29udHJvbGxlci4hJF4kJV4-",   "subscriptionstatus":null,   "subscriptionurl":"Resources\/Subscription\/Q29udHJvbGxlci4hJF4kJV4-"   },... ], "subscriptionsEnabled":true,}
```
###Example: Request all resources (full enumeration) 
####Request
```curl
POST http://webserver/Citrix/StoreWeb/Resources/List HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8
Csrf-Token: 1062D9DA90BA01931DB472C09D61A6EBX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 56Cookie: CsrfToken=1062D9DA90BA01931DB472C09D61A6EB;CtxsAuthId=FEB9E833C66E9D7B4124E04AEC12C3B5;ASP.NET_SessionId=2zsqy14dgxdctivbs351fmvoConnection: keep-alivePragma: no-cacheCache-Control: no-cacheformat=json&resourceDetails=Default&resourceDetails=Full
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/json; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Tue, 24 Sep 2013 11:03:37 GMTContent-Length: xxxxx{"categories":[], "resources":[  {    "type": "Citrix.MPS.Application",    "subscriptionurl": "Resources\/Subscription\/X83heiDGddg1ldasf87asdfg--",    "shortcutvalidationurl": "Resources\/ValidateAppShortcutLaunch\/X83heiDGddg1ldasf87asdfg--",    "shortcuturl": "http:\/\/kontiki\/Citrix\/StoreWeb\/#\/launch\/Notepad",    "publishername": "foobar-ic6659",    "path": "\\",    "name": "Notepad",    "launchurl": "Resources\/LaunchIca\/X83heiDGddg1ldasf87asdfg--",    "launchstatusurl": "Resources\/GetLaunchStatus\/X83heiDGddg1ldasf87asdfg--",    "images": [{"size": 48,"depth": 4 },{"size": 32,"depth": 4 },{"size": 48,"depth": 8 },
{"size": 32,"depth": 8 },       {         "size": 256,         "depth": 32       },{"size": 48,         "depth": 32       },{"size": 32,         "depth": 32       },     ],    "id": "X83heiDGddg1ldasf87asdfg--",    "iconurl": "Resources\/Icon\/NUM2RDNDRDU1QzdBMUE0RjU0NjA4NjRBNTkwMzY0NzQyMEM2OTQ3QQ--?size=48",    "description": "Take note!",    "clienttypes": ["ica30","rdp" ]},... ], "subscriptionsEnabled":true,}
```
##ICA LaunchUse this request to check if a resource is ready to launch, or to get an ICA file for launching a resource.###Request
| URL (indicative only) | Method | Description |
|-----------------------|--------|-------------||/Resources/ GetLaunchStatus/{id} | POST | Request whether the specified resource is ready to launch or not.|| /Resources/LaunchIca/{id} | GET | Request an ICA file for launching the specified resource.
| Parameter | Description |
|-----------|-------------||{id}|Unique identifier for a particular resource. Note, this parameter is a component of the URL.|
|displayNameDesktopTitle | The desktop display name. This is inserted in the generated ICA file as the value for the Title setting. This name is then displayed in the title bar of the Desktop Viewer. Note: this is a POST parameter for GetLaunchStatus and a query string parameter for LaunchIca.|

!!! tip "Notes"
	* Typically, these requests require an authenticated session, indicated by the cookies 	ASP.NET_SessionId and CtxsAuthId. However, when the Web Proxy is configured to use an 	unauthenticated Store, an authenticated session is not required.	* The URLs given above are for illustrative purposes; the actual URLs used by a client 	must be taken from the result of an earlier enumeration request to /Resources/List.	* LaunchIca is a GET instead of a POST so that it can be loaded by a browser in a hidden 	iframe (using the iframe's src="url" attribute) to trigger a launch via file-type 	association.	* GetLaunchStatus makes a launch request to the Store Service to determine whether the 	specified resource is ready to launch or not. If this returns an ICA file, the ICA file is 	cached for up to 90 seconds. If a subsequent call is made to LaunchIca within this time, 	the cached ICA file is returned without making an additional launch request to the Store 	Service.	* For LaunchIca, clients must append a query string key with a random value to prevent 	browsers from returning a cached response when making multiple launch requests for the 	same resource. See the launchId query string parameter in the examples below.	* Calling GetResourceStatus can trigger a desktop VM to start up.
###Response
|Response Code | Description |
|--------------|-------------|| 200|Success/Retry required/failure, or authentication challenge.||403 | Forbidden, due to one of the following reasons: || | * Invalid CSRF token || | * Invalid X-Citrix-IsUsingHTTPS header (only required for the POST request) || | * Invalid CtxsAuthId cookie ||404 | Resource identified by {id} was not known to the Web Proxy. |
| Response Format | Request Accept/Response Content-Type Header ||------|-------|| JSON | application/json or text/plain (see below) || ICA File | application/octet-stream |
###Success Response Content
When a successful response (HTTP status code 200) for GetLaunchStatus is returned, the response body contains a JSON string describing whether the supplied resource is ready to be launched or not, with the following fields:
| Attribute | JavaScript Type | Required | Description |
|---|----|----|----|| status | String | Yes | One of the following strings: || | | | * success: the resource is ready to be launched.|| | | | * retry: currently, the resource is not ready to be launched (for example, a desktop VM that first needs to be powered on before a connection can be made to it), but the launch attempt may be retried later.|| | | | * failure: the attempt to retrieve launch information failed.||pollTimeout|Number | No | || errorId | String | No | || suggestRestart | Boolean | No | |
When a successful response for LaunchIca is returned, the response body can be either a JSON string, as described above, for GetLaunchStatus or, if the resource is ready to launch, an ICA file. Clients typically load the LaunchIca URL into an iframe to obtain an ICA file and trigger a launch via file type association. If LaunchIca returns a JSON response instead of an ICA file, the content type is set to "text/plain" because Internet Explorer does not render an "application/json" response into the iframe document and instead prompts the user to Open or Save it. If the client is using jQuery, the JSON text response can be deserialized to a JavaScript object by calling $.parseJSON(responseData).###Example: Successful ICA launch
####Request```curl GET http://webserver/Citrix/StoreWeb/Resources/LaunchIca/Q29udHJvbGxlci5EZXNrdG9w.ica?CsrfToken=85E9295DFD9CF333F31F0A53B769D915&launchId=1380030775058&displayNameDesktopTitle=Desktop HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=85E9295DFD9CF333F31F0A53B769D915;CtxsAuthId=5A0B7A991C8136CE17A0D43113C00740;ASP.NET_SessionId=jel5evcolmhl4bcm1i31exqoConnection: keep-alive
```
####Response
```curlHTTP/1.1 200 OKCache-Control: private, max-age=0, s-maxage=0Content-Type: application/octet-stream; charset=utf-8Expires: Tue, 24 Sep 2013 13:52:55 GMTLast-Modified: Tue, 24 Sep 2013 13:52:55 GMTServer: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Tue, 24 Sep 2013 13:52:55 GMTContent-Length: 1263[Encoding]InputEncoding=UTF8[WFClient]ProxyFavorIEConnectionSetting=YesProxyTimeout=30000ProxyType=AutoProxyUseFQDN=OffRemoveICAFile=yesTransportReconnectEnabled=On<... etc. >
```
###Example: Failed ICA launch 
####Request
```curlPOST http://webserver/Citrix/StoreWeb/Resources/GetLaunchStatus/Q29udHJvbGxlci5Db3B5IG9mIFdvcmRQYWQz HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflateCsrf-Token: 2730933D4A9C7EFCDA52BD89EC345DD5X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=2730933D4A9C7EFCDA52BD89EC345DD5;CtxsAuthId=669C20DF67B0ABC5C0E1F35451EF02A5;ASP.NET_SessionId=jel5evcolmhl4bcm1i31exqo; AGSSOHasOccurred=;PasswordChangeAllowed=Connection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response
```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/json; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Tue, 24 Sep 2013 15:49:50 GMTContent-Length: 77{"status":"failure"}
```###Example: ICA launch with retry 
####Request
```curl
POST http://webserver/Citrix/StoreWeb/Resources/GetLaunchStatus/Q29udHJvbGxlci5GaXNoY2FrZSE- HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: 0035B0DB846D2399576612132C95AF33X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=0035B0DB846D2399576612132C95AF33;CtxsAuthId=421E99814A2B99CFA57BB146EE036710;ASP.NET_SessionId=vmia5swazanokecxwjefwvubConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0displayNameDesktopTitle=Desktop+Two!
```
####Response```curl HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/jsonExpires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Tue, 15 Oct 2013 16:22:51 GMTContent-Length: 34{"status":"retry","pollTimeout":5}
```
##IconsUse this request to retrieve icon image data relating to one or more resources. This uses the concept of a 'thumbprint' to allow sharing of image data for resources with equivalent images. The 'thumbprint' is designed to be the same for images with the same content.
###Request
| URL (indicative only)| Method | Description |
|---|----|-----||/Resources/Icon/ {thumbprint}?size={size}| GET | Returns the specified icon image. For more information about the format and details of the response, see below.|
| Parameter | Description |
|------|-----||{thumbprint}|The thumbprint for the icon image. This value is included in the iconurl returned from an earlier enumeration request.|
|{size}|The pixel size of the icon image to return. Only the values 16, 24, 32, 48, 64, 96, 128, 256 and 512 are supported. This value is included in the iconurl returned from an earlier enumeration request, based on the image size configured in the Citrix Receiver for Web site configuration file (defaults to 48).|

!!! tip "Notes"
	* This request requires an authenticated session, indicated by the cookies 	ASP.NET_SessionId and CtxsAuthId.	* A CSRF token is not required, nor is the X-Citrix-IsUsingHTTPS header, allowing the icon 	URL to be directly fetched by a browser (HTTP GET) when specified as the src for an HTML 	img element.
	* The URLs above are for illustrative purposes only; the actual URLs used by a client must 	be taken from the result of an earlier enumeration request, which provides a separate icon 	URL for each resource.	* The thumbprint represents the image data for the resource at the time of enumeration and 	so may be different in a subsequent enumeration if the image data has changed.	* The response image is always returned in PNG format, with the Content-Type set to image/	png.	* The Web Proxy uses the StoreFront Resources API to obtain icon images. The image data is 	cached to disk as a performance optimization by default, unless persistent caching is 	disabled in the Citrix Receiver for Web configuration file.	* Caching headers are set in the response to indicate that the icon image may be cached by 	the client for one year.
###Response |Response Code | Description |
|-----------------------|-----||200 (OK)|Success||304 (Not Modified)|The request is a 'conditional GET', indicated by the presence of an If-Modified-Since header. If the image has been changed at the back-end, this is only discovered at the next enumeration.||400 (Bad Request)|The specified size does not match one of the supported icon sizes.||403 (Forbidden)|Forbidden, due to an invalid `CtxsAuthId` cookie.||404 (Not Found)|Returned for the following cases:|| |* Unknown/missing thumbprint|| |* The requested size does not match the size configured for the Citrix Receiver for Web site|

|Response Format | Request Accept /Response Content-Type Header|
|---------|--------------|| PNG |image/png|
###Example: Successful request for a 48x48 image 
####Request```curl
GET http://webserver/Citrix/StoreWeb/Resources/Icon/RjczNDEyMzc3ODlENzE5REZDRUQ4MDczQ0QxMDBGRjI4MDY5MDg2RQ--/48HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/
20100101 Firefox/23.0Accept: image/png,image/*;q=0.8,*/*;q=0.5Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=A902FEE631743C79C5B125FE4BC4DB56;CtxsAuthId=5E4A8BF161FBBBC90F64241E40A7D849;ASP.NET_SessionId=tzqrwypgtof5fnna1fh1jmmeConnection: keep-alive
```
####Response```curlHTTP/1.1 200 OKCache-Control: private, max-age=31536000, s-maxage=0Content-Type: image/pngExpires: Thu, 25 Sep 2014 12:28:46 GMTLast-Modified: Wed, 25 Sep 2013 12:28:46 GMTServer: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Wed, 25 Sep 2013 12:28:46 GMTContent-Length: 3184... 48 x 48 png image data ...
```
##Machine Power OffUse this request to trigger a power off operation for the specified resource. Only certain resources support this action, and typically only for a limited set of users. If the power off operation does not occur within the time-limit defined on the XenDesktop server, an error response may be returned even if the power off is successful.###Request
|URL (indicative only)|Method|Description|
|--------|-------|------||/Resources/PowerOff/{id}|POST|Attempts to power off the specified resource.|
|Parameter |Description|
|------|-----||{id}|Unique identifier for a particular resource.|
!!! tip "Notes"	* This request requires an authenticated session, indicated by the cookies 	ASP.NET_SessionId and CtxsAuthId.	* The URL above is for illustrative purposes only; the actual URL used in a request must 	be taken from the result of an earlier enumeration request to /Resources/List.
###Response

|Response Code | Description |
|----|-----||200|PowerOff request sent to machine leading to success/ failure of power off operation, or authentication challenge.||403|Forbidden, due to one of the following reasons:|
| |* Invalid CSRF token|| |* Invalid X-Citrix-IsUsingHTTPS header| 
| |* Invalid CtxsAuthId cookie||404|Resource identified by {id} was not found or the power- off action did not exist or was not enabled for that resource for the current user.|
|Response Format|Request Accept/Response Content-Type Header|
|---|---||JSON|application/json|
The response returns a simple JSON object containing the following fields:|Field |JavaScript Type |Description||---|---|---||status|String|"success" if the power off operation was reported to have completed successfully, otherwise "failure".||errorId|String|A string providing a reason for a power off failure (see below).|
If the power off operation fails, the error reason is indicated by one of the following error id strings:|Error Id|Description|
|---|----||in-maintenance-mode|The requested operation could not be performed because the machine is in maintenance mode.||no-machine|No assigned machines were found for the user in the specified machine group.||not-supported|The requested operation is not supported on the requested machine group type.|
|operation-in-progress|The server is busy with a control operation on the specified machine and cannot handle another request at this time.||timed-out|The server timed out waiting for the request to complete. Note: the power off operation may have succeeded, but not within the timeout period defined on the XenDesktop server.||not-trusted|The client is not trusted to perform the requested operation. This does not indicate whether the supplied credentials are valid or not.||unspecified|Error condition not covered by the other values.|
###Example: Successful Power Off 
####Request```curlPOST http://webserver/Citrix/StoreWeb/Resources/PowerOff/Q29udHJvbGxlci5NaWtlQiBEZXNrdG9wIEdyb3VwICRTMS0x HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: 5798C908E45771AD767E66F1D176E2D1X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=5798C908E45771AD767E66F1D176E2D1;CtxsAuthId=01FBA1051F0D45129D308C6E2F2C303D;ASP.NET_SessionId=j3xcfc2fdvmjuynowgqlpad4Connection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/jsonExpires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Thu, 17 Oct 2013 09:12:53 GMTContent-Length: 43
{"status":"success"}
```
##Resource SubscriptionUse these requests to perform resource subscription and unsubscription, and to update the relative position (as shown in the UI) of subscribed resources. Subscribed resources are displayed on the Receiver for Web "Home" screen, visible when the user logs on. These represent a list of "favorites" for quick access. Receiver for Web requires that application resources are subscribed before they can be launched, although no such restriction exists in the protocol. Desktop resources are treated as a special case and are always displayed by Receiver for Web (on a separate UI tab), regardless of subscription state.###Request|URL (indicative)|Method|Description|
|---|----|----||/Resources/Subscription/ {id}|POST|Action depends upon the operation attribute value specified in the POST parameters:|
| | | * **subscribe**—attempt to subscribe to the resource. This may create a new subscription (if one does not already exist) and, by default, sets the subscription to the subscribed state.|| | |* **unsubscribe**—attempt to unsubscribe from the resource. This may delete the subscription and, by default, set the subscription to the notSubscribed state.|| | |* **update**—updates the subscription properties for the resource.|
|POST parameter|Description|
|----|----|
|Id|Unique identifier for a particular resource. Note: this parameter is a component of the URL.|
|operation|The subscription operation to perform: either **subscribe**, **unsubscribe**, or **update**.||updateMode|Whether any supplied subscription properties are to be merged with existing properties, or if the batch of supplied properties will completely replace any existing properties; either **merge** or **replace**.||*subscription properties*|Other key=value pairs supplied as request parameters are taken to represent subscription properties.|
!!! tip "Notes"
	* This request requires an authenticated session, indicated by the cookies `ASP . NET _ 	SessionId` and `CtxsAuthId`.	* The URL above is for illustrative purposes only; the actual URLs used in a request must 	be taken from the result of an earlier enumeration request to /Resources/List.	* When the Web Proxy is configured to use an unauthenticated Store, subscription 	operations are unavailable and these URLs are omitted from the resource enumeration 	response. They are also omitted for resources that are configured at XenApp or XenDesktop 	to be mandatory resources, which are always displayed to all users.	* Subscription information is persisted in the Store Service's subscription store and is 	returned during enumeration, allowing subscriptions to remain intact across a Citrix 	Receiver for Web session and be visible to other Receivers.
|Response Code (and friendly name)|Description|
|----|-----||200 (OK)|Resource subscribed or unsubscribed successfully, or authentication challenge.||400 (Bad Request)|An unsupported value was supplied for operation or updateMode.||403 (Forbidden)|Forbidden, due to one of the following reasons:|
| | * Invalid CSRF token|| | * Invalid X-Citrix-IsUsingHTTPS header|| | * Invalid CtxsAuthId cookie||404 (Not Found)|Resource identified by {id} was not found.|
|503 (Service Unavailable)|Subscription operations are unavailable for the specified resource, due to one of the following reasons:|| | * No subscription URL was returned for the requested resource when the previous enumeration request was made, indicating that the StoreFront subscription service was unavailable when that enumeration was performed|| | * The Store Service subscription database is currently unavailable|
###Success Response Content
When a successful response (HTTP status code 200) is returned, the response body contains a JSON object containing one of the following fields:
|Field|JavaScript Type|Description|
|---|---|-----||status|String|The new subscription status for the resource, as indicated by one of the following values: "subscribed", "unsubscribed", "pending", "approved", "denied", "pendingunsubscribe", "subscribedpendingunsubsc ribe", "failure". The first two values are returned for successful operations, when subscriptions are not associated with workflow. The "failure" value indicates the subscription request was not successfully proxied to the Store service. The other values relate to workflow scenarios.|
|Response Format|Request Accept /Response Content- Type Header|
|---|-----||JSON|application/json|
###Example: Successful subscription 
####Request
```curl
POST http://webserver/Citrix/StoreWeb/Resources/Subscription/Q29udHJvbGxlci5Xb3JkUGFk HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: 35D3DAC189174D65DC6D843C9FDAB46AX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 42Cookie: CsrfToken=35D3DAC189174D65DC6D843C9FDAB46A;CtxsAuthId=535CF2577B2FF0DF53F76D3C2D994B92;ASP.NET_SessionId=0eu5dnpqapdgeu2j1n3sz4zhConnection: keep-alivePragma: no-cacheCache-Control: no-cacheoperation=subscribe&position=B
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/json; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Wed, 25 Sep 2013 15:58:41 GMTContent-Length: 23{"status":"subscribed"}
```
###Example: Unsuccessful unsubscription 
####Request```curl
POST http://webserver/Citrix/StoreWeb/Resources/Subscription/Q29udHJvbGxlci5Xb3JkUGFk HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/
20100101 Firefox/23.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: 35D3DAC189174D65DC6D843C9FDAB46AX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 33Cookie: CsrfToken=35D3DAC189174D65DC6D843C9FDAB46A;CtxsAuthId=535CF2577B2FF0DF53F76D3C2D994B92;ASP.NET_SessionId=0eu5dnpqapdgeu2j1n3sz4zhConnection: keep-alivePragma: no-cacheCache-Control: no-cacheoperation=unsubscribe
```
####Response```curl
HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/json; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Wed, 25 Sep 2013 16:00:23 GMTContent-Length: 20{"status":"failure"}
```
###Example: Successful update of subscription propertiesThis is an example of a successful update of the data associated with a subscription. The property ids and values are arbitrary from the perspective of the Resources service. Note that the 'bar' property key is repeated to specify a multi-valued property.####Request
```curl
POST http://webserver/Citrix/StoreWeb/Resources/Subscription/Q29udHJvbGxlci5GaXNoY2FrZSE- HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: 48C7A008D81F87116B4BDE418FB63B3CX-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 24
Cookie: CsrfToken=48C7A008D81F87116B4BDE418FB63B3C;CtxsAuthId=1AA0681CE60D7E625A504BA0B1E70824;ASP.NET_SessionId=stoi5utb5zfam1xtfqkjklfdConnection: keep-alivePragma: no-cacheCache-Control: no-cacheoperation=update&updateMode=replace&foo=fooValue&bar=barValue&bar=barValue2
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/jsonExpires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Tue, 15 Oct 2013 17:12:49 GMTContent-Length: 23{"status":"subscribed"}
```
##Session EnumerationUse this request to enumerate the authenticated user's ICA sessions that are not connected to by the current client, regardless of whether the sessions are disconnected or active on another client. Once enumerated, these sessions can be reconnected using the session launch API.###Request|URL (indicative)|Method|Description|
|----|-----|-----||/Sessions/ListAvailable|POST|Returns a list of all available sessions for the user in JSON format.|
|POST parameter|Description|
|---|----||resourceTypes|The types of resource to include in the response, one of the following values: Citrix.MPS.Application - to request application sessions. Citrix.MPS.Desktop - to request desktop sessions.|
!!! tip "Notes"
	* This request requires an authenticated session, indicated by the cookies 	ASP.NET_SessionId and CtxsAuthId. When the Web Proxy is configured to use an 	unauthenticated Store, an empty session list is returned.	* Sessions initiated by the current client, as indicated by the DeviceId, are not included 	in the returned list of sessions.	* The downstream request to enumerate sessions from the StoreFront Store Service always 	adds the parameter to include active sessions.	* When used with previous versions of XenApp and XenDesktop, this request also disconnects 	any active sessions. This issue was fixed in XenDesktop 7.	* The expected usage pattern is for clients to enumerate all available sessions (possibly 	for a particular type of resource) and then launch each one in succession. This is how the 	Citrix Receiver for Web "auto reconnect at logon" functionality is implemented.
###Response|Response Code (and friendly name)|Description|
|------|------||200 (OK)|List of available sessions (possibly empty), or authentication challenge.||403 (Forbidden)|Forbidden, due to one of the following reasons:|| | * Invalid CSRF token|| | * Invalid X-Citrix-IsUsingHTTPS header w Invalid CtxsAuthId cookie|###Success Response ContentWhen a successful response (HTTP status code 200) is returned, the response body contains a JSON array of objects, each containing the following fields:|Field|JavaScript Type|Description|
|----|------|------||launchurl|String|The URL to make a launch request (see ICA Launch on page 57)||launchstatusurl|String|The URL to determine whether a resource is ready to launch (see ICA Launch on page 57)||initialApp|String|The name of a previously launched app that that caused the session to initially be created.||publishername|String|The name of the publisher (the farm name for XA).|
|Response Format|Request Accept/Response Content-Type Header|
|----|-----||JSON|application/json|
###Example: Session EnumerationIn this example, all sessions are requested by not qualifying the server and client types. 
####Request
```curlPOST http://webserver/Citrix/StoreWeb/Sessions/ListAvailableHTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8Csrf-Token: BC8E733316E514C1C1E31541D9E44AF9X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Content-Length: 36Cookie: CtxsDeviceId=WR_AjT2owY5yJ4ED0J-x;CsrfToken=BC8E733316E514C1C1E31541D9E44AF9;CtxsAuthId=35037C55868C4C1AEE3A24488062C3BD;ASP.NET_SessionId=ltutfqnaollcehgvre25mwipConnection: keep-alivePragma: no-cacheCache-Control: no-cacheresourceTypes=Citrix.MPS.Application
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/jsonExpires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 18 Oct 2013 09:25:45 GMTContent-Length: 191[
 {  "initialapp":"Notepad",  "launchstatusurl":"Sessions\/GetLaunchStatus\/Q29udHJvbGxlci4xODM5MC4y",  "launchurl":"Sessions\/LaunchIca\/Q29udHJvbGxlci4xODM5MC4y",  "publishername":"johnc-ic6659" }]
```
##Session LaunchUse this request to attempt to reconnect to an existing session (either disconnected or active on another client), as specified by session id.###Request|URL (indicative)|Method|Description|
|---|----|----||/Sessions/Launch/{id}|GET|Request whether the specified session is ready to launch or not.||/Sessions/ GetLaunchStatus/{id}|POST|Request an ICA file for launching the specified session.|
|URL Parameter|Description|
|----|-----||{id}|Unique identifier for a particular session.|
!!! tip "Notes"
	* These requests require an authenticated session, indicated by the cookies `ASP . NET _ 	SessionId` and `CtxsAuthId`.	* The URLs above are for illustrative purposes only; the actual URLs used by a client must 	be taken from the result of an earlier session enumeration request to / Sessions/	ListAvailable. When the Web Proxy is configured to use an unauthenticated Store, session 	enumeration returns an empty list and session launch is therefore unavailable.	* Launch is a GET instead of a POST so that it can be loaded by a browser in a hidden 	iframe (using the iframe's src="url" attribute) to trigger a launch via file-type 	association.	* GetLaunchStatus makes a launch request to the Store Service to determine whether the 	specified resource is ready to launch or not. If this returns an ICA file, the ICA file is 	cached for up to 90 seconds. If a subsequent call is made to LaunchIca within this time, 	the cached ICA file is returned without making an additional launch request to the Store 	Service.	* For LaunchIca, clients must append a query string key with a random value to prevent 	browsers from returning a cached response when making multiple launch requests for the 	same resource. See the launchId query string parameter in the examples below.
###Response
 |Response Code|Description|
|----|----||200|Success/Retry required/failure, or authentication challenge.||403|Forbidden, due to one of the following reasons: a) Invalid CSRF token b) Invalid `X-Citrix-IsUsingHTTPS` header c) Invalid `CtxsAuthId` cookie||404|Resource identified by {id} was not found.|
|Response Format|Request Accept/Response Content-Type Header|
|----|-----||JSON|application/json|
|ICA File|application/octet-stream|

###Success Response ContentWhen a successful response (HTTP status code 200) for GetLaunchStatus is returned, the response body contains a JSON object describing whether the supplied resource is ready to be launched, with the following possible fields:
|Attribute|Required|Description|
|----|----|----||status|Yes|One of the following strings:|| | |* success—the resource is ready to be launched|| | |* retry—the resource is not currently ready to be launched (for example, a desktop VM that first needs to be powered on before a connection can be made to it), but the launch attempt may be retried later.|| | |* failure—the attempt to retrieve launch information failed|
|pollTimeout|No|Only supplied when status is **retry**, the number of seconds to wait before retrying the launch request.||errorId|No|Only supplied when status is **failure** , an error code as described in the Launch section of the StoreFront Store Services API specification.||suggestRestart|No|Only supplied when status is **failure** , a **true** or **false** value indicating whether the Store service included a "remedy hint" that a failed desktop launch could potentially be resolved by restarting the desktop.|

When a successful response for LaunchIca is returned, the response body can be either a JSON string as described above for `GetLaunchStatus` or, if the resource is ready to launch, an ICA file.###Example: Session Get Launch Status Success 
####Request```curl
POST http://webserver/Citrix/StoreWeb/Sessions/GetLaunchStatus/Q29udHJvbGxlci4xODM5MC4y HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: BC8E733316E514C1C1E31541D9E44AF9X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=BC8E733316E514C1C1E31541D9E44AF9;CtxsAuthId=35037C55868C4C1AEE3A24488062C3BD;ASP.NET_SessionId=ltutfqnaollcehgvre25mwip
Connection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response```curl HTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/jsonExpires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 18 Oct 2013 09:25:45 GMTContent-Length: 20{"status":"success"}```
###Example: Session Launch Success 
####Request```curlGET http://webserver/Citrix/StoreWeb/Sessions/Launch/Q29udHJvbGxlci4xODM5MC41.ica?CsrfToken=0068C0184E13600DE24B6C1469952BEB&launchId=1380199200494 HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=0068C0184E13600DE24B6C1469952BEB;CtxsAuthId=6E4966414BE6CE4E46D791655730672B;ASP.NET_SessionId=kxh5cmlkkjbm5njp22feodrtConnection: keep-alive
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/x-ica; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Thu, 26 Sep 2013 12:40:00 GMTContent-Length: 1279[Encoding]InputEncoding=UTF8
[WFClient]ProxyFavorIEConnectionSetting=YesProxyTimeout=30000ProxyType=Auto<etc...>
```
##Session Disconnect and LogoffUse these requests to disconnect or logoff a user's currently connected sessions at the server.###Request
|URL (indicative)|Method|Description|
|----|-----|-----||/Sessions/Disconnect|POST|Disconnects the user's sessions.||/Sessions/Logoff|POST|Logs off the user's sessions.|
!!! tip "Notes"
	* These requests require an authenticated session, indicated by the cookies `ASP .NET_ 	SessionId` and `CtxsAuthId`.	* When the Web Proxy is configured to use an unauthenticated Store, there is no associated 	user for whom sessions can be disconnected, and session disconnect has no effect.	* These requests operate only on sessions that were initiated from the current client, as 	indicated by the DeviceId cookie.
###Response|URL (indicative)|Method|Description|
|----|----|----||/Sessions/Disconnect|POST|Disconnects the user's sessions.||/Sessions/Logoff|POST|Logs off the user's sessions.||Response Code|Description||----|----|
|200|Success/failure, or authentication challenge.||403|Forbidden, due to one of the following reasons:|| | * Invalid CSRF token|| | * Invalid X-Citrix-IsUsingHTTPS header|
| | * Invalid CtxsAuthId cookie|

|Response Format|Request Accept/Response Content-Type Header|
|---|----||JSON|application/json|
###Success Response ContentWhen a successful response (HTTP status code 200) for Disconnect or Logoff is returned, the response body contains a JSON object with a single JavaScript String field "status" with one of the values: "success", "failure", "partial" indicating whether the user's sessions were successfully disconnected or not. The value "partial" means that some of the user's sessions were successfully disconnected while others were not.###Example: Session Disconnect 
####Request
```curl
POST http://webserver/Citrix/StoreWeb/Sessions/Disconnect HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: D6E47EE6160CA2121C3797D0E850FFA0X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=D6E47EE6160CA2121C3797D0E850FFA0;CtxsAuthId=BC5CC0F3EC36E6577B3810A12063280C;ASP.NET_SessionId=jzvwqr2uh1ksws4c3bd2x4gpConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response
```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/json; charset=utf-8Expires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Thu, 26 Sep 2013 14:23:56 GMTContent-Length: 20{"status":"success"}
```
###Example: Session Logoff

####Request
```curl
POST http://webserver/Citrix/StoreWeb/Sessions/Logoff HTTP/1.1Host: kontikiUser-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflateCsrf-Token: EA871815F7B33602B391EA5F85757FE8X-Citrix-IsUsingHTTPS: NoX-Requested-With: XMLHttpRequestReferer: http://webserver/Citrix/StoreWeb/Cookie: CsrfToken=EA871815F7B33602B391EA5F85757FE8;CtxsAuthId=C1796CE16F1841181ABFD7DC5DC3E7E2;ASP.NET_SessionId=zegkvwsdy0hqglxkgtgdcxdaConnection: keep-alivePragma: no-cacheCache-Control: no-cacheContent-Length: 0
```
####Response```curlHTTP/1.1 200 OKCache-Control: no-cache, no-storePragma: no-cacheContent-Type: application/jsonExpires: -1Server: Microsoft-IIS/8.0X-Powered-By: ASP.NETX-Citrix-Application: Receiver for WebDate: Fri, 18 Oct 2013 11:12:19 GMTContent-Length: 20{"status":"success"}
```
