*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Invalid username. Username must have at least 3 lowercase letters.

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kall3  kalle123
    Output Should Contain  Invalid username. Username must have at least 3 lowercase letters.

Register With Valid Username And Too Short Password
    Input Credentials  kalle  alle123
    Output Should Contain  Invalid password. Password must have at least 8 characters and contain non-letter characters.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Invalid password. Password must have at least 8 characters and contain non-letter characters.
