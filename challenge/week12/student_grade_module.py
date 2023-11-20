from student import Student

def loadData(lines):
    score = []
    for i in range(1,len(lines)):
        line = lines[i].replace("\n","").split(',')
        std_ins = Student(line[0],float(line[1]),float(line[2]),float(line[3]))
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
fp.write("-----학생들의 평균 점수-----\n")
for i in score:
    fp.write(f"{i.name}의 평균 점수는 {i.get_average()}입니다.\n")
fp.close()