import requests as req
import json

def initialization(api_url):
    res = req.post(url = api_url, json = {
    "title": "Mouse Color Changer",
    "description": "Testing the Razer SDK",
    "author": {
        "name": "Mazbrew",
        "contact": "peteryeoh50@gmail.com"
    },
    "device_supported": ["mouse"],
    "category": "application"
    })

    URI = res.json()['uri']

    print("Initialization:\n\t" + repr(res.content) + "\n")

    return URI

def read_info(api_url):
    res= req.get(url = api_url)

    print("Info:\n\t" + repr(res.content) + "\n")

def effect_gen_turn_off(URI):
    res = req.post(url = URI + "/mouse", json ={
        "effect": "CHROMA_NONE"
    })

    print("Effect Generator:\n\t" + repr(res.content) + "\n")

    return res.json()["id"]

def apply_effect(URI,id):
    data = {}
    data['id'] = id
    json_data = json.dumps(data, separators=(',', ':'))

    print(json_data)

    #this one here is broken
    res = req.post(url = URI + "/effect" , json = json_data)

    print("Apply Effect:\n\t" + repr(res.content) +"\n")

def uninitialization(api_url):
    res = req.post(url = api_url, json = {
        "result" : 0
    })

if __name__ == "__main__":
    api_url = "http://localhost:54235/razer/chromasdk"
    URI = initialization(api_url)
    
    read_info(api_url)
    
    id = effect_gen_turn_off(URI)
    
    apply_effect(URI,id)



    


    