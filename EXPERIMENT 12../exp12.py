n = int(input().strip())
phone_db = {}

for _ in range(n):
	command = input().strip().split()

	if command[0] == "ADD":
		name = command[1]
		phone = command[2]
		phone_db[name] = phone

	elif command[0] == "REMOVE":
		name = command[1]
		if name in phone_db:
			del phone_db[name]  

	elif command[0] == "DISPLAY":
		if not phone_db:
			print("No contacts")
		else:
			for name in sorted(phone_db):
				print(f"{name}: {phone_db[name]}")
