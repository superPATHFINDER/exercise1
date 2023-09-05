def count_terrible_occurrences(text):
    return text.lower().count("terrible")

def replace_terrible(text):
    words = text.split()
    for i in range(len(words)):
        if words[i].lower() == "terrible":
            if i % 2 == 0:
                words[i] = "pathetic"
            else:
                words[i] = "marvellous"
    return ' '.join(words)

with open("file_to_read.txt", "r") as file:
    file_content = file.read()

terrible_count = count_terrible_occurrences(file_content)
print(f"Total occurrences of 'terrible': {terrible_count}")

new_content = replace_terrible(file_content)

with open("result.txt", "w") as result_file:
    result_file.write(new_content)

print("Replacement completed. New content written to 'result.txt'.")
