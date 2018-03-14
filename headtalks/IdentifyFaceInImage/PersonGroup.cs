using Microsoft.ProjectOxford.Common.Contract;
using Microsoft.ProjectOxford.Face;
using Microsoft.ProjectOxford.Face.Contract;
using System.Configuration;
using System.Threading.Tasks;

namespace IdentifyFaceInImage
{
    public class PersonGroup
    {
        private readonly IFaceServiceClient faceServiceClient;

        public PersonGroup()
        {
            faceServiceClient = new FaceServiceClient(ConfigurationManager.AppSettings["subscriptionKey"]);
        }

        public async Task CreatePersonGroup(string personGroupId, string name)
        {
            // create person group
            await faceServiceClient.CreatePersonGroupAsync(personGroupId, name);
        }
    }
}
