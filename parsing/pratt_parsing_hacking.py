#!/bin/env python3
from dataclasses import dataclass
from enum import Enum, IntEnum
from pprint import pformat, pprint 
from pathlib import Path


class TokenType(Enum):
    Number = 0
    Name = 1
    Bang = "!"
    Equal = "=="
    LT = "<"
    GT = ">"
    Plus = "+"
    Minus = "-"
    Slash = "/"
    Asterix = "*"


@dataclass
class Integer:
    token: TokenType.Number
    value: str


@dataclass
class Token:
    t_type: TokenType
    text: str


@dataclass
class Expression:
    Token: Token


@dataclass
class PrefixExpression:
    token: TokenType
    operator: str
    right: Expression


@dataclass
class InfixExpression:
    token: TokenType
    left: Expression
    operator: str
    right: Expression


class Precedence(IntEnum):
    Lowest = 0
    Equals = 1
    LessGreater = 2
    Sum = 3
    Product = 4
    Prefix = 5
    Call = 6


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.peek_token = tokens[0]
        self.cur_token = self.peek_token 
        self.peek_token = tokens[1]
        self.index = 1 
        self.prefix_parsers = {
            TokenType.Number: self.parse_integer,
            # TokenType.Name: self.parse_name,
            TokenType.Bang: self.parse_prefix_expression,
            TokenType.Minus: self.parse_prefix_expression,
        }
        self.debug = []
        self.infix_parsers = {TokenType.Plus: self.parse_infix_expression, TokenType.Asterix: self.parse_infix_expression}
        self.precedence = {
            TokenType.Equal: Precedence.Equals,
            TokenType.LT: Precedence.LessGreater,
            TokenType.GT: Precedence.LessGreater,
            TokenType.Plus: Precedence.Sum,
            TokenType.Minus: Precedence.Sum,
            TokenType.Slash: Precedence.Product,
            TokenType.Asterix: Precedence.Product,
        }

    def next_token(self):
        self.cur_token = self.peek_token
        if self.index + 1 < len(self.tokens):
            self.index +=1
            self.peek_token = self.tokens[self.index]
            return self.tokens[self.index]
        self.peek_token = None
        return None

    def parse_prefix_expression(self):
        expression = PrefixExpression(self.cur_token.t_type, self.cur_token.text)

        self.next_token()

        expression.right = self.parse_expression(self.precedence_map[Precedence.Prefix])

        return expression

    def parse_integer(self):
        return Integer(self.cur_token.t_type, self.cur_token.text)

    def parse_infix_expression(self, left):

        expression = InfixExpression(self.cur_token.t_type.value,  left, self.cur_token.text, None)
        prev_precedence = self.precedence[self.cur_token.t_type]
        print('before')
        print(self.cur_token)
        self.next_token()
        print('after')
        print(self.cur_token)
        expression.right = self.parse_expression(prev_precedence)
        return expression

    def peek_token(self):
        return self.tokens[self.index + 1].type

    def peek_precedence(self):
        print('peek token')
        print(self.peek_token.t_type)
        if self.peek_token.t_type in self.precedence:
            print(self.precedence[self.peek_token.t_type])
            return self.precedence[self.peek_token.t_type]
        return Precedence.Lowest 
    def parse_expression(self, prev_precedence):
        prefix = self.prefix_parsers[self.cur_token.t_type]  # a: Int
        print('[DEBUG] parse_expression')
        print(prefix, prev_precedence)
        left_expression = prefix()  # int expressio INTEGER(Number, b)

        while self.peek_token is not None and prev_precedence < self.peek_precedence():
            infix = self.infix_parsers[self.peek_token.t_type]
            print('[DEBUG] while loop')
            print(infix)
            if not infix:
                self.debug.append(left_expression)
                return left_expression

            self.next_token()

            left_expression = infix(left_expression)  # cur = +, prev = a
            print('[DEBUG] returned left_expression')
            print(left_expression)
        self.debug.append(left_expression)
        return left_expression


def main():

    tokens = [
        Token(TokenType.Number, "1"),
        Token(TokenType.Plus, "+"),
        Token(TokenType.Number, "2"),
        Token(TokenType.Asterix, "*"),
        Token(TokenType.Number, "3"),
        Token(TokenType.Asterix, "*"),
        Token(TokenType.Number, "4"),
    ]

    p = Parser(tokens)

    res = p.parse_expression(Precedence.Lowest)
    print(res)
    Path('./debug').write_text(pformat(res, indent=4))
    for i in p.debug:
        print('hi')
        print(i)


if __name__ == "__main__":
    main()
