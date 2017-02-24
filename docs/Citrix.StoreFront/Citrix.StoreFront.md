#Citrix.StoreFront
##TOPIC
about_Citrix.StoreFront
##SHORT DESCRIPTION
The Citrix.StoreFront module provides administrative functions for the required StoreFront components.
##COMMAND PREFIX
All commands in this module have 'STF' in their name to denote they are part of the StoreFront product.
##LONG DESCRIPTION
The Citrix.StoreFront PowerShell module enables local administration of StoreFront support components. The Authentication, Store and Receiver for Web services are dependant on the base components to deliver applications, desktops, self-service and authentication. Examples of usage can be found in <InstallPath>\PowerShellSDK\Examples. 

    The module provides the following main entities: 

    RoamingService 
        The configuration for accessing StoreFront deployments. External gateways are service access information is stored in this service. 

    ServerGroup 
        The configuration of servers that comprise the StoreFront group. 

    SubscriptionStoreService 
        The Windows service based data store used for storing self-service application and desktop subscriptions.
