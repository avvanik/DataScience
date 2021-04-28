class Dice:

    def rollDice():
        self.value = random.randint(1, 6)

    def reset():
        self.value=0

    def getValue():
        return value
    
class DiceCup:

    dices = [Dice() for i in range(5)]

    def __init__():
        currRounds = 0
        initDices()

    def initDices():
        for i in dices:
            dices[i] = Dice()

    def rollAll():
        currRounds = 0
        for i in dices:
            dice.rollDice()

    def rollIndex(index):
        dices[index].rollDice()

    def incRounds():
        currRounds +=1

    def getRounds():
        return currRounds

    def resetRounds():
        currRounds = 0

    def resetDices():
        for i in dices:
            dice.reset()

class Scores:

    yDiceCup = DiceCup()

    def initializePoints():
        points = [ones, fives, sixes]

    def calculatePoints(dices):
        for i in dices:
            if dices[i].getValue() == 1:
                ones +=1
            if dices[i].getValue() == 5:
                fives +=5
            if dices[i].getValue() == 6:
                sixes +=6

    def resetPoints():
        ones=0
        fives=0
        sixes=0

class Gameboard:

    yView = View () #Gui Class

    def __init__(Gui):
        yView = view

    yDiceCup = DiceCup()
    yScores = Scores()

    def roll():
        yDiceCup.incRounds()
        resetButtons()

        switcher = yDiceCup.getRounds() {

            0:
                yDiceCup.rollAll()
                setDiceColumn()
                break
            1:
                pickDice()
                setDiceColumn()
                break
            2:
                pickDice()
                setDiceColumn()
                break
            3:
                pickDice()
                setDiceColumn()
                yView.rollButton.setDisable(true)
                yDiceCup.resetDices()
                yDiceCup.resetRounds()
                break
            }

    def takePoints(#ActionEvent):
        handleNextRound()
        if event.getSource() == yView.onesButton:
           handlePoints(yView.onesButton, yScores.ones, yView.onesField)

        if event.getSource() == yView.fivesButton:
           handlePoints(yView.fivesButton, yScores.fives, yView.fivesField)

        if event.getSource() == yView.sixesButton:
            handlePoints(yView.sixesButton, yScores.sixes, yView.sixesField)

        if event.getSource() == yView.totalButton:
            yView.rollButton.setDisable(true)
            yView.totalField.setText(" " + yScores.calculateTotal())


    def setDiceColumn():
        for i in yView.dicelabes:
            yView.dicelabels[i].setText(" " + yDiceCup.dices[i].getValue())

        yScores.resetPoints()
        yScores.calculatePoints(yDiceCup.dices)

        for i in yView.pointlabels:
            yScores.initializePoints()
            yView.pointlabels[i].setText(" " + yScores.points[i])


    def pickDice():
        for i in yView.checkboxes:
            if !yView.checkboxes[i].isSelected():
                yDiceCup.rollIndex(i)
                yView.dicelabels[i].setText(" " + yDiceCup.dices[i].getValue())


    resultlist = []

    def handlePoints(pointsbutton, points, pointsfields, resultlist):
        pointbuttons.setDisable(true)
        pointsfields.setText(" " + points)
        yScores.resultlist.add(points)
        yView.rollButton.setDisable(false)

    def handleNextRound():
        resetBoxes()
        resetLabels()
        yDiceCup.resetDices()
        yDiceCup.resetRounds()

    def playAgain():
        yView.initializeControls()
        yView.rollButton.setDisable(false)
        yDiceCup.resetRounds()
        yScores.resetPoints()
        resetButtons()
        resetFields()
        resetLabes()
        resetBoxes()
        yDiceCup.resetDices()


    def resetLabels():
        for i in yView.pointlabels:
            yView.pointlabels[i].setText(" ")
        for i in yView.dicelabels:
            yView.dicelabels[i].setText(" ")

    def resetFields():
        for i in yView.pointsfields:
            yView.pointsfields[i].setText(" ")

    def resetBoxes():
        for i in yView.checkboxes:
            yView.checkboxes[i].setSelected(false)

    def resetButtons():
        for i in yView.pointbuttons:
            yView.pointbuttons[i].setDisable(false)
        

        

 

    

        
            

        
        
    

    
             











