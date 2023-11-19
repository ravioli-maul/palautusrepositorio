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
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password_Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Invalid username. Username must have at least 3 lowercase letters

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalle
    Set Password_Confirmation  kalle
    Submit Credentials
    Register Should Fail With Message  Invalid password. Password must have at least 8 characters and contain non-letter characters.

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password_Confirmation  321ellak
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match.

*** Keywords ***
Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}