# PythonでCプログラムを連続して実行する
cont_exec_c.pyは、Cプログラムを連続して実行する場合を想定して作成したモジュールである。
事前に実行時間の上限を設定する。
無限ループなどで実行時間が上限を超過した場合、プロセスを中断させる。
プロセスIDを走査し、中断されたプロセスのみを終了させる。

動作の流れ
1. Cプログラムをコンパイルする。
2. 一時変数を用意し、引数なしでモジュールを呼び出す。
