## XenApp and XenDesktop SDK

<span id="par_richtext" class="anchor"></span>

XenApp and XenDesktop provide an SDK based on a number of Microsoft
Windows PowerShell version 3.0 snap-ins that allows you to perform the
same tasks as you would with the Citrix Studio console, together with
tasks you cannot do with Studio alone.

As from version 7.5,XenApp and XenDesktop share a unified architecture and management: the
FlexCast Management Architecture. This means that XenApp provides many
features previously only available in XenDesktop; elements of the SDK
that relate to common features therefore apply equally to both XenApp
and XenDesktop, even though the commands themselves refer only to
XenDesktop.

### Key differences between the XenDesktop 5 and XenDesktop 7 SDK

-   **New high-level SDK** — XenDesktop 7 provides a new high-level SDK
    that enables you to script and automate site creation and
    maintenance quickly and easily. The high-level SDK insulates you
    from much of the complexity of the low-level SDKs, such that you can
    create a new site simply by running two cmdlets.

-   **New low-level SDKs **— Individual low-level SDKs are provided for
    the new XenDesktop 7 services, including a dedicated and enhanced
    SDK for the Delegated Administration Service (DAS), which was
    previously part of the Broker SDK in XenDesktop 5. There are also
    SDKs for new features including the Monitor Service, Environment
    Test, and Configuration Logging.

-   **Windows Server OS Machine catalogs and delivery groups** — You can
    use the XenDesktop 7 SDK to deliver cost-effective applications and
    desktops hosted on server operating systems.

-   **Desktop OS Machine applications** — Desktop OS Machine
    applications have changed significantly at the SDK level. If you
    have existing scripts for running applications on Desktop OSs, you
    will have to update these scripts for XenDesktop 7 as there is
    little backwards compatibility.

-   **Apply settings to machines in Delivery Groups** — In XenDesktop 7,
    using configuration slots, you can apply settings to machines in a
    specific delivery group, rather than to all machines in a site. This
    enables you to configure, for a given delivery group, which settings
    apply to that group. A number of pre-defined configuration slots are
    provided that contain different types of settings, such as settings
    for StoreFront addresses for use with Receiver or App-V publishing
    server locations. You can use one collection of settings from a slot
    to affect only a particular delivery group, and a different
    collection of settings from the same slot to affect another
    delivery group. You can use names appropriate to your particular
    deployment; for example, "Sales Department policy."

-   **Catalog types replaced** — In XenDesktop 7, catalog types have
    been replaced by catalogs with individual properties. However, for
    backwards compatibility, you can still use existing scripts that
    employ catalog types, such as single image (pooled) and thin
    clone (dedicated) etc., but internally these are converted into sets
    of properties.

!!! warning "Caution"
    Backwards compatibility with XenDesktop 5 catalog types has been maintained where possible and practicable. However, when writing new scripts, do not use catalog types; instead, specify catalogs with individual properties.

-   **Desktop object replaced** — In XenDesktop 5, the Desktop object is
    one of the main types of SDK object used in Broker SDK scripts. The
    Desktop object describes both the machine and the session on
    the machine. In XenDesktop 7, this object is replaced by the Session
    object and the Machine object, both of which have been expanded to
    do the work of the Desktop object. However, for backwards
    compatibility, you can still use existing scripts that employ the
    Desktop object.

!!! warning "Caution"
    Backwards compatibility with XenDesktop 5 has been maintained where possible and practicable. However, when writing new scripts, do not use the Desktop object; instead, specify Session and Machine objects.

### Differences in policy rules

There are differences between the SDK and the Studio console in terms of
policy rules. Entitlement and assignment policy rules are independent
entities in the SDK; in the console, these entities are not visible as
they are seamlessly merged with the Delivery Group. Also, access policy
rules are less restrictive in the SDK.

### Use the SDK

The SDK comprises of a number of PowerShell snap-ins installed
automatically by the installation wizard when you install the Controller
or Studio components.

To access and run the cmdlets:

1.Start a shell in PowerShell 3.0.

> To start a shell from the console, click **Studio**, select the
> PowerShell tab, and click on **Launch PowerShell**.
>
> You must run the shell or script using an identity that has Citrix
> administration rights. Although members of the local administrators
> group on the Controller automatically have full administrative
> privileges to allow XenDesktop to be installed, Citrix recommends that
> for normal operation, you create Citrix administrators with the
> appropriate rights, rather than use the local administrators account.
> If you are running Windows Server 2008, you must run the shell or
> script as a Citrix administrator, and not as a member of the local
> administrators group.

2.To use SDK cmdlets within scripts, set the execution policy in PowerShell.

> For more information about PowerShell execution policy, see your
> Microsoft documentation.

3.Add the snap-ins you require into the PowerShell environment using
    the **Add -PSSnapin** command in the Windows PowerShell console. V1
    and V2 denote the version of the snap-in (XenDesktop 5 snap-ins are
    version 1; XenDesktop 7 snap-ins are version 2.). For example, type:

> Add-PSSnapin Citrix.ADIdentity.Admin.V2
>
> To import all the cmdlets, type:
>
> Add-PSSnapin Citrix.\*.Admin.V\*
>
> After importing, you have access to the cmdlets and their associated
> help.

For an example of a typical use case, see [*Get started with the
SDK*](./getstarted).

!!! tip "Note"
    For a complete listing of all help text for the cmdlets, see [PowerShell cmdlet help](http://docs.citrix.com/en-us/xenapp-and-xendesktop/7-6/cds-sdk-wrapper-rho/xad-commands.html).

### Group Policy SDK usage

The Citrix Group Policy SDK allows you to display and configure Group
Policy settings and filters. It uses a PowerShell provider to create a
virtual drive that corresponds to the machine and user settings and
filters. The provider appears as an extension to New-PSDrive. To use the
Group Policy SDK, either Studio or the XenApp and XenDesktop SDK must be
installed.

**Adding the Group Policy SDK**

1.To add the Group Policy SDK, type:

```
Add-PSSnapin citrix.common.grouppolicy
```
<br>          
2.To access help, type:

```
help New-PSDrive -path localgpo:/
```

**Using the Group Policy SDK**

1.To create a virtual drive and load it with settings, type:

```  
New-PSDrive &lt;Standard Parameters&gt; \[-PSProvider\]
CitrixGroupPolicy *-Controller* &lt;string&gt;
```

```
**New-PSDrive &lt;Standard Parameters&gt; \[-PSProvider\]
CitrixGroupPolicy ***-Controller*** &lt;string&gt;**
```

> where *-Controller* is the fully qualified domain name of a controller
> in the site you want to connect to and load settings from.
