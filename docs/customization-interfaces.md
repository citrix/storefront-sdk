# Customization interfaces
This topic details the interfaces exposed by StoreFront and explains how to use these to apply customizations.
There are four main types of customization:

1.	Resources customization—uses the IEnumerationResultModifier interface
2.	Sessions customization—uses the ISessionListModifier interface
3.	ICA file customization—uses the ILaunchResultModifier interface
4.	Request customization—uses the IInputModifier interface

The interfaces are bundled in the
`Citrix.DeliveryServices.ResourcesCommon.Customization.Contract` assembly.

The implementing assembly must target .NET Framework 4.5.
Each interface exposes the following members (see the appropriate interface for more details), unless specified otherwise:

- `Modify`: This virtual method is the calling point of the interface. To customize, the implementing class must override this method. The signature of this method is detailed in the appropriate interface section below.
- `RunExtendedValidation`: This property indicates whether or not StoreFront validates the returned value to ensure it is of the correct form. Because there is a performance impact associated with extended validation, only set this on during development and debugging, and ensure that extended validation is set to off in the production environment.
- `ReturnOriginalValueOnFailure`: This property indicates whether or not StoreFront returns the original computed value, whenever there's an error in the customized value returned by the method. We recommend you set this property to true.

##Resources customization

Use this type of customization to modify the resource enumeration, as computed by
StoreFront, before it is sent to the client. StoreFront calls the Modify method of the
IEnumerationResultModifier interface with the computed resource enumeration result and a context parameter. The implementing class must override the method, modify the enumeration result and return it back to StoreFront. StoreFront then sends the modified result to the client for further processing.

Refer to the Store Service Customization API file and the sample solution supplied with the SDK for examples of how to use this interface.

!!! tip "Note"
	Resources customizations only take effect for Receivers using the native protocols; 	customizations do not take effect for clients that access the store using legacy 	protocols, such as Program Neighbourhood Agent.

###Interface
The custom class must implement the `IEnumerationResultModifier` interface.

###Class Name
Name the custom class `EnumerationResultModifier`.

###Assembly Name
Place the custom class in the `StoreCustomization_Enumeration` assembly.

###Method Signature
String `Modify` (`CustomizationContextData` context, string `valueToModify`)

Use this method when you want to modify the entire resource enumeration result. All the code to customize the resource enumeration must be contained within this method.

###Method Signature 
String `ModifySingleApp` (`CustomizationContextData` context, string `valueToModify`)

Use this method when you want to modify a single resource. All the code to customize the resource enumeration must be contained within this method.

####Parameters

- `context`: This parameter is of type `CustomizationContextData` and contains a set of context data, such as device information, `HttpContext`, user identity, access conditions, farm details and any user access preferences. See the Store Service Customization API file for details about this type; use this as a reference to base the customization logic on.

- `valueToModify`: This parameter is of type string and contains the resource enumeration result, as computed by StoreFront. This string adheres to the resource enumeration result, as specified in the Store Service Customization API file.

####Return Value

This method returns a string containing the resource enumeration result, as specified in the StoreFront Service API.
The implementing class must run all the validations against the resource enumeration result before returning it from the method.

###Sessions customization

Use this interface to modify the ICA sessions enumeration, as computed by StoreFront, before it is sent to the client. StoreFront calls the Modify method of the ISessionListModifier interface with the computed session enumeration result and a context parameter. The implementing class must override the method, modify the enumeration result, and return it back to StoreFront. StoreFront then sends the modified result to the client for further processing.

Refer to the Store Service Customization API file and the sample solution supplied with the SDK for examples of how to use this interface.

!!! tip "Note"
Sessions customizations only take effect for Receivers using the native protocols; customizations do not take effect for clients that access the store using legacy protocols, such as Program Neighbourhood Agent.

- **Interface**: the custom class must implement the `ISessionListModifier` interface.
- **Class Name**: name the custom class `SessionListModifier`.
- **Assembly Name**: place the custom class in the `StoreCustomization_SessionEnumeration` assembly.
- **Method Signature**: string `Modify`(`CustomizationContextData` context, string `valueToModify`)

Use this method to modify the session enumeration result. All the code to customize the session enumeration must be contained within this method.

####Parameters

- `context`: This parameter is of type CustomizationContextData. It contains a set of context data, such as device information, HttpContext, user identity, access conditions, farm details and any user access preferences. See the Store Service Customization API file for details about this type; use this as a reference on which to base customization logic.

