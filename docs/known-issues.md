
# Known issues in the SDK

This topic lists any known issues specific to this SDK; review this carefully before you begin using the SDK.

1.	When a user logs onto StoreFront using credentials in User Principal Name (UPN) format, the AuthenticationType field of the UserIdentity object stored in CustomizationContextData is set to an empty string and Name is set to the UPN name used when logging on.

2.	When extended validation is enabled and StoreFront experiences high usage, some requests may fail the validation process despite these requests being valid. This issue occurs intermittently, and the following error may appear: 

```
Citrix.DeliveryServices.ResourcesCommon.Customization.ValidationException: XML validation against schema failed". Ensure extended validation is set to off in the production environment.
```