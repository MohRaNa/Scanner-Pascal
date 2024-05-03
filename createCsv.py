import csv


# CREA UN CSV DE LA LIBRERIA DE LOS TOKENS
def csvTokens(libraryTokens):
    with open('tokens.csv', 'w', newline='') as csvfile:
        fieldnames = ["Tokens"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for token_list in libraryTokens:
            for token in token_list:
                writer.writerow({"Tokens": token})

# CREA UN CSV DE LA LIBERIA DE LOS TOKENS DE IDENTIFICADORES LLAMADA tokensIdentifier.csv
def csvIdentifiertokens(libraryTokens):
    with open('tokensIdentifier.csv','w', newline='') as csvfile:
        fieldnames = ["Entry", "Contents"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for token_list in libraryTokens:
            for token in token_list:
                writer.writerow({"Entry": token[0], "Contents": token[1]})

# CREA UN CSV DE LA LIBRERIA DE TOKENS DE DIGITOS LLAMADA 'tokensDigit.csv'
def csvDigitTokens(libraryTokens):
    with open('tokensDigit.csv', 'w', newline='') as csvfile:
        fieldnames = ["Entry", "Contents"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for token_list in libraryTokens:
            for token in token_list:
                writer.writerow({"Entry": token[0], "Contents": token[1]})