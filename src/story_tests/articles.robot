
*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
After adding an article citation, it is displayed on the front page
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Smith2024
    Fill Text  [name="author"]  John Smith
    Fill Text  [name="title"]  Introduction to Artificial Intelligence
    Fill Text  [name="year"]  2024
    Fill Text  [name="journal"]  Journal of Computer Science
    Click  button >> text=Create
    Get Text  body  *=  Introduction to Artificial Intelligence
    Get Text  body  *=  John Smith
    Get Text  body  *=  2024
    Get Text  body  *=  Journal of Computer Science
