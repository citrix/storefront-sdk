#Add-STFFeatureState
Adds a new FeatureState object
##Syntax
```Add-STFFeatureState [-FeatureState] <FeatureState> [<CommonParameters>]
Add-STFFeatureState [-Name] <String> [[-IsEnabled] <Boolean>] [[-Properties] <Hashtable>] [<CommonParameters>]
```
##Detailed Description
Adds a new FeatureState object
##Related Commands
*[Get-STFFeatureState](Get-STFFeatureState)
*[Get-STFFeatureStateNames](Get-STFFeatureStateNames)
*[New-STFFeatureState](New-STFFeatureState)
*[New-STFFeatureStateProperty](New-STFFeatureStateProperty)
*[Remove-STFFeatureState](Remove-STFFeatureState)
*[Reset-STFFeatureStates](Reset-STFFeatureStates)
*[Set-STFFeatureState](Set-STFFeatureState)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||FeatureState|The FeatureState object to add|true|true (ByValue)||Name|A unique identifier of the FeatureState object.|true|false||IsEnabled|Flag indicating whether the FeatureState is toggled on or off|false|false||Properties|A list of key value pairs representing properties of the FeatureState object|false|false|##Input Type
###Citrix.DeliveryServices.Framework.FeatureToggle.FeatureState
Parameter FeatureState: The .NET 'Citrix.DeliveryServices.Framework.FeatureToggle.FeatureState' reference type
###System.String
Parameter Name: The .NET 'System.String' reference type
###System.Boolean
Parameter IsEnabled: The .NET 'System.Boolean' value type
###System.Collections.Hashtable
Parameter Properties: The .NET 'System.Collections.Hashtable' reference type
##Return Values
##Examples
###EXAMPLE 1 Adds a new FeatureState object
```Add-STFFeatureState -featureState stateObject
```
REMARKS
Adds the specified FeatureState object
###EXAMPLE 2 Adds a new FeatureState object
```Add-STFFeatureState -Name feature1 -IsEnabled $true -Properties @{'Property1' = 'Property1Value';'Property2' = 'Property2Value'}
```
REMARKS
Creates and saves a new FeatureState object.
