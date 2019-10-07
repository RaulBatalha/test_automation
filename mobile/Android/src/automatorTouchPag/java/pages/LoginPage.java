package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

public class LoginPage extends BasePage {

    //*********Constructor*********
    public LoginPage(WebDriver driver,WebDriverWait wait) 
	{
        super(driver, wait);
    }

    //*********Web Elements*********
    By usernameBy = By.id("email");
    By passwordBy = By.id("password");
    By loginButtonBy = By.id("loginButton");
    By errorMessageUsernameBy = By.cssSelector("#loginForm .error:nth-of-type(1) .errorMessage");
    By errorMessagePasswordBy = By.cssSelector("#loginForm .error:nth-of-type(2) .errorText");

    //*********Page Methods*********
    public void login (String username, String password)
	{	
        //Enter Username(Email)
        writeText(usernameBy,username);
        //Enter Password
        writeText(passwordBy, password);
        //Click Login Button
        click(usernameBy); //In order to click right, this line needed. Site related.
        click(loginButtonBy);
    }

    //Verify Username Condition
    public void verifyLoginUserName (String expectedText) {
        wait.until(ExpectedConditions.visibilityOfElementLocated(errorMessageUsernameBy));
        Assert.assertEquals(readText(errorMessageUsernameBy), expectedText);
    }

    //Verify Password Condition
    public void verifyLoginPassword (String expectedText) {
        wait.until(ExpectedConditions.visibilityOfElementLocated(errorMessagePasswordBy));
        Assert.assertEquals(readText(errorMessagePasswordBy), expectedText);
    }
}
