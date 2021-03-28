import requests

url = "http://localhost:3000/api"

inp_str = "Choose mode (create (C), grab (G), view(V)) or E to exit: "
mode = input(inp_str)

while mode != "E":
	if mode == "C":
		title = input("Enter MiniEgg Title: ")
		response = requests.post(url+"/create", data={"title": title})
		if response.status_code == 200:
			print("MiniEgg created successfully!")

	if mode == "G":
		response = requests.get(url+"/grab")
		if response.status_code == 404:
			print("No MiniEggs found!")
		else:
			print(response.json()["title"])

	if mode == "V":
		response = requests.get(url+"/count")
		print("Showing " + str(response.json()["count"]) + " MiniEggs:")
		response = requests.get(url+"/view")
		for thing in response.json()["minieggs"]:
			print("  - " + thing)

	print()
	mode = input(inp_str)
