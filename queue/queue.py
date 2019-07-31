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
    elif menu == 2:
        pass
        #node.pop()
    elif menu == 3:
        pass
        #node.popAll()
    elif menu == 4:
        print("프로그램을 종료합니다.")
        break