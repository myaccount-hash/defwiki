<a id="todo-153"></a>

## 153

パケットとヘッダを定義するか検討する．[IPパケット](wiki.md#w9btgk)と[struct sk_buff](wiki.md#klvvmj)が平語で用いる．[カプセル化](wiki.md#oh434k)の「データの単位」とも統一する．あわせて根ディレクトリと作業ディレクトリ（[ディレクトリ](wiki.md#j1d7gn)，[パス名](wiki.md#ymj65u)，[struct fs_struct](wiki.md#yve2sf)が平語で用いる）を定義するか検討する．

<a id="todo-152"></a>

## 152

[Amazon VPC Lattice](wiki.md#i24o70)のサービスネットワークとサービスの単位（リスナー，ルール，ターゲットグループを含む）を定義するか検討する．

<a id="todo-151"></a>

## 151

[Language Server Protocol](wiki.md#dfaxj3)と[Debug Adapter Protocol](wiki.md#jt8i5n)の上位概念（[テキストエディタ](wiki.md#nud9su)と言語固有の機能の提供者を分離するプロトコル）を定義し，M×NからM+Nへの削減の記述をそこへ移すか検討する．

<a id="todo-150"></a>

## 150

[MCPクライアント](wiki.md#skno5x)が[MCPサーバー](wiki.md#fimtpo)へ提供する機能（サンプリング，ルート，エリシテーション）を定義するか検討する．[大規模言語モデル](wiki.md#q89hwf)の生成などを参照するため，言語モデルの体系の定義とあわせて行う．

<a id="todo-149"></a>

## 149

[C言語](wiki.md#4pg9c8)の実効型（割付けの領域の[Cオブジェクト](wiki.md#rq1bpp)の[データ型](wiki.md#w7t735)は格納で定まる）を定義するか検討する．型によるアクセスの制約（strict aliasing）とあわせて定義しなければ参照先が無い．

<a id="todo-148"></a>

## 148

[EPROCESS](wiki.md#ops4d2)を[アドレス空間記述子](wiki.md#sjz43t)とみなせるか検討する．[アドレス空間記述子](wiki.md#sjz43t)が保持する集合を[メモリ領域記述子](wiki.md#q3l4ki)から[アドレス区間記述子](wiki.md#k4ztwu)に一般化するかもあわせて検討する．

<a id="todo-147"></a>

## 147

[jail](wiki.md#xoam9f)と[コンテナ](wiki.md#uds0ak)，[Linux名前空間](wiki.md#rmoy1r)の関係を整理する上位概念を定義するか検討する．

<a id="todo-144"></a>

## 144

[Linux](wiki.md#eh8l2u)と[FreeBSD](wiki.md#ofaawr)の構造体の対応で未処理のものを検討する．[struct super_block](wiki.md#7yjz2f)と[struct mount](wiki.md#zsv4ce)の役割の差（[Linux](wiki.md#eh8l2u)はファイルシステムの実体とマウント点を分ける）を定義で表すか．[struct socket](wiki.md#8a9dsr)と[struct sock](wiki.md#cn7ia0)の組と[struct socket](wiki.md#os8s4h)の対応．[置換更新](wiki.md#gv4jmw)を用いる他の対象．[スレッドグループ](wiki.md#qugvsb)が共有するstruct signal_structを[プロセス記述子](wiki.md#smq3zz)とみなせるか（確信がなく書かなかった）．

<a id="todo-141"></a>

## 141

[記憶域期間](wiki.md#uvaml5)を[C++](wiki.md#drl0oo)と共通の抽象にできるか検討する（[C++](wiki.md#drl0oo)では割付けにあたるものを動的と呼ぶ）．

<a id="todo-139"></a>

## 139

[システムコール](wiki.md#saksfm)の実現方式（番号による識別，特殊な命令による[特権モード](wiki.md#uk5ihn)への移行）と，[C標準ライブラリ](wiki.md#oyypas)の関数がそれを包むことを書くか検討する．全ての[オペレーティングシステム](wiki.md#c8v8vw)に成り立つか確信がなく書かなかった．

<a id="todo-136"></a>

## 136

[Windows NT](wiki.md#jzpnq4)の構造体で今回追加しなかったものを定義するか検討する．ディスパッチャオブジェクト（DISPATCHER_HEADER，KEVENT，KMUTANT，KSEMAPHORE，KTIMER．[KTHREAD](wiki.md#6offhs)の待機を含む），KAPCと非同期プロシージャ呼び出し，KDPC（[遅延プロシージャ呼び出し](wiki.md#ajw0fy)の構造体），CONTEXTとEXCEPTION_RECORD，CLIENT_ID，RTL_USER_PROCESS_PARAMETERSとPEB_LDR_DATA（[PEB](wiki.md#hfgg6x)が参照するもの）．あわせて，x86，x64，セグメントレジスタ，スレッドローカル記憶域を定義するか．確信がなく書かなかった事柄を確かめる．[WoW64](wiki.md#cyz8ys)の[プロセス](wiki.md#lm3iq5)が32ビットと64ビットの[PEB](wiki.md#hfgg6x)と[TEB](wiki.md#lnr2ip)を併せもつこと．

<a id="todo-130"></a>

## 130

[FreeBSD](wiki.md#ofaawr)の構造体で今回追加しなかったものを定義するか検討する．GEOMとそのstruct bio（[device-mapper](wiki.md#aqu8xq)と[struct bio](wiki.md#k31ju1)との抽象化を含む），struct cdev，struct pgrpとstruct session，struct protoswとstruct inpcbとstruct sockbuf（[struct socket](wiki.md#os8s4h)が参照するもの），struct pwddesc（作業ディレクトリと根ディレクトリ），struct ifaddr，rforkによる[struct filedesc](wiki.md#nij06r)と[struct vmspace](wiki.md#1p4y2z)の共有．確信がなく書かなかった事柄を確かめる．[struct vm_map_entry](wiki.md#xx4asa)の対応付け先（下位のvm_map，vm_objectをもたない区間）を書き切れるか，[jail](wiki.md#xoam9f)のネットワークの扱い（アドレスの制限とVNET）．

<a id="todo-127"></a>

## 127

[Linux名前空間](wiki.md#rmoy1r)の種類（ユーザー名前空間，PID名前空間を含む）を定義し，[struct cred](wiki.md#hotd7l)と[struct nsproxy](wiki.md#nsn2y1)の平語を参照に置き換えるか検討する．あわせてLinuxのcapabilityを定義するか検討する（ToDoのUID・rootの件と関係する）．

<a id="todo-126"></a>

## 126

[Linux](wiki.md#eh8l2u)の構造体で今回追加しなかったものを定義するか検討する．struct signal_struct，struct sighand_struct（シグナルの概念を含む），struct pid，struct vfsmountとstruct path，struct gendisk，struct css_set（[struct task_struct](wiki.md#1jy9hb)と[cgroup](wiki.md#rh5dah)の関係）．また，[I/O要求パケット](wiki.md#dd3rvj)と[struct bio](wiki.md#k31ju1)，[カーネルオブジェクト](wiki.md#4d5j7r)とLinuxの構造体を抽象化できるか検討する．[Netfilter](wiki.md#feag1h)と[device-mapper](wiki.md#aqu8xq)が処理する対象を[struct sk_buff](wiki.md#klvvmj)，[struct bio](wiki.md#k31ju1)の参照で書くか検討する．

<a id="todo-125"></a>

## 125

Linuxのユーザー・ファイル所有者・パーミッション（任意アクセス制御）の体系を定義するか検討する．[setuidプログラム](wiki.md#zv7vha)は「所有者」を平語で，[権限昇格](wiki.md#rzi1ck)は[セキュリティ文脈](wiki.md#lxnyp5)で抽象的に書き，Linuxのスーパーユーザー（root）やUIDを定義していない．

<a id="todo-123"></a>

## 123

Hyperplaneを定義するか検討する（[NATゲートウェイ](wiki.md#2ii7xa)，[Network Load Balancer](wiki.md#mddvjx)，[AWS PrivateLink](wiki.md#8irydc)との関係を含む）．確信がなく書かなかった事柄を確かめる．[Hyperplane ENI](wiki.md#sl4ng3)の削除の時機，[Network Load Balancer](wiki.md#mddvjx)の[リクエスターマネージド型ネットワークインターフェース](wiki.md#8gfkr4)を書くか．

<a id="todo-122"></a>

## 122

[Identity Centerインスタンス](wiki.md#5mx2oh)が外部の[アイデンティティプロバイダ](wiki.md#3z77qd)を用いる構成と，アプリケーションの割り当てを定義するか検討する．

<a id="todo-106"></a>

## 106

[VPCピアリング接続](wiki.md#z6xphd)，[AWS Transit Gateway](wiki.md#afxugq)，[AWS PrivateLink](wiki.md#8irydc)，[Amazon VPC Lattice](wiki.md#i24o70)を，ネットワーク同士をつなぐか，特定の通信先だけを利用させるかという軸で整理する上位概念を定義するか検討する．

<a id="todo-116"></a>

## 116

[大規模言語モデル](wiki.md#q89hwf)を支える体系を定義するか検討する．言語モデル，トークン（[トークン](wiki.md#qt96h9)とは別の概念），訓練，コンテキスト，汎用のプロンプト，ツール使用を定義し，[大規模言語モデル](wiki.md#q89hwf)，[MCPプロンプト](wiki.md#lv4fgp)，[MCPツール](wiki.md#lrik9i)をそれらの参照で書き直すか．

<a id="todo-104"></a>

## 104

[Terraform](wiki.md#i3c7fx)周辺の未定義語を定義するか検討する．実行計画（plan，apply），データソース，変数，出力，バックエンド．確信がなく書かなかった事柄を確かめる．[Terraform状態](wiki.md#ufk7we)の[ロック](wiki.md#7x5us3)に対応するバックエンドの範囲，[Terraformプロバイダ](wiki.md#5nckv0)と[Terraform](wiki.md#i3c7fx)の通信方式．あわせて，[Terraform](wiki.md#i3c7fx)の1回の適用と[調整ループ](wiki.md#gibl6s)の関係（望ましい状態との差を減らす操作の抽象）を整理する．

<a id="todo-103"></a>

## 103

[Zabbix](wiki.md#o6myi6)周辺の未定義語を定義するか検討する．SNMP，IPMI，JMX，正規表現，タグ，プロトタイプ，グラフ（[LLDルール](wiki.md#dkfxg4)が生成するもの），ユーザー，マスタアイテム．確信がなく書かなかった事柄を確かめる．[アイテム](wiki.md#as86xt)の値の型の全種類（Zabbix 7.0でのバイナリ型の有無），[サービス](wiki.md#8vi40f)の状態の算出規則，[プロキシグループ](wiki.md#t7lw5k)のフェイルオーバーの挙動，内部および[サービス](wiki.md#8vi40f)を発生源とする[イベント](wiki.md#przzj5)を[障害](wiki.md#ilz3yu)に含めるか．

<a id="todo-102"></a>

## 102

[サンドボックス](wiki.md#2xz9pb)周辺で確信がなく書かなかった事柄を確かめる．[Windows NT](wiki.md#jzpnq4)でAppContainerを用いる[プロセス](wiki.md#lm3iq5)の範囲，[Linux](wiki.md#eh8l2u)のsetuidサンドボックスを記述するか．
