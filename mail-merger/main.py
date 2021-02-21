with open("Input\\Letters\\starting_letter.txt") as letter:
    letter_lines = letter.readlines()

with open("Input\\Names\\invited_names.txt") as file:
    receivers = file.readlines()

for receiver in receivers:
    with open(f"Output\\Ready_to_send\\{receiver.strip()}.txt", "w") as send:
        for line in letter_lines:
            send.write(line.replace('[name]', f"{receiver.strip()}"))
