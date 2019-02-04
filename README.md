# Клиент для PartnerAPI


```python
from spg_client.spg_client import SpgClient
from spg_client.card import Card
from spg_client.spg_requests import Pay, Block, Unblock, GetState, Refund, Charge
card = Card(pan='номер карты', month='месяц', year='год действия карты', 
            secure_code='секретный код CVC', 
            card_holder='Имя Фамилия владельца', cvc2reason_code='1')

spg_client = SpgClient(service_id='номер сервиса',
                       base_url='https://test_server_url.ru/',
                       secret='secret_key')

order_id = 'номер операции'

######### Пример одностадийного платежа
print('Одностадийная выплата')
request = Pay(card, order_id, 100, 'operation')
spg_client.perform(request)

print('Статус')
request = GetState(order_id)
spg_client.perform(request)



######### Пример оплаты с блокировкой средств
print('Блок')
request = Block(card, order_id, 100, 'tranzaka11')
spg_client.perform(request)

print('Разблокировка части средств')
request = Unblock(order_id, 10)
spg_client.perform(request)

print('Проведение платежа, charge')
request = Charge(order_id)
spg_client.perform(request)

print('Возврат')
request = Refund(order_id, 5)
spg_client.perform(request)
```
