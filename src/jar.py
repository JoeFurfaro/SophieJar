import requests

url = "http://joefurfaro.ca:3000/api"

inp_str = "Choose mode (create (c), grab (g), view (v), finished (f)) or e to exit: "
mode = input(inp_str)

while mode != "e":
	if mode == "c":
		title = input("Enter MiniEgg Title: ")
		response = requests.post(url+"/create", data={"title": title})
		if response.status_code == 200:
			print("MiniEgg created successfully!")

	if mode == "g":

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

	if mode == "v":
		response = requests.get(url+"/count")
		print("Showing " + str(response.json()["jar"]) + " MiniEggs:")
		response = requests.get(url+"/view")
		for thing in response.json()["minieggs"]:
			print("  - " + thing)
	
	if mode == "f":
		response = requests.get(url+"/count")
		print("Showing " + str(response.json()["finished"]) + " Past-Picked MiniEggs:")
		response = requests.get(url+"/view")
		for thing in response.json()["finished"]:
			print("  - " + thing)

	print()
	mode = input(inp_str)
