class gameOfLife:

    def __init__(self,row, col):
        self.rows = row
        self.cols = col
        self.Array = [[0 for j in range(self.cols)] for i in range(self.rows)]
                
    def showGrid(self):
        for i in range(len(self.Array)):
            for j in range(len(self.Array[0])):
                print(self.Array[i][j], end=" ")
            print()

    def config(self,mylist):
        length = len(mylist)
        for i in range(length):
            assert 0 <= mylist[i][0] < self.rows and 0 <= mylist[i][1] < self.cols, "invalid Index!"
            self.Array[mylist[i][0]][mylist[i][1]] = 1 
                
    def checking(self):
        newMat = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                live = 0
                positions = [(i+1, j),(i+1,j-1),(i+1,j+1),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j),(i-1,j+1)]
                length = len(positions)
                for k in range(length):
                    if 0 <= positions[k][0] < self.rows and 0 <= positions[k][1] < self.cols:
                        if self.Array[positions[k][0]][positions[k][1]] == 1:
                            live += 1
                if 2 <= live <= 3 and self.Array[i][j] == 1:
                    row.append(1)
                elif live == 3 and self.Array[i][j] == 0:
                    row.append(1)
                else:
                    row.append(0)
            newMat.append(row)
        self.Array = newMat