- `valueToModify`: This parameter is of type string and contains the session enumeration result, as computed by StoreFront; see the Store Service Customization API file.


####Return Value
This method returns a string containing the session enumeration result, as specified in the StoreFront Service API. The implementing class must run all validations against the session enumeration before returning it from the method.

## ICA File customization

Use this interface to modify the content of an ICA file, as computed by StoreFront, before it is sent to the client. StoreFront calls the Modify method of the ILaunchResultModifier interface with the computed ICA file and a context parameter. The implementing class must override the method, modify the ICA file, and return it back to StoreFront. StoreFront then sends the modified file to the client for further processing.

Refer to the Store Service Customization API file and the sample solution supplied with the SDK for examples of how to use this interface.

- **Interface**:the custom class must implement the `ILaunchResultModifier` interface.
- **Class Name**: name the custom class `LaunchResultModifier`.
- **Assembly Name**: place the custom class in the `StoreCustomization_Launch` assembly.
- **Method Signature**: string `Modify`(`CustomizationContextData` context, string `valueToModify`)

Use this method to modify the content of the ICA file. All the code to customize the ICA file must be contained within this method.

###Parameters

-`context`: This parameter is of type `CustomizationContextData` and contains a set of context data, such as device information, `HttpContext`, user identity, access conditions, farm details and any user access preferences. See the Store Service Customization API file for details about this type; use this as a reference on which to base the customization logic.
-`valueToModify`: This parameter is of type string and contains the content of ICA file as computed by StoreFront.

###Return Value

This method returns a string, which forms the content of the ICA file. The implementing class must run all validations against the modified file content before returning it from the method.

###Request customization

Use this interface to modify a request before it is forwarded to the back-end XML services, such as the XenDesktop Delivery Controller.

Unlike other customization points where the custom code is called after StoreFront computes the result, this customization code is called before the request is sent to the back-end XML services, after partial request processing by StoreFront. StoreFront calls the Modify method of the IInputModifier interface with a set of request parameters and a context parameter. The implementing class must override this method and can alter the value of the properties of the request parameters. StoreFront uses the modified request parameters when contacting the back-end XML services.

!!! tip "Note"
	The Request Customization interface cannot be used if the site is configured with multi-	site farms (configured using the `userFarmMappings` configuration element or `Set-	DSUserMappings` cmdlet).

Refer to the Store Service Customization API file and the sample solution supplied with the SDK for examples of how to use this interface.

- **Interface**: the custom class must implement the `IInputModifier` interface.
- **Class Name**: name the custom class `IInputModifier`.
- **Assembly Name**: place the custom class in the `StoreCustomization_Input` assembly.
- **Method Signature**: void `Modify` (`CustomizationContextData` context, out `FarmSetsContext farmSetsContext`, out `DeviceInfo deviceInfo`, out `AccessConditions accessConditions`)

Use this method to modify the request. All the code to modify the request must be contained within this method.

Refer to the Store Service Customization API file and the sample solution supplied with the SDK for examples of how to use this interface.

- **Interface**: the custom class must implement the IInputModifier interface.
- **Class Name**: name the custom class IInputModifier.
- **Assembly Name**: place the custom class in the StoreCustomization_Input assembly.
- **Method Signature**: void Modify (CustomizationContextData context, out FarmSetsContext farmSetsContext, out DeviceInfo deviceInfo, out AccessConditions accessConditions)

Use this method to modify the request. All the code to modify the request must be contained within this method.


###Parameters

- `context`: This parameter is of type `CustomizationContextData`. It contains a set of context data, such as device information, `HttpContext`, user identity, access conditions, farm details and any user access preferences.
- `farmSetsContext`: This parameter is of type `FarmSetsContext` and contains the list of farms which will be contacted by StoreFront. The customization modifies this list. StoreFront contacts each farm in the modified list.
- `deviceInfo`: This parameter is of type `DeviceInfo` and contains the client device information as sent by the client. Use this customization to modify this information before StoreFront sends it to the back-end XML services.
- `accessConditions`: This parameter is of type `AccessConditions`. It contains the access conditions sent by the client and computed by StoreFront. Use this customization to modify these conditions before StoreFront sends this information to the back-end XML services.

For more information about the parameters, see the Store Service Customization API file.

## Deploy customizations
This topic explains how to deploy your customizations. Customization modules must be contained within their respective assemblies. To deploy customizations:

