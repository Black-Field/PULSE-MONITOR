# OpenCV, matplotlib, time のインポート
import cv2
import matplotlib.pyplot as plt
import time

# 脈拍を測定する関数
def get_pulse(x, y):
    """脈拍を得るための関数"""
    n = len(y)
    p = 0
    for i in range(n-3):
        A1 = y[i]
        A2 = y[i+1]
        A3 = y[i+2]
        diff1 = abs(A1-A2)
        diff2 = abs(A3-A2)
        diff = abs(diff1-diff2)
        if diff>= 1 :
            p += 1;
    bb = p*6
    return bb

# VideoCaptureのインスタンスを作成する。
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
fps = cap.get(cv2.CAP_PROP_FPS)
# 各パラメータの初期値
me = 0
HB = -1
start = 0
# 無条件ループ
while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()
    t = time.time()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## グレースケールに変換
    mean, stddev = cv2.meanStdDev(gray) ## 平均・分散の計算
    # スクリーンショットを撮りたい関係で1/4サイズに縮小
    frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4)))
    # 表示画面
    if HB >= 0:
        cv2.putText(frame, str(HB), (100,150), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255,0), 3, cv2.LINE_AA)
        cv2.putText(frame, 'A pulse rate', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)
    else:
        cv2.putText(frame, 'Press Enter', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)
    cv2.imshow('PUSH THE ENTER KEY TO START MEASUREMENT', frame)
    # 条件分岐
    if cv2.waitKey(1) == 113: break ## qで終了
    elif cv2.waitKey(1) == 13: ## ENTERで計測開始
        start = time.time()
        HB = -1
        plt.cla()
        i = 0
        j = mean[0,0]
        x = []
        y = []
        plt.ion()
        # MATPLOTLIB コンフィグ
        plt.title('The beat of the pulse') ## グラフタイトル
        plt.xlabel('Time') ## x軸ラベル
        plt.ylabel('Brightness') ## y軸ラベル
        plt.xlim(0,10) ## x軸範囲固定
        plt.grid() ## グリッド線オン
        me = 1
    #グラフの更新
    if me == 1:
        # 描画データ生成
        i = t-start
        j = mean[0,0]
        x.append(i) ### x軸データ
        y.append(j) ### y軸データ
        plt.plot(x,y,color='blue')
        # グラフ描画
        plt.draw()
        plt.pause(0.0000000001)
        # 脈拍計測
        if i >= 10:
            me = 0
            HB = get_pulse(x,y)


cap.release()
cv2.destroyAllWindows()
