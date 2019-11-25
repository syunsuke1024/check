from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'check1.html')

def check2(request):
    nyuryoku=request.POST['nyuryoku']
    S=list(nyuryoku.split())
    SL = []
    for i in range(len(S)):
        if S[i] != "":
            SL.append(S[i])
    # 日ごとに分解
    # /が入っているのは日付だけなので、/で日付データを検出
    SD = []
    s = []
    for i in range((len(SL))):
        if "/" in SL[i]:
            SD.append(s)
            s = [SL[i]]
        else:
            s.append(SL[i])
    SD.append(s)
    # print(SD)
    # print("-"*10)

    L = []
    l = ["" for _ in range(20)]
    week = ["日", "月", "火", "水", "木", "金", "土"]
    for i in range(32):
        if i == len(SD):
            break
        for j in range(100):
            if j == len(SD[i]):
                L.append(l)
                l = ["" for _ in range(20)]
                break
            if j == 0:
                l[0] = SD[i][0]
            if j == 1:
                if "[" in SD[i][j]:
                    pass
                    # l[1]=SD[i][1]
                # else:
                # l[1]=" "
            if j == 1 or j == 2:
                if SD[i][j] in week:
                    l[1] = SD[i][j]
            if j == 2 or j == 3:
                if SD[i][j] == "出勤":
                    l[2] = "出勤"
                elif "休" in SD[i][j]:
                    l[2] = SD[i][j]
            if l[2] == "出勤":
                if j == 3 or j == 4:
                    if "時" in SD[i][j]:
                        l[3] = SD[i][j]
            if "時" in l[3]:
                if (j == 4 and l[5] == "") or (j == 5 and l[5] == ""):
                    if "時" in SD[i][j]:
                        l[4] = SD[i][j]
                        li = []
                        cnt = 0
                        for k in range(j + 1, len(SD[i])):
                            if ":" in SD[i][k]:
                                li.append(SD[i][k])
                                cnt += 1
                            if "時" in SD[i][k]:
                                break
                        # print(li,cnt)
                        cnt2 = 0
                        for k in range((cnt * 2) // 3):
                            l[5 + k] = li[k]
                            cnt2 += 1
                        for k in range((cnt * 2) // 3, cnt):
                            l[13 + k - cnt2] = li[k]
                        if int(l[3][3:5]) % 15 == 0 and int(l[4][3:5]) % 15 == 0:
                            l[17] = "success"
                        else:
                            l[17] = "danger"

    L[0] = ["日付", "曜日", "出勤?", "開始", "終了", "休1始", "休1終", "休2始", "休2終", "休3始", "休3終", "休4始", "休4終", "休1計", "休2計", "休3計",
            "休4計","15分","6h","8h"]


    DATA = [["" for j in range(20)] for i in range(32)]

    for i in range(len(L)):
        for j in range(len(L[i])):
            DATA[i][j] = L[i][j]

    # print("-" * 20)
    Dic = {}

    d = [{} for i in range(32)]
    # print(d)
    for i in range(32):
        for j in range(len(DATA[i])):
            d[i][j] = DATA[i][j]
    # print(d)
    for i in range(32):
        Dic[i] = d[i]
    # print(D)
    Kansan = [["" for j in range(10)] for i in range(32)]
    for i in range(1, 32):
        if Dic[i][3] != "":
            Kansan[i] = [0, 0, 1440, 1440, 1440, 1440, 0, 0, 0, 0]
        if Dic[i][3] != "":
            Kansan[i][0] = int(Dic[i][3][:2]) * 60 + int(Dic[i][3][3:5])
        if Dic[i][4] != "":
            Kansan[i][1] = int(Dic[i][4][:2]) * 60 + int(Dic[i][4][3:5])
        if Dic[i][5] != "":
            Kansan[i][2] = int(Dic[i][5][:2]) * 60 + int(Dic[i][5][3:5])
        if Dic[i][7] != "":
            Kansan[i][3] = int(Dic[i][7][:2]) * 60 + int(Dic[i][7][3:5])
        if Dic[i][9] != "":
            Kansan[i][4] = int(Dic[i][9][:2]) * 60 + int(Dic[i][9][3:5])
        if Dic[i][11] != "":
            Kansan[i][5] = int(Dic[i][11][:2]) * 60 + int(Dic[i][11][3:5])
        if Dic[i][13] != "":
            Kansan[i][6] = int(Dic[i][13][0]) * 60 + int(Dic[i][13][2:])
        if Dic[i][14] != "":
            Kansan[i][7] = int(Dic[i][14][0]) * 60 + int(Dic[i][14][2:])
        if Dic[i][15] != "":
            Kansan[i][8] = int(Dic[i][15][0]) * 60 + int(Dic[i][15][2:])
        if Dic[i][16] != "":
            Kansan[i][9] = int(Dic[i][16][0]) * 60 + int(Dic[i][16][2:])
    for i in range(1, 32):
        if Kansan[i][0] != "":
            if Kansan[i][1] - Kansan[i][0] > 6 * 60:
                kyukei = 0
                for j in range(2, 6):
                    if Kansan[i][j] <= Kansan[i][0] + 360:
                        kyukei += Kansan[i][j + 4]
                if kyukei >= 45:
                    Dic[i][18] = "success"
                else:
                    Dic[i][18] = "danger"
            else:
                Dic[i][18] = "success"
    for i in range(1, 32):
        if Kansan[i][0] != "":
            if Kansan[i][1] - Kansan[i][0] > 8 * 60 +45:
                kyukei = 0
                for j in range(2, 6):
                    if Kansan[i][j] <= Kansan[i][0] + 525:
                        kyukei += Kansan[i][j + 4]
                if kyukei >= 60:
                    Dic[i][19] = "success"
                else:
                    Dic[i][19] = "danger"
            else:
                Dic[i][19] = "success"
    context={}
    context["Dic"]=Dic
    return render(request,'check2.html',context)