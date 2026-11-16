*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
Adding a book citation without a key is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new book citation
    Fill Text  [name="author"]  Jane Doe
    Fill Text  [name="title"]  Introduction to Programming
    Fill Text  [name="year"]  2024
    Fill Text  [name="publisher"]  Example Publishing
    Click  button >> text=Create
    Get Text  body  *=  Please fill in all required fields

Adding a book citation without an author is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new book citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="title"]  Introduction to Programming
    Fill Text  [name="year"]  2024
    Fill Text  [name="publisher"]  Example Publishing
    Click  button >> text=Create
    Get Text  body  *=  Please fill in all required fields

Adding a book citation without a title is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new book citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="author"]  Jane Doe
    Fill Text  [name="year"]  2024
    Fill Text  [name="publisher"]  Example Publishing
    Click  button >> text=Create
    Get Text  body  *=  Please fill in all required fields

Adding a book citation without a year is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new book citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="author"]  Jane Doe
    Fill Text  [name="title"]  Introduction to Programming
    Fill Text  [name="publisher"]  Example Publishing
    Click  button >> text=Create
    Get Text  body  *=  Please fill in all required fields

Adding a book citation without a publisher is not allowed
    Go To  ${HOME_URL}
    Click  text=Create new citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="author"]  Jane Doe
    Fill Text  [name="title"]  Introduction to Programming
    Fill Text  [name="year"]  2024
    Click  button >> text=Create
    Get Text  body  *=  Please fill in all required fields

Adding a book citation without an address is allowed
    Go To  ${HOME_URL}
    Click  text=Create new book citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="author"]  Jane Doe
    Fill Text  [name="title"]  Introduction to Programming
    Fill Text  [name="year"]  2024
    Fill Text  [name="publisher"]  Example Publishing
    Click  button >> text=Create
    Get Text  body  *=  Introduction to Programming

