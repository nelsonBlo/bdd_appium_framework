Mobile Automation Testing Framework (BDD)
===

This testing framework is developed for mobile application testing, utilizing Python, Behave, Allure Reporting, 
and Appium with the Page Object Model (POM) design principles. 

It's designed to provide a pretty simple, scalable, and easy-to-maintain testing solution for mobile applications. 

It has two features that were automated to test the James Rider app. Due to time restrictions, this framework only supports 
Android devices.

It's highly not recommended to test apps on emulated devices, but for practical and time reasons, and only for demo, 
these instructions are made to run project Tests on emulators.


Project Pre-requisites
---
- [Python](https://www.python.org/downloads/) >= 3.x installed
- [Node/npm](https://nodejs.org/) installed
- [Java](https://www.oracle.com/ca-en/java/technologies/downloads/) installed with `JAVA_HOME` added to PATH (Java 8-202 is recommended for this project)
- [Android Studio](https://developer.android.com/studio) installed with `ANDROID_HOME` added to PATH
- [Appium](https://appium.io/docs/en/2.2/quickstart/install/) installed
- [UIAutomator2](https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/) driver installed
- [Allure Report](https://allurereport.org/docs/gettingstarted-installation/) installed
- Mobile device must have installed the James Rider application version 1.22.0 (3416)
- User must be logged once to the James Rider application. App can be closed if needed.

Setup Instructions
---
1. Clone repository to your local system.
2. Navigate to the project directory.
3. Run this command in order to install all project python dependencies:
   ```sh
    pip install -r requirements.txt
   ```
4. Connect to your machine the mobile device with the James Rider app installed on it. 
You can use en Android Studio Emulator to load an emulated device.
5. Run this command to get the emulated device name:
    ```sh
    emulator -list-avds
    ```
6. Modify `appium:deviceName": "Pixel_3a"` in `/src/features/environment.py` according to your device name.
7. Run this command to load device:
    ```sh
    emulator @'device_name' -no-snapshot-load
    ```
   
Creating Tests
---
- Add app page elements and methods under pages directory. Use classes.
- Add BDD features under `features/`. The steps corresponding to these features must be located under `/steps` folder.
- Ensure python naming standards are followed.


Tests made as example
---
There are 2 features already automated for the James Rider app.
- Profile Changes
- Logout

On Profile Changes there are 2 scenarios (Test Cases). One of them uses the Examples Table.
On Logout there is only 1 scenario.

Both features were tagged with @android tag since these scripts were only developed for this platform.

Running Tests
---
Behave supports several ways to run tests.
- Be sure to locate under `/src` directory.
- Run all features at the automation project:
    ```sh
    behave ./features
    ```
- Run only a specific feature:
  ```sh
    behave ./features/profile_change_profile.feature
  ```
- Run tagged features or scenarios:
  ```sh
    behave  --tags="@names"
  ```
  In this case just one scenario will be executed. 

Test Report
---
This framework uses Allure Report library to produce an HTML Test Report. 
- Run features with any of the previous commands.
- Run this command to process the test results and save an HTML report into the `allure-report` directory. 
  ```sh
  allure generate --clean
  ```
- Run this command to view Test Report in system default browser:
  ```sh
  allure open
  ```

Project Structure
---
- `allure-report`: Stores the test run report (`index.html`) and related files and directories.
- `allure-results`: Stores result artifacts in json format used to generate the Allure report.
- `data`: Centralized storage for test data.
- `features`: Contains test definitions in Gherkin language features. 
- `features/steps`: Contains test steps. 
- `features/environment`: Contains configuration for the Appium driver. 
- `pages`: Central repository for all page objects of the application.
- `resources`: Stores the application under test.
- `utils`: Holds custom actions.
- `behave.ini`: Behave-specific configuration.
- `requirements.txt`: Framework dependencies.
