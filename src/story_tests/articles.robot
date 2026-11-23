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

After editing an article citation, it is displayed on the front page
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Smith2024
    Fill Text  [name="author"]  John Smith
    Fill Text  [name="title"]  Introduction to Artificial Intelligence
    Fill Text  [name="year"]  2024
    Fill Text  [name="journal"]  Journal of Computer Science
    Click  button >> text=Create
    Click  text=Edit
    Fill Text  [name="key"]  Updated key
    Fill Text  [name="author"]  Updated author
    Fill Text  [name="title"]  Updated title
    Fill Text  [name="year"]  Updated year
    Fill Text  [name="journal"]  Updated journal
    Click  button >> text=Save
    Get Text  body  *=  Updated title
    Get Text  body  *=  Updated author
    Get Text  body  *=  Updated year
    Get Text  body  *=  Updated journal

After deleting an article citation, it is not displayed on the front page anymore
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Smith2024
    Fill Text  [name="author"]  John Smith
    Fill Text  [name="title"]  Introduction to Artificial Intelligence
    Fill Text  [name="year"]  2024
    Fill Text  [name="journal"]  Journal of Computer Science
    Click  button >> text=Create
    Click  text=Delete
    Get Text  body  *=  Do you want to remove article citation?
    Click  input[name="continue"]
    ${page_text}=  Get Text  body
    Should Not Contain  ${page_text}  Introduction to Artificial Intelligence
