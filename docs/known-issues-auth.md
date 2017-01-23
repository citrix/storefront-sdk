#Known Issues for Version 2.6

The following issues are known to exist in this release 

***Not all Citrix clients correctly handle Citrix Common Forms Multi-Combo input***

Not all clients support the Citrix Common Forms Multi-Combo input and will fail a conversation if a form contains this type of input. [#496360] 

***Strings in the wrong language appear in the sample installers***

Some untranslated strings appear during TestForms and MagicWord uninstallation process when SF admin console is opened [#493758]

AuthSDK installers shows Chinese (People's Republic of China) text on Chinese (Taiwan) environment rather than English [#497560]

***Receiver for Web does not always deal correctly with Cancel and Failure cases***

Some Cancel and Failure forms result in 'Can not complete your request' message displayed in WebReceiver [#498737]

If an individual label is referenced more than once by a FormsMessage (information, warning, error etc) than the label is also marked with more than one '*'(star) in front of it. [#490830]
