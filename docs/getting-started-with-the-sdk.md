#Getting started with the SDK

This topic explains how to apply customizations using the Store Customization SDK. A list of minimum requirements is provided, and an overview of the main steps you must perform.

All the customizations follow the same pattern: the method in the particular interface is called with the StoreFront computed value and a context parameter. The customized code alters the original value and returns a new value. This new value is then used for further processing by StoreFront. Implementing classes use the context parameter to compute the returned value.

Supplied with the SDK are typical customization examples (see the Examples folder) and "template files". These are simple files you can use as a starting point and add your own logic to. Simply populate the template files with your own code to implement your customizations, as described in the steps below. See the sample solution for more information about the template files.

Before you begin, review the Known issues section.

##Requirements
Using the Store Customization SDK requires moderate programming skills, preferably in C# 4.0 or later.
Minimum system requirements

-	OS Requirement: Windows 7
-	Visual Studio 2012
-	.NET Framework 4.5

##Overview of the steps

This section provides an overview of the main steps you perform when using the Store Customization SDK. The steps are:

1.	In Visual Studio, identify the interface you want to use; for example "Resources customization". See Customization interfaces on page 8 for more information.
2.	Select the relevant template file. See the sample solution for more information about the template files.
3.	Add your custom logic to the template file.
4.	Build the solution.
5.	Deploy your customization. See Deploy customizations on page 12 for more information.
6.	Restart services. See Restart services on page 13 for more information.
7.	Test and debug your customizations. See Test and debug on page 13 for more information.
The following topics describe these steps in more detail.

##If you upgrade StoreFront

Note that customizations are not persisted during an upgrade. After upgrading, you must redeploy your customized assembles and test these before rolling out to the production environment.

##Removing customizations

Provided you backed-up the original assemblies, as described in Deploying Customizations, you can restore the original behavior of StoreFront.

To remove customizations:

- Copy the backed-up assembles in the Store's bin folder onto one of the StoreFront servers.
- Once the assemblies are successfully copied, perform the propagation action on the StoreFront server on 
which the assemblies are copied. This pushes the original assemblies onto other members of the StoreFront cluster.

!!! tip "Tip"
	You can also remove customizations by removing the dlls and performing the propagation 	action; the dlls are removed from all machines in the server group.
