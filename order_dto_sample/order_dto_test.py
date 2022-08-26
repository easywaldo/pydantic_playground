import json

from pydantic import BaseModel
from typing import Dict, List, Optional

class OrderGoodsOptionDto(BaseModel):
    delivery_type: str
    sno: int
    ea: int
    cart_sno: int
    cart_sno: Optional[int]
    text_option: Optional[str]

    class Config:
        validate_assignment = 'limited'

    def showMemo(self):
        print(f'memo: {self.memo}')


class OrderRequestDto(BaseModel):
    total_price: int
    receiver_name: str
    receiver_postcode: str
    pay_method: str
    receiver_tel: str
    receiver_addr_detail: str
    is_toss_transfer: bool
    receipt_type: str
    goods_options: List[OrderGoodsOptionDto]
    emoney: int
    receiver_addr: str
    delivery_fee: int
    memo: str


request_body_dict = {
	"total_price": 15800,
	"receiver_name": "easywaldo",
	"receiver_postcode": "06234",
	"pay_method": "card",
	"receiver_tel": "111-222-6789",
	"receiver_addr_detail": "155층",
	"is_toss_transfer": True,
	"receipt_type": "0",
	"goods_options": [{
		"delivery_type": "standard",
		"sno": 9999999999,
		"text_option": None,
		"ea": 1,
		"cart_sno": None
	}],
	"emoney": 0,
	"receiver_addr": "Seoul, Korea",
	"delivery_fee": 0,
	"memo": ""
}
json_str = json.dumps(request_body_dict)
received_json_data = json.loads(json_str)
order_data: OrderRequestDto = OrderRequestDto.parse_obj(received_json_data)

print(type(order_data))
print(order_data.total_price)
print(order_data.receiver_name)