1.	Back up the original assemblies
2.	Deploy customizations

These steps are explained in more detail below.

###Back up the original assemblies

Citrix recommends you back up the original assemblies before replacing them with the new customized assemblies. Original assemblies are required for restoring the default behavior. Ensure you back up the following:

1.	StoreCustomization_Enumeration.dll
2.	StoreCustomization_Input.dll
3.	StoreCustomization_Launch.dll
4.	StoreCustomization_SessionEnumeration.dll

###Deploy customizations

To deploy customizations, manually copy the new customized assemblies to the Store's bin folder on the appropriate StoreFront server. This replaces the existing assemblies.

If the StoreFront server is part of a cluster deployment, perform the propagation action to push the new assemblies to other members of the cluster.

!!! tip "Note"
	Only these files, and accompanying pdbs, are propagated using the propagation action. If 	there are additional files, these must be copied manually to all machines in the cluster.

###Example
The following example shows how to locate the Store's bin folder on the StoreFront Server.

In this example, the home directory for the website is `C:\inetpub\wwwroot`.

StoreFront is configured on this website with a store named "Store". The valid full directory path you copy new customized assemblies to is:

`C:\inetpub\wwwroot\Citrix\Store\bin`

##Restart services##

After deploying your customizations, restart the following services. Restarting forces the services to clear any cached data from previous implementations of the assemblies.

!!! tip "Note"
	Services should restart automatically when customizations are deployed, but Citrix 	recommend you check that this has occurred.

- Internet Information Service: this is the IIS service running on the StoreFront Server.
- `CitrixSubscriptionsStore`: this is a Windows service running on the StoreFront Server.

###Test and debug

This topic explains how to test and debug your customizations. It explains how to enable tracing, and attach the debugger so that you can debug within Visual Studio.

To troubleshoot your implementation, first look in the event log. You can also consult the trace which provides more information than in the event log. During testing, set the trace level to "verbose"; in production, set it to Error or Warning—see the section below for details of how to enable tracing.

For information on debugging your implementation within Visual Studio, see the section below.

You can also configure StoreFront to run extended validation against returned values during development and testing. To do this, set RunExtendedValidation to true; for more information see [Customization interfaces](customization-interfaces.md). However, because there is a performance impact when running extended validation, ensure you set this off in the production environment.

###Enable tracing
The tracing feature writes detailed information to the trace. The default location for trace dumps is `C:\Program Files\Citrix\Receiver StoreFront\Admin\trace`.

To enable tracing and set the trace level, use the PowerShell script `SetDSStoreCustomizationTraceLevel.ps1` which is supplied with the SDK. This script takes the following parameters:

- `SiteId`: the IIS Site Id where the store is deployed
-	`VirtualPath`: the virtual path of the store
-	`TraceLevel`: use to set the following trace levels:
	a.	`Error`
	b.	`Info`
	c.	`Off`
	d.	`Verbose`
	e.	`Warning`

!!! tip "Note"
	Citrix recommend you set the trace level to `Verbose` during development, and to `Error` or 	`Warning` in theproduction environment.

!!! tip "Note"
	If you do not know the SiteId and VirtualPath of the Store, run the following PowerShell 	commands:
```
cd 'c:\program files\Citrix\Receiver Storefront\Scripts'. 
.\ImportModules.ps1
Get-DSStoreFeatureInstances
```

###Write to the trace
The Store Customization SDK includes a tracing class named `Tracer`. This class has the following methods which allow you to output to the trace from the Store Customization SDK:
- `TraceWarning`: writes a warning trace message at `TraceEventType.Warning`
- `TraceInfo`: writes an informational trace message at `TraceEventType.Information`
- `TraceError`: writes an error trace message at `TraceEventType.Error`
- `Trace Method`: writes a trace message at `TraceEventType.Verbose`

###Debugging

This section explains how to attach the debugger so that you can debug your implementation line-by-line within Visual Studio, and specify breakpoints where execution of the code pauses.

1.	Open your customized solution in Visual Studio 2012.
2.	Attach to process w3wp.exe which has the user name `IIS APPPOOL\Citrix Delivery Services Resources`.

Subsequent requests for resources using the preferred client will hit a breakpoint in Visual Studio.

To set up remote debugging, see Enabling Remote Debugging. You need to do this if the development machine running Visual Studio is different from the StoreFront deployment machine running your customizations.