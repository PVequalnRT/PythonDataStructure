class stackNode:
    def __init__(self,data):
        self.data = data
        self.downNode = None

class searchNode:
    def __init__(self):
        self.top = None
    def push(self, data):
        if self.top == None:
            self.top = stackNode(data)
        else:
            temp = stackNode(data)
            temp.downNode = self.top
            self.top = temp
    def pop(self):
        if self.top == None:
            return "No Data!"
        else:
            temp = self.top
            self.top = temp.downNode
            return temp.data

#Menu
node = searchNode()

while True:
    print("""1. 데이터 추가
2. 데이터 삭제
3. 데이터 전체 출력
4. 종료""")
    menu = int(input("메뉴를 선택해주세요 :"))

    if menu == 1:
        data = int(input("데이터를 입력해주세요 :"))
        node.push(data)
        print("데이터 입력 성공!", end="\n\n\n")

    elif menu == 2:
        result = node.pop()
        if result == "No Data!":
            print(result, end="\n\n\n")
        else:
            print("삭제된 데이터 : {0}".format(result), end="\n\n\n")
    elif menu == 3:
        pass
    elif menu == 4:
        pass
