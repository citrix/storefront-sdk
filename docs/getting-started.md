## Getting started with the SDK

To create a script,perform the following steps:

1.  Use Citrix Studio to perform the operation that you want to script; for example, to
    create a catalog for a set of Machine Creation Services Machines.

2.  Collect the log of SDK operations that Studio made to perform
    the task.

3.  Review the script to understand what each part is doing. This will
    help you with the customization of your own script. For more
    information, see the example use case which explains in detail what
    the script is doing.

4.  Convert and adapt the Studio script fragment to turn it into a
    script that is more consumable. To do this:

    -   Use variables. Some cmdlets take parameters, such as TaskId.
        However, it may not be clear where the value used in these
        parameters comes from because Studio uses values from the result
        objects from earlier cmdlets.

    -   Remove any commands that are not required.

    -   Add some steps into a loop so that these can be
        easily controlled. For example, add machine creation into a loop
        so that the number of machines being created can be controlled.

**Examples**

**Note:** When creating a script, to ensure you always get the latest enhancements and fixes,
Citrix recommends you follow the procedure described above rather than
copying and pasting the example scripts.

| Examples                                |                                   Description                                  |
|-----------------------------------------|:------------------------------------------------------------------------------:|
| [Example: Create catalog](./creating-a-catalog.md)   | Script: create a catalog for a set of Machine Creation Services (MCS) machines |
| [Example: Create and configure a host](./creating-and-configuring-a-host.md)| Script: create and configure a host                                            |
| [Example: Create a PvD Desktop](./creating-a-pvd-desktop.md)| Script: create a Delivery Group containing Personal vDisk (PvD) desktops       |
| [Example: Get load balancing information ](./getting-load-balancing-information.md)| Display load index values for Server OS Machines                               |
