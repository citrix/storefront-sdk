# Using configuration elements
This topic describes the elements and attributes of the XML document that is returned following a successful request to /Home/Configuration. These settings specify the behavior of the client and provide Web Proxy URLs for subsequent operations.!!! tip "Note"
	Default values appear in bold. 

##SessionXPath: /clientSettings/session
| Attribute     | Values                                                        | Description                                                                                            |
|---------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| timeout       | Time in minutes (**20**)                                          | The number of minutes of idle time before the web session times out and the user must re-authenticate. |
| userLanguages | **The value of the Accept-Language header sent by the browser** | The list of languages supported by the client (typically browser).                                     |

##Authentication ManagerXPath: /clientSettings/authManager
| Attribute            | Values                                 | Description                                                   |
|----------------------|----------------------------------------|---------------------------------------------------------------|
| getUsernameURL       | **Authentication/ GetUserName**            | URL to obtain the full user name.                             |
| changeCredentialsURL | **ExplicitAuth/ GetChangeCredentialFor m** | URL to initiate a change password operation.                  |
| logoffURL            | **Authentication/Logoff**                  | URL to log off the Citrix Receiver for Web session.           |
| loginFormTimeout     | Time in minutes (**5**)                    | How long Citrix Receiver for Web displays the logon form for. |
##Store ProxyXPath: /clientSettings/storeProxy
| Attribute    | Values (default in bold) | Description                    |
|--------------|--------------------------|--------------------------------|
| keepAliveURL | **Home/KeepAlive**| URL to keep the session alive. |

##Resources ProxyXPath: /clientSettings/storeProxy/resourcesProxy
| Attribute       | Values (default in bold) | Description                                                      |
|-----------------|--------------------------|------------------------------------------------------------------|
| listURL         | **Resources/List**           | URL to enumerate the user's available resources.                 |
| resourceDetails | **default** | full           | Whether to return default or extended resource enumeration data. |

##Sessions ProxyXPath: /clientSettings/storeProxy/sessionsProxy
| Attribute        | Values (default in bold) | Description                                     |
|------------------|--------------------------|-------------------------------------------------|
| listAvailableURL | **Sessions/ListAvailable**   | URL to enumerate the user's available sessions. |
| disconnectURL    | **Sessions/Disconnect**      | URL to disconnect the user's sessions.          |
| logoffURL        | **Sessions/Logoff**          | URL to log off the user's sessions.             |

##Plugin AssistantXPath: /clientSettings/pluginAssistant
| Attribute      | Values       | Description                                                                                                         |
|----------------|--------------|---------------------------------------------------------------------------------------------------------------------|
| enabled        | **true** | false | Whether to show Receiver download information or not when HDX engine is not detected and when upgrade is available. |
| upgradeAtLogin | true | **false** | Whether to detect if a Receiver upgrade is available or not.                                                        |

XPath: /configuration/citrix.deliveryservices/webReceiver/clientSettings/ pluginAssistant/win32

| Attribute | Values                   | Description                                               |
|-----------|--------------------------|-----------------------------------------------------------|
| path      | Relative or absolute url | The location for downloading Citrix Receiver for Windows. |

XPath: /configuration/citrix.deliveryservices/webReceiver/clientSettings/ pluginAssistant/macOS

| Attribute                  | Values                   | Description                                                       |
|----------------------------|--------------------------|-------------------------------------------------------------------|
| path                       | Relative or absolute url | The location for downloading Citrix Receiver for MacOS.           |
| minimumSupportedOSVersi on | Version number (**10.6**)    | The minimum MacOS version required for Citrix Receiver for MacOS. |

XPath: /configuration/citrix.deliveryservices/webReceiver/clientSettings/ pluginAssistant/html5

| Attribute        | Values                                                                                     | Description                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| enabled          | Always/Fallback/Never                                                                  | Whether to enable Receiver for HTML5 or not.                                                                                                           |
| platforms        | Semi-column separated list of regular expressions. **Firefox;Chrome;Version/ ([6-9]\d\d).*Safari;MSIE \d\d;Trident; Android;iPad;iPhone;iPod** ;                                         | Regular expressions to search the UserAgent string to identify supported browsers.                                                                                                                                                                                                                                            |
| launchURL        | Relative URL                                                                               | Location of the Receiver for HTML5 launch page.                                                                                                        |
| singleTabLaunch  | true / **false**                                                                               | Whether to launch applications on the same browser tab as the Citrix Receiver for Web home screen or not.                                              |
| chromeAppOrigins | **chrome-extension:// bgiigkppjadidglloadcadeih lnbpagp**                                      | List of origin URLs identifying official releases of the Citrix Chrome App in the Google Chrome web store. Each URL is separated by a pipe (|) symbol. |

##User InterfaceXPath: /configuration/citrix.deliveryservices/webReceiver/clientSettings/userInterface
| Attribute         | Values                    | Description                                                                                          |
|-------------------|---------------------------|------------------------------------------------------------------------------------------------------|
| frameOptions      | allow/deny/sameorigin | Whether or not to allow Citrix Receiver for Web to be displayed in a frame/ iframe.                  |
| autoLaunchDesktop | true/false              | Whether or not to auto- launch desktop at logon if there is only one desktop available for the user. |

XPath: /configuration/citrix.deliveryservices/webReceiver/clientSettings/ userInterface/workspaceControl

| Attribute            | Values                        | Description                                                                                        |
|----------------------|-------------------------------|----------------------------------------------------------------------------------------------------|
| enabled              | true/false                  | Whether to enable workspace control or not.                                                        |
| autoReconnectAtLogon | true/false                  | Whether to perform auto- reconnect at logon or not.                                                |
| logoffAction         | disconnect/terminate/none | Whether to disconnect or terminate HDX sessions when actively logging off Citrix Receiver for Web. |
| showReconnectButton  | true/false                  | Whether to show the reconnect button/link or not.                                                  |
| showDisconnectButton | true/false                  | Whether to show the disconnect button/link or not.                                                 |

XPath: /configuration/citrix.deliveryservices/webReceiver/clientSettings/ userInterface/receiverConfiguration

| Attribute | Values       | Description                                                   |
|-----------|--------------|---------------------------------------------------------------|
| enabled   | true/false | Whether to enable Receiver provisioning file download or not. |

XPath: /configuration/citrix.deliveryservices/webReceiver/clientSettings/ userInterface/appShortcuts

| Attribute             | Values       | Description                                                                                             |
|-----------------------|--------------|---------------------------------------------------------------------------------------------------------|
| enabled               | true/false | Whether to enable app shortcuts or not.                                                                 |
| allowSessionReconnect | true/false | Whether to enable session reconnect or not when Citrix Receiver for Web is launched by an app shortcut. |