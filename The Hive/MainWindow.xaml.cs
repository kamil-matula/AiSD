using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;

namespace The_Hive
{
    public partial class MainWindow : Window
    {
        static string result = "";

        public MainWindow()
        {
            InitializeComponent();
        }

        private void CheckInput(object sender, TextCompositionEventArgs e)
        {
            string text = (sender as TextBox)?.Text;   // wpisany tekst
            if (text.Length == 10) e.Handled = true;   // limit znaków
            else if (string.IsNullOrEmpty(text))       // pierwszy znak...
            {
                if (e.Text == "-") return;             // ...to minus...

                if (!double.TryParse(text + e.Text, out _)) // ...lub cyfra
                {
                    e.Handled = true;
                }
            }
            else if (text == "0" && e.Text != ",") (sender as TextBox).Text = "";  // jeśli jest zero to zamień na coś innego
            else
            {
                if (e.Text == "," && !text.Contains(",")) return; // przecinek, tylko jeśli nie ma jeszcze przecinka

                if (!double.TryParse(text + e.Text, out _)) // litery nie są dozwolone
                {
                    e.Handled = true;
                }
            }
        }

        private void Calculate(object sender, RoutedEventArgs e)
        {
            if (ChosenFunction.SelectedIndex == -1 || ChosenExtremum.SelectedIndex == -1 || string.IsNullOrEmpty(leftEnd.Text) 
                || string.IsNullOrEmpty(rightEnd.Text) || leftEnd.Text == "od" || rightEnd.Text == "do")
            {
                Result.Content = "UZUPEŁNIJ DANE!";
            }
            else
            {
                double from, to;
                try
                {
                    from = double.Parse(leftEnd.Text); 
                    to = double.Parse(rightEnd.Text);
                }
                catch (Exception)
                {
                    Result.Content = "NIEPOPRAWNE DANE!";
                    return;
                }

                if (from >= to)
                {
                    Result.Content = "NIEPOPRAWNE DANE!";
                    return;
                }

                var process = new Process
                {
                    StartInfo = new ProcessStartInfo
                    {
                        FileName = "python",
                        Arguments = $"BeeAlgorithm.py {ChosenFunction.SelectedIndex} {leftEnd.Text} {rightEnd.Text} {ChosenExtremum.SelectedIndex}",
                        UseShellExecute = false,
                        RedirectStandardOutput = true,
                        CreateNoWindow = true
                    },
                    EnableRaisingEvents = true
                };

                result = "";
                process.OutputDataReceived += Process_OutputDataReceived;

                process.Start();
                process.BeginOutputReadLine();
                process.WaitForExit();

                Result.Content = result.Replace("f(x)", "\nf(x)");
            }   
        }

        static void Process_OutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            result += e.Data;
        }

        private void TextBox_GotFocus(object sender, RoutedEventArgs e)
        {
            TextBox txtbx = (TextBox)sender;
            if (txtbx.Text == "od" || txtbx.Text == "do")
                txtbx.Text = "";
        }
    }
}