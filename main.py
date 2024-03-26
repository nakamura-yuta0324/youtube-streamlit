import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title("streamlit 超入門")

#st.write("DataFrame")

#df = pd.DataFrame({
#    "一列目": [1, 2, 3, 4] , 
#    "二列目": [10, 20, 30, 40]
#})

#st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
#st.write(df)
#writeの方だと縦横を指定できない
#st.table(df.style.highlight_max(axis=0))

#Markdown
#"""
## 小
### 節
#### 項
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

#折れ線グラフ
#dg = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
#)
#st.line_chart(dg) #折れ線グラフ１
#st.area_chart(dg) #折れ線グラフ２
#st.bar_chart(dg) #棒グラフ

#マップのプロット
#dg = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], 
# #新宿の緯度軽度
#    columns=['lat', 'lon'] #lat=緯度、lon=軽度
#)
#st.map(dg)

#0.1秒ごとにバーが進んでいき、100になると以下が表示される
st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i + 1)
    time.sleep(0.0001) #値が小さくなればなるほどゲージが早く進む

"Doneee!"

st.write("Interactive Widgets")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ回答を書く")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ回答を書く")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ回答を書く")
#趣味
hobby = st.text_input("あなたの趣味を教えてください。")
"あなたの趣味は", hobby, "です。"

#好きな数字
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)
'あなたの好きな数字は、', option , 'です。'

#コンディション
condition = st.slider("あなたの今の調子は?", 0, 100, 50)
"コンディション：", condition, 

#買い物リスト
items = ["apples", "bananas", "potatoes","peach", "peanuts", "trees"]
choices = st.multiselect("買い物リスト", items)
select_items = ", ".join(choices) if choices else "なし"
"買うもの：", select_items

#写真
st.write("Display Image")
if st.checkbox('Show Image'): #チェックを入れると写真が表示
    img = Image.open('rion1.jpeg')
    st.image(img, caption='rion in SAWAMURA', use_column_width=True)
    