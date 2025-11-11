*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  sami  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  uusi_salasana3
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kajnsalasana2
    Output Should Contain  Username should be at least 3 char and password should be at least 8 char

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ka8  kaansalasana!
    Output Should Contain  Username should contain only letters a-ö


Register With Valid Username And Too Short Password
    Input Credentials  kaj  moi
    Output Should Contain  Username should be at least 3 char and password should be at least 8 char

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sampsa  sampsansalasana
    Output Should Contain  Password should include at least one special char ex. number or symbol


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  salainensalasana123
