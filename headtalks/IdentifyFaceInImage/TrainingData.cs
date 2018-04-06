using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IdentifyFaceInImage
{
    public class TrainingData
    {
        public static TrainingData Create(string path)
        {
            return new TrainingData
            {
                People = new ObservableCollection<TrainingPerson>(new DirectoryInfo(path).GetDirectories().Select(d =>
               {
                   return new TrainingPerson
                   {
                       Name = d.Name,
                       Images = new ObservableCollection<string>(d.GetFiles("*.jpg").Select(f => f.FullName))
                   };
               }))
            };
        }

        public ObservableCollection<TrainingPerson> People { get; set; }
    }


    public class TrainingPerson
    {
        public string Name { get; set; }
        public ObservableCollection<string> Images { get; set; }
    }
}
