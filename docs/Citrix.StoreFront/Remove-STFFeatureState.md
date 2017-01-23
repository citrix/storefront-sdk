#Remove-STFFeatureState
Removes the FeatureState object
##Syntax
```Remove-STFFeatureState [-Name] <String> [<CommonParameters>]
```
##Detailed Description
Removes the FeatureState object
##Related Commands
*[Add-STFFeatureState](Add-STFFeatureState)
*[Get-STFFeatureState](Get-STFFeatureState)
*[Get-STFFeatureStateNames](Get-STFFeatureStateNames)
*[New-STFFeatureState](New-STFFeatureState)
*[New-STFFeatureStateProperty](New-STFFeatureStateProperty)
*[Reset-STFFeatureStates](Reset-STFFeatureStates)
*[Set-STFFeatureState](Set-STFFeatureState)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||Name|The unique identifier of the FeatureState|true|false|##Input Type
###System.String
Parameter Name: The .NET 'System.String' reference type
##Return Values
##Examples
###EXAMPLE 1 Removes the FeatureState object
```Remove-STFFeatureState -Name feature1
```
REMARKS
Removes the FeatureState object registered as feature1
