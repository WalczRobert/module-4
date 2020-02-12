

class Testscores():
    def input(self):
        score1, score2, score3 = input("what are your 3 scores (comma separated): ").split(',')
        average(score1, score2, score3)


    def average(self, score1, score2, score3):
        NUMBER_TESTS = 3
        score = float((score1 + score2 + score3) / NUMBER_TESTS)
        try:
            if self.score1 < 0:
                raise ValueError('Invalid score value')
            if self.score2 < 0:
                raise ValueError('Invalid score value')
            if self.score3 < 0:
                raise ValueError('Invalid score value')
        except:
            print('except - Invalid score value')
        else:
            print (score)
            return score



if __name__ == '__main__':
    input()