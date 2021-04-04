import requests

url = "http://joefurfaro.ca:3000/api"

inp_str = "Choose mode (create (C), grab (G), view(V)) or E to exit: "
mode = input(inp_str)

while mode != "E":
	if mode == "C":
		title = input("Enter MiniEgg Title: ")
		response = requests.post(url+"/create", data={"title": title})
		if response.status_code == 200:
			print("MiniEgg created successfully!")

	if mode == "G":

		take = "n"
		cur = None
		while take != "y":
			response = requests.get(url+"/grab")
			if response.status_code == 404:
				print("No MiniEggs found!")
				take = "y"
			else:
				print()
				cur = response.json()["title"]
				print(f"You grabbed \"{cur}\"")
				take = input("Take this MiniEgg? (y/n)")
		
		if cur != None:
			response = requests.post(url+"/pick", data={"title": cur})
			if response.status_code == 200:
				print("MiniEgg grabbed!")
			else:
				print("Could take grab MiniEgg :(")

	if mode == "V":
		response = requests.get(url+"/count")
		print("Showing " + str(response.json()["count"]) + " MiniEggs:")
		response = requests.get(url+"/view")
		for thing in response.json()["minieggs"]:
			print("  - " + thing)

	print()
	mode = input(inp_str)
