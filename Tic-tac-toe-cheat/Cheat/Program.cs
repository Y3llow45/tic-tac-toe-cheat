using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;


namespace Cheat
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            using IWebDriver driver = new ChromeDriver();

            try
            {
                driver.Navigate().GoToUrl("https://www.google.com/search?client=firefox-b-d&q=tic+tac+toe");

                // Find an element by its name attribute and interact with it
                IWebElement exampleElement = driver.FindElement(By.Name("exampleName"));
                exampleElement.SendKeys("Some text");

                // Perform actions like clicking a button
                IWebElement button = driver.FindElement(By.Id("exampleButtonId"));
                button.Click();

                // Extract text from an element
                IWebElement resultElement = driver.FindElement(By.ClassName("resultClassName"));
                Console.WriteLine(resultElement.Text);

                // Optionally, wait for elements to load
                // WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
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
