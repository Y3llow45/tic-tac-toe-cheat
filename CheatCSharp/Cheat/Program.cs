using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using System;

namespace BrowserAutomation
{
    class Program
    {
        static void Main(string[] args)
        {
            var options = new ChromeOptions();
            options.AddArgument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36");
            using IWebDriver driver = new ChromeDriver(options);
            try
            {
                driver.Navigate().GoToUrl("https://www.google.com/search?q=tic+tac+toe");

                System.Threading.Thread.Sleep(1000);

                new WebDriverWait(driver, TimeSpan.FromSeconds(10)).Until(
                d => ((IJavaScriptExecutor)d).ExecuteScript("return document.readyState").Equals("complete"));
                //WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
                System.Threading.Thread.Sleep(1000);
                IWebElement corner = driver.FindElement(By.XPath("//td[@jsname='WfZakb']"));
                corner.Click();

                /*IWebElement resultElement = driver.FindElement(By.ClassName("resultClassName"));
                Console.WriteLine(resultElement.Text);*/
                //WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(50));
                // IWebElement element = wait.Until(SeleniumExtras.WaitHelpers.ExpectedConditions.ElementIsVisible(By.Id("elementId")));
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
            finally
            {
                // Close the browser
                driver.Quit();
            }
        }
    }
}
