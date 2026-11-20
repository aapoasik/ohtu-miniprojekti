*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
After adding a book citation, it is displayed on the front page
    Go To  ${HOME_URL}
    Click  text=Create new book citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="author"]  Jane Doe
    Fill Text  [name="title"]  Introduction to Programming
    Fill Text  [name="year"]  2024
    Fill Text  [name="publisher"]  Example Publishing
    Click  button >> text=Create
    Get Text  body  *=  Introduction to Programming
    Get Text  body  *=  Jane Doe
    Get Text  body  *=  2024
    Get Text  body  *=  Example Publishing
