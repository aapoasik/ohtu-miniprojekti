*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
Adding an article with only spaces in the author field is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Smith2024
    Fill Text  [name="author"]  ${SPACE * 3}
    Fill Text  [name="title"]  Introduction to AI
    Fill Text  [name="year"]  2024
    Fill Text  [name="journal"]  Journal of Computer Science
    Click  button >> text=Create
    Get Text  body  *=  Must not contain only spaces

Adding an article with an invalid year is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Smith2024
    Fill Text  [name="author"]  John Smith
    Fill Text  [name="title"]  Introduction to AI
    Fill Text  [name="year"]  24
    Fill Text  [name="journal"]  Journal of Computer Science
    Click  button >> text=Create
    Get Text  body  *=  Enter only 4 digits

Adding an article with an invalid month is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Smith2024
    Fill Text  [name="author"]  John Smith
    Fill Text  [name="title"]  Introduction to AI
    Fill Text  [name="year"]  2024
    Fill Text  [name="journal"]  Journal of Computer Science
    Fill Text  [name="month"]  InvalidMonth
    Click  button >> text=Create
    Get Text  body  *=  Invalid month

Adding an article with an invalid volume is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Smith2024
    Fill Text  [name="author"]  John Smith
    Fill Text  [name="title"]  Introduction to AI
    Fill Text  [name="year"]  2024
    Fill Text  [name="journal"]  Journal of Computer Science
    Fill Text  [name="volume"]  abc
    Click  button >> text=Create
    Get Text  body  *=  Invalid volume

Adding an article with an invalid DOI is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Smith2024
    Fill Text  [name="author"]  John Smith
    Fill Text  [name="title"]  Introduction to AI
    Fill Text  [name="year"]  2024
    Fill Text  [name="journal"]  Journal of Computer Science
    Fill Text  [name="doi"]  invalid-doi
    Click  button >> text=Create
    Get Text  body  *=  invalid doi
