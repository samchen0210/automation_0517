# This tester olny runs in Windows systems.
# Before starting the testing, please make sure to use Chrome version 113.x.xxxx.xxx as the browser. 
# If you have a different version, please download the corresponding WebDriver from https://chromedriver.chromium.org/downloads and replace chromedriver.exe in "./case" directory.

1. Download "automation_0517" repository, than unzip it.

2. Open "config.ini" , in the [run_case] section, set "true" in the test items that you want to execute.
Currently, this tester only supports case1 to case7, so you can only modify the status of case1 to case7.

3. Open CMD window, then switch to testing folder.
for example, "cd automation_0517-main/automation_0517-main"

4. Keyin "install_env.bat" to install the venv.

5. Keyin "run_test.bat", it will start the testing.

6. When the testing was finished, you can open "Barco_result.xlsx" to see your testing results.

7. If you want to check the tester's logs, all the information will be stored in tester.log ~ tester.log5.
