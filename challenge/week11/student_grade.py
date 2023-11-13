class Student:
    name = ""
    korean = 0.0
    math = 0.0
    english = 0.0
    def get_average(self):
        return (self.korean + self.math + self.english)/3

def loadData(lines):
    score = []
    for i in range(1,len(lines)):
        std_ins = Student()
        line = lines[i].replace("\n","").split(',')
        std_ins.name = line[0]
        std_ins.korean =float(line[1])
        std_ins.math = float(line[2])
        std_ins.english = float(line[3])
        score.append(std_ins)
    return score
def getAverage(score):
    print("-----학생들의 평균 점수-----")
    for i in score:
        print(f"{i.name}의 평균 점수는 {i.get_average()}입니다.")

lines = open("students.csv","r", encoding="utf8").readlines()
subject = lines[0].split(',')

# # TODO 1: 학생 정보를 딕셔너리에 저장
score = loadData(lines)
# # TODO 2: 학생 별 평균 점수를 계산

getAverage(score)

# TODO 3: 평균 점수를 코드 실행결과와 동일하게 파일로 출력 (average.txt)
fp = open("average.txt", "w", encoding="utf8")
fp.write("-----학생들의 평균 점수-----")
for i in score:
    fp.write(f"{i.name}의 평균 점수는 {i.get_average()}입니다.\n")
fp.close()