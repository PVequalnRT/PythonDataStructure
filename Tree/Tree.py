import os #CLS 명령어 사용

#데이터 저장 가능한 Node 생성
#사용자로부터 data를 받아오고 다음 노드를 모두 None으로 초기화
class node:
    def __init__(self, data):
        self.data = data
        self.rightNode = None
        self.leftNode = None

#노드를 저장 및 관리하는 새로운 클래스 생성
class nodeSearch:
    #클래스 초기화 : ROOT 초기화
    def __init__(self):
        self.root = None
    #새로운 데이터 추가 함수
    def push(self, data):
        #트리에 저장된 값이 없을 때
        if self.root == None:
            self.root = node(data)
        #트리에 저장된 값이 있을 때
        else:
            temp = self.root
            #데이터 대소를 계속 비교해서 가장 아래단계 노드를 찾은 후
            #사용자로부터 입력받은 데이터를 삽입
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
    #가장 큰 값 찾아서 출력
    def biggestData(self):
        #재귀함수를 이용해 검색
        #계속 오른쪽 노드로 이동해서 가장 아랫단계 노드 찾기
        def searchRightNode(temp):
            if temp.rightNode == None:
                print("가장 큰 값 : %d"%temp.data)
            else:
                searchRightNode(temp.rightNode)
        #만약 저장된 값이 없으면 NO DATA! 출력
        if self.root == None:
            print("No Data!")
        else:
            searchRightNode(self.root)
    #가장 작은 값 찾아서 출력
    #가장 큰 값 찾는 함수와 동일
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
    #특정 데이터 존재여부 찾음
    def findData(self, target):
        temp = self.root
        #대소를 비교해서 저장되어있을 만한 위치로 찾아감
        while True:
            #만약 찾지 못하면 NO DATA! 리턴
            if temp == None:
                print("No Data!")
                return
            else:
                #데이터 존재 확인되면 print
                if temp.data == target:
                    print("데이터가 존재합니다.")
                    return
                else:
                    if temp.data > target:
                        temp = temp.leftNode
                    elif temp.data < target:
                        temp = temp.rightNode
    #데이터 내림차순 정렬
    def In_order_traversal(self):
        def _in_order_traversal(temp):
            if temp is None:
                pass
            else:
                _in_order_traversal(temp.rightNode)
                print(temp.data,end=',')
                _in_order_traversal(temp.leftNode)
        _in_order_traversal(self.root)
    #데이터 오름차순 정렬
    def In_order_traversal2(self):
        def _in_order_traversal(temp):
            if temp is None:
                pass
            else:
                _in_order_traversal(temp.leftNode)
                print(temp.data,end=',')
                _in_order_traversal(temp.rightNode)
        _in_order_traversal(self.root)

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
        root.In_order_traversal()
    elif menu == 6:
        root.In_order_traversal2()
    elif menu == 7:
        print("프로그램을 종료합니다.")
        break

    input("") #사용자로부터 enter 기다림
    os.system("cls") #화면 지우기