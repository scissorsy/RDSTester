#WAREHOUSE Table Layout
WAREHOUSE = 'WAREHOUSE'
W_ID = 'W_ID'
W_NAME = 'W_NAME'
W_STREET_1 = 'W_STREET_1'
W_STREET_2 = 'W_STREET_2'
W_CITY = 'W_CITY'
W_STATE = 'W_STATE'
W_ZIP = 'W_ZIP'
W_TAX = 'W_TAX'
W_YTD = 'W_YTD'

#STOCK Table Layout
STOCK = 'STOCK'
S_I_ID = 'S_I_ID'
S_W_ID = 'S_W_ID'
S_QUANTITY = 'S_QUANTITY'
S_DIST_01 = 'S_DIST_01'
S_DIST_02 = 'S_DIST_02'
S_DIST_03 = 'S_DIST_03'
S_DIST_04 = 'S_DIST_04'
S_DIST_05 = 'S_DIST_05'
S_DIST_06 = 'S_DIST_06'
S_DIST_07 = 'S_DIST_07'
S_DIST_08 = 'S_DIST_08'
S_DIST_09 = 'S_DIST_09'
S_DIST_10 = 'S_DIST_10'
S_YTD = 'S_YTD'
S_ORDER_CNT = 'S_ORDER_CNT'
S_REMOTE_CNT = 'S_REMOTE_CNT'
S_DATA = 'S_DATA'

#DISTRICT Table Layout
DISTRICT = 'DISTRICT'
D_ID = 'D_ID'
D_W_ID = 'D_W_ID'
D_NAME = 'D_NAME'
D_STREET_1 = 'D_STREET_1'
D_STREET_2 = 'D_STREET_2'
D_CITY = 'D_CITY'
D_STATE = 'D_STATE'
D_ZIP = 'D_ZIP'
D_TAX = 'D_TAX'
D_YTD = 'D_YTD'
D_NEXT_O_ID = 'D_NEXT_O_ID'

#CUSTOMER Table Layout
CUSTOMER = 'CUSTOMER'
C_ID = 'C_ID'
C_D_ID = 'C_D_ID'
C_W_ID = 'C_W_ID'
C_LAST = 'C_LAST'
C_MIDDLE = 'C_MIDDLE'
C_FIRST = 'C_FIRST'
C_STREET_1 = 'C_STREET_1'
C_STREET_2 = 'C_STREET_2'
C_CITY = 'C_CITY'
C_STATE = 'C_STATE'
C_ZIP = 'C_ZIP'
C_PHONE = 'C_PHONE'
C_SINCE = 'C_SINCE'
C_CREDIT = 'C_CREDIT'
C_CREDIT_LIM = 'C_CREDIT_LIM'
C_DISCOUNT = 'C_DISCOUNT'
C_BALANCE = 'C_BALANCE'
C_YTD_PAYMENT = 'C_YTD_PAYMENT'
C_PAYMENT_CNT = 'C_PAYMENT_CNT'
C_DELIVERY_CNT = 'C_DELIVERY_CNT'
C_DATA = 'C_DATA'

#HISTORY Table Layout
HISTORY = 'HISTORY'
H_C_ID = 'H_C_ID'
H_C_D_ID = 'H_C_D_ID'
H_C_W_ID = 'H_C_W_ID'
H_D_ID = 'H_D_ID'
H_W_ID = 'H_W_ID'
H_DATE = 'H_DATE'
H_AMOUNT = 'H_AMOUNT'
H_DATA = 'H_DATA'

#ORDERS Table Layout
ORDERS = 'ORDERS'
O_ID = 'O_ID'
O_C_ID = 'O_C_ID'
O_D_ID = 'O_D_ID'
O_W_ID = 'O_W_ID'
O_ENTRY_D = 'O_ENTRY_D'
O_CARRIER_ID = 'O_CARRIER_ID'
O_OL_CNT = 'O_OL_CNT'
O_ALL_LOCAL = 'O_ALL_LOCAL'

#ORDER_LINE Tabel Layout
ORDER_LINE = 'ORDER_LINE'
OL_O_ID = 'OL_O_ID'
OL_D_ID = 'OL_D_ID'
OL_W_ID = 'OL_W_ID'
OL_NUMBER = 'OL_NUMBER'
OL_I_ID = 'OL_I_ID'
OL_SUPPLY_W_ID = 'OL_SUPPLY_W_ID'
OL_DELIVERY_D = 'OL_DELIVERY_D'
OL_QUANTITY = 'OL_QUANTITY'
OL_AMOUNT = 'OL_AMOUNT'
OL_DIST_INFO = 'OL_DIST_INFO'

#NEW_ORDER Table Layout
NEW_ORDER = 'NEW_ORDER'
NO_O_ID = 'NO_O_ID'
NO_D_ID = 'NO_D_ID'
NO_W_ID = 'NO_W_ID'

#ITEM Table Layout
ITEM = 'ITEM'
I_ID = 'I_ID'
I_IM_ID = 'I_IM_ID'
I_NAME = 'I_NAME'
I_PRICE = 'I_PRICE'
I_DATA = 'I_DATA'

num_of_cols = {WAREHOUSE: 9,
               STOCK: 17,
               DISTRICT: 11,
               CUSTOMER: 21,
               HISTORY:8,
               ORDERS:8,
               ORDER_LINE:10,
               NEW_ORDER:3,
               ITEM:5}
population = {ITEM: 100000,
              STOCK: 100000,
              CUSTOMER: 3000,
              DISTRICT: 10}