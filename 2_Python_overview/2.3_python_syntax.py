# 2019/04/05

##### 2.3.1 変数と型 #####
# 変数がどの型であるかはtype関数を用いて知ることができる
a = 123
print( type(a) ) # <class 'int'>

# bool型の値は数値として扱うことができる．
# True:1 False:0
a = True; b = False
print( a+b ) # 1
# Pythonでは，上記のように;（セミコロン）で区切ることで，
# 1行以内に複数の処理を書くことができる．

# 浮動小数点型の指数表記が可能．
1.2e5   # 1.2×10の５乗  120000.0
1.2e-5  # 1.2×10の-５乗 0.000012



##### 2.3.2 演算子 #####
# Pythonの演算子については，他のプログラミング言語と大きな違いはない
a = 3; b = 4

c = a + b
print(c) # 7

d = a < b # 比較
print(d) # True

e = 3 < 4 and 4 < 5 # 論理和
print(e) # True



##### 2.3.3 リスト #####
a = [1, 2, 3, 4, 5] # リストの作成

b = a[2] # 3番目の要素を取得
print(b) # 3

a.append(6) # 末尾に要素を加える
print(a) # [1, 2, 3, 4, 5, 6]

a[2] = 7 # 要素の入れ替え
print(a) # [1, 2, 7, 4, 5, 6]



##### 2.3.4 タプル #####
# タプルはリストと同じく複数の値をまとめて扱いたいときに利用するが，
# 要素の追加や削除，入れ替えなどはできない．
# 要素を変更する予定がない場合は，リストよりもタプルを使用するほうがベター．
a = (1, 2, 3, 4, 5) # タプルの作成

b = a[2] # 3番目の要素を取得
print(b) # 3

# 要素が一つだけのタプルは，以下のように要素の直後に,が必要．
(3,)

# +の演算子で，タプル同士を結合した新たなタプルを作ることができる．
print( a + (6, 7, 8, 9, 10) ) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

a = [1, 2, 3]
a1, a2, a3 = a # リストの各要素を別々の変数に代入
print(a1, a2, a3) # 1 2 3

b = (4, 5, 6)
b1, b2, b3 = b # タプルの各要素を別々の変数に代入
print(b1, b2, b3) # 4 5 6



##### 2.3.5 辞書 #####
# 辞書は，キーと値の組み合わせでデータを格納する．
a = {"Apple":3, "Pineapple":4} # 辞書の作成

print( a["Apple"] ) # "Apple"のキーをもつ値を取得

a["Pineapple"] = 6 # 要素の入れ替え
print( a["Pineapple"] ) # "Pineapple"のキーをもつ値を取得

a["Melon"] = 3 # 要素の追加
print( a ) # {'Apple': 3, 'Pineapple': 6, 'Melon': 3}

# 上記の例では，キーに文字列を使用しているが，
# キーには数値や文字列，タプルを利用することもできる．



##### 2.3.6 if文 #####
a = 7
if a < 12:
    print("Good morning!")
elif a < 17:
    print("Good afternoon!")
elif a < 21:
    print("Good evening!")
else:
    print("Good night!")



##### 2.3.7 for文 #####
range([開始番号,] 終了番号 [, ステップ数])
# []で囲まれた引数は省略可能

for a in [4, 7, 10]: # リストを使ったループ
    print(a)
# 4
# 7 
# 10

for a in range(3): # range関数を使ったループ
    print(a)
# 0
# 1 
# 2



##### 2.3.8 while文 #####
a = 0
while a < 3:
    print(a)
    a += 1
# 0
# 1 
# 2



##### 2.3.9 内包表記 #####
# 新たなリスト = [要素への処理 for 要素 in リスト]
a = [1, 2, 3, 4, 5, 6, 7]
b = [c*2 for c in a] # aの要素を2倍して新たなリストを作る
print(b) # [2, 4, 6, 8, 10, 12, 14]

# 以下のように，内包表記にifを用いた条件式を含めることが可能
# 新たなリスト = [要素への処理 for 要素 in リスト if 条件式]
a = [1, 2, 3, 4, 5, 6, 7]
b = [c*2 for c in a if c < 5] # 5より小さい要素のみ処理する
print(b) # [2, 4, 6, 8]



##### 2.3.10 関数 #####
def add(a, b):
    c = a + b
    return c
print( add(3,4) ) # 7

# 引数にはデフォルト値を設定できる
def add(a, b=4):
    c = a + b
    return c
print( add(3) ) # 7

# *を付けたタプルを用いて，複数の引数を一度に渡すことができる
def add(a, b, c):
    d = a + b + c
    print(d) # 6
e = (1, 2, 3)
add(*e) # *をつけてタプルを渡す



##### 2.3.11 変数のスコープ #####
a = 123 # グローバル変数

def showNum():
    b = 456 # ローカル変数
    print(a, b)

showNum()
# 123 456

# Pythonでは，関数内でグローバル変数に値を代入しようとすると，
# 新しいローカル変数とみなされる．
a = 123

def setLocal():
    a = 456 # aはローカル変数とみなされる
    print("Local:", a) 

setLocal()
print("Global:", a)
# Local: 456
# Global: 123

a = 123 # グローバル変数

def setGlobal():
    global a # 関数内でグローバル変数を使う準備
    a = 456
    print("Global:", a) 

setGlobal()
print("Global:", a)
# Global: 456
# Global: 456



##### 2.3.12 クラス #####
# オブジェクト指向には，クラスとインスタンスという概念がある．
# クラスは設計図のようなもので，インスタンスは実体．
class Calc:
    # コンストラクタ
    def __init__(self, a):
        self.a = a

    def add(self, b):
        print(self.a + b)

    def multiply(self, b):
        print(self.a * b)

calc = Calc(3) # Calcクラスのインスタンスを生成
calc.add(4)
calc.multiply(4)
# 7
# 12

class CalcPlus(Calc): # Calcクラスを継承
    def subtract(self, b):
        print(self.a - b)

    def devide(self, b):
        print(self.a / b)

calc_plus = CalcPlus(3) # CalcPlusクラスのインスタンスを生成
calc_plus.add(4)
calc_plus.multiply(4)
calc_plus.subtract(4)
calc_plus.devide(4)
# 7
# 12
# -1
# 0.75