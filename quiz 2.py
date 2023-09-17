# 환율
ex_rate = {"달러":1320, "엔":950,"위안":182}

# 달러, 엔, 위안
money = [13, 200, 13]

# 환전 후 한화로 계산
total_money = (ex_rate["달러"]*money[0])+(ex_rate["엔"]*money[1])+(ex_rate["위안"]*money[2])

#결과 출력
print("철수가 가지고 있는 돈의 원화 가치는", total_money, "입니다.")
