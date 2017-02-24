#Get-STFWebReceiverFeaturedAppGroup
Gets the Featured App groups definitions configured within the Receiver for Web
##Syntax
```Get-STFWebReceiverFeaturedAppGroup [-WebReceiverService] <WebReceiverService> [<CommonParameters>]
```
##Detailed Description
The cmdlet gets the Featured App groups definitions as configured within the Receiver for Web
##Related Commands
*[Add-STFWebReceiverFeaturedAppGroup](Add-STFWebReceiverFeaturedAppGroup)
*[Clear-STFWebReceiverFeaturedAppGroup](Clear-STFWebReceiverFeaturedAppGroup)
*[Remove-STFWebReceiverFeaturedAppGroup](Remove-STFWebReceiverFeaturedAppGroup)
*[Set-STFWebReceiverFeaturedAppGroup](Set-STFWebReceiverFeaturedAppGroup)
##Parameters
|Name|Description|Required?|Pipeline Input||--|--|--|--||WebReceiverService|WebReceiver to get the FeaturedAppGroups from|true|true (ByValue)|##Input Type
###Citrix.StoreFront.Model.ReceiverForWeb.WebReceiverService
Parameter WebReceiverService: A .NET class representing the configuration of a StoreFront Web Receiver service
##Return Values
###FeaturedAppGroups
The .NET 'Citrix.StoreFront.Model.ReceiverForWeb.FeaturedAppGroups' reference type
##Examples
###EXAMPLE 1 Get the FeaturedAppGroups
```$webReceiver = Get-STFWebReceiverService
$group = New-STFWebReceiverFeaturedAppGroup -Title "Worx Suite" `
-Description "Improve productivity with a suite of secure mobile apps made for business." `
-TileId appBundle1 `
-ContentType Keyword `
-Contents Worx
Add - STFWebReceiverFeaturedAppGroup - WebReceiverService $webReceiver - FeaturedAppGroup $group
Get-STFWebReceiverFeaturedAppGroup -WebReceiverService $webReceiver
```
REMARKS
Get the featured application groups
OUTPUT
```Title       : Worx Suite
Description : Improve productivity with a suite of secure mobile apps made for business.
TileId      : appBundle1
ContentType : Keyword
Contents    : {Worx}
```
