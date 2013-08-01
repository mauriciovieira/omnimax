//Required namespaces
using net.openstack.Providers.Rackspace.Objects;
using net.openstack.Providers.Rackspace;
using net.openstack.Core.Providers;
using net.openstack.Core.Exceptions.Response;

public class Authenticate
{
   public static void Main()
   {
        try
        {
            IIdentityProvider identityProvider = new CloudIdentityProvider();
            var userAccess = identityProvider.Authenticate(new RackspaceCloudIdentity
               {
                   Username = System.Environment.GetEnvironmentVariable("RAX_USERNAME"),
                   APIKey = System.Environment.GetEnvironmentVariable("RAX_API_KEY")
               });
            System.Console.WriteLine("Authenticated");
        }
        catch(ResponseException ex2)
        {
          throw;
            // do something
        }
    }
}
