#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import requests
def get_definition(term):
    url = "https://urban-dictionary7.p.rapidapi.com/v0/define"
    querystring = {"term":term}

    headers = {
        "x-rapidapi-key": "066b666a77msh9bb357e6cfa4065p14c7ebjsn35b1d1cfb89d",
        "x-rapidapi-host": "urban-dictionary7.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data=response.json()
    if data['list']:
            definition = data['list'][0]['definition']
            example = data['list'][0]['example']
            return definition, example
    else:
           print("No definition or example available. kindly enter a valid word!")
def main():
    print("Welcome to your own terminal Dictionary: ")
    print("Type 'exit' to quit the bot.")
    
    while True:
        term = input("\nEnter a term to look up: ")
        if term.lower() == 'exit':
            print("Goodbye!hope to see u next tym")
            break
        definition, example = get_definition(term)
        
        if definition:
            print(f"\nDefinition of '{term}':\n{definition}")
            print(f"\nExample:\n{example}")
        else:
            print(f"No definition found for '{term}'.")

if __name__ == "__main__":
    main()


# In[ ]:




