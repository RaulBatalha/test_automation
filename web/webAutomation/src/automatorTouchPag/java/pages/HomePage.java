package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import utilities.PropertyManager;

public class HomePage extends BasePage {

    //*********Constructor*********
    public HomePage (WebDriver driver, WebDriverWait wait) 
	{
        super(driver, wait);
    }

    //*********Page Variables*********
    String baseURL = PropertyManager.getInstance().getURL();

    //*********Web Elements*********
    String signInButtonClass = "btnSignIn";

    //*********Page Methods*********

    //Go to Homepage
    public void goTo (){
        driver.get(baseURL);
        //driver.navigate().to(baseURL)
    }

    //Go to LoginPage
    public void goToLoginPage (){
        click(By.className(signInButtonClass));
    }
}
