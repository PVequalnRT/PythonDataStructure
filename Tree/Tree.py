class node:
    def __init__(self, data):
        self.data = data
        self.rightNode = None
        self.leftNode = None

class nodeSearch:
    def __init__(self):
        self.root = None
    def push(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            temp = self.root
            while True:
                if data > temp.data:
                    if temp.rightNode == None:
                        temp.rightNode = node(data)
                        break
                    else:
                        temp = temp.rightNode
                elif data < temp.data:
                    if temp.leftNode == None:
                        temp.leftNode = node(data)
                        break
                    else:
                        temp = temp.leftNode
    def biggestData(self):
        def searchRightNode(temp):
            if temp.rightNode == None:
                print("가장 큰 값 : %d"%temp.data)
            else:
                searchRightNode(temp.rightNode)
        if self.root == None:
            print("No Data!")
        else:
            searchRightNode(self.root)
    def leastData(self):
        def searchData(temp):
            if temp.leftNode == None:
                print("가장 작은 값 : %d" %temp.data)
            else:
                searchData(temp.leftNode)
        if self.root == None:
            print("No Data!")
        else:
            searchData(self.root)
    def findData(self, target):
        temp = self.root
        while True:
            if temp == None:
                print("No Data!")
                return
            else:
                if temp.data == target:
                    print("데이터가 존재합니다.")
                    return
                else:
                    if temp.data > target:
                        temp = temp.leftNode
                    elif temp.data < target:
                        temp = temp.rightNode

menuIndex = """1.데이터 추가
2.가장 큰 값 출력
3.가장 작은 값 출력
4.데이터 찾기
5.내림차순 전체출력
6.오름차순 전체출력
7.종료."""

root = nodeSearch()

while True:
    print(menuIndex)
    menu = int(input("\n메뉴를 선택해주세요 : "))

    if menu == 1:
        data = int(input("추가할 데이터 : "))
        root.push(data)
    elif menu == 2:
        root.biggestData()
    elif menu == 3:
        root.leastData()
    elif menu == 4:
        target = int(input("찾고자 하는 데이터를 입력해주세요 :"))
        root.findData(target)
    elif menu == 5:
        pass
    elif menu == 6:
        pass
    elif menu == 7:
        pass