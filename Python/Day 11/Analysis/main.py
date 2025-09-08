def main():
    print("Hello, Andmetarkus 2025!")

# Siia hakkame lisama koodi, millega testime loodud funktsioone.


with open("request-log.txt", encoding='utf-8') as f:
    filecontent = f.read()
print(filecontent)

request_log_entries = filecontent.split("\n")


for line in request_log_entries:
    print(line + "\n")


if __name__ == "__main__":
    main()
