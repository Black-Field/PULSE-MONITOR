# Pulse Monitor
====

# Overview

  Webカメラのカメラレンズに指を押し当て、脈拍を測定するPythonコード

## Description

  OpenCVでWebカメラ画像を取得し、毎フレームの輝度の平均値をリアルタイムでグラフにプロットする。

## Demo

  ![](https://github.com/Black-Field/PULSE-MONITOR/blob/master/file/demo.gif)

## Requirement

  Pythonのバージョンと使用したライブラリを以下に示す。
  > Python : 3.7.3
  >> opencv-python==4.1.0.25  
  >> matplotlib==3.1.1
  
  MacBook Air (13-inch, Early 2015)で動作確認を行った。このコードは、リアルタイムでグラフに毎フレームの輝度の平均値をプロットしているため、while分の1サイクルで1フレームに追いつけない事が分かった。1サイクルで最大0.1秒ほどかかる事が分かった。しかし、今回測定しているのは脈拍なので、十分なプロットが得られると考え、解決策として、実際の時間を測定してデータに反映させている程度に留まった。

## Usage

  1. コンソールからこのプログラムを実行する。
  2. 指をWebカメラのカメラレンズに押し当てる。
  3. enter key を押す。
  4. 脈拍の計測が始まる。この時、指を動かしたり、周囲の光を動かさないで下さい。
  5. 10秒後測定結果が表示される。
  6. q key を押すと終了し、enter key を押すと再び測定を行う。

## Install

  pulsation.pyをダウンロードして使ってください。

## References

  [OpenCV 1](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_video_display/py_video_display.html)
  > Webカメラからフレーム毎に画像を取得する方法について参考にした。
  
  [OpenCV 2](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_image_display/py_image_display.html)
  > 取得した各フレームの扱い方について参考にした。
  
  [Qiita](https://qiita.com/hausen6/items/b1b54f7325745ae43e47)
  > matplotlibを使ったリアルタイム描画について参考にした。
