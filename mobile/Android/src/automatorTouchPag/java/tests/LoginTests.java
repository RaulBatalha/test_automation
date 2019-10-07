package tests;

import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import pages.HomePage;
import pages.LoginPage;

import utilities.PropertyManager;


public class LoginTests extends BaseTest {

    //Test Data
    String wrongUsername = PropertyManager.getInstance().getWrongUsername();
    String wrongPassword = PropertyManager.getInstance().getWrongPassword();

    private HomePage homePage;
    private LoginPage loginPage;

    @BeforeMethod
    public void methodLevelSetup() {
        //*************PAGE INSTANTIATIONS*************
        homePage = new HomePage(driver,wait);
        loginPage = new LoginPage(driver,wait);

        //*************PAGE METHODS********************
        //Open HomePage
        homePage.goToN11();

        //Go to LoginPage
        homePage.goToLoginPage();
    }


    @Test (priority = 1, description="Invalid Login Scenario with wrong username and password.")
    public void invalidLoginTest_InvalidUserNameInvalidPassword ()  {
        //Login to N11
        loginPage.loginToN11(wrongUsername, wrongPassword);

        //*************ASSERTIONS***********************
        loginPage.verifyLoginPassword(("E-posta adresiniz veya şifreniz hatalı"));
    }

    @Test (priority = 2, description="Invalid Login Scenario with empty username and password.")
    public void invalidLoginTest_EmptyUserEmptyPassword ()  {
        //Login to N11
        loginPage.loginToN11("","");

        //*************ASSERTIONS***********************
        loginPage.verifyLoginUserName("Lütfen e-posta adresinizi girin.");
        loginPage.verifyLoginPassword("Bu alanın doldurulması zorunludur.");
    }
}
