import joblib

def func(i):
    return i

# n_jobs でコア数指定
# joblib.Parallel(<Parallelへの引数>)(
#     joblib.delayed(<実行する関数>)(関数への引数) for 変数名 in リテラル
# )
result = joblib.Parallel(n_jobs=-1)(
    joblib.delayed(func)(i) for i in range(5)
)

# 明日TODO: 色々試してみる

# 明日TODO: リスト内包表記の学習

print(result)

