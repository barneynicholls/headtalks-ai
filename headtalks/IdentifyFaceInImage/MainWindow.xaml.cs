using MahApps.Metro.Controls;
using Microsoft.ProjectOxford.Face;
using Microsoft.ProjectOxford.Face.Contract;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace IdentifyFaceInImage
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        public MainWindow()
        {
            InitializeComponent();

            Task.Run(async () =>
            {
                var key = ConfigurationManager.AppSettings["subscriptionKey"];
                var apiRoot = ConfigurationManager.AppSettings["apiRoot"];
                var faceServiceClient = new FaceServiceClient(key, apiRoot);

                var samplesDir = ConfigurationManager.AppSettings["samplesDir"];

                string personGroupId = "test-group";

                //await faceServiceClient.DeletePersonGroupAsync(personGroupId);

                //await faceServiceClient.CreatePersonGroupAsync(personGroupId, "Test Group");

                //var personGroupDir = System.IO.Path.Combine(samplesDir, "PersonGroup");

                //DirectoryInfo di = new DirectoryInfo(personGroupDir);

                //var personDirectories = di.GetDirectories();

                //foreach (var personDirectory in personDirectories)
                //{
                //    string personName = personDirectory.Name;

                //    CreatePersonResult person = await faceServiceClient.CreatePersonAsync(
                //        // group id
                //        personGroupId,
                //        // person name
                //        personName);

                //    foreach (var image in personDirectory.GetFiles("*.jpg"))
                //    {
                //        using (Stream s = File.OpenRead(image.FullName))
                //        {
                //            await faceServiceClient.AddPersonFaceAsync(
                //                personGroupId,
                //                person.PersonId,
                //                s);
                //        }
                //    }


                //}

                //await faceServiceClient.TrainPersonGroupAsync(personGroupId);

                //TrainingStatus trainingStatus = null;
                //while (true)
                //{
                //    trainingStatus = await faceServiceClient.GetPersonGroupTrainingStatusAsync(personGroupId);

                //    var status = trainingStatus.Status.ToString().ToLower();

                //    if (status != "running")
                //    {
                //        break;
                //    }

                //    await Task.Delay(1000);
                //}

                string testImageFile = System.IO.Path.Combine(samplesDir, @"identification3.jpg");

                using (Stream s = File.OpenRead(testImageFile))
                {
                    var faces = await faceServiceClient.DetectAsync(s);
                    var faceIds = faces.Select(face => face.FaceId).ToArray();

                    var results = await faceServiceClient.IdentifyAsync(personGroupId, faceIds);
                    foreach (var identifyResult in results)
                    {
                        Console.WriteLine("Result of face: {0}", identifyResult.FaceId);
                        if (identifyResult.Candidates.Length == 0)
                        {
                            Console.WriteLine("No one identified");
                        }
                        else
                        {
                            // Get top 1 among all candidates returned
                            var candidateId = identifyResult.Candidates[0].PersonId;
                            var person = await faceServiceClient.GetPersonAsync(personGroupId, candidateId);
                            Console.WriteLine("Identified as {0}", person.Name);
                        }
                    }
                }
            });
        }
    }

}