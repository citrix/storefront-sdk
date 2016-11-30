# Samples

## IEnumrationResultModifier

This example demonstrates how to use `IEnumrationResultModifier` interface to disable the resources based upon the time of the request.

```
using System;
using System.Xml.Linq;
using Citrix.DeliveryServices.ResourcesCommon.Customization.Contract;
namespace StoreCustomization_Enumeration
{
    public class EnumerationResultModifier : IEnumerationResultModifier
    {
        public string Modify(CustomizationContextData context, string valueToModify)
        {
            if (context != null && !IsTimeAcceptable(context.HttpContext.Timestamp))
            {
                var document = XDocument.Parse(valueToModify);
                if (document.Root != null)
                {
                    XNamespace ns = "http://citrix.com/delivery-services/2-0/resources";
                    var resources = document.Root.Descendants(ns + "resource");
                    foreach (var enabledElement in resources)
                    {
                        enabledElement.SetElementValue(ns + "enabled", "false");
                    }
                    return document.ToString();
                }
            }
            return valueToModify;
        }
        public bool RunExtendedValidation { get { return false; } }
        public bool ReturnOriginalValueOnFailure { get { return true; } }
    }
}
```

## IInputModifier

This example demonstrates how to use `IInputModifier` interface to add a new `AccessConditions` based on `AuthenticationType`.

```
using System;
using System.Collections.Generic;
using Citrix.DeliveryServices.ResourcesCommon.Customization.Contract;
namespace StoreCustomization_Input
{
    public class InputModifier : IInputModifier
    {
        public bool RunExtendedValidation { get { return false; } }
        public bool ReturnOriginalValueOnFailure { get { return false; } }
        public void Modify(CustomizationContextData context, out FarmSetsContext farmSetsContext, out DeviceInfo deviceInfo, out AccessConditions accessConditions)
        {
            farmSetsContext = context.FarmSetsContext;
            deviceInfo = context.DeviceInfo;
            accessConditions = context.AccessConditions;
            if (context.UserIdentity.IsAuthenticated)
            {
                accessConditions = new AccessConditions(new List<string> { @"New_Apps_Access" }, @"AGFarm");
            }
        }
    }
}
```

#ILaunchResultModifier

This example demonstrates how to use `ILaunchResultModifier` interface to modify a property in ICAfile based upon Device Info.

```
using System;
using Citrix.DeliveryServices.ResourcesCommon.Customization.Contract;
namespace StoreCustomization_Launch
{
public class LaunchResultModifier : ILaunchResultModifier
{
        public string Modify(CustomizationContextData context, string valueToModify)
        {
            const string colorKey = "DesiredColor";
            const string newValue = "16";
            if (context.DeviceInfo.DisplayWidth > 1024 && !string.IsNullOrEmpty(valueToModify))
            {
                var indexOfKey = valueToModify.IndexOf(colorKey, StringComparison.OrdinalIgnoreCase);
                if (indexOfKey > 0)
                {
                    var indexOfEndOfLine = valueToModify.IndexOf(Environment.NewLine, indexOfKey, StringComparison.OrdinalIgnoreCase);
                    var oldKeyValuePair = valueToModify.Substring(indexOfKey, (indexOfEndOfLine - indexOfKey));
                    var newKeyValuePair = string.Format("{0}={1}", colorKey, newValue);
                    valueToModify = valueToModify.Replace(oldKeyValuePair, newKeyValuePair);
                }
            }
            return valueToModify;
        }
        public bool RunExtendedValidation { get { return false; } }
        public bool ReturnOriginalValueOnFailure { get { return true; } }
    }
}
```

