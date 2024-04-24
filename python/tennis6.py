# -*- coding: utf-8 -*-

class TennisGame6:
    # 1) Les noms des joueurs devraient être des chaînes de caractères
    # Problème : Les noms des joueurs peuvent être de tout type, ce qui peut causer des erreurs imprévues.
    # Recommandation : Vérifier que les noms des joueurs sont des chaînes de caractères non vides avant de les utiliser. typé les noms des joueurs
    def __init__(self, player1Name, player2Name):
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    # 2) Simplification de la condition (amélioration de la lisibilité)
    # Problème : La condition `playerName == "player1"` est redondante et peut être simplifiée.
    # Recommandation : Remplacer la condition par `if playerName == self.player1Name`.
    def won_point(self, playerName):
        if (playerName == "player1"):
            self.player1Score += 1
        else:
            self.player2Score += 1


    # 3) Noms de variables descriptifs
    # Problème : Les noms de variables `endGameScore` et `regularScore` ne sont pas assez descriptifs.
    # Recommandation : Utiliser des noms de variables plus explicites, tels que `finalScore` et `regularScore`.
    def score(self):
        result: str

        if (self.player1Score == self.player2Score):
            # tie score
            tieScore: str
            match self.player1Score:
                case 0:
                    tieScore = "Love-All"
                case 1:
                    tieScore = "Fifteen-All"
                case 2:
                    tieScore = "Thirty-All"
                case _:
                    tieScore = "Deuce"

            result = tieScore
        # 4) Constante à réaliser et expliqué
        # Problème : Pourquoi le nombre 4 ?
        # Recommandation : Creer des constantes.
        elif (self.player1Score >= 4 or self.player2Score >= 4):
            # end-game score
            endGameScore: str

            if (self.player1Score - self.player2Score == 1):
                endGameScore = "Advantage " + self.player1Name
            elif (self.player1Score - self.player2Score == -1):
                endGameScore = "Advantage " + self.player2Name
            elif (self.player1Score - self.player2Score >= 2):
                endGameScore = "Win for " + self.player1Name
            else:
                endGameScore = "Win for " + self.player2Name

            result = endGameScore
        else:
            # regular score
            regularScore: str

            # 5) L'usage de match-case n'est pas cohérent avec le reste du code Python
            # son usage ici peut rendre le code moins compréhensible pour ceux qui ne sont pas familiers avec cette syntaxe.
            # regular score

            match (self.player1Score):
                case 0:
                    score1 = "Love"
                case 1:
                    score1 = "Fifteen"
                case 2:
                    score1 = "Thirty"
                case _:
                    score1 = "Forty"

            match (self.player2Score):
                case 0:
                    score2 = "Love"
                case 1:
                    score2 = "Fifteen"
                case 2:
                    score2 = "Thirty"
                case _:
                    score2 = "Forty"

            regularScore = score1 + "-" + score2

            result = regularScore

        return result