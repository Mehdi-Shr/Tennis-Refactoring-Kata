# -*- coding: utf-8 -*-

class TennisGame6Part2:
    # TODO: Vérifier que les noms des joueurs sont des chaînes de caractères non vides avant de les utiliser.
    def __init__(self, player1Name: str, player2Name: str):  # Typé les noms des joueurs
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    # TODO: Remplacer la condition par `if playerName == self.player1Name`.
    def won_point(self, playerName: str):
        if playerName == self.player1Name:
            self.player1Score += 1
        else:
            self.player2Score += 1

    def score(self) -> str:
        result: str

        if self.player1Score == self.player2Score:
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
        # TODO: Créer des constantes pour expliquer la signification des valeurs numériques magiques.
        elif self.player1Score >= 4 or self.player2Score >= 4:
            # end-game score
            endGameScore: str

            if self.player1Score - self.player2Score == 1:
                endGameScore = "Advantage " + self.player1Name
            elif self.player1Score - self.player2Score == -1:
                endGameScore = "Advantage " + self.player2Name
           
