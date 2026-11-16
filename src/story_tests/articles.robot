*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
After adding an article citation, it is displayed on the front page
    Go To  ${HOME_URL}
    Click  text=Create new article citation
    Fill Text  [name="key"]  Doe2024
    Fill Text  [name="author"]  Dave Mbiazi, Meghana Bhange, Maryam Babaei, Ivaxi Sheth, Patrik Kenfack, Samira Ebrahimi Kahou
    Fill Text  [name="title"]  Survey on AI Ethics: A Socio-Technical Perspective
    Fill Text  [name="year"]  2025
    Fill Text  [name="journal"]  Computational Intelligence
    Fill Text  [name="pages"]  e70149
    Fill Text  [name="volume"]  41
    Fill Text  [name="month"]  November
    Fill Text  [name="doi"]  10.1111/coin.70149
    Click  button >> text=Create
    Get Text  body  *=  Survey on AI Ethics: A Socio-Technical Perspective
    Get Text  body  *=  Dave Mbiazi, Meghana Bhange, Maryam Babaei, Ivaxi Sheth, Patrik Kenfack, Samira Ebrahimi Kahou
    Get Text  body  *=  2025
    Get Text  body  *=  Computational Intelligence
    Get Text  body  *=  e70149
    Get Text  body  *=  41
    Get Text  body  *=  November
    Get Text  body  *=  10.1111/coin.70149