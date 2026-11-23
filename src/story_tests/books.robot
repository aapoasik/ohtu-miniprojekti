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

After editing a book citation, it is displayed on the front page
    Go To  ${HOME_URL}
    Click  text=Create new book citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="author"]  Jane Doe
    Fill Text  [name="title"]  Introduction to Programming
    Fill Text  [name="year"]  2024
    Fill Text  [name="publisher"]  Example Publishing
    Click  button >> text=Create
    Click  text=Edit
    Fill Text  [name="key"]  Updated key
    Fill Text  [name="author"]  Updated author
    Fill Text  [name="title"]  Updated title
    Fill Text  [name="year"]  2025
    Fill Text  [name="publisher"]  Updated publisher
    Click  button text=Save
    Get Text  body  *=  Updated title
    Get Text  body  *=  Updated author
    Get Text  body  *=  2025
    Get Text  body  *=  Updated publisher

After deleting a book citation, it is not displayed on the front page anymore
    Go To  ${HOME_URL}
    Click  text=Create new book citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="author"]  Jane Doe
    Fill Text  [name="title"]  Introduction to Programming
    Fill Text  [name="year"]  2024
    Fill Text  [name="publisher"]  Example Publishing
    Click  button >> text=Create
    Click  text=Delete
    Get Text  body  *=  Do you want to remove book citation?
    Click  input[name="continue"]
    ${page_text}=  Get Text  body
    Should Not Contain  ${page_text}  Introduction to Programming
