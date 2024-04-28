from tokens import *
class checkTokens():
    def readToken(self, word):

        program = programToken()
        real = realToken()
        repeat = repeatToken()
        procedure = procedureToken()
        string = stringToken()
        until = untilToken()
        function = functionToken()
        array = arrayToken()
        forT = forToken()
        begin = beginToken()
        of = ofToken()
        to = toToken()
        end = endToken()
        ifT = ifToken()
        do = doToken()
        var = varToken()
        then = thenToken()
        readLn = readLnToken()
        elseT = elseToken()
        writeLN = writeLNToken()
        integer = integerToken()

        #IDENTIFIER

        identifier = identifierToken()

        #SYMBOLS
        addition = additionToken()
        substraction = substractionToken()
        multiplication = multiplicationToken()
        division = divisionToken()
        lessThan = lessThanNToken()
        lessEqualThan = lessEqualThanLNToken()
        greaterThan = greaterEqualThanToken()
        greaterEqualThan = greaterEqualThanToken()
        equal = equalToken()
        logic = logicToken()
        assignation = assignationToken()
        colon = colonToken()
        semiColon = semiColonToken()
        coma = comaToken()
        singleQuote = singleQuoteToken()
        dot = dotToken()
        openParenthesis = openParenthesisToken()
        closeParenthesis = closeParenthesisToken()
        openSquareBrackets = openSquareBracketsToken()
        closeSquareBrackets = closeSquareBracketsToken()
        openSingleLineComment = openSingleLineCommentToken()
        closeSingleLineComment = closeSingleLineCommentToken()
        openMultiLineComment = openMultiLineCommentToken()
        closeMultiLineComment = closeMultiLineCommentToken()

        #Integer - Real
        integerConstant = integerConstantToken()

        #String
        stringT = stringToken()


        switch = {
            #Reserved Words
            "program": lambda: program.getToken(), #1
            "real": lambda: real.getToken(), #2
            "repeat": lambda: repeat.getToken(), #3
            "procedure": lambda: procedure.getToken(), #4
            "string": lambda: string.getToken(), #5
            "until": lambda: until.getToken(), #6
            "function": lambda: function.getToken(), #7
            "array": lambda: array.getToken(),#8
            "for": lambda: forT.getToken(), #9
            "begin": lambda: begin.getToken(), #10
            "of": lambda: of.getToken(), #11
            "to": lambda: to.getToken(), #12
            "end": lambda: end.getToken(), #13
            "if": lambda: ifT.getToken(), #14
            "do": lambda: do.getToken(), #15
            "var": lambda: var.getToken(), #16
            "then": lambda: then.getToken(), #17
            "readln": lambda: readLn.getToken(), #18
            "else": lambda: elseT.getToken(), #19
            "writeln": lambda: writeLN.getToken(), #20
            "integer": lambda: integer.getToken(), #21
            "identifier": lambda: identifier.getToken(), #22
            #Symbols
            "+": lambda: addition.getToken(), #23
            "-": lambda: substraction.getToken(), #24
            "*": lambda: multiplication.getToken(), #25
            "/": lambda: division.getToken(), #26
            "<": lambda: lessThan.getToken(), #27
            "<=": lambda: lessEqualThan.getToken(), #28
            ">": lambda: greaterThan.getToken(), #29
            ">=": lambda: greaterEqualThan.getToken(), #30
            "=": lambda: equal.getToken(), #31
            "<>": lambda: logic.getToken(), #32
            ":=": lambda: assignation.getToken(), #33
            ":": lambda: colon.getToken(), #34
            ";": lambda: semiColon.getToken(), #35
            ",": lambda: coma.getToken(), #36
            "'": lambda: singleQuote.getToken(), #37
            ".": lambda: dot.getToken(), #38
            "(": lambda: openParenthesis.getToken(), #39
            ")": lambda: closeParenthesis.getToken(), #40
            "[": lambda: openSquareBrackets.getToken(), #41
            "]": lambda: closeSquareBrackets.getToken(), #42
            "{": lambda: openSingleLineComment.getToken(), #43
            "}": lambda: closeSingleLineComment.getToken(), #44
            "(*": lambda: openMultiLineComment.getToken(), #45
            "*)": lambda: closeMultiLineComment.getToken(), #46
            "digit": lambda: integerConstant.getToken(), #47
            "string": lambda: stringT.getToken(), #48


        }


        return switch.get(word, switch["program"])()