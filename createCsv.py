import csv

def csvTokens(libraryTokens):
    with open('tokens.csv', 'w', newline='') as csvfile:
        fieldnames = ["Tokens"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for token_list in libraryTokens:
            for token in token_list:
                writer.writerow({"Tokens": token})

def csvIdentifiertokens(libraryTokens):
    with open('tokensIdentifier.csv','w', newline='') as csvfile:
        fieldnames = ["Entry", "Contents"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for token_list in libraryTokens:
            for token in token_list:
                writer.writerow({"Entry": token[0], "Contents": token[1]})


def csvDigitTokens(libraryTokens):
    with open('tokensDigit.csv', 'w', newline='') as csvfile:
        fieldnames = ["Entry", "Contents"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for token_list in libraryTokens:
            for token in token_list:
                writer.writerow({"Entry": token[0], "Contents": token[1]})