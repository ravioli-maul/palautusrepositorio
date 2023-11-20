*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nalle
    Set Password  kalle123
    Set Password_Confirmation  kalle123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password_Confirmation  kalle123
    Submit Registration
    Register Should Fail With Message  Invalid username. Username must have at least 3 lowercase letters

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalle
    Set Password_Confirmation  kalle
    Submit Registration
    Register Should Fail With Message  Invalid password. Password must have at least 8 characters and contain non-letter characters.

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password_Confirmation  321ellak
    Submit Registration
    Register Should Fail With Message  Password and password confirmation do not match.

Login After Successful Registration
    Set Username  palle
    Set Password  kalle123
    Set Password_Confirmation  kalle123
    Submit Registration
    Go To Main Page
    Click Button  Logout
    Set Username  palle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ralle
    Set Password  kalle123
    Set Password_Confirmation  321ellak
    Submit Registration
    Click Link  Login
    Set Username  ralle
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Registration
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}