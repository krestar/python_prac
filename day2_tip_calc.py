print("팁 계산기입니다.\n")
total_bill=float(input("총 지불 금액을 입력해주세요. 입력:$"))
tiprate=float(input("팁을 10,12,15% 중 몇배율로 지불하시겠습니까? 입력:"))
how_many_people=float(input("몇분과 함께 지불하십니까? 입력:"))
tip_100rate=tiprate/100
tip=round((total_bill)*(tip_100rate+1)/how_many_people,3)
print(f"1인당 ${tip} 지불하시면 됩니다.")