import csv

def csvTokens(libraryTokens):
    with open('tokens.csv', newline='') as csvfile:
        writer = csv.writer('tokens.csv')
        writer.writerows(libraryTokens)

def csvIdentifiertokens(libraryTokens):
    with open('tokensIdentifer.csv', newline='') as csvfile:
        writer = csv.writer('tokensIdentifier.csv')
        writer.writerows(libraryTokens)

def csvDigitTokens(libraryTokens):
    with open('tokensDigit.csv', newline='') as csvfile:
        writer = csv.writer('tokensIdentifier.csv')
        writer.writerows(libraryTokens)