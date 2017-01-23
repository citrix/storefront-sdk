#New-STFFeatureState
Creates and returns a new FeatureState object
##Syntax
```New-STFFeatureState [-Name] <String> [[-IsEnabled] <Boolean>] [[-Properties] <Hashtable>] [<CommonParameters>]
```
##Detailed Description
Creates and returns a new FeatureState object
##Related Commands
*[Add-STFFeatureState](Add-STFFeatureState)
*[Get-STFFeatureState](Get-STFFeatureState)
*[Get-STFFeatureStateNames](Get-STFFeatureStateNames)
*[New-STFFeatureStateProperty](New-STFFeatureStateProperty)
*[Remove-STFFeatureState](Remove-STFFeatureState)
*[Reset-STFFeatureStates](Reset-STFFeatureStates)
*[Set-STFFeatureState](Set-STFFeatureState)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||Name|The unique identifier of the FeatureState object.|true|false||IsEnabled|Flag indicating whether the FeatureState is toggled on or off|false|false||Properties|A list of key value pairs representing properties of the FeatureState object|false|false|##Input Type
###System.String
Parameter Name: The .NET 'System.String' reference type
###System.Boolean
Parameter IsEnabled: The .NET 'System.Boolean' value type
###System.Collections.Hashtable
Parameter Properties: The .NET 'System.Collections.Hashtable' reference type
##Return Values
###FeatureState
The .NET 'Citrix.DeliveryServices.Framework.FeatureToggle.FeatureState' reference type
##Examples
###EXAMPLE 1 Creates a new FeatureState object
```New-STFFeatureState -Name feature1
```
REMARKS
Creates a new FeatureState object without properties and status set to disabled
OUTPUT
```Name                       IsEnabled Properties               
----                       --------- ----------                
something                  False     {}
```
###EXAMPLE 2 Creates a new FeatureState object
```New-STFFeatureState -Name feature1 -IsEnabled $true
```
REMARKS
Creates a new FeatureState object without properties and status set to enabled
OUTPUT
```Name                       IsEnabled Properties               
----                       --------- ----------                
something                  True      {}
```
###EXAMPLE 3 Creates a new FeatureState object
```New-STFFeatureState -Name feature1 -IsEnabled $true -Properties @{'Property1' = 'Property1Value';'Property2' = 'Property2Value'}
```
REMARKS
Creates a new FeatureState object with properties and status set to enabled
OUTPUT
```Name                       IsEnabled Properties               
----                       --------- ----------                
something                  True      {Property1, Property2}
```
