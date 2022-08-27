import subprocess
from timeout_decorator import timeout, TimeoutError

id = 0 #プロセスID

def func():
    cmd = './a.out' #Cプログラムの実行コマンド
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    if proc.poll() is None:
        global id
        id = proc.pid
    out = proc.communicate()
    out = out[0]
    out = str(out, 'utf-8')
    return out #実行結果を文字列で返す

def ex_func():
    subprocess.run('kill ' + str(id),shell=True)
    out = 'タイムアウトしました。'
    return out

@timeout(1) #タイムアウトの時間設定
def main():
    try:
        out_str = func()
        return out_str
    except TimeoutError:
        out_str = ex_func()
        return out_str

if __name__ == "__main__":
    main()