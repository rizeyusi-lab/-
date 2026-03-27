def get_price(is_vip):
    if is_vip == True:
     return 15000
    else:
        return 15000

price = get_price(True)
print(f'커트 가격은{price}원 입니다.')
price = get_price(False)
print(f'커트 가격은{price}원 입니다.')