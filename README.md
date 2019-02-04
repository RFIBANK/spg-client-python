# Клиент для PartnerAPI
print('Одностадийная выплата')
request = Pay(card, order_id, 100, 'operation')
spg_client.perform(request)

print('Статус')
request = GetState(order_id)
spg_client.perform(request)





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
