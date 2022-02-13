from datetime import datetime
import os

# 직원의 출근 시간을 체크해주는 메서드
# 서버로 리턴 해줄 예정(JSON 형태로 딕셔너리로)
# empnoList는 사원정보 리스트, min_score_name는 확인된 직원번호
def empAttTimeCheck(empnoList, min_score_name):
    print('############empAttTimeCheck start########')
    print('empnoList, min_score_name : ', empnoList, min_score_name)
    # 사원 출근 체크 후 key값은 사원번호로, 벨류는 시간으로 주기 위한 딕셔너리 생성
    empAttTimeDict = dict()
    # 날짜 형식 지정 지금 날짜와 시간
    today = datetime.today().strftime('%Y_%m_%d_%H:%M:%S')
    # empAttList에 empno가 있는지 확인하고 있으면
    if min_score_name in empnoList:
        print('진입 등록된 직원임')
        # 등록된 직원정보와 같은 사원번호가 있다면
        empAttTimeDict[min_score_name] = today
    else:
        print('등록된 사원번호가 아님')

    return empAttTimeDict

# 동영상에서 사람 인식하면 시간을 체크하여 log에 저장
# 나는 관리자를 위해 엑셈아닌 엑셀에 저장 할꺼야]
def makeCsv():
    # 로그파일에 오늘 날자를 기록하기 위한 변수
    today = datetime.today().strftime('%Y_%m_%d')
    # 로그파일 저장 이름을 위한 변수
    fileName = "Attendance_" + today + ".csv"
    # 로그 파일 생성 만약 해당 경로에 이미 설정되어 있으면 패쓰
    if os.path.isfile(fileName):
        print("이미 파일이 있슮")
        pass
    else:
        fileW = open(fileName, 'w')
    # 이상없이 파일이 생성되었으면 파일 이름을 리턴해라
    return fileName

def checkAttendance(name, fileName):
# csv 파일을 읽어오는 r+는 읽을 거라는 뜻 별명은 f
    with open(fileName, 'r+') as f:

        myDataList = f.readlines()
        nameList = []

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            print("출석체크 : ", name)


