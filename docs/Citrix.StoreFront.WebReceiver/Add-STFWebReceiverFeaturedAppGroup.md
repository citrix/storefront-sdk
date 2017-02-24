#Add-STFWebReceiverFeaturedAppGroup
Add a featured application group
##Syntax
```Add-STFWebReceiverFeaturedAppGroup [-WebReceiverService] <WebReceiverService> [-FeaturedAppGroup] <FeaturedAppGroup[]> [<CommonParameters>]
```
##Detailed Description
Add a featured application group that will appear on the unified Receiver home page
##Related Commands
*[New-STFWebReceiverFeaturedAppGroup](New-STFWebReceiverFeaturedAppGroup)
*[Clear-STFWebReceiverFeaturedAppGroup](Clear-STFWebReceiverFeaturedAppGroup)
*[Get-STFWebReceiverFeaturedAppGroup](Get-STFWebReceiverFeaturedAppGroup)
*[Set-STFWebReceiverFeaturedAppGroup](Set-STFWebReceiverFeaturedAppGroup)
*[Remove-STFWebReceiverFeaturedAppGroup](Remove-STFWebReceiverFeaturedAppGroup)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||WebReceiverService|WebReceiver to which the FeatureAppGroup is to be added|true|true (ByValue)||FeaturedAppGroup|FeaturedAppGroup to add|true|false|##Input Type
###Citrix.StoreFront.Model.ReceiverForWeb.WebReceiverService
Parameter WebReceiverService: A .NET class representing the configuration of a StoreFront Web Receiver service
###Citrix.StoreFront.Model.ReceiverForWeb.FeaturedAppGroup[]
Parameter FeaturedAppGroup: The .NET 'Citrix.StoreFront.Model.ReceiverForWeb.FeaturedAppGroup' reference type
##Return Values
##Examples
###EXAMPLE 1 Add a new FeaturedAppGroup
```$webReceiver = Get-STFWebReceiverService
$group = New-STFWebReceiverFeaturedAppGroup -Title "Worx Suite" `
-Description "Improve productivity with a suite of secure mobile apps made for business." `
-TileId appBundle1 `
-ContentType Keyword `
-Contents Worx
Add - STFWebReceiverFeaturedAppGroup - WebReceiverService $webReceiver - FeaturedAppGroup $group
```
REMARKS
Create and add a FeaturedAppGroup to the unified WebReceiver.
