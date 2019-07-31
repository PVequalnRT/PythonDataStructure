class queueNode:
    def __init__(self):
        self.data = None
        self.nextNode = None

class searchNode:
    def __init__(self):
        pass

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
        node.push(data)
    elif menu == 2:
        node.pop()
    elif menu == 3:
        node.popAll()
    elif menu == 4:
        print("프로그램을 종료합니다.")
        break
        