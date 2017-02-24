#Set-STFDiagnostics
Configure StoreFront diagnostics
##Syntax
```
Set-STFDiagnostics [-All] <SwitchParameter> [-TraceLevel] <Off | Error | Warning | Info | Verbose> [-FileSizeKb <Int32>] [-FileCount <Int32>] [<CommonParameters>]
Set-STFDiagnostics [-AllUserFacingServices] <SwitchParameter> [-TraceLevel] <Off | Error | Warning | Info | Verbose> [-FileSizeKb <Int32>] [-FileCount <Int32>] [<CommonParameters>]
Set-STFDiagnostics [-ConfigFile] <String> [-TraceLevel] <Off | Error | Warning | Info | Verbose> [-FileSizeKb <Int32>] [-FileCount <Int32>] [<CommonParameters>]
```
##Detailed Description
Configure StoreFront service tracing and logging.
##Related Commands
##Parameters
|Name|Description|Required?|Pipeline Input|
###Citrix.StoreFrontConfiguration.Interfaces.IConfigBasedFeature
Parameter Service: The .NET 'Citrix.StoreFrontConfiguration.Interfaces.IConfigBasedFeature' reference type
###System.Management.Automation.SwitchParameter
Parameter All: The .NET 'System.Management.Automation.SwitchParameter' value type
###System.Management.Automation.SwitchParameter
Parameter AllUserFacingServices: The .NET 'System.Management.Automation.SwitchParameter' value type
###System.String
Parameter ConfigFile: The .NET 'System.String' reference type
###System.Diagnostics.TraceLevel
Parameter TraceLevel: The .NET 'System.Diagnostics.TraceLevel' value type
###System.Int32
Parameter FileSizeKb: The .NET 'System.Int32' value type
###System.Int32
Parameter FileCount: The .NET 'System.Int32' value type
##Return Values
##Examples
###EXAMPLE 1 Enable all tracing
```
```
REMARKS
Configures all StoreFront services to perform verbose level tracing useful for identifying configuration issues.

```
Set-STFDiagnostics -Service $store -TraceLevel Verbose
```
REMARKS
Configures the Store service at /Citrix/Store to perform verbose level tracing useful for identifying configuration
issues.
