#Clear-STFDefaultPnaStore
Clear the default PNA store
##Syntax
```Clear-STFDefaultPnaStore [[-SiteId] <Int64>] [<CommonParameters>]
```
##Detailed Description
Clears the default PNA store hosted at the default PNA url, http://example.storefront.com/Citrix/Store/PNAgent/config.xml.
##Related Commands
*[Enable-STFStorePna](Enable-STFStorePna)
*[Disable-STFStorePna](Disable-STFStorePna)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||SiteId|The IIS Site to clear the default Pna store from|false|false|##Input Type
###System.Int64
Parameter SiteId: The .NET 'System.Int64' value type
##Return Values
##Examples
###EXAMPLE 1 Clear the default PNA store
```Clear-STFDefaultPnaStore
```
REMARKS
Clears the default PNA store.
