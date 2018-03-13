using MahApps.Metro.Controls;
using System;
using System.Collections.Generic;
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

namespace DetectFaceInImage
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        public MainWindow()
        {
            InitializeComponent();

            SetImage(Properties.Settings.Default.ImagePath);

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();

            dlg.DefaultExt = ".jpg";
            dlg.Filter = "All Files (*.*)|*.*|PNG Files (*.png)|*.png|JPG Files (*.jpg)|*.jpg|GIF Files (*.gif)|*.gif";

            Nullable<bool> result = dlg.ShowDialog();

            if (result == true)
            {
                SetImage(dlg.FileName);
            }
        }

        private void SetImage(string path)
        {
            if (System.IO.File.Exists(path))
            {
                imagePath.Text = path;
                imageDisplay.Source = new BitmapImage(new Uri(path));

                Properties.Settings.Default.ImagePath = path;
                Properties.Settings.Default.Save();
            }
            else
            {
                Properties.Settings.Default.ImagePath = string.Empty;
            }
            Properties.Settings.Default.Save();
        }
    }
}
