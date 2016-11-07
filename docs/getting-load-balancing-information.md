## Getting load balancing information

You can use Server OS Machines to deliver cost-effective applications and desktops hosted on
server operating systems to multiple users.

To load balance Server OS Machines in a deployment, you use Citrix policies. There are several
load balancing policy settings for enabling and configuring load management between servers delivering Windows Server OS machines. For more information, see the load management policy settings reference documentation. You work with policies through Studio or the Group Policy Management Console in Windows; see the Policies documentation for details.

To see the load, you can use either the Citrix Director or Studio consoles, or the PowerShell
SDK. The following example shows how to use the PowerShell SDK to display the load.

!!! tip "Note"
    If you've used previous versions of XenDesktop, you may be familiar with the **qfarm/load** command. This tool is no longer available, but you can use PowerShell to display similar output as shown in the example below.

**Example: Get load index values**

To display a list of machines with their calculated/measured load index values, together with
counts of sessions running on them:

1.  Start a shell in PowerShell. For more information, see [XenApp and XenDesktop SDK](./).

2.  Type:
```powershell
Get-BrokerMachine -SessionSupport MultiSession -Property 'DnsName','LoadIndex','SessionCount'
```
**Note:** Load index values go up to 10000. They indicate VDA machine load calculated from the configured sources, such as number of sessions. A value of 10000 indicates a fully loaded VDA machine; the broker will not send another user session to that machine.

For more information and examples, see the cmdlet help for the get-brokermachine cmdlet and About topics such as about_broker_filtering-xd7.html. See: [PowerShell cmdlet help](http://docs.citrix.com/en-us/xenapp-and-xendesktop/7-6/cds-sdk-wrapper-rho/xad-commands.html).
