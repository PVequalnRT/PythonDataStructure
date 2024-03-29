class queueNode:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class searchNode:
    def __init__(self):
        self.firstNode = None
    def push(self, data):
        if self.firstNode == None:
            self.firstNode = queueNode(data)
        else:
            temp = self.firstNode
            while temp.nextNode != None:
                temp = temp.nextNode
            temp.nextNode = queueNode(data)
    def pop(self):
        if self.firstNode == None:
            return "No Data!"
        data = self.firstNode.data
        self.firstNode = self.firstNode.nextNode
        return data
    def popAll(self):
        while self.firstNode != None:
            self.pop()
        print("데이터 전체 삭제 완료!")

selectMenu = """1.데이터 추가
2.데이터 삭제
3.데이터 전체 출력
4.프로그램 종료
"""

node = searchNode()
while True:
    print(selectMenu)
    menu = int(input("메뉴를 선택해주세요 : "))
    if menu == 1:
        data = int(input("\n\n데이터를 입력해주세요 : "))
        node.push(data)
        print("\n\n")
    elif menu == 2:
        print("삭제 데이터 : {0}\n".format(node.pop()))
    elif menu == 3:
        node.popAll()
    elif menu == 4:
        print("프로그램을 종료합니다.")
        break