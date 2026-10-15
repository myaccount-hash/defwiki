<a id="8hltrb"></a>

## 3GPP

[セルラー通信](#fibo1z)の規格を策定する，各地域の標準化団体の共同事業．

<a id="ukvr2v"></a>

## 5G NR

[3GPP](#8hltrb)が策定した，第5世代の[セルラー通信](#fibo1z)の無線方式の規格．

<a id="wlnfs0"></a>

## AAAAレコード

所有者の[ドメイン名](#d8xx9q)に対応する[IPv6](#4elryy)の[IPアドレス](#3ksnfe)を示す[資源レコード](#syx2b4)．

<a id="2ywo5m"></a>

## ACID特性

[トランザクション](#v5hhix)が満たす[原子性](#7anb5g)，[一貫性](#qp3v5d)，[分離性](#79gxog)，[永続性](#ihllp7)の4つの性質．

<a id="gclsru"></a>

## ADD-PATH

同じ[IPプレフィックス](#6rwn5e)への複数の[経路](#5433mk)を，パス識別子で区別して1つの[BGPセッション](#s9mnt1)で広告する[ケイパビリティ](#6vfi5n)．

<a id="9e509k"></a>

## API

ソフトウェアが他のソフトウェアに機能を提供する，呼び出しの形式と振る舞いの取り決め．

<a id="my3zbg"></a>

## AS_PATH

[経路](#5433mk)が通過した[自律システム](#8wkkrz)の[AS番号](#wvk6j6)を記録する周知必須の[パス属性](#q885vr)．[AS_SEQUENCE](#f2qawn)と[AS_SET](#vqwgle)の区間からなる．[eBGP](#vz4jtn)で広告するとき，[BGPスピーカー](#v9rnch)は自身の[AS番号](#wvk6j6)を先頭に追加する．末尾の要素が発生源を示す．

<a id="6wjxke"></a>

## AS_PATHプリペンド

自身の[AS番号](#wvk6j6)を[AS_PATH](#my3zbg)へ複数回追加して広告し，他の[自律システム](#8wkkrz)の[最良経路選択](#raisax)でその[経路](#5433mk)を選ばれにくくする手法．

<a id="f2qawn"></a>

## AS_SEQUENCE

[AS_PATH](#my3zbg)の区間で，[経路](#5433mk)が通過した[自律システム](#8wkkrz)の[AS番号](#wvk6j6)を，最後に通過したものを先頭として並べたもの．

<a id="vqwgle"></a>

## AS_SET

[AS_PATH](#my3zbg)の区間で，[経路集約](#ofoz7i)で併合された[経路](#5433mk)が通過した[自律システム](#8wkkrz)の[AS番号](#wvk6j6)を，順序なく集めたもの．

<a id="wvk6j6"></a>

## AS番号

[自律システム](#8wkkrz)を一意に識別する番号．2[オクテット](#yimp6h)または4[オクテット](#yimp6h)の値をとる．64512から65534まで，および4200000000から4294967294まではプライベート用に予約され，[インターネット](#3qoztf)への[経路](#5433mk)の広告に用いない．4[オクテット](#yimp6h)の値を扱えない[BGPスピーカー](#v9rnch)に対しては，[AS_PATH](#my3zbg)中の2[オクテット](#yimp6h)に収まらない値を23456（AS_TRANS）に置き換え，元の値をAS4_PATH属性で伝える．

<a id="z1q1fs"></a>

## AS間ピアリング

2つの[自律システム](#8wkkrz)が，それぞれ自身と[トランジット](#mcggb8)の顧客の[経路](#5433mk)のみを互いに広告する関係．

<a id="8153tt"></a>

## AWS Artifact

[Amazon Web Services](#totant)に対する第三者機関の[監査](#7slqlb)の報告書を提供する[AWSサービス](#40hiw9)．

<a id="wvcwae"></a>

## AWS Audit Manager

[AWSサービス](#40hiw9)から証拠を収集し，[監査](#7slqlb)を自動化する[AWSサービス](#40hiw9)．

<a id="sdsuhi"></a>

## AWS CloudFormation

[スタック](#ib0gqz)と，それに属する[AWSリソース](#78qg7h)を[テンプレート](#iwvz04)に従って一括で作成，更新，削除する[Infrastructure as Code](#gq4l0t)の[AWSサービス](#40hiw9)．

<a id="vnjjs2"></a>

## AWS CloudTrail

[AWSアカウント](#r2ghkv)内の[AWSサービス](#40hiw9)の[API](#9e509k)の呼び出しを，呼び出した[プリンシパル](#t8ujsy)，時刻，送信元を含む情報とともに[イベント](#35wv5r)として記録する[AWSサービス](#40hiw9)．

<a id="tt9c6l"></a>

## AWS Fargate

[Amazon Elastic Container Service](#4azxa9)と[Amazon Elastic Kubernetes Service](#rtypm1)の[コンテナ](#uds0ak)を[サーバーレス](#vnbuyu)で実行する計算エンジン．

<a id="cdv3og"></a>

## AWS IAM Identity Center

複数の[AWSアカウント](#r2ghkv)とアプリケーションへのアクセスを一元管理する[AWSサービス](#40hiw9)．

<a id="nm8gp9"></a>

## AWS Identity and Access Management

[AWSアカウント](#r2ghkv)内の[IAMアイデンティティ](#ix9em5)を管理し，[プリンシパル](#t8ujsy)の要求を[IAMポリシー](#let9u3)に基づいて[認可](#8esn53)する[AWSサービス](#40hiw9)．

<a id="szs4of"></a>

## AWS Key Management Service

[鍵](#atfb8r)を作成，管理し，それを用いた[暗号](#o5aaif)の演算を行う[AWSサービス](#40hiw9)．[鍵](#atfb8r)の秘密の素材はハードウェアセキュリティモジュール内で保護され，平文でこのサービスの外に出ない．[鍵](#atfb8r)へのアクセスはキーポリシーと呼ぶ[リソースベースポリシー](#z6oh15)で制御される．

<a id="d2cxxc"></a>

## AWS Lambda

[Lambda関数](#v7xjp0)を[サーバーレス](#vnbuyu)で実行する[AWSサービス](#40hiw9)．

<a id="yj1k74"></a>

## AWS Organizations

複数の[AWSアカウント](#r2ghkv)を[組織](#sm4tb3)により一元管理し，請求を一括する[AWSサービス](#40hiw9)．

<a id="8irydc"></a>

## AWS PrivateLink

利用側の[VPC](#4ln6ld)に作成した[VPCエンドポイント](#pguegu)から，[エンドポイントサービス](#7rs9yk)または[リソースゲートウェイ](#ia2trf)の先にある[通信先](#b2znuk)へ，[VPC](#4ln6ld)の間に[経路](#5433mk)を設けずに接続させる[AWSサービス](#40hiw9)．接続は利用側からだけ開始でき，利用側と提供側の[VPC](#4ln6ld)の[IPプレフィックス](#6rwn5e)が重なってもよい．

ToDo: [123](todo.md#todo-123)，[106](todo.md#todo-106)

<a id="q44rf3"></a>

## AWS Security Token Service

[アクセスキーID](#6blyao)，[シークレットアクセスキー](#f2nfys)，[セッショントークン](#8xzr27)からなり，有効期限をもつ一時的な[認証情報](#pyxpuc)を発行する[AWSサービス](#40hiw9)．

<a id="afxugq"></a>

## AWS Transit Gateway

複数の[VPC](#4ln6ld)と[オンプレミス](#29xuc7)の[ネットワーク](#uy18d2)を，その間の通信を中央のハブで[中継](#zgr0mv)して相互に接続する[AWSサービス](#40hiw9)．[オンプレミス](#29xuc7)の[ネットワーク](#uy18d2)への[経路](#5433mk)は，静的に設定するか，[BGP](#0ey58g)で学習する．

ToDo: [106](todo.md#todo-106)

<a id="r2ghkv"></a>

## AWSアカウント

[AWSリソース](#78qg7h)の所有と課金の単位であり，[AWSリソース](#78qg7h)と[IAMアイデンティティ](#ix9em5)を他のAWSアカウントから隔離する境界．

<a id="wuqhd7"></a>

## AWSアカウントID

[AWSアカウント](#r2ghkv)を一意に識別する12桁の数字．

<a id="2bvry9"></a>

## AWSアクセスポータル

[Identity Centerユーザー](#ypfrjn)がサインインし，割り当てられたアクセス先を選択する画面．[AWSアカウント](#r2ghkv)へのアクセス先は[アカウント割り当て](#n4iumx)により定まる．

<a id="40hiw9"></a>

## AWSサービス

[Amazon Web Services](#totant)の[クラウドサービス](#i5ziux)．固有の[サービスプレフィックス](#xvi8o5)をもつ．

<a id="5q5a61"></a>

## AWSパーティション

互いに隔離された[リージョン](#1df8fw)の集まり．[AWSアカウント](#r2ghkv)は1つのAWSパーティションに属し，その[認証情報](#pyxpuc)は他のAWSパーティションで有効でない．

<a id="78qg7h"></a>

## AWSリソース

[AWSサービス](#40hiw9)により作成，管理される，利用者が操作する実体．[Amazon Resource Name](#c6b1z3)で識別され，作成した[AWSアカウント](#r2ghkv)が所有する．

<a id="e55vmk"></a>

## Adj-RIB-In

[BGPスピーカー](#v9rnch)が[ピア](#7wmnel)ごとに保持する，受信した[経路](#5433mk)の集合．

<a id="hfn0ts"></a>

## Adj-RIB-Out

[Loc-RIB](#d67w81)の要素にエクスポートの[ルーティングポリシー](#4bwmon)を適用した，[ピア](#7wmnel)ごとに広告する[経路](#5433mk)の集合．

<a id="65nzk0"></a>

## Amazon Aurora

[Amazon Relational Database Service](#txfy2g)で提供される，MySQLまたはPostgreSQLと互換性をもつ[リレーショナルデータベース](#ev8ocv)の[データベース管理システム](#wn1pbv)．データを3つの[アベイラビリティゾーン](#zb3vp3)にわたる6つの[レプリカ](#filo46)として保持する，[分散システム](#6cc980)をなすストレージを用いる．

<a id="912vnc"></a>

## Amazon CloudFront

[エッジロケーション](#r05bfh)にコンテンツを[キャッシュ](#kj4w0z)して配信する，[コンテンツ配信ネットワーク](#gyftmn)の[AWSサービス](#40hiw9)．

<a id="y77mp8"></a>

## Amazon CloudWatch

[AWSリソース](#78qg7h)とアプリケーションの[メトリクス](#1s1rpf)と[ログ](#9rxwgw)を収集し，[アラーム](#ra546q)の状態変化に応じて指定された処理を実行する監視の[AWSサービス](#40hiw9)．

<a id="knkcrh"></a>

## Amazon DynamoDB

[キーバリューストア](#trahzf)および[ドキュメントストア](#rw3kg0)を[サーバーレス](#vnbuyu)で提供する[AWSサービス](#40hiw9)．テーブルの項目は[主キー](#7ckf0e)で識別される．

<a id="sxdluo"></a>

## Amazon Elastic Block Store

[EBSボリューム](#bauqgu)と[EBSスナップショット](#4320z7)を提供する[AWSサービス](#40hiw9)．

<a id="y42e2r"></a>

## Amazon Elastic Compute Cloud

[EC2インスタンス](#0d2awr)を[IaaS](#hih6s5)として提供する[AWSサービス](#40hiw9)．

<a id="4azxa9"></a>

## Amazon Elastic Container Service

[コンテナオーケストレーション](#ldx08d)を行う[AWSサービス](#40hiw9)．[コンテナ](#uds0ak)の構成を記述した定義に従い，[コンテナ](#uds0ak)の集まりを[EC2インスタンス](#0d2awr)または[AWS Fargate](#tt9c6l)上で実行する．

<a id="atmeox"></a>

## Amazon Elastic File System

[EC2インスタンス](#0d2awr)を含む複数の計算機から，[ネットワーク](#uy18d2)越しにファイルを共有する[プロトコル](#bhk5im)であるNFSで同時に[マウント](#96n6sj)でき，容量が自動的に伸縮する[ファイルシステム](#pp17bd)を提供する[AWSサービス](#40hiw9)．

<a id="rtypm1"></a>

## Amazon Elastic Kubernetes Service

[コントロールプレーン](#b8ign2)を[Amazon Web Services](#totant)が運用する[AWSサービス](#40hiw9)．[Pod](#k4ef3z)を[EC2インスタンス](#0d2awr)または[AWS Fargate](#tt9c6l)上で実行する．

<a id="f6a76h"></a>

## Amazon Machine Image

[EC2インスタンス](#0d2awr)の起動に用いる[マシンイメージ](#biu4lz)．起動許可と，接続する[ブロックデバイス](#1frbzb)の対応付けをもつ．[リージョンリソース](#tynhcw)である．

<a id="txfy2g"></a>

## Amazon Relational Database Service

[リレーショナルデータベース](#ev8ocv)の構築，バックアップ，パッチの適用を含む運用を[Amazon Web Services](#totant)が担う[AWSサービス](#40hiw9)．

<a id="c6b1z3"></a>

## Amazon Resource Name

[AWSリソース](#78qg7h)を一意に識別する文字列．`arn:partition:service:region:account-id:resource`の形式をとる．partitionは[AWSパーティション](#5q5a61)を，serviceは[サービスプレフィックス](#xvi8o5)を，account-idは[AWSアカウントID](#wuqhd7)を表し，[リージョン](#1df8fw)や[AWSアカウント](#r2ghkv)に属さない[AWSリソース](#78qg7h)では該当部分が空となる．

<a id="w3fb2h"></a>

## Amazon Route 53

[権威DNSサーバー](#9es8da)，[ドメイン名](#d8xx9q)の登録，[ヘルスチェック](#4ofscj)を提供する[AWSサービス](#40hiw9)．

<a id="s81260"></a>

## Amazon Simple Notification Service

[トピック](#qiadm1)に発行されたメッセージを，その[トピック](#qiadm1)を購読する全ての送信先へ配信する[パブリッシュ/サブスクライブ型](#8rrdgi)の[AWSサービス](#40hiw9)．

<a id="ws95t3"></a>

## Amazon Simple Queue Service

送信者と受信者の間でメッセージを保持する[待ち行列](#lhxknx)を提供する[AWSサービス](#40hiw9)．[待ち行列](#lhxknx)の種類に標準とFIFOがある．標準は各メッセージを1回以上配信し，重複した配信と送信順と異なる順の配信を許す．FIFOは[キュー](#mqlfip)として送信順を保ち，重複排除の期間内に送信された同じメッセージを1回のみ配信する．

<a id="u2wout"></a>

## Amazon Simple Storage Service

[オブジェクトストレージ](#k4obt0)を提供する[AWSサービス](#40hiw9)．データを[S3バケット](#wtv4f2)内の[S3オブジェクト](#o1ut81)として格納する．

<a id="i24o70"></a>

## Amazon VPC Lattice

サービスネットワークに登録したサービスと[リソースゲートウェイ](#ia2trf)の先の[通信先](#b2znuk)を，そのサービスネットワークに関連付けた[VPC](#4ln6ld)，またはそこへの[VPCエンドポイント](#pguegu)から，[VPC](#4ln6ld)と[AWSアカウント](#r2ghkv)をまたいで利用させる[AWSサービス](#40hiw9)．

ToDo: [152](todo.md#todo-152)，[106](todo.md#todo-106)

<a id="mkyn41"></a>

## Amazon Virtual Private Cloud

[VPC](#4ln6ld)を提供する[AWSサービス](#40hiw9)．

<a id="totant"></a>

## Amazon Web Services

Amazon.com, Inc.の子会社であるAmazon Web Services, Inc.が提供する[クラウドコンピューティング](#yy3buk)の基盤．利用者は[AWSアカウント](#r2ghkv)の下で[AWSサービス](#40hiw9)を利用する．

<a id="o7jjj5"></a>

## Apache ZooKeeper

[ZooKeeperアンサンブル](#csow5k)が[znode](#xus9ny)からなる階層的な[名前空間](#m7lbe4)を保持し，[分散システム](#6cc980)をなすアプリケーションの協調に用いられるサービス．[znode](#xus9ny)により，設定の保持，[リーダー選出](#brj8ci)，[ロック](#7x5us3)を実装できる．書き込みは[線形化可能性](#q83z5h)を満たし，各[クライアント](#xv4m3d)の要求は送信順に実行される．読み取りは接続先の[サーバー](#uteg7y)が自身の状態から返し，最新の書き込みの反映は保証されない．[sync操作](#4665g9)でその状態を追いつかせる．

<a id="kp9j1c"></a>

## Application Load Balancer

[Elastic Load Balancing](#4l33a1)の[L7ロードバランサー](#irtyc8)で，[HTTP](#31abh6)の要求を，対象の[ホスト](#0qt5x4)，パス，クエリ，ヘッダ，メソッド，送信元の[IPアドレス](#3ksnfe)を条件とする規則に基づき[通信先](#b2znuk)に振り分けるもの．

<a id="avuc2r"></a>

## Assertion Consumer Service

[SAML](#yoebmp)において，[アイデンティティプロバイダ](#3z77qd)からの応答を受け付ける[サービスプロバイダ](#l5pssm)の[エンドポイント](#9i1lg3)．

<a id="yegu9n"></a>

## AssumeRole

[プリンシパル](#t8ujsy)が[IAMロール引受け](#0d235w)を要求する[AWS Security Token Service](#q44rf3)の操作．

<a id="yndlvl"></a>

## AssumeRoleWithSAML

[アイデンティティプロバイダ](#3z77qd)が発行した[SAMLアサーション](#m7caca)を示して[IAMロール引受け](#0d235w)を要求する[AWS Security Token Service](#q44rf3)の操作．要求に[プリンシパル](#t8ujsy)の[認証情報](#pyxpuc)を要さない．

<a id="lsp9h7"></a>

## AssumeRoleWithWebIdentity

[アイデンティティプロバイダ](#3z77qd)が発行した[IDトークン](#1bvsna)または[アクセストークン](#8w6s21)を示して[IAMロール引受け](#0d235w)を要求する[AWS Security Token Service](#q44rf3)の操作．要求に[プリンシパル](#t8ujsy)の[認証情報](#pyxpuc)を要さない．

<a id="qs2tbc"></a>

## Auto Scalingグループ

希望する数を望ましい状態とする[調整ループ](#gibl6s)により数を維持される[EC2インスタンス](#0d2awr)の集まり．希望する数は，指定した最小数と最大数の範囲で，[Amazon CloudWatch](#y77mp8)の[メトリクス](#1s1rpf)に基づく規則またはスケジュールに従って増減する．[ヘルスチェック](#4ofscj)に失敗した[EC2インスタンス](#0d2awr)を置き換える．

<a id="xeno3r"></a>

## Aレコード

所有者の[ドメイン名](#d8xx9q)に対応する[IPv4](#un6pgt)の[IPアドレス](#3ksnfe)を示す[資源レコード](#syx2b4)．

<a id="0ey58g"></a>

## BGP

[自律システム](#8wkkrz)の間で[経路](#5433mk)を交換する[パスベクタ型](#xj5xfp)の[ルーティングプロトコル](#ktkn70)．現行の版は4である．

<a id="gnpq9g"></a>

## BGP/MPLS IP VPN

[マルチプロトコル拡張](#hz8j1v)で顧客ごとの[経路](#5433mk)を交換し，[IPパケット](#w9btgk)を[MPLS](#bqd0v7)で運んで，顧客の拠点の間を事業者網上で他の顧客から隔離して接続する方式．顧客ごとの[経路](#5433mk)を[VRF](#3a4xlv)に保持し，[経路識別子](#dlraom)で区別し，[経路ターゲット](#4z8ok7)で取り込み先を定める．

<a id="y1mii1"></a>

## BGPコンフェデレーション

1つの[自律システム](#8wkkrz)を複数のメンバーASに分割し，メンバーASの間を[eBGP](#vz4jtn)と同様のセッションで接続する構成．外部からは単一の[自律システム](#8wkkrz)として見える．

<a id="v9rnch"></a>

## BGPスピーカー

[BGP](#0ey58g)を実行する[ルータ](#5f2okm)．[BGP識別子](#p2n7t4)で識別される．

<a id="s9mnt1"></a>

## BGPセッション

2つの[BGPスピーカー](#v9rnch)の間で[TCP](#cndtkv)の[ポート番号](#avetpx)179の[接続](#st4cz5)上に確立され，[経路](#5433mk)を交換する関係．[BGP状態機械](#gci3lp)がEstablishedに達したのち[UPDATEメッセージ](#zqwllr)を交換する．

<a id="xrq0o5"></a>

## BGPメッセージ

[BGPセッション](#s9mnt1)で交換する単位．マーカー，長さ，型からなる19[オクテット](#yimp6h)のヘッダをもつ．

<a id="gci3lp"></a>

## BGP状態機械

[BGPセッション](#s9mnt1)の確立過程を表す状態機械．Idle，Connect，Active，OpenSent，OpenConfirm，Establishedの6状態をとる．

<a id="p2n7t4"></a>

## BGP識別子

[BGPスピーカー](#v9rnch)に割り当てる4[オクテット](#yimp6h)の値．同じ[自律システム](#8wkkrz)内で一意である．

<a id="3svuh5"></a>

## Blink

[Chromium](#2aag3y)のレンダリングエンジン．[HTML](#n9liw2)と[CSS](#hks4qq)を解釈して[DOM](#mtrvw2)を構築し，[レンダリングパイプライン](#8wjced)のうち[ラスタライズ](#3o1tma)より前の段階を[メインスレッド](#663plp)で実行する．2013年にWebKitから分岐した．

<a id="ukqdvo"></a>

## BrowsingInstance

[Chromium](#2aag3y)において，[JavaScript](#y8ql3q)から互いに参照し合える可能性のある，[フレーム](#mtx2pq)の[木](#dj2zcx)の集合．[SiteInstance](#1811pf)に分かれる．

<a id="nk0zyz"></a>

## B木

各頂点が複数のキーと子をもち，全ての葉が同じ深さにある[平衡探索木](#duers5)．1つの頂点を記憶装置の1つの[ブロック](#k60l5g)に対応させ，操作あたりの[ブロック](#k60l5g)の読み書きを減らす．記憶装置上の[インデックス](#c5u142)の実現に用いられる．

<a id="drl0oo"></a>

## C++

[C言語](#4pg9c8)から派生した，[静的型付け](#c7sqk0)で[ガベージコレクション](#6exqbl)をもたない[プログラミング言語](#nw9j2i)．[未定義動作](#1d4gs1)を規格に含み，[メモリ安全性](#qbsksa)を保証しない．

ToDo: [141](todo.md#todo-141)

<a id="txuqj9"></a>

## C++オブジェクト

[C++](#drl0oo)における[データオブジェクト](#wvtf4u)で，[データ型](#w7t735)をもつもの．

<a id="yio0lk"></a>

## CAP定理

[レプリケーション](#rv2ppc)を行う[分散システム](#6cc980)は，計算機の間の通信が途絶して互いに通信できない部分に分かれたとき，[線形化可能性](#q83z5h)と，故障していない全ての計算機が要求に応答する可用性とを同時には満たせないという定理．

<a id="1r0j49"></a>

## CLUSTER_LIST

[経路リフレクタ](#iz5p1h)が[経路](#5433mk)を再広告するたびに自身の[クラスタID](#8rb2lo)を追加するオプション非推移の[パス属性](#q885vr)．[経路リフレクタ](#iz5p1h)は自身の[クラスタID](#8rb2lo)を含む[経路](#5433mk)を破棄する．

<a id="dsbf8s"></a>

## CNAMEレコード

所有者の[ドメイン名](#d8xx9q)が別名であることを示し，その正規の[ドメイン名](#d8xx9q)を示す[資源レコード](#syx2b4)．これをもつ[ドメイン名](#d8xx9q)は，[DNSSEC](#roxnj7)に関わるもの以外の[資源レコード](#syx2b4)をもたない．[名前解決](#tpx3c2)は正規の[ドメイン名](#d8xx9q)について続けられる．

<a id="yli8gq"></a>

## CORS

[サーバー](#uteg7y)が[HTTP](#31abh6)の応答で読み取りを許した[オリジン](#3f4vd8)の[Web文書](#qbtpp4)に，[Webブラウザ](#gcly3z)が[同一オリジンポリシー](#q18xj8)の拒む応答の読み取りを許す仕組み．

<a id="itq0mu"></a>

## CSMA/CA

送信前に媒体の空きを確かめ，空いていても乱数で定めた時間を待ってから送信することで，複数の送信者の衝突を避けて媒体を共有する方式．

<a id="hks4qq"></a>

## CSS

[Web文書](#qbtpp4)の要素の表示の仕方を，要素を選ぶセレクタと，プロパティと値の組からなる宣言とで記述する言語．

<a id="2aag3y"></a>

## Chromium

Googleが主導して開発する，[オープンソースライセンス](#kv40ye)で配布される[Webブラウザ](#gcly3z)．[Blink](#3svuh5)と[V8](#4qyfuw)を用い，[特権分離](#u90lkn)に基づき，[ブラウザプロセス](#ejqo3w)と，[レンダラープロセス](#53ckw6)，[GPUプロセス](#4hdszd)，[ユーティリティプロセス](#0lze03)を含む子の[プロセス](#lm3iq5)に分かれて動作する．Google ChromeとMicrosoft Edgeはこれを基にする．

<a id="ckmh8m"></a>

## Cinder

[仮想マシン](#uwly1k)に接続する[ブロックストレージ](#8ztcnx)を提供する[OpenStackサービス](#xb2kcb)．

<a id="4hf4xa"></a>

## ClusterRole

[Role](#3kkitq)と同じ形式の権限を[名前空間](#6bdul4)に属さずに定める[オブジェクト](#8ot6zr)．[名前空間](#6bdul4)に属さない種類の[オブジェクト](#8ot6zr)にも適用できる．

<a id="e37fh9"></a>

## ClusterRoleBinding

[ClusterRole](#4hf4xa)の権限を，[クラスタ](#dx7pxd)全体の範囲で[主体](#pyjgmb)に与える[オブジェクト](#8ot6zr)．

<a id="9ng0n3"></a>

## Code - OSS

[Visual Studio Code](#fqq24m)のソースコードを[MITライセンス](#d3w99m)で公開するリポジトリ．製品の[Visual Studio Code](#fqq24m)はこれに，Microsoftのブランド，[拡張機能](#1erfeu)の取得先の設定，利用情報の収集を加える独自の変更を施し，[プロプライエタリライセンス](#r4wode)で配布するものである．

<a id="gyxatn"></a>

## CompositorFrame

[Chromium](#2aag3y)において，[viz](#87mh85)へ送られる1回分の表示内容．[ラスタライズ](#3o1tma)済みの画像を参照する四辺形の列と，それぞれの位置，変形，透明度を記述する．

<a id="3x7wht"></a>

## ConfigMap

機密でない設定データをキーと値の組として保持し，[Pod](#k4ef3z)に環境変数，コマンド引数，[ボリューム](#0zbizc)内のファイルとして渡す[オブジェクト](#8ot6zr)．

<a id="kccq14"></a>

## Container Network Interface

[コンテナ](#uds0ak)の[ネットワークインターフェース](#cufd0s)の作成と設定を，[プラグイン](#dz7dp9)に委ねる仕様．

<a id="ttawc3"></a>

## Container Runtime Interface

[kubelet](#zh69qe)が[コンテナランタイム](#nl5o0m)に，[Pod](#k4ef3z)の実行環境と[コンテナ](#uds0ak)の作成，実行，停止を要求する仕様．

<a id="jhdprm"></a>

## Cookie

[サーバー](#uteg7y)が[HTTP](#31abh6)の応答で[Webブラウザ](#gcly3z)に保存させ，[Webブラウザ](#gcly3z)がそれの属する[ホスト](#0qt5x4)とパスの範囲への以後の要求に添えて送り返す，名前と値の組．

<a id="xxdsz9"></a>

## CronJob

分，時，日，月，曜日の5つの欄からなるcron形式の予定に従って[Job](#62xnqs)を作成する[ワークロードリソース](#qg1bbv)．

<a id="b5ztot"></a>

## CustomResourceDefinition

[カスタムリソース](#xo9y6e)の種類を[kube-apiserver](#yv6kx0)に追加する[オブジェクト](#8ot6zr)．

<a id="rq1bpp"></a>

## Cオブジェクト

[C言語](#4pg9c8)における[データオブジェクト](#wvtf4u)．寿命は[記憶域期間](#uvaml5)で定まる．

ToDo: [149](todo.md#todo-149)

<a id="oyypas"></a>

## C標準ライブラリ

[C言語](#4pg9c8)の規格が定める，ヘッダで宣言される関数，型，[マクロ](#3llsmk)の集合．

ToDo: [139](todo.md#todo-139)

<a id="4pg9c8"></a>

## C言語

[静的型付け](#c7sqk0)で[ガベージコレクション](#6exqbl)をもたない[プログラミング言語](#nw9j2i)．[ポインタ](#ubm34x)の算術演算と[未定義動作](#1d4gs1)を規格に含み，[メモリ安全性](#qbsksa)を保証しない．[サブルーチン](#y825lm)を関数と呼ぶ．ISOとIECにより標準化されている．

ToDo: [149](todo.md#todo-149)

<a id="lxov83"></a>

## DEPSファイル

[gclient](#djvjxt)が読む，リポジトリの依存先を記すファイル．Pythonの文法で書かれ，依存先ごとに配置先のパスと，取得するリポジトリと版を定める．同期の後に実行するコマンドも記す．

<a id="r86yg3"></a>

## DEVICE_OBJECT

[Windows NT](#jzpnq4)において，[I/O要求パケット](#dd3rvj)の宛先を表す[カーネルオブジェクト](#4d5j7r)．[カーネルモードドライバ](#fnr7ad)が作成する．作成したドライバの[DRIVER_OBJECT](#hbcm14)，ドライバが用途を決める拡張領域，直上に接続された[DEVICE_OBJECT](#r86yg3)への参照をもつ．この接続の連なりが[ドライバスタック](#u4t3xd)をなす．

<a id="x5u5e6"></a>

## DNAT

宛先の[IPアドレス](#3ksnfe)を書き換える[NAT](#4blq8k)．

<a id="v0yvpo"></a>

## DNS

[ドメイン名](#d8xx9q)と[資源レコード](#syx2b4)の対応を，[DNSゾーン](#2eh0s0)に分割して[権威DNSサーバー](#9es8da)に分散して保持し，[名前解決](#tpx3c2)で参照する体系．メッセージは[UDP](#7mvj8m)または[TCP](#cndtkv)の[ポート番号](#avetpx)53で運ばれる．

<a id="7wsrt3"></a>

## DNSKEYレコード

[DNSゾーン](#2eh0s0)の[DNSSEC](#roxnj7)の[公開鍵](#7xb1uk)を示す[資源レコード](#syx2b4)．

<a id="roxnj7"></a>

## DNSSEC

[資源レコード](#syx2b4)セットに[電子署名](#wr3566)を付し，応答の発信元と完全性を検証可能にする[DNS](#v0yvpo)の拡張．署名は[RRSIGレコード](#m4w5n1)に，[公開鍵](#7xb1uk)は[DNSKEYレコード](#7wsrt3)に置き，親の[DNSゾーン](#2eh0s0)は子の[DSレコード](#1hq998)を保持して署名する．検証者は[DNSルートサーバー](#p77v01)が保持する[DNSゾーン](#2eh0s0)の[公開鍵](#7xb1uk)を起点とし，[DNS委任](#dmv9zd)を辿る[信頼チェーン](#l7b2yn)により下位の[DNSゾーン](#2eh0s0)の[公開鍵](#7xb1uk)を信頼する．応答を[暗号化](#e382sn)しない．

<a id="2eh0s0"></a>

## DNSゾーン

[ドメイン名](#d8xx9q)の[名前空間](#m7lbe4)がなす[木](#dj2zcx)のうち，1つの管理者が[権威DNSサーバー](#9es8da)で管理する連結な部分．その根の[ドメイン名](#d8xx9q)に[SOAレコード](#sktwnj)と[NSレコード](#3qy5m1)をもつ．

<a id="7siuzh"></a>

## DNSラベル

[DNS](#v0yvpo)の階層的な[名前空間](#m7lbe4)がなす[木](#dj2zcx)の各頂点に付く，63[オクテット](#yimp6h)以下の名前．同じ親をもつ頂点の間で互いに異なり，根のものは空である．

<a id="p77v01"></a>

## DNSルートサーバー

[ドメイン名](#d8xx9q)の[木](#dj2zcx)の根を含む[DNSゾーン](#2eh0s0)を保持する[権威DNSサーバー](#9es8da)．a.root-servers.netからm.root-servers.netまでの13の名前をもち，それぞれ[エニーキャスト](#lz4omp)により多数の地点から提供される．[フルリゾルバ](#0n86br)はその[IPアドレス](#3ksnfe)を初期設定として保持する．

<a id="dmv9zd"></a>

## DNS委任

[DNSゾーン](#2eh0s0)の一部を下位の[DNSゾーン](#2eh0s0)として切り出し，その[権威DNSサーバー](#9es8da)を上位の[DNSゾーン](#2eh0s0)の[NSレコード](#3qy5m1)で示すこと．委任先の[権威DNSサーバー](#9es8da)の名前が下位の[DNSゾーン](#2eh0s0)に含まれるとき，上位の[DNSゾーン](#2eh0s0)はその[IPアドレス](#3ksnfe)を示すグルーレコードも保持する．

<a id="mtrvw2"></a>

## DOM

[Web文書](#qbtpp4)を節点の[木](#dj2zcx)として表し，[JavaScript](#y8ql3q)から参照・変更するための[API](#9e509k)．

<a id="hbcm14"></a>

## DRIVER_OBJECT

[Windows NT](#jzpnq4)において，読み込まれた1つの[カーネルモードドライバ](#fnr7ad)を表す[カーネルオブジェクト](#4d5j7r)．[I/Oマネージャ](#2wuacp)が作成してドライバの初期化の[サブルーチン](#y825lm)に渡す．[I/O要求パケット](#dd3rvj)の主機能コードごとの処理を並べた[操作表](#xxcrwp)，アンロード時の[サブルーチン](#y825lm)，そのドライバが作成した[DEVICE_OBJECT](#r86yg3)の一覧をもつ．

<a id="1hq998"></a>

## DSレコード

親の[DNSゾーン](#2eh0s0)に置かれ，子の[DNSゾーン](#2eh0s0)の[DNSKEYレコード](#7wsrt3)の[公開鍵](#7xb1uk)の[ハッシュ関数](#fnegr1)の値を示す[資源レコード](#syx2b4)．

<a id="anbgas"></a>

## DaemonSet

条件に合う全ての[ノード](#6qrxi1)で，それぞれ1つの[Pod](#k4ef3z)を実行する[ワークロードリソース](#qg1bbv)．

<a id="jt8i5n"></a>

## Debug Adapter Protocol

[テキストエディタ](#nud9su)と，[デバッガ](#49baql)を操作するデバッグアダプタの間の，[JSON](#o3ixrz)のメッセージを用いる[プロトコル](#bhk5im)．

ToDo: [151](todo.md#todo-151)

<a id="fv5438"></a>

## Deployment

[ReplicaSet](#9nbpfp)を介して[Pod](#k4ef3z)を管理する[ワークロードリソース](#qg1bbv)．テンプレートの変更を，既定では新旧の[ReplicaSet](#9nbpfp)の[Pod](#k4ef3z)の数を段階的に入れ替えるローリングアップデートで反映し，ロールバックのため旧[ReplicaSet](#9nbpfp)を保持する．

<a id="lppd9c"></a>

## Diffie-Hellman鍵共有

双方が自身の[秘密鍵](#dak54j)と相手の[公開鍵](#7xb1uk)から同じ秘密値を計算し，[共通鍵](#sie28z)の材料を得る方式．

<a id="4320z7"></a>

## EBSスナップショット

[EBSボリューム](#bauqgu)の[スナップショット](#ahlapd)を，前回のものから変更された[ブロック](#k60l5g)のみを保存する増分形式で保持するもの．[リージョンリソース](#tynhcw)であり，属する[リージョン](#1df8fw)の任意の[アベイラビリティゾーン](#zb3vp3)に[EBSボリューム](#bauqgu)として復元できる．

<a id="bauqgu"></a>

## EBSボリューム

[Amazon Elastic Block Store](#sxdluo)が提供する[ブロックストレージ](#8ztcnx)の[AWSリソース](#78qg7h)．1つの[アベイラビリティゾーン](#zb3vp3)に属し，同じ[アベイラビリティゾーン](#zb3vp3)の[EC2インスタンス](#0d2awr)に接続される．データは[EC2インスタンス](#0d2awr)の停止後も保持される．

<a id="0d2awr"></a>

## EC2インスタンス

[Amazon Elastic Compute Cloud](#y42e2r)が提供する計算環境で，[仮想マシン](#uwly1k)，または[ハイパーバイザ](#dt1rv7)を介さない物理計算機である[AWSリソース](#78qg7h)．1つの[サブネット](#oygsrp)に起動され，[インスタンスタイプ](#h08bfc)と[Amazon Machine Image](#f6a76h)により構成が定まる．

<a id="kqfpq2"></a>

## EGP

[自律システム](#8wkkrz)の間で[経路](#5433mk)を交換する[ルーティングプロトコル](#ktkn70)で，[BGP](#0ey58g)に置き換えられたもの．

<a id="ops4d2"></a>

## EPROCESS

[Windows NT](#jzpnq4)における[プロセス記述子](#smq3zz)で，[カーネルオブジェクト](#4d5j7r)である．先頭に[KPROCESS](#qz11sg)を埋め込み，識別番号，所属する[ETHREAD](#0j9726)の一覧，[HANDLE_TABLE](#8gu4x1)，[アクセストークン](#9ea3s0)，[仮想アドレス記述子](#h318rh)の集合，所属する[ジョブオブジェクト](#mmivp1)，[PEB](#hfgg6x)のアドレスをもつ．

ToDo: [148](todo.md#todo-148)

<a id="0j9726"></a>

## ETHREAD

[Windows NT](#jzpnq4)における[スレッド記述子](#nehk4w)で，[カーネルオブジェクト](#4d5j7r)である．先頭に[KTHREAD](#6offhs)を埋め込み，所属する[プロセス](#lm3iq5)と自身の識別番号の組，[偽装](#w6gowu)に用いる[アクセストークン](#9ea3s0)，発行した[I/O要求パケット](#dd3rvj)の一覧をもつ．

<a id="wyy1dc"></a>

## Elastic IPアドレス

[AWSアカウント](#r2ghkv)に割り当てられ，解放されるまで保持される，静的な[IPv4](#un6pgt)の[パブリックIPアドレス](#kwufcq)．[Elastic Network Interface](#f5pqfi)に関連付けて用いる．

<a id="4l33a1"></a>

## Elastic Load Balancing

複数の[アベイラビリティゾーン](#zb3vp3)にある[通信先](#b2znuk)へ通信を分散する[ロードバランサー](#v7r0tg)を提供する[AWSサービス](#40hiw9)．

<a id="f5pqfi"></a>

## Elastic Network Interface

[サブネット](#oygsrp)に属する仮想的な[ネットワークインターフェース](#cufd0s)．その[サブネット](#oygsrp)の[IPプレフィックス](#6rwn5e)に属する[IPv4](#un6pgt)の[IPアドレス](#3ksnfe)をもち，[セキュリティグループ](#zgzyka)が関連付けられる．

<a id="fkvuw7"></a>

## Electron

[contentモジュール](#e7u8nm)と[Node.js](#d76hl3)を組み合わせ，[HTML](#n9liw2)，[CSS](#hks4qq)，[JavaScript](#y8ql3q)で記述したプログラムを，[Webブラウザ](#gcly3z)の外で独立した[アプリケーション](#zxvj73)として動作させる基盤．

<a id="n5mrfc"></a>

## EndpointSlice

[Service](#3bb8t3)の[通信先](#b2znuk)の集合を保持する[オブジェクト](#8ot6zr)．属する[Service](#3bb8t3)は[ラベル](#zugz1v)kubernetes.io/service-nameで示される．保持する[通信先](#b2znuk)は，全て同じ形式（[IPv4](#un6pgt)の[IPアドレス](#3ksnfe)，[IPv6](#4elryy)の[IPアドレス](#3ksnfe)，[ドメイン名](#d8xx9q)のいずれか）のアドレスをもち，[ポート番号](#avetpx)，[トランスポートプロトコル](#dayw7g)（[TCP](#cndtkv)，[UDP](#7mvj8m)，[SCTP](#m38dhg)のいずれか），[Service](#3bb8t3)の対応するポートの名前の組の集合を共有する．各[通信先](#b2znuk)はアドレスと，ready，serving，terminatingの状態をもつ．servingは通信を受け付けられること，terminatingは終了処理中であること，readyはservingかつterminatingでないことを示す．[ラベルセレクタ](#x5w385)をもつ[Service](#3bb8t3)では[コントローラ](#pboh16)が自動で更新する．

<a id="le0zgf"></a>

## Ethernet

[MACアドレス](#sagh83)で送信元と宛先を示すデータの単位を，ケーブルを介して伝送する有線の[リンク](#xy3alb)の規格．IEEE 802.3で規定される．

<a id="jf67m5"></a>

## FILE_OBJECT

[Windows NT](#jzpnq4)において，ファイルまたは装置を開くごとに作成され，[開かれたファイル記述](#u8r1ic)を表す[カーネルオブジェクト](#4d5j7r)．対象の[DEVICE_OBJECT](#r86yg3)，開いたときに許可された共有の別，[ファイルシステム](#pp17bd)が用いる文脈への参照をもつ．

<a id="83suel"></a>

## FrameTreeNode

[contentモジュール](#e7u8nm)において，[フレーム](#mtx2pq)の[木](#dj2zcx)の頂点を表し，[ナビゲーション](#day4yo)を越えて存続する[C++オブジェクト](#txuqj9)．現在の[RenderFrameHost](#xir7fh)を保持する．

<a id="ofaawr"></a>

## FreeBSD

ベースシステムと呼ぶ，[カーネル](#cktjwx)と[ユーザーモード](#v7n2z8)で動作するコマンドおよびライブラリの集合を，1つのソースツリーで開発する[オペレーティングシステム](#c8v8vw)．[カーネル](#cktjwx)は[モノリシックカーネル](#ezqe8s)に分類され，[カーネルモジュール](#4995ja)による拡張をもつ．

ToDo: [144](todo.md#todo-144)，[130](todo.md#todo-130)

<a id="num0b7"></a>

## GENEVE

[ネットワーク](#uy18d2)の仮想化のために，データの単位を[UDP](#7mvj8m)で[カプセル化](#oh434k)して運ぶ[プロトコル](#bhk5im)．可変長のオプションをもつ．

<a id="bo0w3o"></a>

## GN

[Chromium](#2aag3y)のビルド定義を記述し，それから[Ninja](#w9mk1f)と[Siso](#41yxh0)が読む入力ファイルを生成するプログラム．ビルドの設定は出力ディレクトリごとのargs.gnに記述する．

<a id="o223t2"></a>

## GPU

多数の演算を並列に実行し，画像の生成に用いられる[プロセッサ](#4ad6s1)．

<a id="4hdszd"></a>

## GPUプロセス

[Chromium](#2aag3y)において，[GPU](#o223t2)へのアクセスを集約し，他の[プロセス](#lm3iq5)から受けた[GPU](#o223t2)への命令を実行する[プロセス](#lm3iq5)．[viz](#87mh85)が動作する．

<a id="c27kel"></a>

## GSM

ETSIが策定した，第2世代の[セルラー通信](#fibo1z)の規格．

<a id="uou6rr"></a>

## Gateway Load Balancer

[Elastic Load Balancing](#4l33a1)の[ロードバランサー](#v7r0tg)で，受信した[IPパケット](#w9btgk)を内容を変えずに[GENEVE](#num0b7)で[カプセル化](#oh434k)し，通信を検査する[仮想アプライアンス](#cmoqun)に振り分けるもの．

<a id="4d5lb9"></a>

## Glance

[マシンイメージ](#biu4lz)を登録，保管，配布する[OpenStackサービス](#xb2kcb)．

<a id="8gu4x1"></a>

## HANDLE_TABLE

[Windows NT](#jzpnq4)における，[オブジェクトハンドル](#6onm6b)の[ハンドル表](#n9vofr)．項目ごとに[OBJECT_HEADER](#z7evxc)への参照と許可されたアクセス権をもつ．

<a id="cqjacl"></a>

## HCL

HashiCorp, Inc.が開発した，ブロックと属性で構成を記述する言語．属性は名前と式の組である．

<a id="n9liw2"></a>

## HTML

[Web文書](#qbtpp4)の構造を，タグで区切った要素の入れ子で記述するマークアップ言語．

<a id="31abh6"></a>

## HTTP

[クライアント](#xv4m3d)がメソッドと対象を指定した要求を送り，[サーバー](#uteg7y)が状態コードを含む応答を返す[プロトコル](#bhk5im)．[TLS](#xqkfhy)で保護したものをHTTPSと呼ぶ．

<a id="duz73j"></a>

## HTTPエージェント

[監視主体](#90keyj)が[HTTP](#31abh6)の要求を送り，応答から値を得る[アイテムタイプ](#ugi5pv)．

<a id="gu5qq4"></a>

## Horizon

[OpenStackサービス](#xb2kcb)の[API](#9e509k)を呼び出して操作する，[Webブラウザ](#gcly3z)向けの管理画面を提供する[OpenStack](#pnydk7)の構成要素．

<a id="qgyieb"></a>

## HorizontalPodAutoscaler

[Pod](#k4ef3z)の[資源](#k7gc81)の使用量を含む観測値と目標値の比に基づき，[Pod](#k4ef3z)の数を指定する[ワークロードリソース](#qg1bbv)のその数を自動で増減する[オブジェクト](#8ot6zr)．

<a id="sl4ng3"></a>

## Hyperplane ENI

[AWS Lambda](#d2cxxc)が，[Lambda関数](#v7xjp0)に指定された[サブネット](#oygsrp)と[セキュリティグループ](#zgzyka)の組合せごとに，[実行ロール](#rkn7hg)の権限で作成する[リクエスターマネージド型ネットワークインターフェース](#8gfkr4)．[パブリックIPアドレス](#kwufcq)をもたない．同じ組合せを指定された[Lambda関数](#v7xjp0)の間で共有され，それらの通信の送信元は[NAPT](#9mze5p)によりこれの[IPアドレス](#3ksnfe)に書き換えられる．

ToDo: [123](todo.md#todo-123)

<a id="2wuacp"></a>

## I/Oマネージャ

[エグゼクティブ](#s3eb1d)において，入出力要求を[I/O要求パケット](#dd3rvj)として[カーネルモードドライバ](#fnr7ad)に配送する構成要素．

<a id="dd3rvj"></a>

## I/O要求パケット

[Windows NT](#jzpnq4)において，1つの入出力要求を表し，[I/Oマネージャ](#2wuacp)と[カーネルモードドライバ](#fnr7ad)の間で受け渡される[データ構造](#y9ua1k)．型名はIRPである．[ドライバスタック](#u4t3xd)の層ごとに1つの[IO_STACK_LOCATION](#entmen)をもち，データを置くバッファを[MDL](#rb5sfa)で表すことができる．

ToDo: [126](todo.md#todo-126)

<a id="ix9em5"></a>

## IAMアイデンティティ

[AWS Identity and Access Management](#nm8gp9)において，[アイデンティティベースポリシー](#feccnu)を付与できる実体．

<a id="ymfj7y"></a>

## IAMグループ

[IAMユーザー](#viavkt)の集まりである[IAMアイデンティティ](#ix9em5)．付与された[アイデンティティベースポリシー](#feccnu)は所属する[IAMユーザー](#viavkt)に適用される．[プリンシパル](#t8ujsy)とならず，入れ子にできない．

<a id="let9u3"></a>

## IAMポリシー

[プリンシパル](#t8ujsy)の要求の可否を定める，[JSON](#o3ixrz)で書かれた[ポリシー](#d3j3nj)．1つ以上の[ポリシーステートメント](#bhslyd)からなる．要求は[既定拒否](#kfuctl)と[拒否優先評価](#t93sgu)で評価される．

<a id="viavkt"></a>

## IAMユーザー

パスワードとアクセスキーを含む長期の[認証情報](#pyxpuc)を用い，[プリンシパル](#t8ujsy)となる[IAMアイデンティティ](#ix9em5)．

<a id="k1a9js"></a>

## IAMロール

長期の[認証情報](#pyxpuc)をもたない[IAMアイデンティティ](#ix9em5)．[IAMロール引受け](#0d235w)の対象である．

<a id="0d235w"></a>

## IAMロール引受け

[信頼ポリシー](#x633ta)が許す[プリンシパル](#t8ujsy)，または許す[アイデンティティプロバイダ](#3z77qd)に[認証](#l2zofw)された[主体](#pyjgmb)が，[AWS Security Token Service](#q44rf3)が発行する一時的な[認証情報](#pyxpuc)を得て，[IAMロール](#k1a9js)のセッションとして[プリンシパル](#t8ujsy)となる[権限引受け](#5bn6hq)．

<a id="1bvsna"></a>

## IDトークン

[OpenIDプロバイダ](#r35zaj)が[認可エンドポイント](#17zvxp)または[トークンエンドポイント](#f9akzj)から発行する，[JSON Web Token](#llm2wm)の形式の[認証アサーション](#ki350n)．宛先を[リライングパーティ](#25f1g6)の[クライアントID](#rhlnw8)で示す．

<a id="sekyc5"></a>

## IGP

[自律システム](#8wkkrz)の内部で用いる[ルーティングプロトコル](#ktkn70)．宛先への[経路](#5433mk)ごとにコストと呼ぶ値を計算し，それが最小のものを選ぶ．

<a id="entmen"></a>

## IO_STACK_LOCATION

[I/O要求パケット](#dd3rvj)のうち，[ドライバスタック](#u4t3xd)の1つの層が処理する部分．要求の種類を表す主機能コードと副機能コード，種類ごとの引数，対象の[FILE_OBJECT](#jf67m5)と[DEVICE_OBJECT](#r86yg3)をもつ．各層は，下の層に要求を渡す前に下の層のIO_STACK_LOCATIONを設定する．

<a id="6v61y9"></a>

## IP

[ルータ](#5f2okm)が[IPパケット](#w9btgk)を宛先の[IPアドレス](#3ksnfe)に従って[中継](#zgr0mv)し，送信元から宛先へ届ける[プロトコル](#bhk5im)．到達と順序を保証しない．版に[IPv4](#un6pgt)と[IPv6](#4elryy)がある．

<a id="ofv8m2"></a>

## IPVS

[Linux](#eh8l2u)の[カーネル](#cktjwx)において，[Netfilter](#feag1h)の上に実装された[L4ロードバランサー](#3vn37b)．[通信先](#b2znuk)の選択に[ラウンドロビン](#odhunt)と[最小接続](#avov3h)を含む複数の方式から選べる．

<a id="un6pgt"></a>

## IPv4

32ビットの[IPアドレス](#3ksnfe)を用いる[IP](#6v61y9)の版．

<a id="4elryy"></a>

## IPv6

128ビットの[IPアドレス](#3ksnfe)を用いる[IP](#6v61y9)の版．

<a id="3ksnfe"></a>

## IPアドレス

[IPパケット](#w9btgk)の送信元と宛先を示す，[ネットワークインターフェース](#cufd0s)の識別子．ビット数は[IP](#6v61y9)の版により定まる．

<a id="w9btgk"></a>

## IPパケット

[IP](#6v61y9)で転送されるデータの単位．送信元と宛先の[IPアドレス](#3ksnfe)を含むヘッダをもつ．

ToDo: [153](todo.md#todo-153)

<a id="6rwn5e"></a>

## IPプレフィックス

[IPアドレス](#3ksnfe)の上位から指定したビット数を固定して表すアドレス範囲．先頭の[IPアドレス](#3ksnfe)と，固定するビット数であるプレフィックス長の組で表記する．

<a id="nwgavk"></a>

## IXP

多数の[自律システム](#8wkkrz)が，[ルータ](#5f2okm)を介さずに互いに直接通信できる共有の[ネットワーク](#uy18d2)に接続し，[AS間ピアリング](#z1q1fs)を行う施設．

<a id="hih6s5"></a>

## IaaS

計算機，[ネットワーク](#uy18d2)，[記憶域](#kltl5m)を提供し，その上の[オペレーティングシステム](#c8v8vw)から上を利用者が管理する[クラウドコンピューティング](#yy3buk)の形態．

<a id="5mx2oh"></a>

## Identity Centerインスタンス

[AWS IAM Identity Center](#cdv3og)において，[Identity Centerユーザー](#ypfrjn)とそのアクセス先の割り当てを保持する単位．有効化した1つの[リージョン](#1df8fw)をプライマリリージョンとし，そこで管理される．

ToDo: [122](todo.md#todo-122)

<a id="97jks3"></a>

## Identity Centerグループ

[Identity Centerインスタンス](#5mx2oh)が保持する[Identity Centerユーザー](#ypfrjn)の集まり．これに対する割り当ては所属する[Identity Centerユーザー](#ypfrjn)に及ぶ．

<a id="ypfrjn"></a>

## Identity Centerユーザー

[Identity Centerインスタンス](#5mx2oh)が保持する，人を表す[主体](#pyjgmb)．

<a id="gq4l0t"></a>

## Infrastructure as Code

基盤を構成する実体を機械が読める文書に宣言し，その文書に従って実体を作成，更新，削除する管理の手法．

<a id="2vlun8"></a>

## Ingress

[クラスタ](#dx7pxd)外からの[HTTP](#31abh6)の要求を，対象の[ホスト](#0qt5x4)とパスに基づいて[Service](#3bb8t3)へ振り分ける規則を記述する[オブジェクト](#8ot6zr)．規則を実現するのはIngressを監視する[コントローラ](#pboh16)であり，それが動作していなければ効果をもたない．

<a id="ntrf3f"></a>

## Ironic

物理計算機の登録，起動，[オペレーティングシステム](#c8v8vw)の導入を行う[OpenStackサービス](#xb2kcb)．

<a id="2t5b12"></a>

## JITコンパイル

プログラムの実行中に，その一部を[コンパイラ](#a2nw9z)で[機械語](#ky7oww)に翻訳して実行する手法．

<a id="o3ixrz"></a>

## JSON

名前と値の組の集合であるオブジェクト，配列，文字列，数，真偽値，nullを値とし，値を入れ子にしてデータを表すテキストの形式．

<a id="llm2wm"></a>

## JSON Web Token

当事者間で伝える主張の集合を[JSON](#o3ixrz)のオブジェクトで表し，URLに含められる文字列に符号化した形式．[認証子](#uft843)を付すものと暗号化するものがある．

<a id="ftrcpb"></a>

## JSON-RPC

要求，応答，通知を[JSON](#o3ixrz)のオブジェクトで表す遠隔手続き呼出しの[プロトコル](#bhk5im)．要求はメソッド名，引数，識別子をもち，応答は同じ識別子と，結果またはエラーをもつ．通知は識別子をもたず，応答されない．転送の方式を定めない．

<a id="y8ql3q"></a>

## JavaScript

ECMAScriptとして標準化された，[動的型付け](#zdjtf4)の[プログラミング言語](#nw9j2i)．[Web文書](#qbtpp4)中のスクリプトの記述に用いられる．

<a id="62xnqs"></a>

## Job

指定数の[Pod](#k4ef3z)が正常終了するまで，指定された回数の範囲で失敗した[Pod](#k4ef3z)を再試行する[ワークロードリソース](#qg1bbv)．

<a id="niq3ho"></a>

## KEEPALIVEメッセージ

ヘッダのみからなる[BGPメッセージ](#xrq0o5)．[OPENメッセージ](#x55k1n)の受理の通知と，[ホールドタイム](#ptmib9)の満了を防ぐ[ハートビート](#5urygr)に用いる．

<a id="eft4k3"></a>

## KPCR

[Windows NT](#jzpnq4)において，[プロセッサ](#4ad6s1)ごとに1つ存在し，[KPRCB](#e51swk)を埋め込む[データ構造](#y9ua1k)．[特権モード](#uk5ihn)では，x64ではGSセグメントが，x86ではFSセグメントがこれを指す．

<a id="e51swk"></a>

## KPRCB

[KPCR](#eft4k3)に埋め込まれる，[NTカーネル層](#oobie1)が[プロセッサ](#4ad6s1)ごとに用いる部分．その[プロセッサ](#4ad6s1)で実行中の[KTHREAD](#6offhs)，次に実行する[KTHREAD](#6offhs)，実行すべき[スレッド](#ou7dup)がないときに実行する[KTHREAD](#6offhs)，[スレッド優先度](#4dqyyj)ごとの実行可能な[KTHREAD](#6offhs)の[待ち行列](#lhxknx)，[遅延プロシージャ呼び出し](#ajw0fy)の[待ち行列](#lhxknx)をもつ．

<a id="qz11sg"></a>

## KPROCESS

[EPROCESS](#ops4d2)の先頭に埋め込まれる，[NTカーネル層](#oobie1)が用いる部分．[プロセッサ](#4ad6s1)に設定する[仮想記憶](#ysrn1f)の対応付けの起点の[物理メモリ](#svua87)上のアドレス，基本の[スレッド優先度](#4dqyyj)，所属する[KTHREAD](#6offhs)の一覧をもつ．

<a id="6offhs"></a>

## KTHREAD

[ETHREAD](#0j9726)の先頭に埋め込まれる，[NTカーネル層](#oobie1)が用いる部分．[スケジューラ](#wpudzb)が用いる状態と[スレッド優先度](#4dqyyj)，[特権モード](#uk5ihn)で用いる[スタック](#hfx60b)，[TEB](#lnr2ip)のアドレス，所属する[KPROCESS](#qz11sg)への参照をもつ．

ToDo: [136](todo.md#todo-136)

<a id="693zzd"></a>

## Keystone

利用者の[認証](#l2zofw)と[トークン](#qt96h9)の発行，利用者への[OpenStackプロジェクト](#ek1129)ごとのロールの割当て，[OpenStackサービス](#xb2kcb)の接続先の一覧の提供を行う[OpenStackサービス](#xb2kcb)．

<a id="t6cr2a"></a>

## Kubernetes

[オブジェクト](#8ot6zr)として宣言された望ましい状態に，[コントローラ](#pboh16)の[調整ループ](#gibl6s)により[コンテナ](#uds0ak)の実行状態を一致させ続ける[コンテナオーケストレーション](#ldx08d)のシステム．[クラスタ](#dx7pxd)を単位として動作する．

<a id="3vn37b"></a>

## L4ロードバランサー

[IPアドレス](#3ksnfe)と[ポート番号](#avetpx)に基づいて[通信先](#b2znuk)を選ぶ[ロードバランサー](#v7r0tg)．

<a id="irtyc8"></a>

## L7ロードバランサー

[トランスポートプロトコル](#dayw7g)が運ぶアプリケーションの要求の内容に基づいて[通信先](#b2znuk)を選ぶ[ロードバランサー](#v7r0tg)．要求の内容を読むため，[リバースプロキシ](#dnckyf)として動作する．

<a id="ilzwkt"></a>

## LIST_ENTRY

[Windows NT](#jzpnq4)において，双方向の環状の[埋め込み連結リスト](#0qdj5m)をつくるために要素に埋め込む[構造体](#0fq59c)．前後のLIST_ENTRYへの参照の組からなる．

<a id="dkfxg4"></a>

## LLDルール

[ホスト](#y3ka2w)上の監視対象を検出し，検出結果ごとにプロトタイプを具体化して[アイテム](#as86xt)，[トリガー](#3gz3w5)，グラフ，[ホスト](#y3ka2w)を生成する規則．

ToDo: [103](todo.md#todo-103)

<a id="dalaa4"></a>

## LOCAL_PREF

[自律システム](#8wkkrz)内での[経路](#5433mk)の優先度を示す周知任意の[パス属性](#q885vr)．値が大きいものを優先する．[自律システム](#8wkkrz)の外部へは伝えない．

<a id="up9tp4"></a>

## LTE

[3GPP](#8hltrb)が策定した，第4世代の[セルラー通信](#fibo1z)の規格．

<a id="9tfla3"></a>

## LVM

[Linux](#eh8l2u)において，[物理ボリューム](#uj3w47)を[ボリュームグループ](#um9c12)にまとめ，その[記憶域](#kltl5m)から[論理ボリューム](#es46jv)を切り出す仕組み．[device-mapper](#aqu8xq)の上に実装され，構成の[メタデータ](#f7of70)を各[物理ボリューム](#uj3w47)に保存する．

<a id="sfe9pj"></a>

## LVMスナップショット

元の[論理ボリューム](#es46jv)の[スナップショット](#ahlapd)を，[コピーオンライト](#q33a7g)により保持する[論理ボリューム](#es46jv)．

<a id="v7xjp0"></a>

## Lambda関数

[AWS Lambda](#d2cxxc)が実行するコードと設定の単位．[イベント](#35wv5r)を受けて，または直接の呼び出しにより起動され，[実行ロール](#rkn7hg)の権限で[AWSサービス](#40hiw9)を呼び出す．[サブネット](#oygsrp)と[セキュリティグループ](#zgzyka)を指定されたものは，すべての通信を[Hyperplane ENI](#sl4ng3)を経由して行い，指定されないものは[AWS Lambda](#d2cxxc)が管理する[VPC](#4ln6ld)から[インターネット](#3qoztf)に接続する．

<a id="dfaxj3"></a>

## Language Server Protocol

[テキストエディタ](#nud9su)と[言語サーバー](#69tuqj)の間の，[JSON-RPC](#ftrcpb)に基づく[プロトコル](#bhk5im)．M個の[テキストエディタ](#nud9su)とN個の[プログラミング言語](#nw9j2i)への対応を，個別の実装によるM×NからM+Nに減らす．

ToDo: [151](todo.md#todo-151)

<a id="eh8l2u"></a>

## Linux

[モノリシックカーネル](#ezqe8s)に分類され，[カーネルモジュール](#4995ja)による拡張をもつ[カーネル](#cktjwx)．

ToDo: [144](todo.md#todo-144)，[126](todo.md#todo-126)，[102](todo.md#todo-102)

<a id="rmoy1r"></a>

## Linux名前空間

[Linux](#eh8l2u)において[資源隔離](#1sgoxr)を行う機構．大域的な[資源](#k7gc81)を包み，所属する[プロセス](#lm3iq5)に独立した[資源](#k7gc81)の実体をもつように見せる．

ToDo: [147](todo.md#todo-147)，[127](todo.md#todo-127)

<a id="d67w81"></a>

## Loc-RIB

[Adj-RIB-In](#e55vmk)の要素にインポートの[ルーティングポリシー](#4bwmon)を適用し，[最良経路選択](#raisax)で宛先ごとに選んだ[経路](#5433mk)の集合．[経路表](#dw7079)への登録の元となる．

<a id="u6gjh1"></a>

## MAC

データと[共通鍵](#sie28z)から作成し，同じ[共通鍵](#sie28z)で検証する[認証子](#uft843)．

<a id="sagh83"></a>

## MACアドレス

IEEE 802の規格に従う[リンク](#xy3alb)における，48ビットの[ハードウェアアドレス](#le1wss)．

<a id="skno5x"></a>

## MCPクライアント

[MCPホスト](#wxqazg)が[MCPサーバー](#fimtpo)ごとに1つ保持し，その[MCPサーバー](#fimtpo)と[Model Context Protocol](#9pk9iy)で接続する[クライアント](#xv4m3d)．

ToDo: [150](todo.md#todo-150)

<a id="fimtpo"></a>

## MCPサーバー

[Model Context Protocol](#9pk9iy)に従い，[MCPリソース](#to0ng2)，[MCPツール](#lrik9i)，[MCPプロンプト](#lv4fgp)を[MCPクライアント](#skno5x)に提供する[サーバー](#uteg7y)．

ToDo: [150](todo.md#todo-150)

<a id="lrik9i"></a>

## MCPツール

[MCPサーバー](#fimtpo)が公開する，[大規模言語モデル](#q89hwf)の判断で呼び出され，処理を行う機能．

ToDo: [116](todo.md#todo-116)

<a id="lv4fgp"></a>

## MCPプロンプト

[MCPサーバー](#fimtpo)が公開する，利用者が選んで[大規模言語モデル](#q89hwf)に与える定型の指示文．

ToDo: [116](todo.md#todo-116)

<a id="wxqazg"></a>

## MCPホスト

[大規模言語モデル](#q89hwf)を利用し，[MCPクライアント](#skno5x)を通じて[MCPサーバー](#fimtpo)に接続する[アプリケーション](#zxvj73)．

<a id="to0ng2"></a>

## MCPリソース

[MCPサーバー](#fimtpo)が公開する，読み取られて[大規模言語モデル](#q89hwf)への入力となるデータ．

<a id="rb5sfa"></a>

## MDL

[Windows NT](#jzpnq4)において，[アドレス空間](#rygcc4)上の連続するバッファの開始アドレスと長さ，それを格納する[ページフレーム](#4qztd7)の番号の列を表す[データ構造](#y9ua1k)．

<a id="ge0o29"></a>

## MED

隣接する[自律システム](#8wkkrz)に対し，複数の接続点のうち望ましい入口を示すオプション非推移の[パス属性](#q885vr)．値が小さいものを優先する．標準の手順では，同じ隣接[自律システム](#8wkkrz)から受信した[経路](#5433mk)の間でのみ比較し，受信した[自律システム](#8wkkrz)の外部へは伝えない．

<a id="d3w99m"></a>

## MITライセンス

著作権表示と許諾表示を複製物に含めることのみを条件とし，無保証である[オープンソースライセンス](#kv40ye)．

<a id="bqd0v7"></a>

## MPLS

パケットに[MPLSラベル](#9vqomq)を付加し，通過する各[ルータ](#5f2okm)が[MPLSラベル](#9vqomq)を付け替えて[中継](#zgr0mv)する転送方式．

<a id="9vqomq"></a>

## MPLSラベル

[MPLS](#bqd0v7)でパケットに付加され，転送先の決定に用いられる20ビットの値．

<a id="n3w9i9"></a>

## MXレコード

所有者の[ドメイン名](#d8xx9q)宛ての電子メールを受け取る計算機の[ドメイン名](#d8xx9q)と，その優先度を示す[資源レコード](#syx2b4)．優先度の値の小さいものが優先される．

<a id="jx17v3"></a>

## MiraclePtr

[Chromium](#2aag3y)において，参照されている間に解放された領域を[PartitionAlloc](#8ahx0c)が再利用せずに隔離することで，[解放後使用](#onqz9u)の悪用を防ぐ仕組み．[C++](#drl0oo)の[ポインタ](#ubm34x)の[データ型](#w7t735)raw_ptrとして用いられる．

<a id="9pk9iy"></a>

## Model Context Protocol

[MCPホスト](#wxqazg)が外部のデータと機能を取り込む方法を定める，[MCPクライアント](#skno5x)と[MCPサーバー](#fimtpo)の間の，[JSON-RPC](#ftrcpb)に基づく[プロトコル](#bhk5im)．接続の初めに互いが対応する機能を交換する．規格が定める転送の方式は標準入出力と[HTTP](#31abh6)である．Anthropicが策定した．

<a id="n32mlc"></a>

## Mojo

[Chromium](#2aag3y)の[プロセス間通信](#vjg5ws)の基盤．[メッセージパイプ](#xnwjk2)，[共有メモリ](#76g0nk)，[データパイプ](#hymk0a)を提供し，同じ[プロセス](#lm3iq5)内の[スレッド](#ou7dup)の間の通信にも用いられる．

<a id="rjnxdg"></a>

## Mojom

[Mojoインターフェース](#q1r1b6)を記述する言語．その記述から各言語の[Remote](#g3yk27)と[Receiver](#gz9wdq)が生成される．

<a id="q1r1b6"></a>

## Mojoインターフェース

[Mojom](#rjnxdg)で記述されたメソッドの集まり．メソッドの呼び出しは[メッセージパイプ](#xnwjk2)上のメッセージとして運ばれる．

<a id="9mze5p"></a>

## NAPT

送信元の[IPアドレス](#3ksnfe)と[ポート番号](#avetpx)を書き換え，複数の[端点](#b084uv)に1つの[IPアドレス](#3ksnfe)を共有させる[SNAT](#3uc35a)．

<a id="4blq8k"></a>

## NAT

[IPパケット](#w9btgk)のヘッダの[IPアドレス](#3ksnfe)を書き換えて[中継](#zgr0mv)する機構．[トランスポートプロトコル](#dayw7g)の[ポート番号](#avetpx)もあわせて書き換えるものがある．書換えの対応を保持し，応答の[IPパケット](#w9btgk)には逆の書換えを施す．通信の[端点](#b084uv)は書換えの前後で変わらない．

<a id="2ii7xa"></a>

## NATゲートウェイ

[プライベートサブネット](#vds2br)の[Elastic Network Interface](#f5pqfi)から[VPC](#4ln6ld)外への接続を[NAPT](#9mze5p)で[中継](#zgr0mv)し，外部からの接続の開始を受け付けない[AWSリソース](#78qg7h)．1つの[サブネット](#oygsrp)に[リクエスターマネージド型ネットワークインターフェース](#8gfkr4)をもつ．

ToDo: [123](todo.md#todo-123)

<a id="2js4sd"></a>

## NEXT_HOP

[経路](#5433mk)の宛先へ向かう[IPパケット](#w9btgk)の転送先の[IPアドレス](#3ksnfe)を示す周知必須の[パス属性](#q885vr)．[eBGP](#vz4jtn)で広告するときは，受信者と共有する[IPプレフィックス](#6rwn5e)に属する第三者の[IPアドレス](#3ksnfe)を示す場合を除き，送信者自身のものに設定する．[iBGP](#f6yd97)で広告するときは，明示的な設定がない限り変更しない．

<a id="pks2n8"></a>

## NLRI

[UPDATEメッセージ](#zqwllr)で到達可能として広告する[IPプレフィックス](#6rwn5e)の列．1つのメッセージに含まれるものは同じ[パス属性](#q885vr)を共有する．

<a id="xds7yl"></a>

## NOTIFICATIONメッセージ

エラーを検出した[BGPスピーカー](#v9rnch)が送る[BGPメッセージ](#xrq0o5)．送信後に[BGPセッション](#s9mnt1)を閉じる．

<a id="3qy5m1"></a>

## NSレコード

所有者の[ドメイン名](#d8xx9q)を根とする[DNSゾーン](#2eh0s0)の[権威DNSサーバー](#9es8da)の名前を示す[資源レコード](#syx2b4)．

<a id="42ymz9"></a>

## NTFS

[Windows NT](#jzpnq4)自身を格納する[ブロックデバイス](#1frbzb)に用いられる[ファイルシステム](#pp17bd)．全てのファイルを[マスターファイルテーブル](#uyne50)で管理し，[メタデータ](#f7of70)の変更に[ログ先行書き込み](#w0f35w)を用いて整合性を回復可能にする．

<a id="oobie1"></a>

## NTカーネル層

[ntoskrnl.exe](#tguf9f)のうち，[エグゼクティブ](#s3eb1d)の下に位置し，[スケジューラ](#wpudzb)，[割り込み](#owu45r)と[例外](#zyyhvv)の配送，[プロセッサ](#4ad6s1)間の同期を実装する層．

<a id="feag1h"></a>

## Netfilter

[Linux](#eh8l2u)の[カーネル](#cktjwx)において，[Netfilterフック](#ljpkdd)に登録された処理を[IPパケット](#w9btgk)ごとに呼び出す枠組み．[接続追跡](#d1bl1o)はこの上に実装され，[NAT](#4blq8k)はそれに基づき，接続の最初の[IPパケット](#w9btgk)で書換えを決め，以後の[IPパケット](#w9btgk)に同じ書換えを適用する．

ToDo: [126](todo.md#todo-126)

<a id="2tvkpf"></a>

## Netfilterテーブル

[Netfilter](#feag1h)に設定する規則の最上位の単位で，[チェイン](#0jljvq)をまとめるもの．

<a id="ljpkdd"></a>

## Netfilterフック

[Linux](#eh8l2u)の[カーネル](#cktjwx)が[IPパケット](#w9btgk)を処理する過程の点．受信直後のPREROUTING，自計算機宛てのINPUT，転送されるFORWARD，自計算機が送信するOUTPUT，送信直前のPOSTROUTINGがある．

<a id="mddvjx"></a>

## Network Load Balancer

[Elastic Load Balancing](#4l33a1)の[L4ロードバランサー](#3vn37b)で，[TCP](#cndtkv)，[UDP](#7mvj8m)，[TLS](#xqkfhy)の接続を[通信先](#b2znuk)に振り分けるもの．[アベイラビリティゾーン](#zb3vp3)ごとに静的な[IPアドレス](#3ksnfe)をもつ．

ToDo: [123](todo.md#todo-123)

<a id="qvr78w"></a>

## NetworkPolicy

[ラベルセレクタ](#x5w385)で選んだ[Pod](#k4ef3z)について，許可する入出力の通信を，相手の[Pod](#k4ef3z)，[名前空間](#6bdul4)，[IPプレフィックス](#6rwn5e)と[ポート番号](#avetpx)で指定する[オブジェクト](#8ot6zr)．ある方向についていずれかのNetworkPolicyに選ばれた[Pod](#k4ef3z)には，その方向の通信に，それを選ぶ全てのNetworkPolicyによる[許可加算評価](#kirdkx)が適用される．実施は[Container Network Interface](#kccq14)の[プラグイン](#dz7dp9)が担い，対応しない[プラグイン](#dz7dp9)では効果をもたない．

<a id="rjpynz"></a>

## Neutron

[OpenStackプロジェクト](#ek1129)ごとに[仮想ネットワーク](#cos7bu)，その[サブネット](#e9v7rv)，[ルータ](#5f2okm)を提供する[OpenStackサービス](#xb2kcb)．

<a id="w9mk1f"></a>

## Ninja

入力ファイルに記された依存関係に従い，更新が必要な成果物のみを並列に作り直す[ビルドシステム](#ci6jok)．

<a id="um196p"></a>

## NoSQL

[リレーショナルモデル](#7y7vys)以外の[データモデル](#7qyeyy)に従う[データベース](#vlgsmo)の総称．

<a id="d76hl3"></a>

## Node.js

[V8](#4qyfuw)を用いて，[Webブラウザ](#gcly3z)の外で[JavaScript](#y8ql3q)を実行する実行環境．

<a id="8rmhxx"></a>

## Noise Protocol Framework

[Noiseハンドシェイクパターン](#fg9gpw)に従って[Diffie-Hellman鍵共有](#lppd9c)を行い，その結果と[ハッシュ関数](#fnegr1)から[共通鍵](#sie28z)を導出し，[認証付き暗号](#p3b37s)で後続のメッセージを保護する[プロトコル](#bhk5im)を構成する枠組み．

<a id="fg9gpw"></a>

## Noiseハンドシェイクパターン

[Noise Protocol Framework](#8rmhxx)で，双方が事前に知る[公開鍵](#7xb1uk)の有無，ハンドシェイクメッセージの送受信順序，公開鍵の送信と[Diffie-Hellman鍵共有](#lppd9c)の実行順序を定めるもの．

<a id="csa1sf"></a>

## Nova

計算機を提供する[OpenStackサービス](#xb2kcb)．[ハイパーバイザ](#dt1rv7)を制御して[仮想マシン](#uwly1k)を作成，起動，停止，削除し，[Ironic](#ntrf3f)を通じて物理計算機も提供する．提供先の計算機は[Placement](#g55hns)の記録に基づいて選ぶ．

<a id="2epxko"></a>

## OAuth

[認可クライアント](#47yah2)が[認可サーバー](#kvuagh)から[アクセストークン](#8w6s21)を得て，それを添えた要求で[リソースサーバー](#6lul9i)の[保護対象](#qfjrzs)を操作する，[HTTP](#31abh6)上の[認可](#8esn53)の枠組み．[主体](#pyjgmb)の許可を得て操作する場合も，[認可クライアント](#47yah2)は[主体](#pyjgmb)の[認証情報](#pyxpuc)を得ない．現行の版は2.0である．

<a id="h4zpdj"></a>

## OBJECT_ATTRIBUTES

[ネイティブAPI](#kdca50)で[カーネルオブジェクト](#4d5j7r)を作成するとき，または開くときに渡す[データ構造](#y9ua1k)．[UNICODE_STRING](#flb10w)による[オブジェクト名前空間](#ivjde9)での名前，名前の解釈の起点とする[オブジェクトハンドル](#6onm6b)，大文字と小文字の区別と[オブジェクトハンドル](#6onm6b)の継承の可否を含むフラグ，作成時に設定する[セキュリティ記述子](#28ts3b)をもつ．

<a id="z7evxc"></a>

## OBJECT_HEADER

[Windows NT](#jzpnq4)において，各[カーネルオブジェクト](#4d5j7r)の本体の直前に置かれ，[オブジェクトマネージャ](#qwhtqy)が用いる[データ構造](#y9ua1k)．参照の数，[オブジェクトハンドル](#6onm6b)の数，[OBJECT_TYPE](#bws476)を識別する値，[セキュリティ記述子](#28ts3b)への参照をもつ．[オブジェクト名前空間](#ivjde9)での名前は，これより前に置かれる追加の部分にもつ．

<a id="bws476"></a>

## OBJECT_TYPE

[Windows NT](#jzpnq4)において，[カーネルオブジェクト](#4d5j7r)の種類ごとに1つ存在する[データ構造](#y9ua1k)．種類の名前と，その種類の[カーネルオブジェクト](#4d5j7r)を開く，閉じる，削除する，名前を解析するときに[オブジェクトマネージャ](#qwhtqy)が用いる[操作表](#xxcrwp)をもつ．

<a id="hlovu1"></a>

## OOPIF

[サイト分離](#guozy4)により，親と異なる[レンダラープロセス](#53ckw6)で処理される子の[フレーム](#mtx2pq)．

<a id="x55k1n"></a>

## OPENメッセージ

[BGPセッション](#s9mnt1)の確立時に最初に交換する[BGPメッセージ](#xrq0o5)．版，送信者の[AS番号](#wvk6j6)，[ホールドタイム](#ptmib9)，[BGP識別子](#p2n7t4)，[ケイパビリティ](#6vfi5n)を伝える．

<a id="uhgta7"></a>

## ORB

[ネットワークサービス](#cxvq7l)が，[レンダラープロセス](#53ckw6)が[CORS](#yli8gq)によらずに要求した異なる[オリジン](#3f4vd8)の応答のうち，画像，音声，動画，スクリプト，スタイルシートとして埋め込めないものを，[レンダラープロセス](#53ckw6)に渡さない機構．[サイト分離](#guozy4)を補う．

<a id="zfmc8n"></a>

## ORIGIN

[経路](#5433mk)の発生源を示す周知必須の[パス属性](#q885vr)．値は，発生元の[自律システム](#8wkkrz)の内部で生じたことを示す0，[EGP](#kqfpq2)で学習したことを示す1，その他の手段で学習したことを示す2のいずれかである．

<a id="rrbnra"></a>

## ORIGINATOR_ID

[経路リフレクタ](#iz5p1h)が付すオプション非推移の[パス属性](#q885vr)で，[経路](#5433mk)を[自律システム](#8wkkrz)内に最初に持ち込んだ[BGPスピーカー](#v9rnch)の[BGP識別子](#p2n7t4)を示す．スピーカーは自身を示すこの属性をもつ[経路](#5433mk)を破棄する．

<a id="ac26sv"></a>

## Oilpan

[Blink](#3svuh5)の[C++オブジェクト](#txuqj9)を管理する[ガベージコレクション](#6exqbl)の仕組み．[V8](#4qyfuw)の[ガベージコレクション](#6exqbl)と連携し，[JavaScript](#y8ql3q)と[DOM](#mtrvw2)の間の参照を辿る．

<a id="9pzzlk"></a>

## OpenID Connect

[OAuth](#2epxko) 2.0の上に構築され，[OpenIDプロバイダ](#r35zaj)が[リライングパーティ](#25f1g6)に[IDトークン](#1bvsna)を発行する[認証](#l2zofw)の仕様．

<a id="r35zaj"></a>

## OpenIDプロバイダ

[OpenID Connect](#9pzzlk)において，[認可サーバー](#kvuagh)を兼ねる[アイデンティティプロバイダ](#3z77qd)．

<a id="pnydk7"></a>

## OpenStack

[IaaS](#hih6s5)の基盤を構築する[オープンソースライセンス](#kv40ye)で配布されるソフトウェア群．機能を[OpenStackサービス](#xb2kcb)に分けて実装し，[仮想マシン](#uwly1k)，[ネットワーク](#uy18d2)，[記憶域](#kltl5m)を[OpenStackプロジェクト](#ek1129)に割り当てる．管理画面を[Horizon](#gu5qq4)が提供する．

<a id="xb2kcb"></a>

## OpenStackサービス

[OpenStack](#pnydk7)を構成する[クラウドサービス](#i5ziux)．[HTTP](#31abh6)の[API](#9e509k)を提供し，[Keystone](#693zzd)で[認証](#l2zofw)された要求を受け付ける．

<a id="ek1129"></a>

## OpenStackプロジェクト

[OpenStack](#pnydk7)において，[仮想マシン](#uwly1k)，[ネットワーク](#uy18d2)，[記憶域](#kltl5m)を所有し，[資源制限](#g9mkrr)の単位となるもの．利用者は[Keystone](#693zzd)でロールを割り当てられたOpenStackプロジェクトのものを操作する．

<a id="vgz9zq"></a>

## OpenTofu

[Terraform](#i3c7fx)のMozilla Public License 2.0で提供されていた版から派生した[Infrastructure as Code](#gq4l0t)のツール．Linux Foundationの下で開発される．

<a id="hfgg6x"></a>

## PEB

[Windows NT](#jzpnq4)において，[プロセス](#lm3iq5)の[アドレス空間](#rygcc4)のうち[ユーザーモード](#v7n2z8)から読み書きできる位置に置かれ，その[プロセス](#lm3iq5)の情報を保持する[データ構造](#y9ua1k)．実行ファイルの読み込み先のアドレス，読み込まれた実行ファイルと[ダイナミックリンクライブラリ](#2vuoon)の一覧，コマンドラインと環境変数，[デバッガ](#49baql)の接続の有無をもつ．

ToDo: [136](todo.md#todo-136)

<a id="i3b5sv"></a>

## PKCE

[認可コードグラント](#sdvdsn)において，[認可サーバー](#kvuagh)が，[認可エンドポイント](#17zvxp)への要求の送信元と[トークンエンドポイント](#f9akzj)への要求の送信元の同一性を確かめる，[OAuth](#2epxko)の拡張．[認可クライアント](#47yah2)は秘密の値を生成し，それを[ハッシュ関数](#fnegr1)で写した値またはそれ自体を前者に，秘密の値を後者に含める．

<a id="qoutz8"></a>

## PTRレコード

[IPアドレス](#3ksnfe)から[ドメイン名](#d8xx9q)を引く逆引きに用いる[資源レコード](#syx2b4)．[IPv4](#un6pgt)の[IPアドレス](#3ksnfe)は8ビットごとの十進数を逆順に並べてin-addr.arpaの下の，[IPv6](#4elryy)の[IPアドレス](#3ksnfe)は4ビットごとの16進数字を逆順に並べてip6.arpaの下の[ドメイン名](#d8xx9q)で表す．

<a id="8ahx0c"></a>

## PartitionAlloc

[Chromium](#2aag3y)の[メモリアロケータ](#4lrgjh)．領域を用途と大きさごとの区画に分けて割り当て，[解放後使用](#onqz9u)による別の[データ型](#w7t735)の[C++オブジェクト](#txuqj9)の上書きを難しくする．

<a id="6ftomm"></a>

## PersistentVolume

[クラスタ](#dx7pxd)の[記憶域](#kltl5m)の一単位を表し，[Pod](#k4ef3z)と独立した寿命をもつ[オブジェクト](#8ot6zr)．管理者が事前に作成するか，[StorageClass](#scppoj)に基づいて動的に作成される．

<a id="3b8umf"></a>

## PersistentVolumeClaim

容量と，利用できる範囲と読み書きの可否を示すアクセスモードとを指定した[記憶域](#kltl5m)の要求を表す[オブジェクト](#8ot6zr)．条件を満たす[PersistentVolume](#6ftomm)と1対1に結び付けられ，[Pod](#k4ef3z)はこれを[ボリューム](#0zbizc)として参照する．

<a id="g55hns"></a>

## Placement

[資源](#k7gc81)を提供する対象ごとに，[資源](#k7gc81)の在庫と使用量を記録する[OpenStackサービス](#xb2kcb)．

<a id="k4ef3z"></a>

## Pod

[Kubernetes](#t6cr2a)が配置する最小の単位で，同じ[ノード](#6qrxi1)上で実行され，[IPアドレス](#3ksnfe)と[ポート番号](#avetpx)の空間および[ボリューム](#0zbizc)を共有する1つ以上の[コンテナ](#uds0ak)の集まり．[IPアドレス](#3ksnfe)は[Container Network Interface](#kccq14)の[プラグイン](#dz7dp9)が割り当てる．配置された[ノード](#6qrxi1)から移動せず，置き換えは別のPodの作成による．

<a id="uaym9q"></a>

## Portable Executable形式

[Windows NT](#jzpnq4)における，実行ファイル，[ダイナミックリンクライブラリ](#2vuoon)，[カーネルモードドライバ](#fnr7ad)のファイル形式．

<a id="dz190z"></a>

## QoSクラス

[Pod](#k4ef3z)の[資源要求と制限](#le79r6)の指定から決まる分類．全ての[コンテナ](#uds0ak)が[プロセッサ](#4ad6s1)の時間と[物理メモリ](#svua87)の要求と制限を等しい値で指定するものはGuaranteed，いずれの[コンテナ](#uds0ak)もそれらの要求と制限を指定しないものはBestEffort，それ以外はBurstableである．[ノード](#6qrxi1)の[物理メモリ](#svua87)が逼迫したとき，BestEffort，Burstable，Guaranteedの順に強制終了されやすい．

<a id="1bon32"></a>

## RAID

複数の記憶装置を組み合わせ，データの分散配置と冗長化により性能と耐障害性を高めて，1つの[ブロックストレージ](#8ztcnx)として提供する方式．構成をレベルと呼ぶ番号で区別する．

<a id="qp2xg4"></a>

## RBAC

[Role](#3kkitq)または[ClusterRole](#4hf4xa)で定めた権限を，[RoleBinding](#mg2ixb)または[ClusterRoleBinding](#e37fh9)で[主体](#pyjgmb)に与える，[kube-apiserver](#yv6kx0)の[認可](#8esn53)の方式．要求は[許可加算評価](#kirdkx)で評価される．

<a id="xmhp27"></a>

## ROA

[RPKI](#85wnl0)の[証明書](#30mc00)に対応する[秘密鍵](#dak54j)で[電子署名](#wr3566)を付された，[IPプレフィックス](#6rwn5e)，最大プレフィックス長，および発生源として広告を許可する[AS番号](#wvk6j6)の組．

<a id="1mvy1p"></a>

## ROUTE-REFRESHメッセージ

指定した[アドレスファミリー](#zeoy6t)の[経路](#5433mk)の再広告を[ピア](#7wmnel)に要求する[BGPメッセージ](#xrq0o5)．[ケイパビリティ](#6vfi5n)で対応を通知した[ピア](#7wmnel)に対してのみ送る．

<a id="85wnl0"></a>

## RPKI

[IPプレフィックス](#6rwn5e)と[AS番号](#wvk6j6)の保持を証明する[公開鍵基盤](#qo4wn7)．それらを地域ごとに割り当てる機関を起点とする[証明書](#30mc00)の階層からなる．

<a id="m4w5n1"></a>

## RRSIGレコード

[資源レコード](#syx2b4)セットに対する[DNSSEC](#roxnj7)の[電子署名](#wr3566)を示す[資源レコード](#syx2b4)．

<a id="hkmz80"></a>

## Raft

[リーダー選出](#brj8ci)で選ばれた[リーダー](#v8js9k)が状態の変更を[ログ](#9rxwgw)の項目として他の計算機に送り，[クォーラム](#225nin)が保存した項目を確定する[合意アルゴリズム](#eo61p5)．時間をタームに区切り，各タームの[リーダー](#v8js9k)は高々1台である．

<a id="gz9wdq"></a>

## Receiver

[メッセージパイプ](#xnwjk2)の一端を保持し，受けたメッセージを[Mojoインターフェース](#q1r1b6)の実装のメソッドの呼び出しに変えるもの．

<a id="g3yk27"></a>

## Remote

[メッセージパイプ](#xnwjk2)の一端を保持し，[Mojoインターフェース](#q1r1b6)のメソッドの呼び出しをメッセージとして送るもの．

<a id="xir7fh"></a>

## RenderFrameHost

[contentモジュール](#e7u8nm)において，[ブラウザプロセス](#ejqo3w)の側で，[レンダラープロセス](#53ckw6)内の1つの[フレーム](#mtx2pq)の[Web文書](#qbtpp4)を表す[C++オブジェクト](#txuqj9)．

<a id="9nbpfp"></a>

## ReplicaSet

[ラベルセレクタ](#x5w385)に一致し[コントローラ参照](#xy6h7u)でこのReplicaSetを指す[Pod](#k4ef3z)の数を，[Pod](#k4ef3z)のテンプレートに従う[Pod](#k4ef3z)の作成または削除により，指定された数に保つ[ワークロードリソース](#qg1bbv)．

<a id="4192cj"></a>

## ResourceQuota

1つの[名前空間](#6bdul4)に[資源制限](#g9mkrr)を課す[オブジェクト](#8ot6zr)．上限の対象は[資源要求と制限](#le79r6)の合計と[オブジェクト](#8ot6zr)の個数である．

<a id="3kkitq"></a>

## Role

1つの[名前空間](#6bdul4)内の[オブジェクト](#8ot6zr)の種類ごとに，許可する操作の集合を定める[オブジェクト](#8ot6zr)．

<a id="mg2ixb"></a>

## RoleBinding

[Role](#3kkitq)または[ClusterRole](#4hf4xa)の権限を，1つの[名前空間](#6bdul4)の範囲で[主体](#pyjgmb)に与える[オブジェクト](#8ot6zr)．

<a id="vondey"></a>

## Rule of Two

[Chromium](#2aag3y)の設計規則．信頼できない入力を扱うこと，[メモリ安全性](#qbsksa)を保証しない言語で実装されること，[サンドボックス](#94k6ba)の外で動作すること，の3つのうち，1つの構成要素が同時に満たしてよいのは2つまでである．

<a id="o1ut81"></a>

## S3オブジェクト

[S3バケット](#wtv4f2)内でキーにより識別される，データと[メタデータ](#f7of70)の組．書き込みの成功後に開始した読み出しと一覧は，その書き込みの結果を反映する．

<a id="pt8d9z"></a>

## S3ストレージクラス

[S3オブジェクト](#o1ut81)ごとに指定される，保存の料金，取り出しの料金と所要時間，可用性の組．

<a id="wtv4f2"></a>

## S3バケット

[S3オブジェクト](#o1ut81)を格納する[リージョンリソース](#tynhcw)．その名前は[AWSパーティション](#5q5a61)内で一意である．

<a id="yoebmp"></a>

## SAML

Security Assertion Markup Language．[SAMLアサーション](#m7caca)を用いて，[アイデンティティプロバイダ](#3z77qd)が[サービスプロバイダ](#l5pssm)に[認証](#l2zofw)の結果を伝える仕様．現行の版は2.0である．

<a id="m7caca"></a>

## SAMLアサーション

[SAML](#yoebmp)において[アイデンティティプロバイダ](#3z77qd)が発行する，[主体](#pyjgmb)についての主張を表す[XML](#wjqbo3)のデータ．[認証](#l2zofw)の結果を表すものは[認証アサーション](#ki350n)である．

<a id="m38dhg"></a>

## SCTP

[SCTPアソシエーション](#sd7szm)を確立し，[端点](#b084uv)の間でメッセージの境界を保って到達を保証する[トランスポートプロトコル](#dayw7g)．順序を要しないと指定したメッセージは，[ストリーム](#wmv9lk)の順序によらずに渡される．

<a id="sd7szm"></a>

## SCTPアソシエーション

[SCTP](#m38dhg)の[接続](#st4cz5)．各[端点](#b084uv)は複数の[IPアドレス](#3ksnfe)をもて，互いに独立した複数の[ストリーム](#wmv9lk)を運ぶ．

<a id="xdzan2"></a>

## SIM

[移動体通信事業者](#em1w73)の加入者の識別子と，その事業者と共有する[共通鍵](#sie28z)を保持し，[端末](#zw6tbw)が[コアネットワーク](#7ll5nd)に[認証](#l2zofw)されるのに用いる部品．[端末](#zw6tbw)に挿すICカードと，[端末](#zw6tbw)に組み込まれたチップがある．

<a id="3uc35a"></a>

## SNAT

送信元の[IPアドレス](#3ksnfe)を書き換える[NAT](#4blq8k)．

<a id="3i22kd"></a>

## SNMPエージェント

[監視主体](#90keyj)がSNMPで値を取得する[アイテムタイプ](#ugi5pv)．

<a id="sktwnj"></a>

## SOAレコード

[DNSゾーン](#2eh0s0)の根に1つ置かれ，主たる[権威DNSサーバー](#9es8da)の名前，管理者のメールアドレス，シリアル番号，[ゾーン転送](#zil7hp)の間隔と期限，問い合わせた[ドメイン名](#d8xx9q)または型の[資源レコード](#syx2b4)が存在しないという応答を[キャッシュ](#kj4w0z)する時間を示す[資源レコード](#syx2b4)．

<a id="v61vr0"></a>

## SQL

[リレーショナルデータベース](#ev8ocv)の[データベース管理システム](#wn1pbv)に対し，[表](#iuztvu)の定義，問合せ，更新，[トランザクション](#v5hhix)の制御を記述する宣言的な言語．ISOとIECにより標準化されている．

<a id="2c4um1"></a>

## SSID

[Wi-Fi](#r9it7l)において，[アクセスポイント](#tzn2n7)が収容する[ネットワーク](#uy18d2)を示す，32[オクテット](#yimp6h)以下の名前．

<a id="vfgxw6"></a>

## SSOサービス

[SAML](#yoebmp)において，[サービスプロバイダ](#l5pssm)からの認証要求を受け付ける[アイデンティティプロバイダ](#3z77qd)の[エンドポイント](#9i1lg3)．

<a id="w8962q"></a>

## Seatbelt

[macOS](#0ml2dc)において，[プロセス](#lm3iq5)に許す操作をプロファイルの規則で定め，[カーネル](#cktjwx)がそれ以外の操作を拒む[サンドボックス](#94k6ba)の機構．

<a id="a2mhw3"></a>

## Secret

機密データを保持し，[ConfigMap](#3x7wht)と同じ方法で[Pod](#k4ef3z)に渡す[オブジェクト](#8ot6zr)．値は文字列への可逆な符号化のみを施され，既定では[etcd](#c0gd56)に[暗号化](#e382sn)されずに格納される．

<a id="3bb8t3"></a>

## Service

[通信先](#b2znuk)の集合に，安定した名前による到達手段を与える[オブジェクト](#8ot6zr)．[通信先](#b2znuk)は[EndpointSlice](#n5mrfc)に保持され，[ラベルセレクタ](#x5w385)をもつServiceではそれが選ぶ[Pod](#k4ef3z)である．種類に，[クラスタ](#dx7pxd)内からのみ到達できる仮想的な[IPアドレス](#3ksnfe)を与えるClusterIP，それに加えて各[ノード](#6qrxi1)の固定の[ポート番号](#avetpx)で公開するNodePort，それに加えて外部の[ロードバランサー](#v7r0tg)で公開するLoadBalancer，外部の[ドメイン名](#d8xx9q)への別名を[CNAMEレコード](#dsbf8s)で与えるExternalNameがある．

<a id="856hn3"></a>

## ServiceAccount

[Pod](#k4ef3z)内の処理が[kube-apiserver](#yv6kx0)に[認証](#l2zofw)される際の[主体](#pyjgmb)を表し，[名前空間](#6bdul4)に属する[オブジェクト](#8ot6zr)．

<a id="41yxh0"></a>

## Siso

[Ninja](#w9mk1f)の入力ファイルを読み，ビルドの手順を遠隔の計算機でも実行できる[ビルドシステム](#ci6jok)．Googleが開発する．

<a id="1811pf"></a>

## SiteInstance

[Chromium](#2aag3y)において，1つの[BrowsingInstance](#ukqdvo)内で，同じ[レンダラープロセス](#53ckw6)で処理される[Web文書](#qbtpp4)の集まり．[サイト分離](#guozy4)では1つの[サイト](#gqdkk9)に対応する．

<a id="w2zitm"></a>

## Skia

[Chromium](#2aag3y)が[ディスプレイリスト](#2zr71h)の[ラスタライズ](#3o1tma)に用いる2Dグラフィックスライブラリ．

<a id="0ygryr"></a>

## Spectre

[プロセッサ](#4ad6s1)が[投機的実行](#wxs2uf)で実行した命令が[キャッシュ](#kj4w0z)に残す状態の変化を観測し，同じ[アドレス空間](#rygcc4)内の，読み取りを許されないデータを推定する攻撃の類．

<a id="2ccw4i"></a>

## StatefulSet

各[Pod](#k4ef3z)に序数に基づく固定の名前と，[PersistentVolumeClaim](#3b8umf)による固有の[記憶域](#kltl5m)を与える[ワークロードリソース](#qg1bbv)．[Pod](#k4ef3z)が置き換えられても名前と[記憶域](#kltl5m)は引き継がれる．既定では序数の順に[Pod](#k4ef3z)を作成し，逆順に削除する．

<a id="scppoj"></a>

## StorageClass

[PersistentVolume](#6ftomm)の動的な作成を担うプログラムであるプロビジョナと，それに渡すパラメータを指定する[オブジェクト](#8ot6zr)．

<a id="6t597t"></a>

## Swift

[オブジェクトストレージ](#k4obt0)を提供する[OpenStackサービス](#xb2kcb)．

<a id="bfxke9"></a>

## Systemプロセス

[Windows NT](#jzpnq4)において，[特権モード](#uk5ihn)でのみ動作する[スレッド](#ou7dup)を収める[プロセス](#lm3iq5)．[プロセス](#lm3iq5)の識別番号は4である．

<a id="cndtkv"></a>

## TCP

[接続](#st4cz5)を確立し，[端点](#b084uv)の間で，到達を保証したバイト列の[ストリーム](#wmv9lk)を各方向に1つずつ運ぶ[トランスポートプロトコル](#dayw7g)．

<a id="lnr2ip"></a>

## TEB

[Windows NT](#jzpnq4)において，所属する[プロセス](#lm3iq5)の[アドレス空間](#rygcc4)のうち[ユーザーモード](#v7n2z8)から読み書きできる位置に置かれ，[スレッド](#ou7dup)の情報を保持する[データ構造](#y9ua1k)．その[スレッド](#ou7dup)が[ユーザーモード](#v7n2z8)で用いる[スタック](#hfx60b)の範囲，[Windows API](#fg2wal)の直近のエラー値，スレッドローカル記憶域，[PEB](#hfgg6x)のアドレスをもつ．[ユーザーモード](#v7n2z8)では，x64ではGSセグメントが，x86ではFSセグメントがこれを指す．

ToDo: [136](todo.md#todo-136)

<a id="xqkfhy"></a>

## TLS

到達と順序を保証する[接続](#st4cz5)の上で，通信の[暗号化](#e382sn)，[MAC](#u6gjh1)または[認証付き暗号](#p3b37s)による改ざんの検出，[証明書](#30mc00)による通信相手の[認証](#l2zofw)を提供する[プロトコル](#bhk5im)．

<a id="i3c7fx"></a>

## Terraform

[Terraformモジュール](#tfnkcp)に宣言された[Terraformリソース](#65q92o)を，[Terraformプロバイダ](#5nckv0)を介して作成，更新，削除する[Infrastructure as Code](#gq4l0t)のツール．宣言，[Terraform状態](#ufk7we)，実在する実体の属性を比較して実行計画を作り，それを適用して実体を宣言に一致させる．[Terraformリソース](#65q92o)間の参照から依存関係を求め，その順序で操作する．HashiCorp, Inc.が開発し，1.6以降の版はBusiness Source License 1.1で提供される．

ToDo: [104](todo.md#todo-104)

<a id="5nckv0"></a>

## Terraformプロバイダ

特定の[API](#9e509k)を操作して[Terraformリソース](#65q92o)の種類を実装する，[Terraform](#i3c7fx)の[プラグイン](#dz7dp9)．

ToDo: [104](todo.md#todo-104)

<a id="tfnkcp"></a>

## Terraformモジュール

1つの[ディレクトリ](#j1d7gn)に置かれた，[HCL](#cqjacl)で書かれたファイルの集合．[Terraformリソース](#65q92o)を宣言し，他のTerraformモジュールを呼び出せる．[Terraform](#i3c7fx)を実行するディレクトリのものをルートモジュールと呼ぶ．

<a id="65q92o"></a>

## Terraformリソース

[Terraformモジュール](#tfnkcp)のresourceブロックで宣言され，[Terraformプロバイダ](#5nckv0)が作成，更新，削除する実体．種類と名前で識別される．

<a id="ufk7we"></a>

## Terraform状態

[Terraform](#i3c7fx)が記録する，[Terraformリソース](#65q92o)と実在する実体との対応，および実体の最後に把握された属性．ローカルのファイル，またはバックエンドと呼ぶ遠隔の保存先に保存される．

ToDo: [104](todo.md#todo-104)

<a id="7mvj8m"></a>

## UDP

接続を確立せず，到達と順序を保証しないデータグラムを運ぶ[トランスポートプロトコル](#dayw7g)．

<a id="w2fhil"></a>

## UID

[オブジェクト](#8ot6zr)の作成時に[kube-apiserver](#yv6kx0)が割り当てる，[クラスタ](#dx7pxd)の存続期間を通じて一意な識別子．同じ名前で作り直した[オブジェクト](#8ot6zr)は別のものをもつ．

<a id="zq6ytz"></a>

## UMTS

[3GPP](#8hltrb)が策定した，[GSM](#c27kel)の後継となる第3世代の[セルラー通信](#fibo1z)の規格．

<a id="flb10w"></a>

## UNICODE_STRING

[Windows NT](#jzpnq4)の[ネイティブAPI](#kdca50)と[カーネル](#cktjwx)が用いる，UTF-16の文字列を表す[データ構造](#y9ua1k)．バイト単位の文字列の長さとバッファの容量，バッファへの参照をもつ．文字列の終端に零を必要としない．

<a id="zqwllr"></a>

## UPDATEメッセージ

[経路](#5433mk)の広告と撤回を伝える[BGPメッセージ](#xrq0o5)．撤回する[IPプレフィックス](#6rwn5e)の列，[パス属性](#q885vr)，[NLRI](#pks2n8)を含む．

<a id="ydpswy"></a>

## URL

取得する対象の位置を表す文字列．[スキーム](#yo9qhx)を含み，[ホスト](#0qt5x4)，[ポート番号](#avetpx)，パス，クエリ，フラグメントを含みうる．

<a id="4qyfuw"></a>

## V8

[Chromium](#2aag3y)の[JavaScript](#y8ql3q)エンジン．ソースを[バイトコード](#47l5g8)に変換して[インタプリタ](#8e4tig)のIgnitionで実行し，実行回数の多い[サブルーチン](#y825lm)を，Sparkplug，Maglev，TurboFanの順に段階的に[JITコンパイル](#2t5b12)する．最適化したコードは実行中に観測した[データ型](#w7t735)を前提とし，前提が崩れると最適化前のコードに戻る．メモリは[ガベージコレクション](#6exqbl)で管理する．

<a id="pg1lac"></a>

## VFSノード

[仮想ファイルシステム](#gid8it)において，[ファイルシステム](#pp17bd)内の1つのファイルを表す[データ構造](#y9ua1k)．種別と，実装の[操作表](#xxcrwp)をもち，名前をもたない．

<a id="4ln6ld"></a>

## VPC

[Amazon Virtual Private Cloud](#mkyn41)が提供する，[仮想ネットワーク](#cos7bu)である[リージョンリソース](#tynhcw)．[IPv4](#un6pgt)の[IPプレフィックス](#6rwn5e)を1つ以上もち，[サブネット](#oygsrp)に分割される．

<a id="pguegu"></a>

## VPCエンドポイント

[VPC](#4ln6ld)から[インターネットゲートウェイ](#qmmwja)を経ずに[通信先](#b2znuk)へ私的に接続する[AWSリソース](#78qg7h)．ゲートウェイ型は[サブネット](#oygsrp)に関連付けられた[経路表](#dw7079)の転送先として働き，[Amazon Simple Storage Service](#u2wout)または[Amazon DynamoDB](#knkcrh)に接続する．ゲートウェイ型以外は[AWS PrivateLink](#8irydc)を用い，[サブネット](#oygsrp)に[リクエスターマネージド型ネットワークインターフェース](#8gfkr4)を作成する．

<a id="z6xphd"></a>

## VPCピアリング接続

2つの[VPC](#4ln6ld)を接続し，互いの[IPプレフィックス](#6rwn5e)に属する[IPアドレス](#3ksnfe)で直接通信できるようにする[AWSリソース](#78qg7h)．推移的な[経路](#5433mk)を提供せず，[IPプレフィックス](#6rwn5e)が重なる[VPC](#4ln6ld)の間には作成できない．

ToDo: [106](todo.md#todo-106)

<a id="3a4xlv"></a>

## VRF

1つの[ルータ](#5f2okm)内に独立して保持される[経路表](#dw7079)と，それを用いる転送の単位．

<a id="uz3cja"></a>

## Visual Studio

Microsoftが開発する[統合開発環境](#wr7tbp)．[Visual Studio Code](#fqq24m)とは別の製品である．

<a id="fqq24m"></a>

## Visual Studio Code

Microsoftが開発する[テキストエディタ](#nud9su)．[Electron](#fkvuw7)を基に構築され，[拡張機能](#1erfeu)により機能を追加できる．言語ごとの機能は[Language Server Protocol](#dfaxj3)で[言語サーバー](#69tuqj)から得て，[デバッガ](#49baql)は[Debug Adapter Protocol](#jt8i5n)で操作する．ソースコードは[Code - OSS](#9ng0n3)として公開される．

<a id="f7cwfp"></a>

## WPA2

[Wi-Fi](#r9it7l)の通信を保護する規格．AES-CCMPによる[認証付き暗号](#p3b37s)を用い，事前に共有した[共通鍵](#sie28z)またはIEEE 802.1Xにより[端末](#zw6tbw)を[認証](#l2zofw)する．

<a id="yjka93"></a>

## WPA3

[WPA2](#f7cwfp)の後継の規格．事前に共有した[共通鍵](#sie28z)による[認証](#l2zofw)にSAEを用い，接続を傑受した者がその記録からパスワードを推測できないようにする．

<a id="066occ"></a>

## WebContents

[contentモジュール](#e7u8nm)において，1つの[タブ](#u7pfjr)の内容である[フレーム](#mtx2pq)の[木](#dj2zcx)と，その[ナビゲーション](#day4yo)の履歴を保持する[C++オブジェクト](#txuqj9)．

<a id="gcly3z"></a>

## Webブラウザ

[URL](#ydpswy)で指定された[Web文書](#qbtpp4)をその[スキーム](#yo9qhx)の定める手段で取得し，解釈して表示し，[Web文書](#qbtpp4)中の[JavaScript](#y8ql3q)を実行する[クライアント](#xv4m3d)．

<a id="qbtpp4"></a>

## Web文書

[Webブラウザ](#gcly3z)が[フレーム](#mtx2pq)に表示する内容の単位．[HTML](#n9liw2)を含む形式の文書から構築され，[DOM](#mtrvw2)で表される．

<a id="r9it7l"></a>

## Wi-Fi

IEEE 802.11に基づき，免許を要しない[周波数帯](#utnq9w)の[無線通信](#1zfkze)で[リンク](#xy3alb)を構成する規格．[MACアドレス](#sagh83)を用い，[CSMA/CA](#itq0mu)で媒体を共有する．通信を保護する規格に[WPA2](#f7cwfp)と[WPA3](#yjka93)がある．

<a id="fg2wal"></a>

## Windows API

[Windows NT](#jzpnq4)において，kernel32.dllとuser32.dllを含む[ダイナミックリンクライブラリ](#2vuoon)を通じて[アプリケーション](#zxvj73)に公開される，文書化された[API](#9e509k)．

<a id="jzpnq4"></a>

## Windows NT

[ntoskrnl.exe](#tguf9f)を[カーネル](#cktjwx)の中核とする[オペレーティングシステム](#c8v8vw)の系統．

ToDo: [136](todo.md#todo-136)，[102](todo.md#todo-102)

<a id="s709hz"></a>

## Windowsサービス

[Windows NT](#jzpnq4)において，[サービス制御マネージャ](#k0p5vs)の制御下で起動・停止されるプログラム．

<a id="f0u95h"></a>

## Windowsセッション

[Windows NT](#jzpnq4)において，[プロセス](#lm3iq5)と，それらが用いる[ウィンドウ](#zbv6hc)と画面と入力装置の[資源](#k7gc81)を包み，[資源隔離](#1sgoxr)を行う単位．ユーザーが対話的に[認証](#l2zofw)されるたびに作成される．セッション0は[Windowsサービス](#s709hz)とシステムの[プロセス](#lm3iq5)が用い，対話的に[認証](#l2zofw)されたユーザーには割り当てられない．

<a id="cyz8ys"></a>

## WoW64

64ビットの[Windows NT](#jzpnq4)において，32ビットの[Portable Executable形式](#uaym9q)のプログラムを実行させる[ユーザーモード](#v7n2z8)の互換層．

ToDo: [136](todo.md#todo-136)

<a id="wjqbo3"></a>

## XML

開始タグと終了タグで囲んだ要素を入れ子にして，[木](#dj2zcx)の構造のデータを表すテキストの形式．

<a id="fg7rfz"></a>

## Zab

[ZooKeeperアンサンブル](#csow5k)が用いる[合意アルゴリズム](#eo61p5)．[リーダー](#v8js9k)が状態の変更を，エポックと計数からなるzxidで全順序付けて提案し，[クォーラム](#225nin)の[フォロワー](#telc65)が記録したのち確定させる．[リーダー](#v8js9k)の故障時には，[リーダー選出](#brj8ci)により最も新しいzxidをもつ[サーバー](#uteg7y)を新しい[リーダー](#v8js9k)とする．

<a id="o6myi6"></a>

## Zabbix

[ホスト](#y3ka2w)から値を収集し，[障害](#ilz3yu)を判定して通知する，[オープンソースライセンス](#kv40ye)で配布される監視ソフトウェア．

ToDo: [103](todo.md#todo-103)

<a id="5l6oih"></a>

## Zabbix Agent

[ホスト](#y3ka2w)上で動作し，そのホストの値を[パッシブチェック](#n8ur2q)または[アクティブチェック](#v4p3tn)で[監視主体](#90keyj)に提供する[プロセス](#lm3iq5)．

<a id="pjiioj"></a>

## Zabbix Proxy

[Zabbix Server](#tm6l00)に代わって値を収集し，一時保存してから[Zabbix Server](#tm6l00)へ送る[監視主体](#90keyj)．[Zabbix Agent](#5l6oih)との通信手順は[Zabbix Server](#tm6l00)と同一である．高々1つの[プロキシグループ](#t7lw5k)に属する．

<a id="tm6l00"></a>

## Zabbix Server

[Zabbix](#o6myi6)の中核である[監視主体](#90keyj)．自ら収集した値と[Zabbix Proxy](#pjiioj)から受けた値を[データベース](#vlgsmo)に格納し，[トリガー](#3gz3w5)の評価と[アクション](#pfbsnf)の実行を行う．

<a id="ait45t"></a>

## Zabbixトラッパー

外部から[監視主体](#90keyj)に送られた値を受け取る[アイテムタイプ](#ugi5pv)．

<a id="csow5k"></a>

## ZooKeeperアンサンブル

[Apache ZooKeeper](#o7jjj5)を構成する[サーバー](#uteg7y)の集まり．[Zab](#fg7rfz)により1台の[リーダー](#v8js9k)が定まり，他は投票に参加する[フォロワー](#telc65)と参加しないオブザーバーとなる．各[サーバー](#uteg7y)はデータの全体をメモリ上に保持する．

<a id="lcbo8w"></a>

## ZooKeeperウォッチ

[クライアント](#xv4m3d)が読み取りの際に[znode](#xus9ny)に設定し，その[znode](#xus9ny)の変更を通知させる仕組み．標準のウォッチは一度の通知で解除される．通知は，変更後の状態を[クライアント](#xv4m3d)が読むより前に届く．

<a id="z4pzpk"></a>

## ZooKeeperセッション

[クライアント](#xv4m3d)と[ZooKeeperアンサンブル](#csow5k)の間の関係．[クライアント](#xv4m3d)はタイムアウトより短い間隔で要求または[ハートビート](#5urygr)を送って維持し，接続先の[サーバー](#uteg7y)を替えても保たれる．

<a id="q8nfco"></a>

## Zygote

[Linux](#eh8l2u)上の[Chromium](#2aag3y)において，起動時に共通の初期化を済ませ，自身を複製して[レンダラープロセス](#53ckw6)を含む子の[プロセス](#lm3iq5)を作る[プロセス](#lm3iq5)．複製された[プロセス](#lm3iq5)は，初期化済みの[ページ](#05by8w)を[コピーオンライト](#q33a7g)で共有する．

<a id="rh5dah"></a>

## cgroup

[Linux](#eh8l2u)において，[プロセス](#lm3iq5)を階層的な集合に組織し，集合ごとに[資源](#k7gc81)の使用を計測して[資源制限](#g9mkrr)を課す機構．

ToDo: [126](todo.md#todo-126)

<a id="64p7b9"></a>

## clone

[Linux](#eh8l2u)において新しい[スレッド](#ou7dup)を作成する[システムコール](#saksfm)．呼び出し元の[スレッド](#ou7dup)と共有する[資源](#k7gc81)を引数で指定する．

<a id="e7u8nm"></a>

## contentモジュール

[Chromium](#2aag3y)のソースのうち，[サンドボックス](#2xz9pb)と複数の[プロセス](#lm3iq5)からなる[Webブラウザ](#gcly3z)の中核を実装し，Google Chrome固有の機能を含まない層．埋め込み側にContent [API](#9e509k)を提供する．

<a id="aqu8xq"></a>

## device-mapper

[Linux](#eh8l2u)において，仮想的な[ブロックデバイス](#1frbzb)の各区間を，対応表に従って他の[ブロックデバイス](#1frbzb)の区間に対応付ける[カーネル](#cktjwx)の枠組み．対応付けの種類はターゲットとして実装される．

ToDo: [130](todo.md#todo-130)，[126](todo.md#todo-126)

<a id="vz4jtn"></a>

## eBGP

異なる[自律システム](#8wkkrz)に属する[ピア](#7wmnel)の間の[BGPセッション](#s9mnt1)．

<a id="c0gd56"></a>

## etcd

[Raft](#hkmz80)により[レプリケーション](#rv2ppc)される，[分散システム](#6cc980)をなす[キーバリューストア](#trahzf)．[Kubernetes](#t6cr2a)では[クラスタ](#dx7pxd)の全ての[オブジェクト](#8ot6zr)を格納する．

<a id="djvjxt"></a>

## gclient

[Chromium](#2aag3y)のソースと，[DEPSファイル](#lxov83)に記された依存先のリポジトリを取得し，同期するツール．depot_toolsに含まれる．

<a id="f6yd97"></a>

## iBGP

同じ[自律システム](#8wkkrz)に属する[ピア](#7wmnel)の間の[BGPセッション](#s9mnt1)．[経路リフレクタ](#iz5p1h)でない[BGPスピーカー](#v9rnch)は，このセッションで学習した[経路](#5433mk)を同種の他のセッションの[ピア](#7wmnel)へ広告しない．このため，[自律システム](#8wkkrz)内の全ての[BGPスピーカー](#v9rnch)に[経路](#5433mk)を行き渡らせるには，全ての[BGPスピーカー](#v9rnch)の全ての対の間のセッション，[経路リフレクタ](#iz5p1h)，または[BGPコンフェデレーション](#y1mii1)を用いる．

<a id="5yd9eo"></a>

## initプロセス

[Linux](#eh8l2u)が起動処理の最後に実行する，最初の[ユーザーモード](#v7n2z8)の[プロセス](#lm3iq5)．識別番号は1である．

<a id="134vyo"></a>

## iptables

[Netfilter](#feag1h)に規則を設定する手段．規則を，目的ごとに固定された[Netfilterテーブル](#2tvkpf)（filter，nat，mangle，raw，security）に属する[チェイン](#0jljvq)に並べる．組込みの[チェイン](#0jljvq)は[Netfilterフック](#ljpkdd)に結び付く．規則は先頭から照合し，一致した規則の[iptablesターゲット](#n0xlay)を適用する．照合を終える[iptablesターゲット](#n0xlay)を適用せずに組込みの[チェイン](#0jljvq)の末尾に達すると，その[チェイン](#0jljvq)に定めた既定の[iptablesターゲット](#n0xlay)（ACCEPTまたはDROP）を適用する．

<a id="n0xlay"></a>

## iptablesターゲット

[iptables](#134vyo)の規則が，一致した[IPパケット](#w9btgk)に適用する処理．

<a id="xoam9f"></a>

## jail

[FreeBSD](#ofaawr)において[資源隔離](#1sgoxr)を行う機構．所属する[プロセス](#lm3iq5)に，[ファイルシステム](#pp17bd)の部分木を根として見せ，jailの外の[プロセス](#lm3iq5)を見えなくし，独自のホスト名を与える．jailの中にjailを作れる．

ToDo: [147](todo.md#todo-147)，[130](todo.md#todo-130)

<a id="yv6kx0"></a>

## kube-apiserver

[オブジェクト](#8ot6zr)の作成，読取り，更新，削除，監視を受け付ける[HTTP](#31abh6)の[API](#9e509k)を提供する[コントロールプレーン](#b8ign2)の構成要素．要求に[認証](#l2zofw)，[認可](#8esn53)，[アドミッションコントロール](#w88wo5)を順に適用し，結果を[etcd](#c0gd56)に永続化する．[etcd](#c0gd56)と直接通信する唯一の構成要素である．

<a id="9xikob"></a>

## kube-controller-manager

組込みの[コントローラ](#pboh16)群を1つの[プロセス](#lm3iq5)として実行する[コントロールプレーン](#b8ign2)の構成要素．

<a id="r7qr24"></a>

## kube-proxy

[ノード](#6qrxi1)上で動作し，[Service](#3bb8t3)の仮想的な[IPアドレス](#3ksnfe)への通信を[通信先](#b2znuk)の[Pod](#k4ef3z)へ転送する規則を，[iptables](#134vyo)，[IPVS](#ofv8m2)，[nftables](#6nsmli)のいずれかによりその[ノード](#6qrxi1)に設定する構成要素．

<a id="62x28a"></a>

## kube-scheduler

[ノード](#6qrxi1)が未割当ての[Pod](#k4ef3z)ごとに，[資源要求と制限](#le79r6)，[テイント](#r85zs1)，[アフィニティ](#1ipr3r)の制約を満たす[ノード](#6qrxi1)のうち評価の最も高いものを選び，割り当てる[コントロールプレーン](#b8ign2)の構成要素．

<a id="zh69qe"></a>

## kubelet

各[ノード](#6qrxi1)で動作し，その[ノード](#6qrxi1)に割り当てられた[Pod](#k4ef3z)の[コンテナ](#uds0ak)を[Container Runtime Interface](#ttawc3)を介して[コンテナランタイム](#nl5o0m)に実行させ，[コンテナプローブ](#xj5eeh)を行い，状態を[kube-apiserver](#yv6kx0)に報告するエージェント．

<a id="0ml2dc"></a>

## macOS

Appleが開発する，XNUを[カーネル](#cktjwx)とする[オペレーティングシステム](#c8v8vw)．

<a id="6nsmli"></a>

## nftables

[iptables](#134vyo)の後継として，[Netfilter](#feag1h)に規則を設定する手段．[Netfilterテーブル](#2tvkpf)，[チェイン](#0jljvq)，規則を全て利用者が定義し，規則を[カーネル](#cktjwx)内の[インタプリタ](#8e4tig)が実行する[バイトコード](#47l5g8)に変換する．[IPv4](#un6pgt)と[IPv6](#4elryy)を1つの体系で扱う．

<a id="z6nvth"></a>

## ntdll.dll

[Windows NT](#jzpnq4)において，[ネイティブAPI](#kdca50)の入口と，[ユーザーモード](#v7n2z8)で動作する[動的リンカ](#sxisir)とを提供する[ダイナミックリンクライブラリ](#2vuoon)．

<a id="tguf9f"></a>

## ntoskrnl.exe

[Windows NT](#jzpnq4)において，[エグゼクティブ](#s3eb1d)と[NTカーネル層](#oobie1)を収め，[特権モード](#uk5ihn)で動作する実行ファイル．

<a id="ood9pc"></a>

## propagationPolicy

[オブジェクト](#8ot6zr)の削除時に指定する，それを[所有者参照](#zktekl)で指す[オブジェクト](#8ot6zr)の扱い．Orphanはそれらの[所有者参照](#zktekl)を除いて残し，Backgroundは所有者を直ちに削除してそれらを[ガベージコレクタ](#3x9bon)に削除させ，ForegroundはblockOwnerDeletionをもつものの削除を待ってから所有者を削除する．

<a id="x4wvbi"></a>

## seccomp-BPF

[Linux](#eh8l2u)において，[スレッド](#ou7dup)が発行する[システムコール](#saksfm)を，その番号と引数を検査する[バイトコード](#47l5g8)のフィルタにより許可または拒否する機構．フィルタは子孫に継承され，解除できない．

<a id="zv7vha"></a>

## setuidプログラム

実行した[プロセス](#lm3iq5)に，そのファイルの所有者の[セキュリティ文脈](#lxnyp5)での[権限引受け](#5bn6hq)をさせるプログラム．

ToDo: [125](todo.md#todo-125)

<a id="6df5pk"></a>

## struct address_space

[Linux](#eh8l2u)の[仮想ファイルシステム](#gid8it)において，1つの[struct inode](#6a5x2m)の内容のうち[ページキャッシュ](#yobm0y)にある[struct folio](#x1g5fz)を，ファイル内の位置で索引する[データ構造](#y9ua1k)．

<a id="k31ju1"></a>

## struct bio

[Linux](#eh8l2u)において，[ブロックデバイス](#1frbzb)への1つの入出力要求を表す[データ構造](#y9ua1k)．対象の[ブロックデバイス](#1frbzb)，開始位置，読み書きの別，データを置く[物理メモリ](#svua87)の区間の列をもつ．

ToDo: [130](todo.md#todo-130)，[126](todo.md#todo-126)

<a id="hotd7l"></a>

## struct cred

[Linux](#eh8l2u)において，[スレッド](#ou7dup)の[セキュリティ文脈](#lxnyp5)を表す[データ構造](#y9ua1k)．ユーザーとグループの識別番号，capability，ユーザー名前空間である[Linux名前空間](#rmoy1r)への参照をもつ．[置換更新](#gv4jmw)で更新される．

ToDo: [127](todo.md#todo-127)

<a id="5t7a17"></a>

## struct dentry

[Linux](#eh8l2u)における[名前キャッシュ](#lnizbx)の要素．名前を，親のstruct dentryと，その名前のファイルの[struct inode](#6a5x2m)に結び付ける．

<a id="3gg1hf"></a>

## struct file

[Linux](#eh8l2u)において，1つの[開かれたファイル記述](#u8r1ic)を表す[データ構造](#y9ua1k)．対象の[struct dentry](#5t7a17)と[操作表](#xxcrwp)をもつ．

<a id="o771j1"></a>

## struct file

[FreeBSD](#ofaawr)において，1つの[開かれたファイル記述](#u8r1ic)を表す[データ構造](#y9ua1k)．対象の種類，種類ごとの[操作表](#xxcrwp)，対象を表す[データ構造](#y9ua1k)への参照をもつ．対象が[ファイルシステム](#pp17bd)内のファイルであれば[struct vnode](#6qdkzg)を，[ソケット](#oscpon)であれば[struct socket](#os8s4h)を参照する．

<a id="nij06r"></a>

## struct filedesc

[FreeBSD](#ofaawr)において，[プロセス](#lm3iq5)が用いる[ファイルディスクリプタ表](#rxedfi)．

ToDo: [130](todo.md#todo-130)

<a id="84r2z8"></a>

## struct files_struct

[Linux](#eh8l2u)において，[スレッド](#ou7dup)が用いる[ファイルディスクリプタ表](#rxedfi)．

<a id="x1g5fz"></a>

## struct folio

[Linux](#eh8l2u)において，物理的に連続する2の冪個の[ページフレーム](#4qztd7)を1単位として表す[データ構造](#y9ua1k)．

<a id="yve2sf"></a>

## struct fs_struct

[Linux](#eh8l2u)において，[スレッド](#ou7dup)が[パス名](#ymj65u)の解決の起点とする根ディレクトリと作業ディレクトリを保持する[データ構造](#y9ua1k)．

ToDo: [153](todo.md#todo-153)

<a id="0c72yy"></a>

## struct hlist_node

[Linux](#eh8l2u)において，双方向で環状でない[埋め込み連結リスト](#0qdj5m)をつくるために要素に埋め込む[構造体](#0fq59c)．次の要素のstruct hlist_nodeへの参照と，前の要素がもつ次への参照の欄への参照からなる．リストの先頭は，最初の要素への参照のみからなるstruct hlist_headで表す．

<a id="wbs4wg"></a>

## struct ifnet

[FreeBSD](#ofaawr)における[ネットワークインターフェース記述子](#u4q636)．割り当てられたアドレスの一覧をもつ．

<a id="6a5x2m"></a>

## struct inode

[Linux](#eh8l2u)における[VFSノード](#pg1lac)．許可，所有者，大きさ，時刻の[メタデータ](#f7of70)と，[struct address_space](#6df5pk)をもつ．複数の[struct dentry](#5t7a17)から参照されうる．

<a id="bmh3mr"></a>

## struct list_head

[Linux](#eh8l2u)において，双方向の環状の[埋め込み連結リスト](#0qdj5m)をつくるために要素に埋め込む[構造体](#0fq59c)．前後のstruct list_headへの参照の組からなる．

<a id="0btwul"></a>

## struct mbuf

[FreeBSD](#ofaawr)における[パケットバッファ](#ebra35)．連鎖して1つのパケットまたはデータ列を表す．データはstruct mbuf内の領域か，それが参照する外部の領域に格納される．パケットの先頭のstruct mbufは，パケット全体の長さと，受信した[struct ifnet](#wbs4wg)をもつ．

<a id="3s221u"></a>

## struct mm_struct

[Linux](#eh8l2u)における[アドレス空間記述子](#sjz43t)．同じ[スレッドグループ](#qugvsb)に属する[スレッド](#ou7dup)はこれを共有する．

<a id="zsv4ce"></a>

## struct mount

[FreeBSD](#ofaawr)の[仮想ファイルシステム](#gid8it)において，[ファイルシステム](#pp17bd)の1つの実体を表す[データ構造](#y9ua1k)．実装の[操作表](#xxcrwp)をもち，根の[struct vnode](#6qdkzg)はこれを通じて得る．[マウント](#96n6sj)されたものは，マウント先の[ディレクトリ](#j1d7gn)の[struct vnode](#6qdkzg)を参照する．

ToDo: [144](todo.md#todo-144)

<a id="ix9fth"></a>

## struct namecache

[FreeBSD](#ofaawr)における[名前キャッシュ](#lnizbx)の要素．[ディレクトリ](#j1d7gn)の[struct vnode](#6qdkzg)と名前の組を，その名前のファイルの[struct vnode](#6qdkzg)に結び付ける．

<a id="bcbwbu"></a>

## struct net_device

[Linux](#eh8l2u)における[ネットワークインターフェース記述子](#u4q636)．[ハードウェアアドレス](#le1wss)をもつ．

<a id="nsn2y1"></a>

## struct nsproxy

[Linux](#eh8l2u)において，[スレッド](#ou7dup)が用いる[Linux名前空間](#rmoy1r)への参照を束ね，同じ組をもつ[スレッド](#ou7dup)の間で共有される[データ構造](#y9ua1k)．ユーザー名前空間は含まず，[struct cred](#hotd7l)が参照する．PID名前空間は，自身の属するものでなく，作成する子の属するものを参照する．

ToDo: [127](todo.md#todo-127)

<a id="04vse1"></a>

## struct page

[Linux](#eh8l2u)における[ページフレーム記述子](#o7oik1)．

<a id="kx0thl"></a>

## struct pmap

[FreeBSD](#ofaawr)において，1つの[アドレス空間](#rygcc4)の[仮想記憶](#ysrn1f)の対応付けのうち[プロセッサ](#4ad6s1)に設定するものを，機種依存の形式で保持する[データ構造](#y9ua1k)．失われた対応付けは[struct vm_map](#9j376u)から再構成される．

<a id="zlzhsg"></a>

## struct prison

[FreeBSD](#ofaawr)において，1つの[jail](#xoam9f)を表す[データ構造](#y9ua1k)．識別番号，名前，親のstruct prison，根とする[ディレクトリ](#j1d7gn)，ホスト名をもつ．

<a id="gt9zce"></a>

## struct proc

[FreeBSD](#ofaawr)における[プロセス記述子](#smq3zz)．識別番号をもち，所属する[struct thread](#u3ag9q)の集合，[struct vmspace](#1p4y2z)，[struct filedesc](#nij06r)，[struct ucred](#s1h4s6)を参照する．

<a id="klvvmj"></a>

## struct sk_buff

[Linux](#eh8l2u)における[パケットバッファ](#ebra35)．1つで1つのパケットを表し，データを格納する領域と，その中の各層のヘッダの位置と，通過する[struct net_device](#bcbwbu)をもつ．

ToDo: [153](todo.md#todo-153)，[126](todo.md#todo-126)

<a id="cn7ia0"></a>

## struct sock

[struct socket](#8a9dsr)が参照する，[ソケット](#oscpon)の[プロトコル](#bhk5im)に依存する状態を保持する[データ構造](#y9ua1k)．送信と受信の[待ち行列](#lhxknx)に[struct sk_buff](#klvvmj)を保持する．

ToDo: [144](todo.md#todo-144)

<a id="8a9dsr"></a>

## struct socket

[Linux](#eh8l2u)において，1つの[ソケット](#oscpon)を[struct file](#3gg1hf)と結び付けて表し，[struct sock](#cn7ia0)を参照する[データ構造](#y9ua1k)．

ToDo: [144](todo.md#todo-144)

<a id="os8s4h"></a>

## struct socket

[FreeBSD](#ofaawr)において，1つの[ソケット](#oscpon)を表す[データ構造](#y9ua1k)．[プロトコル](#bhk5im)の[操作表](#xxcrwp)と，[プロトコル](#bhk5im)に依存する状態への参照をもつ．データを送受信するものは，送信と受信の[待ち行列](#lhxknx)に[struct mbuf](#0btwul)を保持する．

ToDo: [144](todo.md#todo-144)，[130](todo.md#todo-130)

<a id="7yjz2f"></a>

## struct super_block

[Linux](#eh8l2u)の[仮想ファイルシステム](#gid8it)において，[マウント](#96n6sj)された[ファイルシステム](#pp17bd)の1つの実体を表す[データ構造](#y9ua1k)．根の[struct dentry](#5t7a17)と[操作表](#xxcrwp)をもち，[ブロックデバイス](#1frbzb)に格納されるものはその[ブロックデバイス](#1frbzb)を参照する．

ToDo: [144](todo.md#todo-144)

<a id="1jy9hb"></a>

## struct task_struct

[Linux](#eh8l2u)における[スレッド記述子](#nehk4w)．[struct mm_struct](#3s221u)，[struct files_struct](#84r2z8)，[struct fs_struct](#yve2sf)，[struct nsproxy](#nsn2y1)を参照する．[clone](#64p7b9)で作られた[スレッド](#ou7dup)は，指定に応じてこれらを呼び出し元と共有するか，新たに作ったものを参照する．[セキュリティ文脈](#lxnyp5)は[struct cred](#hotd7l)を参照して得る．

ToDo: [126](todo.md#todo-126)

<a id="u3ag9q"></a>

## struct thread

[FreeBSD](#ofaawr)における[スレッド記述子](#nehk4w)．所属する[struct proc](#gt9zce)を参照する．所属する[struct proc](#gt9zce)の[struct ucred](#s1h4s6)への参照を自身でも保持し，[セキュリティ文脈](#lxnyp5)としてこれを用いる．

<a id="s1h4s6"></a>

## struct ucred

[FreeBSD](#ofaawr)において，[セキュリティ文脈](#lxnyp5)を表す[データ構造](#y9ua1k)．ユーザーとグループの識別番号と，所属する[jail](#xoam9f)の[struct prison](#zlzhsg)への参照をもつ．[置換更新](#gv4jmw)で更新される．

<a id="1yzl6g"></a>

## struct vm_area_struct

[Linux](#eh8l2u)における[メモリ領域記述子](#q3l4ki)．対応付け先は，ファイルの区間か，ファイルをもたない無名の領域である．

<a id="9j376u"></a>

## struct vm_map

[FreeBSD](#ofaawr)において，[struct vm_map_entry](#xx4asa)の集合を保持する[データ構造](#y9ua1k)．[仮想記憶](#ysrn1f)の対応付けの正本である．

<a id="xx4asa"></a>

## struct vm_map_entry

[FreeBSD](#ofaawr)における[メモリ領域記述子](#q3l4ki)で，[struct vm_map](#9j376u)の要素である．

ToDo: [130](todo.md#todo-130)

<a id="0prgra"></a>

## struct vm_object

[FreeBSD](#ofaawr)において，内容の中の位置で[struct vm_page](#8lled2)を索引して保持し，保持していない位置の内容を種類に応じた供給元から得る[データ構造](#y9ua1k)．[struct vm_map_entry](#xx4asa)は区間の内容を得るためにこれを参照する．[コピーオンライト](#q33a7g)による写しは，書き込まれた[ページ](#05by8w)を保持する新たなstruct vm_objectが元のstruct vm_objectを背後に参照する連鎖で表される．

<a id="8lled2"></a>

## struct vm_page

[FreeBSD](#ofaawr)における[ページフレーム記述子](#o7oik1)．[struct vm_object](#0prgra)に属するものは，その[struct vm_object](#0prgra)と中の位置をもつ．

<a id="1p4y2z"></a>

## struct vmspace

[FreeBSD](#ofaawr)における[アドレス空間記述子](#sjz43t)．[メモリ領域記述子](#q3l4ki)の集合を[struct vm_map](#9j376u)として，[プロセッサ](#4ad6s1)に設定する対応付けを[struct pmap](#kx0thl)として内包する．

ToDo: [130](todo.md#todo-130)

<a id="6qdkzg"></a>

## struct vnode

[FreeBSD](#ofaawr)における[VFSノード](#pg1lac)．属する[struct mount](#zsv4ce)と，[ファイルシステム](#pp17bd)の実装に固有のデータへの参照をもつ．許可，所有者，大きさの[メタデータ](#f7of70)は[操作表](#xxcrwp)を通じて実装から得る．ファイルの内容の[ページキャッシュ](#yobm0y)は，参照する[struct vm_object](#0prgra)が保持する．

<a id="4665g9"></a>

## sync操作

[Apache ZooKeeper](#o7jjj5)において，接続先の[サーバー](#uteg7y)の状態を[ZooKeeperアンサンブル](#csow5k)の[リーダー](#v8js9k)に追いつかせる操作．

<a id="7js10f"></a>

## sys/queue.h

[FreeBSD](#ofaawr)において，[埋め込み連結リスト](#0qdj5m)をつくる[マクロ](#3llsmk)群を定めるヘッダ．リストは単方向のSLISTとSTAILQ，双方向のLISTとTAILQの4種である．

<a id="87mh85"></a>

## viz

[Chromium](#2aag3y)において，[レンダラープロセス](#53ckw6)と[ブラウザプロセス](#ejqo3w)から受けた[CompositorFrame](#gyxatn)を集めて[合成](#mbw8ar)し，画面に表示する[サービス](#8ytqi4)．[GPUプロセス](#4hdszd)で動作する．

<a id="bhf8md"></a>

## win32k.sys

[Windows NT](#jzpnq4)において，[ウィンドウ](#zbv6hc)管理と画面描画を[特権モード](#uk5ihn)で実装する[Portable Executable形式](#uaym9q)のモジュール．

<a id="xus9ny"></a>

## znode

[Apache ZooKeeper](#o7jjj5)の[名前空間](#m7lbe4)の要素．スラッシュで区切ったパスで識別され，データと子のznodeをもつ．更新のたびに増えるバージョン番号をもち，書き込みは期待するバージョン番号を条件にできる．シーケンシャルの指定で作成すると，親ごとに単調増加する番号が名前に付加される．

<a id="as86xt"></a>

## アイテム

[Zabbix](#o6myi6)において，[ホスト](#y3ka2w)から1系列の値を収集する定義．[アイテムタイプ](#ugi5pv)，[アイテムキー](#dfhotk)，更新間隔，値の型，[ヒストリ](#s04nt7)と[トレンド](#spfrm5)の保存期間，単位，[保存前処理](#zgnkho)をもつ．

ToDo: [103](todo.md#todo-103)

<a id="dfhotk"></a>

## アイテムキー

[アイテム](#as86xt)が収集する値を指定する，`キー[引数,…]`の形式の文字列．[ホスト](#y3ka2w)内で一意である．

<a id="ugi5pv"></a>

## アイテムタイプ

[アイテム](#as86xt)の値の収集方式．

<a id="8yx5pi"></a>

## アイデンティティ

[主体](#pyjgmb)を他の[主体](#pyjgmb)と区別する属性の集合．

<a id="3z77qd"></a>

## アイデンティティプロバイダ

[主体](#pyjgmb)を[認証](#l2zofw)し，その結果を[認証アサーション](#ki350n)として[サービスプロバイダ](#l5pssm)に伝える[サーバー](#uteg7y)．

ToDo: [122](todo.md#todo-122)

<a id="feccnu"></a>

## アイデンティティベースポリシー

[IAMアイデンティティ](#ix9em5)に付与される[主体側ポリシー](#r95ien)である[IAMポリシー](#let9u3)．

<a id="2xbuy8"></a>

## アカウントインスタンス

単一の[AWSアカウント](#r2ghkv)を管理対象とする[Identity Centerインスタンス](#5mx2oh)．[アカウント割り当て](#n4iumx)をもたない．

<a id="n4iumx"></a>

## アカウント割り当て

[組織インスタンス](#ljfr92)において，[Identity Centerユーザー](#ypfrjn)または[Identity Centerグループ](#97jks3)，[許可セット](#p7yj2k)，[AWSアカウント](#r2ghkv)の組．その[Identity Centerユーザー](#ypfrjn)に，[許可セット](#p7yj2k)から作成された[IAMロール](#k1a9js)の[IAMロール引受け](#0d235w)を許す．

<a id="pfbsnf"></a>

## アクション

[Zabbix](#o6myi6)において，指定した発生源の[イベント](#przzj5)に対し，条件を満たすときに実行する処理の定義．[イベント](#przzj5)の発生時，[障害](#ilz3yu)の復旧時，[障害](#ilz3yu)の更新時のそれぞれに実行内容をもち，発生時の実行内容は[エスカレーション](#813is1)に従う．通知には[ユーザーメディア](#0dudjl)を用いる．

<a id="6blyao"></a>

## アクセスキーID

[シークレットアクセスキー](#f2nfys)と組で発行され，その組を識別する公開の文字列．

<a id="8w6s21"></a>

## アクセストークン

[認可サーバー](#kvuagh)が発行し，[認可クライアント](#47yah2)が[リソースサーバー](#6lul9i)への要求に添えて，その操作の[認可](#8esn53)を示す[トークン](#qt96h9)．

<a id="9ea3s0"></a>

## アクセストークン

[Windows NT](#jzpnq4)において，[プロセス](#lm3iq5)または[スレッド](#ou7dup)の[セキュリティ文脈](#lxnyp5)を表す[カーネルオブジェクト](#4d5j7r)．ユーザーと所属グループの[セキュリティ識別子](#kzruy4)，個々の[保護対象](#qfjrzs)によらないシステム全体の操作の権利，[整合性レベル](#79uj26)を保持する．

<a id="tzn2n7"></a>

## アクセスポイント

[Wi-Fi](#r9it7l)の[端末](#zw6tbw)を収容し，[端末](#zw6tbw)の間，および[端末](#zw6tbw)と他の[リンク](#xy3alb)の間でデータを[中継](#zgr0mv)する装置．収容する[ネットワーク](#uy18d2)を[SSID](#2c4um1)で示す．

<a id="gyqv5u"></a>

## アクセス制御エントリ

[Windows NT](#jzpnq4)において，1つの[セキュリティ識別子](#kzruy4)とアクセス権の組に対し，許可，拒否，アクセスの試みの記録を含む種別のうち1つを指定する要素．

<a id="1zwomz"></a>

## アクセス許可モデル

[スタックセット](#9hhp5i)が[スタック](#ib0gqz)を作成，更新，削除するときに[IAMロール引受け](#0d235w)の対象とする[IAMロール](#k1a9js)の用意の仕方を定める，[スタックセット](#9hhp5i)の設定．

<a id="wnrx30"></a>

## アクセス許可境界

[IAMユーザー](#viavkt)または[IAMロール](#k1a9js)に設定され，その[アイデンティティベースポリシー](#feccnu)に対する[許可上限](#id1pzp)を定める[IAMポリシー](#let9u3)．

<a id="v4p3tn"></a>

## アクティブチェック

[Zabbix Agent](#5l6oih)が[監視主体](#90keyj)から対象の[アイテム](#as86xt)の一覧を取得し，自ら値を収集して[監視主体](#90keyj)へ送る方式．送信先は既定で[TCP](#cndtkv)の[ポート番号](#avetpx)10051である．これによる[アイテムタイプ](#ugi5pv)をZabbixエージェント(アクティブ)と呼ぶ．

<a id="w88wo5"></a>

## アドミッションコントロール

[kube-apiserver](#yv6kx0)が[認証](#l2zofw)と[認可](#8esn53)の後，[etcd](#c0gd56)への永続化の前に，[オブジェクト](#8ot6zr)の作成，更新，削除の要求を変更または拒否する処理．変更を行うmutatingの段階の後に，検証を行うvalidatingの段階が続く．各段階で，要求を外部の[HTTP](#31abh6)の[サーバー](#uteg7y)に送り，その応答により変更または拒否を決めることもできる．

<a id="zeoy6t"></a>

## アドレスファミリー

AFI（アドレス体系）とSAFI（後続アドレス体系）の組で表す，[BGP](#0ey58g)で交換する[経路](#5433mk)の種類．

<a id="k4ztwu"></a>

## アドレス区間記述子

[アドレス空間](#rygcc4)のうち，[ページ](#05by8w)の境界に揃った連続する区間1つと，その対応付け先を表す[データ構造](#y9ua1k)．

ToDo: [148](todo.md#todo-148)

<a id="rygcc4"></a>

## アドレス空間

[プロセス](#lm3iq5)が参照できるアドレスの集合．

<a id="sjz43t"></a>

## アドレス空間記述子

[カーネル](#cktjwx)において，1つの[アドレス空間](#rygcc4)を表す[データ構造](#y9ua1k)．[メモリ領域記述子](#q3l4ki)の集合と，[ページテーブル](#yd60a1)を保持する．

ToDo: [148](todo.md#todo-148)

<a id="t6j8bt"></a>

## アノテーション

[オブジェクト](#8ot6zr)に付けるキーと値の組で，選択には用いられず，ツールや[コントローラ](#pboh16)が参照する情報を保持するもの．

<a id="1ipr3r"></a>

## アフィニティ

[Pod](#k4ef3z)の配置先を，[ノード](#6qrxi1)の[ラベル](#zugz1v)，または既に配置された他の[Pod](#k4ef3z)の[ラベル](#zugz1v)に基づいて，必須または優先の条件として制約する指定．後者には，同じ配置を避ける反アフィニティがある．

<a id="zxvj73"></a>

## アプリケーション

利用者が目的の作業を行うために用いるプログラム．

<a id="zb3vp3"></a>

## アベイラビリティゾーン

[リージョン](#1df8fw)内の，1つ以上のデータセンターからなる[障害ドメイン](#84djzd)．同じ[リージョン](#1df8fw)の他のアベイラビリティゾーンと物理的に分離され，低遅延の[ネットワーク](#uy18d2)で接続される．

<a id="ra546q"></a>

## アラーム

[Amazon CloudWatch](#y77mp8)の[監視規則](#pvfe2i)．[メトリクス](#1s1rpf)を閾値と比較する方式をもつ．状態が変化したとき，指定された処理を実行する．

<a id="35wv5r"></a>

## イベント

システムで生じた出来事を表すデータ．

<a id="przzj5"></a>

## イベント

[Zabbix](#o6myi6)において，[Zabbix Server](#tm6l00)が記録する[イベント](#35wv5r)．発生源は[トリガー](#3gz3w5)，[ネットワークディスカバリ](#1ffv8q)，[自動登録](#grye5m)，内部，[サービス](#8vi40f)のいずれかであり，内部の発生源は[アイテム](#as86xt)，[LLDルール](#dkfxg4)，[トリガー](#3gz3w5)の評価可否の変化である．発生時刻と[深刻度](#jcg0dk)をもち，[確認応答](#8zsqwg)の有無を記録する．

ToDo: [103](todo.md#todo-103)

<a id="aoy2yh"></a>

## インスタンスストア

[EC2インスタンス](#0d2awr)を動作させる物理計算機に接続された記憶装置による一時的な[ブロックストレージ](#8ztcnx)．[EC2インスタンス](#0d2awr)の停止，休止，終了によりデータは失われる．

<a id="h08bfc"></a>

## インスタンスタイプ

[EC2インスタンス](#0d2awr)に割り当てる仮想的な[プロセッサ](#4ad6s1)の数，メモリ量，ストレージ，[ネットワーク](#uy18d2)性能の組を表す名前．インスタンスファミリー，世代，付加的な属性を表す接頭部と，サイズを`.`で連結した形式をとる．

<a id="8e4tig"></a>

## インタプリタ

プログラムを[機械語](#ky7oww)に翻訳せずに，その命令を逐次解釈して実行するプログラム．

<a id="3qoztf"></a>

## インターネット

多数の[自律システム](#8wkkrz)が[BGP](#0ey58g)で[経路](#5433mk)を交換して相互に接続した，世界規模の[ネットワーク](#uy18d2)．

<a id="qmmwja"></a>

## インターネットゲートウェイ

[VPC](#4ln6ld)に接続され，[パブリックIPアドレス](#kwufcq)をもつ[Elastic Network Interface](#f5pqfi)と[インターネット](#3qoztf)との双方向の通信を[中継](#zgr0mv)する[AWSリソース](#78qg7h)．[IPv4](#un6pgt)では，[Elastic Network Interface](#f5pqfi)の[VPC](#4ln6ld)内の[IPアドレス](#3ksnfe)と[パブリックIPアドレス](#kwufcq)を[NAT](#4blq8k)で相互に変換する．

<a id="c5u142"></a>

## インデックス

[データベース](#vlgsmo)において，キーの値から該当するデータの位置を全体の走査なしに求めるための補助的な[データ構造](#y9ua1k)．データの更新のたびに保守される．

<a id="zbv6hc"></a>

## ウィンドウ

画面上の矩形の領域で，プログラムが表示と入力の受付けに用いるもの．

<a id="s3eb1d"></a>

## エグゼクティブ

[ntoskrnl.exe](#tguf9f)のうち，[NTカーネル層](#oobie1)の上に位置し，[資源](#k7gc81)を管理する構成要素からなる層．

<a id="813is1"></a>

## エスカレーション

[障害](#ilz3yu)が継続する間，[アクション](#pfbsnf)の発生時の実行内容をステップ順に，指定した間隔で実行する仕組み．

<a id="r05bfh"></a>

## エッジロケーション

[Amazon CloudFront](#912vnc)の拠点として，[リージョン](#1df8fw)とは別に世界各地に置かれる施設．

<a id="lz4omp"></a>

## エニーキャスト

同じ[IPプレフィックス](#6rwn5e)への[経路](#5433mk)を複数の地点から広告し，各送信元の[IPパケット](#w9btgk)を[ルーティングプロトコル](#ktkn70)が選んだ1つの地点に届ける方式．

<a id="di8gj9"></a>

## エフェメラルznode

作成した[ZooKeeperセッション](#z4pzpk)の終了時に自動で削除される[znode](#xus9ny)．子をもてない．

<a id="9i1lg3"></a>

## エンドポイント

要求の宛先となる[URL](#ydpswy)．

<a id="7rs9yk"></a>

## エンドポイントサービス

[AWS PrivateLink](#8irydc)の提供側で，[Network Load Balancer](#mddvjx)または[Gateway Load Balancer](#uou6rr)を，許可された[プリンシパル](#t8ujsy)の[VPCエンドポイント](#pguegu)から利用できるようにする[AWSリソース](#78qg7h)．

<a id="ewuega"></a>

## エンドユーザー検証URI

[認可サーバー](#kvuagh)が公開する[URL](#ydpswy)．[主体](#pyjgmb)から[ユーザーコード](#xnr09h)の入力を受け付け，対の[デバイスコード](#74muqa)を得た[認可クライアント](#47yah2)への許可または拒否を問い合わせる．

<a id="yimp6h"></a>

## オクテット

8ビットからなるデータの単位．

<a id="8ot6zr"></a>

## オブジェクト

[kube-apiserver](#yv6kx0)が管理する永続的な実体で，[クラスタ](#dx7pxd)の望ましい状態または実際の状態を表す．種類，名前，[ラベル](#zugz1v)，[アノテーション](#t6j8bt)，[所有者参照](#zktekl)を[メタデータ](#f7of70)としてもつ．望ましい状態を記したspecと，観測された状態を記したstatusをもつかは，種類ごとに定まる．

<a id="k4obt0"></a>

## オブジェクトストレージ

データを，キーで識別される単位で，階層をもたない[名前空間](#m7lbe4)に格納する[記憶域](#kltl5m)の提供形態．キーからデータを得る点で，[キーバリューストア](#trahzf)と同じ[データモデル](#7qyeyy)をもつ．

<a id="6onm6b"></a>

## オブジェクトハンドル

[Windows NT](#jzpnq4)において，[カーネルオブジェクト](#4d5j7r)を識別する[ハンドル](#ib1jow)．作成時に許可されたアクセス権を保持し，以後の操作はそのアクセス権の範囲に限られる．

<a id="teluba"></a>

## オブジェクトファイル

[翻訳単位](#ncbdz9)の翻訳により作られる，[リンカ](#xbrsqq)の入力となるファイル．機械語とデータ，それらのうち外から参照できるものの名前，外の定義を参照する名前，参照の解決後に書き換える位置を含む．

<a id="qwhtqy"></a>

## オブジェクトマネージャ

[エグゼクティブ](#s3eb1d)において，[カーネルオブジェクト](#4d5j7r)の作成，命名，参照計数，[オブジェクトハンドル](#6onm6b)，保護を管理する構成要素．

<a id="ivjde9"></a>

## オブジェクト名前空間

[オブジェクトマネージャ](#qwhtqy)が管理する，[カーネルオブジェクト](#4d5j7r)の階層的な[名前空間](#m7lbe4)．[オブジェクトマネージャ](#qwhtqy)はこの中の名前から[カーネルオブジェクト](#4d5j7r)への[名前解決](#3or1pp)を行う．

<a id="fm7edw"></a>

## オペレーション設定

[スタックセット](#9hhp5i)が各[スタックインスタンス](#hmll3k)の[スタック](#ib0gqz)を作成，更新，削除するときの実行方法を定める設定．

<a id="qtnfg6"></a>

## オペレータ

[CustomResourceDefinition](#b5ztot)で追加した種類の[オブジェクト](#8ot6zr)を監視する[コントローラ](#pboh16)により，特定のアプリケーションの運用操作を自動化する方式．

<a id="c8v8vw"></a>

## オペレーティングシステム

[資源](#k7gc81)を管理し，抽象化した[資源](#k7gc81)を[プロセス](#lm3iq5)に提供するソフトウェア．中核は[カーネル](#cktjwx)である．

ToDo: [139](todo.md#todo-139)

<a id="3f4vd8"></a>

## オリジン

[URL](#ydpswy)の[スキーム](#yo9qhx)，[ホスト](#0qt5x4)，[ポート番号](#avetpx)の組，または他のいずれとも同一でない不透明なオリジン．組のオリジンは，3つが全て等しいときに同一である．

<a id="29xuc7"></a>

## オンプレミス

利用者が自ら管理する施設に設備を置いて運用する形態．

<a id="kv40ye"></a>

## オープンソースライセンス

ソースコードの利用，改変，再配布を，相手と目的を問わず許す[ソフトウェアライセンス](#tae9qv)．

<a id="xo9y6e"></a>

## カスタムリソース

[CustomResourceDefinition](#b5ztot)により追加された種類の[オブジェクト](#8ot6zr)．

<a id="oh434k"></a>

## カプセル化

ある[プロトコル](#bhk5im)のデータの単位を，別の[プロトコル](#bhk5im)のデータの単位の中身として包むこと．

ToDo: [153](todo.md#todo-153)

<a id="cktjwx"></a>

## カーネル

[特権モード](#uk5ihn)で動作する[オペレーティングシステム](#c8v8vw)の部分．

<a id="4d5j7r"></a>

## カーネルオブジェクト

[Windows NT](#jzpnq4)において，[オブジェクトマネージャ](#qwhtqy)が管理する，[資源](#k7gc81)を表す[データ構造](#y9ua1k)．[ユーザーモード](#v7n2z8)からは[オブジェクトハンドル](#6onm6b)を介してのみ操作される．

ToDo: [126](todo.md#todo-126)

<a id="4995ja"></a>

## カーネルモジュール

[カーネル](#cktjwx)の実行中に読み込みと取り外しができる，[カーネル](#cktjwx)の[拡張プログラム](#iwj5fh)．

<a id="fnr7ad"></a>

## カーネルモードドライバ

[Windows NT](#jzpnq4)において，[特権モード](#uk5ihn)で動作して[I/O要求パケット](#dd3rvj)を処理する，[カーネル](#cktjwx)の[拡張プログラム](#iwj5fh)．実行時に読み込まれる[Portable Executable形式](#uaym9q)のモジュールである．

<a id="6exqbl"></a>

## ガベージコレクション

プログラムから到達できなくなったメモリの領域を自動で検出し，回収する仕組み．

<a id="3x9bon"></a>

## ガベージコレクタ

[kube-controller-manager](#9xikob)で動作し，[所有者参照](#zktekl)の指す所有者が存在しない[オブジェクト](#8ot6zr)を削除する[コントローラ](#pboh16)．

<a id="kj4w0z"></a>

## キャッシュ

得るのに時間のかかるデータの写しを，より速く参照できる場所に一時的に保持し，再度の要求に用いる仕組み．

<a id="mqlfip"></a>

## キュー

最初に追加した要素を最初に取り出す[抽象データ型](#wlwn4m)．

<a id="trahzf"></a>

## キーバリューストア

[連想配列](#lkmji4)を[データモデル](#7qyeyy)とする[NoSQL](#um196p)の[データベース](#vlgsmo)．

<a id="225nin"></a>

## クォーラム

[レプリカ](#filo46)を保持する計算機の集合のうち，決定に必要な承認を与える部分集合．任意の2つのクォーラムが共通の要素をもつように定める．過半数はこれを満たす．

<a id="xv4m3d"></a>

## クライアント

[サーバー](#uteg7y)に要求を送り，応答を受け取るプログラムまたは計算機．

<a id="rhlnw8"></a>

## クライアントID

[認可サーバー](#kvuagh)が[認可クライアント](#47yah2)に割り当てる識別子．

<a id="vhpaym"></a>

## クライアントクレデンシャルグラント

[認可クライアント](#47yah2)の[認証情報](#pyxpuc)のみを示し，[認可クライアント](#47yah2)自身が[主体](#pyjgmb)として[認可](#8esn53)を得る[認可グラント](#n1yjv8)．grant_typeはclient_credentialsである．

<a id="yy3buk"></a>

## クラウドコンピューティング

[ネットワーク](#uy18d2)を介し，計算，記憶，[ネットワーク](#uy18d2)の能力を利用者の要求に応じて即時に割り当て，使用量に応じて課金する提供形態．

<a id="i5ziux"></a>

## クラウドサービス

[クラウドコンピューティング](#yy3buk)の基盤が提供する，[API](#9e509k)で操作される機能の単位．

<a id="dx7pxd"></a>

## クラスタ

[コントロールプレーン](#b8ign2)と，[Pod](#k4ef3z)を実行する1つ以上の[ノード](#6qrxi1)からなる，[Kubernetes](#t6cr2a)の管理単位．

<a id="8rb2lo"></a>

## クラスタID

[経路反射クラスタ](#of0ehz)を識別する4[オクテット](#yimp6h)の値．

<a id="ypg0zz"></a>

## グラフ

頂点の集合と，頂点の対である辺の集合からなる構造．辺の対に順序があるものを有向グラフ，ないものを無向グラフと呼ぶ．

<a id="hegs24"></a>

## グレースフルリスタート

[BGPスピーカー](#v9rnch)の[BGP](#0ey58g)の処理の再起動中も，[ピア](#7wmnel)がその[BGPスピーカー](#v9rnch)から学習した[経路](#5433mk)を保持して転送を継続する[ケイパビリティ](#6vfi5n)．

<a id="bdchaf"></a>

## グローバルリソース

[リージョン](#1df8fw)に属さない[AWSリソース](#78qg7h)．

<a id="6vfi5n"></a>

## ケイパビリティ

[BGPスピーカー](#v9rnch)が[OPENメッセージ](#x55k1n)で対応を通知する，[BGP](#0ey58g)の拡張．

<a id="7ll5nd"></a>

## コアネットワーク

[セルラー通信](#fibo1z)において，[基地局](#00im0x)を収容し，[端末](#zw6tbw)の[認証](#l2zofw)，移動の管理，他の[ネットワーク](#uy18d2)との接続を行う[ネットワーク](#uy18d2)．

<a id="q33a7g"></a>

## コピーオンライト

共有されたデータの写しの作成を書き込みの時点まで遅らせ，書き込まれる部分のみを写す[遅延割り当て](#mwtuz5)．

<a id="ib4lx9"></a>

## コミュニティ

[経路](#5433mk)に付す4[オクテット](#yimp6h)のタグの集合を表すオプション推移の[パス属性](#q885vr)．[ルーティングポリシー](#4bwmon)の適用条件に用いる．周知の値NO_EXPORTを付したものは[自律システム](#8wkkrz)の外部へ広告せず，NO_ADVERTISEを付したものはいずれの[ピア](#7wmnel)へも広告しない．

<a id="uds0ak"></a>

## コンテナ

[カーネル](#cktjwx)を共有しつつ，[プロセス](#lm3iq5)の集合に[資源隔離](#1sgoxr)と[資源制限](#g9mkrr)を施した実行環境．

ToDo: [147](todo.md#todo-147)

<a id="ea366y"></a>

## コンテナイメージ

[コンテナ](#uds0ak)の初期の[ファイルシステム](#pp17bd)を構成する読取り専用のレイヤの積み重ねと，実行の設定からなる不変のパッケージ．タグまたは内容のダイジェストで指定される．

<a id="ldx08d"></a>

## コンテナオーケストレーション

複数の計算機にわたる[コンテナ](#uds0ak)の配置，実行，置き換えを自動で管理すること．

<a id="xj5eeh"></a>

## コンテナプローブ

[kubelet](#zh69qe)が[コンテナ](#uds0ak)に対して行う[ヘルスチェック](#4ofscj)．livenessの失敗は[コンテナ](#uds0ak)の再起動を，readinessの失敗は[Service](#3bb8t3)の[通信先](#b2znuk)からの[Pod](#k4ef3z)の除外をもたらし，startupが成功するまで他のプローブは行われない．

<a id="nl5o0m"></a>

## コンテナランタイム

[コンテナイメージ](#ea366y)を取得し，それから[コンテナ](#uds0ak)を作成，実行，停止するソフトウェア．

<a id="gyftmn"></a>

## コンテンツ配信ネットワーク

コンテンツを利用者の近くの拠点に[キャッシュ](#kj4w0z)して配信し，遅延と配信元の負荷を減らす[ネットワーク](#uy18d2)．

<a id="pboh16"></a>

## コントローラ

[kube-apiserver](#yv6kx0)を介して[オブジェクト](#8ot6zr)を監視し，そのspecを望ましい状態とする[調整ループ](#gibl6s)．

<a id="xy6h7u"></a>

## コントローラ参照

controllerフィールドが真である[所有者参照](#zktekl)で，1つの[オブジェクト](#8ot6zr)につき最大1つ存在する．[ラベルセレクタ](#x5w385)をもつ[ワークロードリソース](#qg1bbv)を調整する[コントローラ](#pboh16)は，その[ラベルセレクタ](#x5w385)に一致しコントローラ参照をもたない[オブジェクト](#8ot6zr)に，その[ワークロードリソース](#qg1bbv)を指すコントローラ参照を追加し（採用），一致しなくなった[オブジェクト](#8ot6zr)からこれを削除する（解放）．

<a id="b8ign2"></a>

## コントロールプレーン

[クラスタ](#dx7pxd)の状態を保持し，[Pod](#k4ef3z)の配置と[オブジェクト](#8ot6zr)の調整を行う構成要素の集合．[kube-apiserver](#yv6kx0)，[etcd](#c0gd56)，[kube-scheduler](#62x28a)，[kube-controller-manager](#9xikob)を含む．

<a id="a2nw9z"></a>

## コンパイラ

ある[プログラミング言語](#nw9j2i)で記述されたプログラムを，意味を保って別の言語のプログラムに翻訳するプログラム．

<a id="gqdkk9"></a>

## サイト

[オリジン](#3f4vd8)の[スキーム](#yo9qhx)と，[ホスト](#0qt5x4)の[登録可能ドメイン](#ij6arz)の組．[ホスト](#0qt5x4)が[登録可能ドメイン](#ij6arz)をもたないときは，[ホスト](#0qt5x4)自体を用いる．

<a id="guozy4"></a>

## サイト分離

異なる[サイト](#gqdkk9)の[Web文書](#qbtpp4)を，異なる[レンダラープロセス](#53ckw6)で処理する[Chromium](#2aag3y)の方式．[ブラウザプロセス](#ejqo3w)は各[レンダラープロセス](#53ckw6)を1つの[サイト](#gqdkk9)に固定し，他の[サイト](#gqdkk9)のデータの要求を拒否する．[Spectre](#0ygryr)と[レンダラープロセス](#53ckw6)の乗っ取りによる，[同一オリジンポリシー](#q18xj8)を越えたデータの読み取りを防ぐ．

<a id="e9v7rv"></a>

## サブネット

[ネットワーク](#uy18d2)を分割した区画のうち，1つの[IPプレフィックス](#6rwn5e)を割り当てられたもの．区画内の[IPアドレス](#3ksnfe)はその[IPプレフィックス](#6rwn5e)に属する．

<a id="oygsrp"></a>

## サブネット

[VPC](#4ln6ld)の[サブネット](#e9v7rv)．[VPC](#4ln6ld)の[IPプレフィックス](#6rwn5e)に含まれる[IPプレフィックス](#6rwn5e)をもち，1つの[アベイラビリティゾーン](#zb3vp3)に属する．1つの[経路表](#dw7079)と1つの[ネットワークACL](#eqsq3o)が関連付けられる．

<a id="y825lm"></a>

## サブルーチン

プログラム中で名前により呼び出され，処理の後に呼び出し元へ制御を戻す命令の列．引数を受け取り，値を返しうる．同じ引数に同じ値を返すとは限らない点で[関数](#egp00x)と異なる．

<a id="2xz9pb"></a>

## サンドボックス

[Chromium](#2aag3y)が子の[プロセス](#lm3iq5)に適用する[サンドボックス](#94k6ba)．[ブラウザプロセス](#ejqo3w)を[ブローカー](#9c98zu)とする．[Windows NT](#jzpnq4)では[制限付きトークン](#pjlcj6)，[ジョブオブジェクト](#mmivp1)，低い[整合性レベル](#79uj26)を，[Linux](#eh8l2u)では[Linux名前空間](#rmoy1r)による隔離と[seccomp-BPF](#x4wvbi)を，[macOS](#0ml2dc)では[Seatbelt](#w8962q)を用いる．

ToDo: [102](todo.md#todo-102)

<a id="94k6ba"></a>

## サンドボックス

[プロセス](#lm3iq5)が利用できる[資源](#k7gc81)と操作を，[オペレーティングシステム](#c8v8vw)の機構により制限した実行環境．

<a id="uteg7y"></a>

## サーバー

[クライアント](#xv4m3d)から要求を受け付けて処理し，応答を返すプログラムまたは計算機．

<a id="vnbuyu"></a>

## サーバーレス

利用者が[サーバー](#uteg7y)の用意，容量の計画，保守を行わずに機能を利用する[クラウドコンピューティング](#yy3buk)の形態．

<a id="8vi40f"></a>

## サービス

[Zabbix](#o6myi6)において，タグで対応付けた[障害](#ilz3yu)から状態を算出する監視単位．階層をなす．

ToDo: [103](todo.md#todo-103)

<a id="8ytqi4"></a>

## サービス

[Chromium](#2aag3y)において，[Mojoインターフェース](#q1r1b6)を通じてのみ他から利用される機能の単位．利用者はそれが動作する[プロセス](#lm3iq5)に依存しない．

<a id="stc42v"></a>

## サービスコントロールポリシー

[組織](#sm4tb3)の頂点に付与され，その頂点を根とする部分木の[組織アカウント](#4q8oz8)が参照する[メンバーアカウント](#yd40pa)内の[プリンシパル](#t8ujsy)に対する[許可上限](#id1pzp)を定める[IAMポリシー](#let9u3)．[組織リソース](#b2lxzl)である．

<a id="xvi8o5"></a>

## サービスプレフィックス

[AWSサービス](#40hiw9)を一意に識別する短い文字列．[Amazon Resource Name](#c6b1z3)と[ポリシーステートメント](#bhslyd)で[AWSサービス](#40hiw9)を指定するのに用いる．

<a id="l5pssm"></a>

## サービスプロバイダ

[アイデンティティプロバイダ](#3z77qd)が発行した[認証アサーション](#ki350n)を検証し，それに基づいて[主体](#pyjgmb)を[認証](#l2zofw)されたものとして扱うプログラム．

<a id="m0e2aa"></a>

## サービスマネージド型アクセス許可

[AWS Organizations](#yj1k74)との連携により[IAMロール](#k1a9js)が自動で作成され，[組織アカウント](#4q8oz8)が参照する[AWSアカウント](#r2ghkv)を[スタックインスタンス](#hmll3k)とする[アクセス許可モデル](#1zwomz)．[組織単位](#1wx4ge)を[スタックインスタンス](#hmll3k)の指定に用いることができ，その[組織単位](#1wx4ge)に加わった[組織アカウント](#4q8oz8)への自動の作成を設定できる．[管理者アカウント](#kh4nz4)は[管理アカウント](#svvkiy)または[委任管理者](#qiqjj5)である．[管理アカウント](#svvkiy)は[ターゲットアカウント](#gjqg2o)とならない．

<a id="k0p5vs"></a>

## サービス制御マネージャ

[Windows NT](#jzpnq4)において，[Windowsサービス](#s709hz)の登録情報を[レジストリ](#0w2o91)から読み，その起動・停止・状態を管理する[ユーザーモード](#v7n2z8)の[プロセス](#lm3iq5)．実行ファイルはservices.exeである．

<a id="j1vxpm"></a>

## システムアクセス制御リスト

[セキュリティ記述子](#28ts3b)において，記録の対象とするアクセスの試みの指定と，[保護対象](#qfjrzs)の[整合性レベル](#79uj26)を保持する[アクセス制御エントリ](#gyqv5u)のリスト．

<a id="saksfm"></a>

## システムコール

[ユーザーモード](#v7n2z8)で動作する[プロセス](#lm3iq5)が[カーネル](#cktjwx)に処理を要求する手段．要求の処理は[特権モード](#uk5ihn)で行われる．

ToDo: [139](todo.md#todo-139)

<a id="1upnid"></a>

## シャーディング

データをキーに基づいて分割し，分割したそれぞれを異なる計算機に保持する手法．

<a id="twt6a6"></a>

## シンプロビジョニング

[記憶域](#kltl5m)の[遅延割り当て](#mwtuz5)により，実際の容量を超える容量を提示する手法．

<a id="f2nfys"></a>

## シークレットアクセスキー

[アクセスキーID](#6blyao)と組で発行され，[AWSサービス](#40hiw9)への要求に付す署名の計算に用いる秘密の値．

<a id="mmivp1"></a>

## ジョブオブジェクト

[Windows NT](#jzpnq4)において，[プロセス](#lm3iq5)の集合をまとめて管理し，その集合に[資源制限](#g9mkrr)を課し，可能な操作を制限する[カーネルオブジェクト](#4d5j7r)．

<a id="yo9qhx"></a>

## スキーム

[URL](#ydpswy)の先頭に置かれ，残りの部分の解釈と，対象を取得する手段を定める名前．

<a id="wpudzb"></a>

## スケジューラ

[スレッド](#ou7dup)に[プロセッサ](#4ad6s1)を割り当てる順序と期間を決める機構．

<a id="35e1pq"></a>

## スタイル計算

[DOM](#mtrvw2)の各要素に適用される[CSS](#hks4qq)のプロパティの値を決める処理．

<a id="hfx60b"></a>

## スタック

最後に追加した要素を最初に取り出す[抽象データ型](#wlwn4m)．

<a id="ib0gqz"></a>

## スタック

1つの[テンプレート](#iwvz04)に従って作成された[AWSリソース](#78qg7h)の集合を，1つの単位として管理する[リージョンリソース](#tynhcw)．

<a id="hmll3k"></a>

## スタックインスタンス

[スタックセット](#9hhp5i)が[スタック](#ib0gqz)を作成する先として登録した，1つの[AWSアカウント](#r2ghkv)と1つの[リージョン](#1df8fw)の組．

<a id="9hhp5i"></a>

## スタックセット

1つの[テンプレート](#iwvz04)に従う[スタック](#ib0gqz)を，各[スタックインスタンス](#hmll3k)に一括で作成，更新，削除する[リージョンリソース](#tynhcw)．1つの[管理者アカウント](#kh4nz4)に属し，1つの[アクセス許可モデル](#1zwomz)をもつ．

<a id="5wdqsg"></a>

## スタブリゾルバ

[DNS委任](#dmv9zd)を自身では辿らず，[フルリゾルバ](#0n86br)に最終的な結果を返すよう求める再帰的な問合せを送って[名前解決](#tpx3c2)の結果を得る[クライアント](#xv4m3d)．

<a id="wmv9lk"></a>

## ストリーム

1つの[接続](#st4cz5)の中で，送信の順序を保って受信側に渡される一連のデータ．

<a id="ahlapd"></a>

## スナップショット

データの集まりの，ある時点における状態．

<a id="ou7dup"></a>

## スレッド

1つの制御の流れをもち，[スケジューラ](#wpudzb)によって[プロセッサ](#4ad6s1)を割り当てられる実行の単位．

<a id="qugvsb"></a>

## スレッドグループ

[Linux](#eh8l2u)において，1つの[プロセス](#lm3iq5)をなす[スレッド](#ou7dup)の集合．[clone](#64p7b9)でCLONE_THREADを指定して作成された[スレッド](#ou7dup)は，呼び出し元と同じスレッドグループに属する．最初の[スレッド](#ou7dup)の識別番号をスレッドグループの識別番号とし，[プロセス](#lm3iq5)の識別番号として用いる．

ToDo: [144](todo.md#todo-144)

<a id="4dqyyj"></a>

## スレッド優先度

[Windows NT](#jzpnq4)において，[スケジューラ](#wpudzb)が[スレッド](#ou7dup)の選択に用いる0から31の整数．16から31の範囲は実時間優先度と呼ばれ，[スケジューラ](#wpudzb)が値を変えない．1から15の範囲は可変優先度と呼ばれ，[スケジューラ](#wpudzb)が入出力の完了を含む事象の際に一時的に引き上げる．0は解放済みの[物理メモリ](#svua87)を零で初期化する[スレッド](#ou7dup)のみが用いる．

<a id="nehk4w"></a>

## スレッド記述子

[カーネル](#cktjwx)が[スレッド](#ou7dup)ごとに1つ保持する，その[スレッド](#ou7dup)を表す[データ構造](#y9ua1k)．[スケジューラ](#wpudzb)が用いる状態をもつ．

<a id="zgzyka"></a>

## セキュリティグループ

[Elastic Network Interface](#f5pqfi)に関連付けられ，[許可加算評価](#kirdkx)を用いるステートフルな[ファイアウォール](#x6zoh6)．規則の送信元または送信先に他のセキュリティグループを指定できる．

<a id="tcttnt"></a>

## セキュリティ参照モニタ

[エグゼクティブ](#s3eb1d)において，[アクセストークン](#9ea3s0)と[セキュリティ記述子](#28ts3b)を照合し，アクセスの可否を判定する構成要素．

<a id="lxnyp5"></a>

## セキュリティ文脈

実行中の処理の要求に対する[認可](#8esn53)で用いられる，その処理が代理する[主体](#pyjgmb)の[アイデンティティ](#8yx5pi)と権限の組．

ToDo: [125](todo.md#todo-125)

<a id="28ts3b"></a>

## セキュリティ記述子

[Windows NT](#jzpnq4)において，[保護対象](#qfjrzs)に付随し，所有者とグループの[セキュリティ識別子](#kzruy4)，[随意アクセス制御リスト](#9ss4j8)，[システムアクセス制御リスト](#j1vxpm)を保持する[データ構造](#y9ua1k)．

<a id="kzruy4"></a>

## セキュリティ識別子

[Windows NT](#jzpnq4)において，[主体](#pyjgmb)を識別する可変長の値．

<a id="frjmk2"></a>

## セクションオブジェクト

[Windows NT](#jzpnq4)において，1つ以上の[アドレス空間](#rygcc4)に対応付けられうるメモリの区域を表す[カーネルオブジェクト](#4d5j7r)．内容はファイルまたは[ページファイル](#e43owm)を背後にもつ．複数の[アドレス空間](#rygcc4)に対応付けることで[共有メモリ](#76g0nk)を実現する．

<a id="8xzr27"></a>

## セッショントークン

[AWS Security Token Service](#q44rf3)が一時的な[認証情報](#pyxpuc)に含める[トークン](#qt96h9)．その一時的な[認証情報](#pyxpuc)が有効であることを示す．

<a id="rvp82m"></a>

## セッションマネージャ

[Windows NT](#jzpnq4)において，[カーネル](#cktjwx)が起動処理で最初に作成する[ユーザーモード](#v7n2z8)の[プロセス](#lm3iq5)．[Windowsセッション](#f0u95h)の作成を担う．実行ファイルはsmss.exeである．

<a id="4lwir4"></a>

## セッション維持

同じ要求元からの通信を同じ[通信先](#b2znuk)へ[中継](#zgr0mv)し続ける[ロードバランサー](#v7r0tg)の機能．

<a id="d9lgtj"></a>

## セル

[セルラー通信](#fibo1z)において，[基地局](#00im0x)が[端末](#zw6tbw)を収容する地理的な範囲の単位．1つの[基地局](#00im0x)は1つ以上のセルを受け持つ．

<a id="1hx920"></a>

## セルフマネージド型アクセス許可

利用者が[IAMロール](#k1a9js)を作成する[アクセス許可モデル](#1zwomz)．[管理者アカウント](#kh4nz4)自身も[ターゲットアカウント](#gjqg2o)とできる．

<a id="fibo1z"></a>

## セルラー通信

地域を[セル](#d9lgtj)に分けて[基地局](#00im0x)に受け持たせ，[移動体通信事業者](#em1w73)が免許を受けた[周波数帯](#utnq9w)で運用する[無線通信](#1zfkze)の方式．[端末](#zw6tbw)は移動に伴い[ハンドオーバー](#2frvtg)を行う．

<a id="oscpon"></a>

## ソケット

[プロセス](#lm3iq5)が[ハンドル](#ib1jow)を通じてデータを送受信する，通信の[端点](#b084uv)を表す[資源](#k7gc81)．

<a id="tae9qv"></a>

## ソフトウェアライセンス

ソフトウェアの著作権者が，その利用，複製，改変，再配布を許す範囲と条件を定める許諾．

<a id="zil7hp"></a>

## ゾーン転送

[DNSゾーン](#2eh0s0)の内容を，[リーダー](#v8js9k)であるプライマリの[権威DNSサーバー](#9es8da)から[フォロワー](#telc65)であるセカンダリの[権威DNSサーバー](#9es8da)へ[レプリケーション](#rv2ppc)する手続き．全体を転送するAXFRと差分を転送するIXFRがあり，[TCP](#cndtkv)で行う．セカンダリは[SOAレコード](#sktwnj)のシリアル番号の増加により更新を検知する．

<a id="u7pfjr"></a>

## タブ

[Webブラウザ](#gcly3z)の[ウィンドウ](#zbv6hc)内で切り替えて表示される，最上位の[フレーム](#mtx2pq)をもつ単位．

<a id="gjqg2o"></a>

## ターゲットアカウント

[スタックインスタンス](#hmll3k)の[AWSアカウント](#r2ghkv)．

<a id="2vuoon"></a>

## ダイナミックリンクライブラリ

[Windows NT](#jzpnq4)における[動的ライブラリ](#imdjs3)で，[Portable Executable形式](#uaym9q)のファイル．

<a id="ccg2j3"></a>

## ダーティリード

[トランザクション](#v5hhix)が，他の[トランザクション](#v5hhix)のコミットされていない書き込みを読む異常．

<a id="0jljvq"></a>

## チェイン

[Netfilter](#feag1h)に設定する規則を並べた列．[Netfilterフック](#ljpkdd)に結び付けたチェインは，そのフックを通る[IPパケット](#w9btgk)に規則を適用する．

<a id="r85zs1"></a>

## テイント

[ノード](#6qrxi1)に付けるキー，値，効果の組で，一致する[トレラーション](#ey9zls)をもたない[Pod](#k4ef3z)を，効果に応じて新たな配置の禁止，配置の回避，実行中のものの削除により拒むもの．

<a id="nud9su"></a>

## テキストエディタ

文字の並びとして記述されたファイルを表示し，編集するソフトウェア．

ToDo: [151](todo.md#todo-151)

<a id="iwvz04"></a>

## テンプレート

[スタック](#ib0gqz)に含める[AWSリソース](#78qg7h)を[JSON](#o3ixrz)またはYAMLで宣言した文書．

<a id="k4ea9r"></a>

## テンプレート

[Zabbix](#o6myi6)において，[ホスト](#y3ka2w)または他のテンプレートにリンクされ，含む設定をリンク先に継承させる設定の集合．リンク関係は循環しない．

<a id="2zr71h"></a>

## ディスプレイリスト

図形，文字，画像を描く命令の列．画素を含まず，[ラスタライズ](#3o1tma)により画素に変換される．

<a id="j1d7gn"></a>

## ディレクトリ

[ファイルシステム](#pp17bd)において，[ハードリンク](#wgjpyk)の集合を保持するファイル．階層の根である根ディレクトリを除き，他のディレクトリに属する．

ToDo: [153](todo.md#todo-153)

<a id="rqm5zv"></a>

## デッドロック

複数の処理が，それぞれ他の処理の保持する[ロック](#7x5us3)の解放を待ち，いずれも進めなくなる状態．

<a id="74muqa"></a>

## デバイスコード

[デバイス認可エンドポイント](#v501wk)が発行し，[デバイス認可グラント](#7b6pse)で示す値．有効期限は発行時の応答のexpires_inで示される．

<a id="v501wk"></a>

## デバイス認可エンドポイント

[認可サーバー](#kvuagh)の[エンドポイント](#9i1lg3)．[バックチャネル](#y4a9oj)で[クライアントID](#rhlnw8)を含む要求を受け付け，[デバイスコード](#74muqa)，[ユーザーコード](#xnr09h)，[エンドユーザー検証URI](#ewuega)を返す．

<a id="7b6pse"></a>

## デバイス認可グラント

[デバイスコード](#74muqa)を示す[認可グラント](#n1yjv8)．grant_typeはurn:ietf:params:oauth:grant-type:device_codeである．[認可クライアント](#47yah2)は，[主体](#pyjgmb)が許可または拒否するか[デバイスコード](#74muqa)が失効するまで，これを繰り返し[トークンエンドポイント](#f9akzj)に示す．

<a id="49baql"></a>

## デバッガ

実行中のプログラムを制御し，その内部状態を観察して欠陥を特定するプログラム．

<a id="wvtf4u"></a>

## データオブジェクト

プログラムが作成，参照，破棄するメモリの領域で，作成から破棄までの寿命をもつもの．

<a id="hymk0a"></a>

## データパイプ

[Mojo](#n32mlc)において，生産者から消費者へ一方向にバイト列を流す通路．

<a id="vlgsmo"></a>

## データベース

[データモデル](#7qyeyy)に従って構造化され，永続的に保持されるデータの集まり．

<a id="wn1pbv"></a>

## データベース管理システム

[データベース](#vlgsmo)を管理し，その問合せと更新を[トランザクション](#v5hhix)として実行するソフトウェア．

<a id="7qyeyy"></a>

## データモデル

データの構造，操作，制約を定める形式．

<a id="w7t735"></a>

## データ型

[プログラミング言語](#nw9j2i)において，値のとりうる範囲と，値に適用できる操作を定める分類．

ToDo: [149](todo.md#todo-149)

<a id="y9ua1k"></a>

## データ構造

データの集まりを，要素間の関係と，それに対する操作の[計算量](#tl94hx)が定まるように記憶領域上に組織する形式．[抽象データ型](#wlwn4m)を実現する．

<a id="qiadm1"></a>

## トピック

[パブリッシュ/サブスクライブ型](#8rrdgi)において，メッセージの発行先となり，受信者に購読される名前付きの宛先．

<a id="53ain9"></a>

## トライ

各辺に1つの記号を対応させ，根から頂点まで辿る辺の記号の列をその頂点のキーとする[木](#dj2zcx)．共通の接頭辞をもつキーは根から辿る辺を共有する．

<a id="v5hhix"></a>

## トランザクション

[データベース管理システム](#wn1pbv)が[ACID特性](#2ywo5m)を満たして一体として実行する操作の列．コミットにより結果が確定し，アボートにより全ての結果が取り消される．

<a id="mcggb8"></a>

## トランジット

提供側の[自律システム](#8wkkrz)が，顧客の[自律システム](#8wkkrz)に[インターネット](#3qoztf)全体への到達性を提供する関係．提供側は全ての[経路](#5433mk)を顧客へ広告し，顧客の[経路](#5433mk)を全ての隣接する[自律システム](#8wkkrz)へ広告する．

<a id="dayw7g"></a>

## トランスポートプロトコル

[IPパケット](#w9btgk)で運ばれ，[IPアドレス](#3ksnfe)と[ポート番号](#avetpx)の組で[端点](#b084uv)を識別する[プロトコル](#bhk5im)．

<a id="3gz3w5"></a>

## トリガー

[Zabbix](#o6myi6)の[監視規則](#pvfe2i)．[トリガー関数](#7jm7xn)を含む条件式で[アイテム](#as86xt)の値から[トリガー値](#hxwb5z)を定める．[アイテム](#as86xt)の新しい値の受信時に評価され，時間に基づく[トリガー関数](#7jm7xn)を含む場合は定期的にも評価される．[深刻度](#jcg0dk)をもつ．復旧には条件式が偽であることを要し，復旧条件式が設定されていればそれも真であることを要する．自動復旧しない設定ももつ．

<a id="hxwb5z"></a>

## トリガー値

[トリガー](#3gz3w5)の判定結果．障害なしを表す`OK`と，障害を表す`PROBLEM`のいずれかである．

<a id="7jm7xn"></a>

## トリガー関数

[トリガー](#3gz3w5)の条件式で[アイテム](#as86xt)の[ヒストリ](#s04nt7)を評価する関数．評価期間を時間または件数で指定する．値が届かないことは`nodata`で検知する．

<a id="ey9zls"></a>

## トレラーション

[Pod](#k4ef3z)に付ける指定で，一致する[テイント](#r85zs1)をもつ[ノード](#6qrxi1)への配置を許すもの．その[ノード](#6qrxi1)への配置を強制しない．

<a id="spfrm5"></a>

## トレンド

[数値型](#4e4la0)の[アイテム](#as86xt)の[ヒストリ](#s04nt7)を1時間ごとに集計した，最小，平均，最大，件数の系列．

<a id="qt96h9"></a>

## トークン

発行者が発行し，要求に添えて提示され，[認証](#l2zofw)または[認可](#8esn53)の判断の根拠となる値．

ToDo: [116](todo.md#todo-116)

<a id="f9akzj"></a>

## トークンエンドポイント

[認可サーバー](#kvuagh)の[エンドポイント](#9i1lg3)．[バックチャネル](#y4a9oj)で[認可グラント](#n1yjv8)を受け付け，検証に成功すれば[アクセストークン](#8w6s21)を返す．

<a id="rw3kg0"></a>

## ドキュメントストア

入れ子の構造をもつ文書を単位としてデータを格納し，文書内の属性で問い合わせる[NoSQL](#um196p)の[データベース](#vlgsmo)．

<a id="d8xx9q"></a>

## ドメイン名

[DNS](#v0yvpo)の階層的な[名前空間](#m7lbe4)がなす[木](#dj2zcx)において，頂点を指す名前．頂点から根までの[DNSラベル](#7siuzh)を順にドットで区切って表記する．全体は255[オクテット](#yimp6h)以下であり，大文字と小文字を区別せずに比較される．

<a id="u4t3xd"></a>

## ドライバスタック

1つの装置に対する[I/O要求パケット](#dd3rvj)を上位から順に処理する，[カーネルモードドライバ](#fnr7ad)の層の列．

<a id="day4yo"></a>

## ナビゲーション

[フレーム](#mtx2pq)が表示する[URL](#ydpswy)を変更する処理．[Web文書](#qbtpp4)の置換を伴うものと伴わないものがある．

<a id="kdca50"></a>

## ネイティブAPI

[エグゼクティブ](#s3eb1d)が[システムコール](#saksfm)として公開する[API](#9e509k)．[ユーザーモード](#v7n2z8)からは，[ntdll.dll](#z6nvth)の名前がNtまたはZwで始まる[サブルーチン](#y825lm)を通じて呼び出される．

<a id="uy18d2"></a>

## ネットワーク

[ネットワークインターフェース](#cufd0s)を介して相互に接続され，データを交換する計算機の集まり．

<a id="eqsq3o"></a>

## ネットワークACL

[サブネット](#oygsrp)に関連付けられ，規則番号の順の[先頭一致評価](#xwqhlo)で通信の可否を決めるステートレスな[ファイアウォール](#x6zoh6)．

<a id="cufd0s"></a>

## ネットワークインターフェース

計算機が[ネットワーク](#uy18d2)に接続する点．[IPアドレス](#3ksnfe)が割り当てられる．

<a id="u4q636"></a>

## ネットワークインターフェース記述子

[カーネル](#cktjwx)が[ネットワークインターフェース](#cufd0s)ごとに1つ保持する，その[ネットワークインターフェース](#cufd0s)を表す[データ構造](#y9ua1k)．名前と[操作表](#xxcrwp)をもつ．

<a id="cxvq7l"></a>

## ネットワークサービス

[Chromium](#2aag3y)において，[HTTP](#31abh6)を含む[プロトコル](#bhk5im)による通信と，[Cookie](#jhdprm)と[キャッシュ](#kj4w0z)の管理を行う[サービス](#8ytqi4)．[ユーティリティプロセス](#0lze03)または[ブラウザプロセス](#ejqo3w)で動作する．

<a id="1ffv8q"></a>

## ネットワークディスカバリ

[Zabbix](#o6myi6)において，指定した[IPアドレス](#3ksnfe)の範囲に指定した検査を行い，応答した計算機を検出する機能．

<a id="atp440"></a>

## ノンリピータブルリード

[トランザクション](#v5hhix)が同じ[行](#rylgay)を再び読み取り，その間にコミットされた他の[トランザクション](#v5hhix)の更新により異なる値を得る異常．

<a id="6qrxi1"></a>

## ノード

[クラスタ](#dx7pxd)において[Pod](#k4ef3z)を実行する計算機．[仮想マシン](#uwly1k)または物理計算機であり，[kubelet](#zh69qe)と[コンテナランタイム](#nl5o0m)を動かす．

<a id="dt1rv7"></a>

## ハイパーバイザ

1台の物理計算機上で複数の[仮想マシン](#uwly1k)を実行し，物理計算機の[プロセッサ](#4ad6s1)，[物理メモリ](#svua87)，入出力装置をそれらに配分するソフトウェア．

<a id="76afpj"></a>

## ハイブ

[レジストリ](#0w2o91)を構成する，単位として読み込まれる[木](#dj2zcx)の部分．揮発性のものを除き，対応するファイルに保存される．

<a id="tbiv0k"></a>

## ハッシュテーブル

キーの[ハッシュ関数](#fnegr1)の値から[配列](#06enpz)内の格納位置を定めて[連想配列](#lkmji4)を実現する[データ構造](#y9ua1k)．位置の衝突は，同じ位置の要素を[連結リスト](#zhodwh)につなぐか，別の空き位置を探すことで解決する．要素数と[配列](#06enpz)の大きさの比を定数以下に保てば，各操作の期待時間は定数である．

<a id="fnegr1"></a>

## ハッシュ関数

任意の値を固定長の値に写す[関数](#egp00x)．異なる入力に同じ出力を与えることを衝突と呼ぶ．

<a id="2frvtg"></a>

## ハンドオーバー

通信中の[端末](#zw6tbw)が，通信を受け持つ[セル](#d9lgtj)を切り替えること．

<a id="ib1jow"></a>

## ハンドル

[プロセス](#lm3iq5)が開いている[資源](#k7gc81)を識別する，[プロセス](#lm3iq5)ごとの値．

<a id="n9vofr"></a>

## ハンドル表

[ハンドル](#ib1jow)から，それが識別する[資源](#k7gc81)を表す[データ構造](#y9ua1k)への対応表．

<a id="5urygr"></a>

## ハートビート

送信元が動作していることを受信側に示すため，一定の間隔で送られるメッセージ．受信側は，これが一定時間届かないことで送信元の故障を判定する[故障検出](#iq5tpn)に用いる．

<a id="le1wss"></a>

## ハードウェアアドレス

[リンク](#xy3alb)において[ネットワークインターフェース](#cufd0s)を識別する識別子．

<a id="5ui5pq"></a>

## ハードウェア抽象化層

[Windows NT](#jzpnq4)において，[割り込み](#owu45r)制御器とタイマを含む，プラットフォーム依存のハードウェアの差異を[ntoskrnl.exe](#tguf9f)から隠す，[特権モード](#uk5ihn)で動作する層．

<a id="wgjpyk"></a>

## ハードリンク

[ディレクトリ](#j1d7gn)が保持する，名前とファイルの対応．1つのファイルは複数のハードリンクをもちうる．

<a id="47l5g8"></a>

## バイトコード

[インタプリタ](#8e4tig)による実行のために定められた，[プロセッサ](#4ad6s1)に依存しない命令の符号の体系．

<a id="y4a9oj"></a>

## バックチャネル

[Webブラウザ](#gcly3z)を介さず，送り手が受け手に直接[HTTP](#31abh6)の要求を送る送受信の経路．

<a id="ebra35"></a>

## パケットバッファ

[カーネル](#cktjwx)が，[ネットワーク](#uy18d2)で送受信するデータを格納し，[プロトコル](#bhk5im)の層の間で受け渡す[データ構造](#y9ua1k)．

<a id="xj5xfp"></a>

## パスベクタ型

[経路](#5433mk)ごとに，それが通過した[自律システム](#8wkkrz)の列を付して伝え，受信者が自身の[AS番号](#wvk6j6)を含む列をもつものを破棄することで，広告が同じ[自律システム](#8wkkrz)を再び通る循環を防ぐ方式．

<a id="ymj65u"></a>

## パス名

[ディレクトリ](#j1d7gn)をたどる名前の列で，[ファイルシステム](#pp17bd)内のファイルを指す文字列．根ディレクトリを起点とする絶対パス名と，作業ディレクトリを起点とする相対パス名がある．

ToDo: [153](todo.md#todo-153)

<a id="q885vr"></a>

## パス属性

[BGP](#0ey58g)の[経路](#5433mk)に付される属性．周知必須，周知任意，オプション推移，オプション非推移のいずれかに分類される．[BGPスピーカー](#v9rnch)は未知のオプション推移属性を保持して他の[ピア](#7wmnel)へ伝え，未知のオプション非推移属性を破棄する．

<a id="n8ur2q"></a>

## パッシブチェック

[監視主体](#90keyj)が[Zabbix Agent](#5l6oih)に[アイテムキー](#dfhotk)を送って要求し，[Zabbix Agent](#5l6oih)が値を応答する方式．[Zabbix Agent](#5l6oih)は既定で[TCP](#cndtkv)の[ポート番号](#avetpx)10050で待ち受ける．これによる[アイテムタイプ](#ugi5pv)をZabbixエージェントと呼ぶ．

<a id="kwufcq"></a>

## パブリックIPアドレス

それを含む[IPプレフィックス](#6rwn5e)への[経路](#5433mk)が[インターネット](#3qoztf)で広告される[IPアドレス](#3ksnfe)．

<a id="mciymw"></a>

## パブリックサブネット

[インターネットゲートウェイ](#qmmwja)への[経路](#5433mk)を，関連付けられた[経路表](#dw7079)にもつ[サブネット](#oygsrp)．

<a id="8rrdgi"></a>

## パブリッシュ/サブスクライブ型

送信者がメッセージを受信者でなく[トピック](#qiadm1)に発行し，その[トピック](#qiadm1)を購読する全ての受信者へメッセージが配信される通信の方式．

<a id="s04nt7"></a>

## ヒストリ

[Zabbix Server](#tm6l00)が保存する，[アイテム](#as86xt)の値と収集時刻の組の系列．[数値型](#4e4la0)の[アイテム](#as86xt)のヒストリは[メトリクス](#1s1rpf)である．

<a id="ouc72p"></a>

## ビットフィールド

[構造体](#0fq59c)または[共用体](#ms7tuh)のメンバーのうち，幅をビット数で指定したもの．アドレスをとれない．

<a id="ci6jok"></a>

## ビルドシステム

ソースから成果物を作る手順を，成果物の依存関係に従って実行するプログラム．

<a id="7wmnel"></a>

## ピア

[BGPセッション](#s9mnt1)における相手側の[BGPスピーカー](#v9rnch)．

<a id="x6zoh6"></a>

## ファイアウォール

[ポリシー](#d3j3nj)に基づき通信を許可または拒否する機構．ステートフルなものは[接続追跡](#d1bl1o)により許可した通信への応答を規則によらず許可し，ステートレスなものは応答にも明示的な許可を要する．

<a id="pp17bd"></a>

## ファイルシステム

データを，名前の付いたファイルとして，[ディレクトリ](#j1d7gn)からなる階層的な[名前空間](#m7lbe4)に格納する[記憶域](#kltl5m)の提供形態．

<a id="rb2704"></a>

## ファイルディスクリプタ

ファイルを識別する，非負整数の[ハンドル](#ib1jow)．

<a id="rxedfi"></a>

## ファイルディスクリプタ表

[ファイルディスクリプタ](#rb2704)から，それが参照する[開かれたファイル記述](#u8r1ic)を表す[データ構造](#y9ua1k)への[ハンドル表](#n9vofr)．

<a id="wgkq3s"></a>

## ファントムリード

[トランザクション](#v5hhix)が同じ条件で再び検索し，その間にコミットされた他の[トランザクション](#v5hhix)の挿入または削除により異なる[行](#rylgay)の集合を得る異常．

<a id="gd0lzy"></a>

## フェイルオーバー

障害を起こした計算機の処理を，待機していた別の計算機に引き継がせること．

<a id="telc65"></a>

## フォロワー

[リーダー](#v8js9k)をもつ協調において，[リーダー](#v8js9k)から伝えられた更新を受け入れる，[リーダー](#v8js9k)以外の計算機．

<a id="qnmpnu"></a>

## フォワードプロキシ

要求元の側に置かれ，要求元が[通信先](#b2znuk)への要求を委ねる[プロキシ](#2f8683)．

<a id="0n86br"></a>

## フルリゾルバ

[名前解決](#tpx3c2)を代行し，[DNSルートサーバー](#p77v01)から[DNS委任](#dmv9zd)を順に辿って，[権威DNSサーバー](#9es8da)に自身の保持する応答または委任先のみを返させる反復的な問合せを行い，得た[資源レコード](#syx2b4)をTTLの間[キャッシュ](#kj4w0z)する[サーバー](#uteg7y)．

<a id="mtx2pq"></a>

## フレーム

[Webブラウザ](#gcly3z)において，1つの[Web文書](#qbtpp4)を表示する領域．[タブ](#u7pfjr)の最上位のフレームを根とし，[Web文書](#qbtpp4)に埋め込まれたフレームを子とする[木](#dj2zcx)をなす．

<a id="xjb5je"></a>

## フロントチャネル

[Webブラウザ](#gcly3z)を介する送受信の経路．送り手は[Webブラウザ](#gcly3z)への応答により，[Webブラウザ](#gcly3z)に受け手への要求を送らせ，情報をその要求に含める．

<a id="ejqo3w"></a>

## ブラウザプロセス

[Chromium](#2aag3y)において，最初に起動し，[サンドボックス](#2xz9pb)の外で動作する[プロセス](#lm3iq5)．他の[プロセス](#lm3iq5)を起動・管理し，それらの[ブローカー](#9c98zu)となる．[ウィンドウ](#zbv6hc)と[タブ](#u7pfjr)を管理し，[ナビゲーション](#day4yo)の要求を開始して，応答を受けた後に[Web文書](#qbtpp4)を処理させる[レンダラープロセス](#53ckw6)を決める．

<a id="k60l5g"></a>

## ブロック

[記憶域](#kltl5m)を固定長に区切った，読み書きの単位．

<a id="8ztcnx"></a>

## ブロックストレージ

[ブロック](#k60l5g)の番号で位置を指定して読み書きする[記憶域](#kltl5m)の提供形態．

<a id="1frbzb"></a>

## ブロックデバイス

[カーネル](#cktjwx)が[ブロックストレージ](#8ztcnx)として扱う装置．

<a id="9c98zu"></a>

## ブローカー

[サンドボックス](#94k6ba)内の[プロセス](#lm3iq5)の要求に対して[権限代行](#lti67d)を行い，[資源](#k7gc81)にアクセスする，より高い権限の[プロセス](#lm3iq5)．

<a id="vds2br"></a>

## プライベートサブネット

[インターネットゲートウェイ](#qmmwja)への[経路](#5433mk)を，関連付けられた[経路表](#dw7079)にもたない[サブネット](#oygsrp)．

<a id="dz7dp9"></a>

## プラグイン

あるプログラムとは別のプログラムとして動作し，そのプログラムが定める規約に従って呼び出される[拡張プログラム](#iwj5fh)．

<a id="rewxde"></a>

## プリプロセッサ

[C言語](#4pg9c8)と[C++](#drl0oo)の翻訳の初めに，#で始まる指令に従ってソースを書き換える処理．指令はファイルの取り込み，[マクロ](#3llsmk)の展開，条件による部分の取捨を含む．

<a id="t8ujsy"></a>

## プリンシパル

[AWSサービス](#40hiw9)へ要求を送る[主体](#pyjgmb)．

<a id="2f8683"></a>

## プロキシ

要求元からの通信を終端し，自らを[端点](#b084uv)とする別の通信で[通信先](#b2znuk)へ[中継](#zgr0mv)する機構．

<a id="t7lw5k"></a>

## プロキシグループ

[Zabbix](#o6myi6)において，[Zabbix Proxy](#pjiioj)の集合．監視を委ねられた[ホスト](#y3ka2w)を，属する[Zabbix Proxy](#pjiioj)の間で分配する．

ToDo: [103](todo.md#todo-103)

<a id="nw9j2i"></a>

## プログラミング言語

プログラムを記述するための人工言語．

<a id="lm3iq5"></a>

## プロセス

[アドレス空間](#rygcc4)と1つ以上の[スレッド](#ou7dup)からなる，プログラムの実行の単位．

ToDo: [136](todo.md#todo-136)，[102](todo.md#todo-102)

<a id="smq3zz"></a>

## プロセス記述子

[カーネル](#cktjwx)が[プロセス](#lm3iq5)ごとに1つ保持する，その[プロセス](#lm3iq5)を表す[データ構造](#y9ua1k)．

ToDo: [144](todo.md#todo-144)

<a id="vjg5ws"></a>

## プロセス間通信

[プロセス](#lm3iq5)の間でデータを受け渡す手段．

<a id="4ad6s1"></a>

## プロセッサ

命令の列を読み出し，順に実行する装置．

<a id="bhk5im"></a>

## プロトコル

通信の[端点](#b084uv)の間で交換するメッセージの形式と，交換の手順の取り決め．

<a id="r4wode"></a>

## プロプライエタリライセンス

[オープンソースライセンス](#kv40ye)でない[ソフトウェアライセンス](#tae9qv)．

<a id="4ofscj"></a>

## ヘルスチェック

対象に定期的に問い合わせ，その応答により行う[故障検出](#iq5tpn)．[ロードバランサー](#v7r0tg)は正常でないと判定した[通信先](#b2znuk)を[中継](#zgr0mv)の対象から外す．

<a id="kkoocc"></a>

## ペイント

[レイアウト](#c23fys)の結果から，各要素を描く[ディスプレイリスト](#2zr71h)を作る処理．

<a id="05by8w"></a>

## ページ

[仮想記憶](#ysrn1f)が対応付けの単位とする，固定長で境界の揃ったアドレスの区間．

<a id="yobm0y"></a>

## ページキャッシュ

[カーネル](#cktjwx)が[物理メモリ](#svua87)に保持する，ファイルの内容の複製．ファイルを実行する[プロセス](#lm3iq5)は，この複製を[アドレス空間](#rygcc4)に対応付けて命令を読む．

<a id="yd60a1"></a>

## ページテーブル

[仮想記憶](#ysrn1f)において，[ページ](#05by8w)ごとに，対応する[ページフレーム](#4qztd7)とアクセス権を保持する表．

<a id="e43owm"></a>

## ページファイル

[Windows NT](#jzpnq4)において，ファイルに対応付けられていない[ページ](#05by8w)の内容を，[物理メモリ](#svua87)から取り除いた後に保持するファイル．

<a id="4qztd7"></a>

## ページフレーム

[ページ](#05by8w)と同じ長さで境界の揃った[物理メモリ](#svua87)の区間．

<a id="o7oik1"></a>

## ページフレーム記述子

[カーネル](#cktjwx)が管理する[ページフレーム](#4qztd7)ごとに1つ保持する，その[ページフレーム](#4qztd7)を表す[データ構造](#y9ua1k)．

<a id="0qt5x4"></a>

## ホスト

[URL](#ydpswy)のうち，対象を提供する計算機を示す部分．[ドメイン名](#d8xx9q)または[IPアドレス](#3ksnfe)である．

<a id="y3ka2w"></a>

## ホスト

[Zabbix](#o6myi6)において，監視対象の管理単位．1つ以上の[ホストグループ](#72maxq)に属する．値を収集する[監視主体](#90keyj)は，[Zabbix Server](#tm6l00)，指定した[Zabbix Proxy](#pjiioj)，[プロキシグループ](#t7lw5k)が割り当てた[Zabbix Proxy](#pjiioj)のいずれかである．

<a id="tyn5dk"></a>

## ホストインターフェース

[ホスト](#y3ka2w)への接続先．[IPアドレス](#3ksnfe)または[ドメイン名](#d8xx9q)と，[ポート番号](#avetpx)をもつ．種別は[Zabbix Agent](#5l6oih)，SNMP，IPMI，JMXのいずれかである．

<a id="72maxq"></a>

## ホストグループ

[Zabbix](#o6myi6)において，[ホスト](#y3ka2w)の集合の管理単位．

<a id="ptmib9"></a>

## ホールドタイム

[KEEPALIVEメッセージ](#niq3ho)または[UPDATEメッセージ](#zqwllr)を受信しないまま経過すると[BGPセッション](#s9mnt1)を閉じる時間．両[ピア](#7wmnel)の[OPENメッセージ](#x55k1n)の値の小さい方を用いる．値は0または3秒以上であり，0のときは満了しない．

<a id="0zbizc"></a>

## ボリューム

[Pod](#k4ef3z)内の[コンテナ](#uds0ak)の[ファイルシステム](#pp17bd)に[マウント](#96n6sj)される[ディレクトリ](#j1d7gn)で，[コンテナ](#uds0ak)の再起動を越えて内容が保たれるもの．emptyDirのように[Pod](#k4ef3z)と寿命を共にするものと，[PersistentVolumeClaim](#3b8umf)を介して[Pod](#k4ef3z)より長く存続するものがある．

<a id="um9c12"></a>

## ボリュームグループ

1つ以上の[物理ボリューム](#uj3w47)の[物理エクステント](#six0ds)を集めた，[LVM](#9tfla3)の[記憶域](#kltl5m)の集まり．[物理ボリューム](#uj3w47)の追加と除去により容量を変えられる．

<a id="ubm34x"></a>

## ポインタ

[データオブジェクト](#wvtf4u)または[サブルーチン](#y825lm)のアドレスを値とし，それを通じて参照先にアクセスするための値．

<a id="d3j3nj"></a>

## ポリシー

要求または通信に照合し，それを許可するか拒否するかを定める規則の集まり．

<a id="bhslyd"></a>

## ポリシーステートメント

[IAMポリシー](#let9u3)の要素で，Sid，Effect，Principal，NotPrincipal，Action，NotAction，Resource，NotResource，Conditionの要素により1つの許可または拒否を記述するもの．Actionは[サービスプレフィックス](#xvi8o5)と操作名を`:`で連結した形式で[AWSサービス](#40hiw9)の操作を，Resourceは[Amazon Resource Name](#c6b1z3)で対象を指定する．

<a id="avetpx"></a>

## ポート番号

[トランスポートプロトコル](#dayw7g)において，同じ[IPアドレス](#3ksnfe)上の[端点](#b084uv)を区別する16ビットの値．

<a id="96n6sj"></a>

## マウント

[ファイルシステム](#pp17bd)を，既存の[ファイルシステム](#pp17bd)の1つの[ディレクトリ](#j1d7gn)に接続し，その下で参照できるようにすること．

<a id="3llsmk"></a>

## マクロ

[プリプロセッサ](#rewxde)において，#define指令で定義される識別子と置換の字句列の組．以降のソース中に現れたその識別子を置換の字句列に展開する．引数をとるものを関数形式マクロと呼ぶ．

<a id="biu4lz"></a>

## マシンイメージ

計算機の起動に用いる，起動元の[ブロックデバイス](#1frbzb)の内容を保持するデータ．

<a id="uyne50"></a>

## マスターファイルテーブル

[NTFS](#42ymz9)において，各ファイルと[ディレクトリ](#j1d7gn)について1つ以上のレコードをもつ表．それ自身もファイルとして格納される．

<a id="ufkar7"></a>

## マルチAZ配置

[Amazon Relational Database Service](#txfy2g)において，更新を受け付ける[リーダー](#v8js9k)と別の[アベイラビリティゾーン](#zb3vp3)に，同期の[レプリケーション](#rv2ppc)で更新される待機用の[レプリカ](#filo46)を保持し，障害時に自動でそれへ[フェイルオーバー](#gd0lzy)する構成．

<a id="hz8j1v"></a>

## マルチプロトコル拡張

[BGP](#0ey58g)で，元来の対象である[IPv4](#un6pgt)の[経路](#5433mk)以外の[アドレスファミリー](#zeoy6t)の[経路](#5433mk)を交換する[ケイパビリティ](#6vfi5n)．広告するものをMP_REACH_NLRI，撤回するものをMP_UNREACH_NLRIのオプション非推移の[パス属性](#q885vr)で伝える．

<a id="8w6ttn"></a>

## マルチホーミング

1つの[自律システム](#8wkkrz)が複数の上流の[自律システム](#8wkkrz)に[eBGP](#vz4jtn)で接続する構成．

<a id="663plp"></a>

## メインスレッド

[レンダラープロセス](#53ckw6)において，[DOM](#mtrvw2)の操作，[Web文書](#qbtpp4)の[JavaScript](#y8ql3q)の実行，[スタイル計算](#35e1pq)，[レイアウト](#c23fys)，[ペイント](#kkoocc)を行う[スレッド](#ou7dup)．[レンダラープロセス](#53ckw6)ごとに1つあり，その中の全ての[フレーム](#mtx2pq)が共有する．

<a id="f7of70"></a>

## メタデータ

他のデータを記述するデータ．

<a id="xnwjk2"></a>

## メッセージパイプ

[Mojo](#n32mlc)において，2つの端点の間で双方向にメッセージを運ぶ通路．端点はメッセージに載せて他の[プロセス](#lm3iq5)へ渡せる．

<a id="egz05p"></a>

## メディアタイプ

[アクション](#pfbsnf)が通知に用いる送信方式．

<a id="1s1rpf"></a>

## メトリクス

監視の対象について，時刻ごとに測定された数値の系列．

<a id="4lrgjh"></a>

## メモリアロケータ

[プロセス](#lm3iq5)内の要求に応じてメモリの領域を割り当て，解放された領域を再利用に回すプログラム．

<a id="n4hz3z"></a>

## メモリマネージャ

[エグゼクティブ](#s3eb1d)において，[仮想記憶](#ysrn1f)を実装する構成要素．

<a id="qbsksa"></a>

## メモリ安全性

プログラムが[範囲外アクセス](#l0kw7s)と[解放後使用](#onqz9u)を起こさないことの保証．

<a id="q3l4ki"></a>

## メモリ領域記述子

区間内でアクセス権が一様な[アドレス区間記述子](#k4ztwu)．

ToDo: [148](todo.md#todo-148)

<a id="yd40pa"></a>

## メンバーアカウント

[組織](#sm4tb3)に属する，[管理アカウント](#svvkiy)以外の[AWSアカウント](#r2ghkv)．

<a id="ezqe8s"></a>

## モノリシックカーネル

主要な機能を，[特権モード](#uk5ihn)で動作し単一の[アドレス空間](#rygcc4)を共有する1つのプログラムとして実装する[カーネル](#cktjwx)．

<a id="gi4ekj"></a>

## ユーザーアカウント制御

[Windows NT](#jzpnq4)において，管理者のグループに属するユーザーが[認証](#l2zofw)されたときに，管理者の権限を除いた[アクセストークン](#9ea3s0)と完全な[アクセストークン](#9ea3s0)を対で作成し，前者で[プロセス](#lm3iq5)を起動し，ユーザーが昇格を承認した場合にのみ後者で起動する機構．

<a id="xnr09h"></a>

## ユーザーコード

[デバイス認可エンドポイント](#v501wk)が[デバイスコード](#74muqa)と対で発行し，[主体](#pyjgmb)が[エンドユーザー検証URI](#ewuega)で入力する短い文字列．有効期限は対の[デバイスコード](#74muqa)と同じである．

<a id="1k4gbg"></a>

## ユーザーマクロ

[Zabbix](#o6myi6)において，`{$NAME}`の形式で参照する変数．グローバル，[テンプレート](#k4ea9r)，[ホスト](#y3ka2w)の単位で定義する．

<a id="0dudjl"></a>

## ユーザーメディア

ユーザーに設定された，[メディアタイプ](#egz05p)ごとの通知先．

<a id="v7n2z8"></a>

## ユーザーモード

[特権モード](#uk5ihn)より実行できる命令が制限された，[プロセッサ](#4ad6s1)の実行状態．

<a id="0lze03"></a>

## ユーティリティプロセス

[Chromium](#2aag3y)において，[サービス](#8ytqi4)を[ブラウザプロセス](#ejqo3w)から分離して実行する[プロセス](#lm3iq5)．[サービス](#8ytqi4)ごとに[サンドボックス](#2xz9pb)の制限の程度が定まる．

<a id="odhunt"></a>

## ラウンドロビン

候補を一定の順に巡回して1つずつ選ぶ方式．

<a id="3o1tma"></a>

## ラスタライズ

[ディスプレイリスト](#2zr71h)を画素の[配列](#06enpz)に変換する処理．

<a id="zugz1v"></a>

## ラベル

[オブジェクト](#8ot6zr)に付けるキーと値の組で，[ラベルセレクタ](#x5w385)による選択に用いられるもの．

<a id="x5w385"></a>

## ラベルセレクタ

[ラベル](#zugz1v)に対する条件で，それを満たす[オブジェクト](#8ot6zr)の集合を指定するもの．等価に基づく条件と集合に基づく条件がある．

<a id="g603fn"></a>

## ラージコミュニティ

広告者の[AS番号](#wvk6j6)を格納する4[オクテット](#yimp6h)のグローバル管理者の欄と，その[自律システム](#8wkkrz)が意味を定める4[オクテット](#yimp6h)のローカルデータの欄2つとからなる，12[オクテット](#yimp6h)のタグで表す[コミュニティ](#ib4lx9)の拡張．

<a id="8gfkr4"></a>

## リクエスターマネージド型ネットワークインターフェース

[AWSサービス](#40hiw9)が利用者の[サブネット](#oygsrp)に作成して管理し，その[AWSサービス](#40hiw9)の通信の口とする[Elastic Network Interface](#f5pqfi)．利用者はこれを変更も切り離しもできない．

ToDo: [123](todo.md#todo-123)

<a id="ia2trf"></a>

## リソースゲートウェイ

[サブネット](#oygsrp)に[リクエスターマネージド型ネットワークインターフェース](#8gfkr4)をもち，[AWS PrivateLink](#8irydc)または[Amazon VPC Lattice](#i24o70)を経て届いた通信を，その[リクエスターマネージド型ネットワークインターフェース](#8gfkr4)を送信元として，[IPアドレス](#3ksnfe)，[ドメイン名](#d8xx9q)，または[Amazon Resource Name](#c6b1z3)で指定された[通信先](#b2znuk)へ[中継](#zgr0mv)する[AWSリソース](#78qg7h)．[エンドポイントサービス](#7rs9yk)と異なり，[ロードバランサー](#v7r0tg)を要しない．

<a id="6lul9i"></a>

## リソースサーバー

[OAuth](#2epxko)において，[保護対象](#qfjrzs)を保持し，[アクセストークン](#8w6s21)を添えた要求を受け付ける[サーバー](#uteg7y)．

<a id="z6oh15"></a>

## リソースベースポリシー

[AWSリソース](#78qg7h)に付与される[保護対象側ポリシー](#4xq8sn)である[IAMポリシー](#let9u3)．対象の[プリンシパル](#t8ujsy)をPrincipal要素で指定する．他の[AWSアカウント](#r2ghkv)の[プリンシパル](#t8ujsy)からの要求は，その[プリンシパル](#t8ujsy)の[アイデンティティベースポリシー](#feccnu)とリソースベースポリシーの双方が許可する場合に限り許可される．

<a id="aodeq1"></a>

## リダイレクトエンドポイント

[認可クライアント](#47yah2)の[エンドポイント](#9i1lg3)．[認可エンドポイント](#17zvxp)の結果を[フロントチャネル](#xjb5je)で受け付ける．

<a id="dnckyf"></a>

## リバースプロキシ

[通信先](#b2znuk)の側に置かれ，要求元からは[通信先](#b2znuk)そのものとして見える[プロキシ](#2f8683)．

<a id="df5trk"></a>

## リフレッシュトークン

[トークンエンドポイント](#f9akzj)が[アクセストークン](#8w6s21)と共に任意で発行し，[リフレッシュトークングラント](#8m372x)で示す[トークン](#qt96h9)．

<a id="8m372x"></a>

## リフレッシュトークングラント

[リフレッシュトークン](#df5trk)を示す[認可グラント](#n1yjv8)．grant_typeはrefresh_tokenである．

<a id="25f1g6"></a>

## リライングパーティ

[OpenID Connect](#9pzzlk)において，[認可クライアント](#47yah2)を兼ねる[サービスプロバイダ](#l5pssm)．

<a id="ev8ocv"></a>

## リレーショナルデータベース

[リレーショナルモデル](#7y7vys)に従う[データベース](#vlgsmo)．

<a id="7y7vys"></a>

## リレーショナルモデル

データを，同じ属性の並びをもつタプルの集合であるリレーションの集まりとして表す[データモデル](#7qyeyy)．

<a id="xbrsqq"></a>

## リンカ

[オブジェクトファイル](#teluba)を結合し，名前の参照を定義に解決して，実行ファイルまたは[動的ライブラリ](#imdjs3)を出力するプログラム．

<a id="xy3alb"></a>

## リンク

[ネットワークインターフェース](#cufd0s)どうしが，[ルータ](#5f2okm)を介さずに直接データを交換できる[ネットワーク](#uy18d2)の範囲．

<a id="7dib68"></a>

## リンケージ

[C言語](#4pg9c8)において，異なる[有効範囲](#c7221m)または[翻訳単位](#ncbdz9)で宣言された同じ識別子が同じ[Cオブジェクト](#rq1bpp)または関数を表すかを定める，識別子の性質．外部リンケージの識別子はプログラム全体で，内部リンケージの識別子は1つの[翻訳単位](#ncbdz9)内で同じ実体を表し，リンケージのない識別子は宣言ごとに別の実体を表す．

<a id="1df8fw"></a>

## リージョン

[Amazon Web Services](#totant)の基盤を地理的に区分した[障害ドメイン](#84djzd)．複数の[アベイラビリティゾーン](#zb3vp3)からなる．

<a id="kgn0vn"></a>

## リージョンの順序

[オペレーション設定](#fm7edw)の項目．[リージョン](#1df8fw)を処理する順序を定める．[リージョン並行度](#dnamdr)が逐次のとき，[リージョン](#1df8fw)はこの順に1つずつ処理される．

<a id="tynhcw"></a>

## リージョンリソース

1つの[リージョン](#1df8fw)に属する[AWSリソース](#78qg7h)．

<a id="dnamdr"></a>

## リージョン並行度

[オペレーション設定](#fm7edw)の項目．複数の[リージョン](#1df8fw)を逐次に処理するか，並列に処理するかを定める．既定は逐次である．

<a id="v8js9k"></a>

## リーダー

複数の計算機の協調において，調整役を担う1台の計算機．リーダーをもつ[レプリケーション](#rv2ppc)では，リーダーのみが更新を受け付けて順序を定め，他の[レプリカ](#filo46)へ伝える．

<a id="brj8ci"></a>

## リーダー選出

複数の計算機から[リーダー](#v8js9k)となる1台を選び，全員にそれを知らせる手続き．

<a id="5f2okm"></a>

## ルータ

[経路表](#dw7079)に従って[IPパケット](#w9btgk)を[中継](#zgr0mv)する装置．

<a id="ktkn70"></a>

## ルーティングプロトコル

[ルータ](#5f2okm)の間で[経路](#5433mk)を交換し，それぞれの[経路表](#dw7079)を構築する[プロトコル](#bhk5im)．

<a id="4bwmon"></a>

## ルーティングポリシー

[経路](#5433mk)の受理または拒否と，[パス属性](#q885vr)の変更を定める規則．受信時に適用するインポートポリシーと，広告時に適用するエクスポートポリシーがある．

<a id="fn2c65"></a>

## ルートユーザー

[AWSアカウント](#r2ghkv)の作成時に作られ，作成に用いたメールアドレスで[認証](#l2zofw)される[プリンシパル](#t8ujsy)．既定でその[AWSアカウント](#r2ghkv)の全ての[AWSリソース](#78qg7h)に完全なアクセス権をもち，[アイデンティティベースポリシー](#feccnu)による制限を受けない．[メンバーアカウント](#yd40pa)では[サービスコントロールポリシー](#stc42v)による制限を受ける．

<a id="c23fys"></a>

## レイアウト

[スタイル計算](#35e1pq)の結果に基づき，[DOM](#mtrvw2)の各要素の位置と大きさを決める処理．

<a id="0w2o91"></a>

## レジストリ

[Windows NT](#jzpnq4)において，システムと[アプリケーション](#zxvj73)の設定を，キーと値からなる階層として保持する[データベース](#vlgsmo)．

<a id="filo46"></a>

## レプリカ

[レプリケーション](#rv2ppc)により複数の計算機または記憶装置に保持される，同じデータのそれぞれの写し．

<a id="rv2ppc"></a>

## レプリケーション

同じデータの[レプリカ](#filo46)を複数の計算機または記憶装置に保持し，更新を[レプリカ](#filo46)の間に伝える手法．更新の完了を[レプリカ](#filo46)への反映の後とするものを同期，前とするものを非同期と呼ぶ．同期のものは障害時のデータの消失を防ぎ，非同期のものは更新の遅延を抑える．

<a id="53ckw6"></a>

## レンダラープロセス

[Chromium](#2aag3y)において，[Blink](#3svuh5)と[V8](#4qyfuw)を実行して[Web文書](#qbtpp4)を処理する[プロセス](#lm3iq5)．[サンドボックス](#2xz9pb)内で動作し，他の[プロセス](#lm3iq5)を介してのみ外部の[資源](#k7gc81)にアクセスする．

<a id="8wjced"></a>

## レンダリングパイプライン

[Web文書](#qbtpp4)を画面の画素に変換する段階の列．[DOM](#mtrvw2)の構築，[スタイル計算](#35e1pq)，[レイアウト](#c23fys)，[ペイント](#kkoocc)，[ラスタライズ](#3o1tma)，[合成](#mbw8ar)の順に進む．

<a id="9rxwgw"></a>

## ログ

記録を追記のみにより発生順に並べた列．

<a id="gkygc9"></a>

## ログアイテム

[ログ](#9rxwgw)を記録したファイルを監視する[アイテム](#as86xt)．`log[]`，`logrt[]`キーは行を，`log.count[]`，`logrt.count[]`キーは行数を値とし，正規表現を指定すると一致した行のみを対象とする．[アクティブチェック](#v4p3tn)でのみ動作する．

<a id="w0f35w"></a>

## ログ先行書き込み

データへの変更を適用する前に，変更内容を[ログ](#9rxwgw)として永続的な[記憶域](#kltl5m)に書き込み，障害後に[ログ](#9rxwgw)から整合した状態を回復する手法．

<a id="7x5us3"></a>

## ロック

並行するアクセスを調停するため，対象へのアクセスに先立って獲得し，後に解放する権利．同時に1者のみが獲得できる排他的なものと，複数者が同時に獲得できる共有のものがあり，両者は同時には獲得できない．

ToDo: [104](todo.md#todo-104)

<a id="sjrv0s"></a>

## ローカルセキュリティ機関

[Windows NT](#jzpnq4)において，ローカルのセキュリティポリシーと[認証](#l2zofw)を管理し，[認証](#l2zofw)されたユーザーの[アクセストークン](#9ea3s0)を作成する[ユーザーモード](#v7n2z8)の[プロセス](#lm3iq5)．実行ファイルはlsass.exeである．

<a id="v7r0tg"></a>

## ロードバランサー

受信した通信を複数の[通信先](#b2znuk)に分散して[中継](#zgr0mv)する機構．

<a id="xf97bc"></a>

## ワーキングセット

[Windows NT](#jzpnq4)において，[プロセス](#lm3iq5)の[アドレス空間](#rygcc4)の[ページ](#05by8w)のうち，[物理メモリ](#svua87)に存在し参照可能なものの集合．

<a id="qg1bbv"></a>

## ワークロードリソース

[Pod](#k4ef3z)のテンプレートを保持し，それに従って[Pod](#k4ef3z)を，直接または他のワークロードリソースを介して作成，管理する[オブジェクト](#8ot6zr)．作成した[Pod](#k4ef3z)は[ラベルセレクタ](#x5w385)と[コントローラ参照](#xy6h7u)で識別される．

<a id="qp3v5d"></a>

## 一貫性

[トランザクション](#v5hhix)が[整合性制約](#u60upi)を満たす状態から満たす状態へ移すという性質．

<a id="0brxik"></a>

## 並行制御

並行する[トランザクション](#v5hhix)の実行において，[分離性](#79gxog)を保つ機構．

<a id="zgr0mv"></a>

## 中継

受信した通信を[通信先](#b2znuk)へ向けて送り出すこと．

<a id="7ckf0e"></a>

## 主キー

[Amazon DynamoDB](#knkcrh)のテーブルの[主キー](#vgslfx)．パーティションキーのみ，またはパーティションキーとソートキーの組からなる．パーティションキーの値の[ハッシュ関数](#fnegr1)の値により，項目を格納する[シャーディング](#1upnid)の分割単位が定まる．

<a id="vgslfx"></a>

## 主キー

[データベース](#vlgsmo)の表において，各行を一意に識別するために選ばれた属性の組．値は空をとらない．

<a id="pyjgmb"></a>

## 主体

操作を要求し，[認証](#l2zofw)と[認可](#8esn53)の対象となる実体．

<a id="r95ien"></a>

## 主体側ポリシー

[主体](#pyjgmb)に付随し，その[主体](#pyjgmb)に許可または拒否する操作を[保護対象](#qfjrzs)ごとに定める[ポリシー](#d3j3nj)．

<a id="3s209z"></a>

## 二分ヒープ

各頂点の優先度がその子の優先度以上である，葉の層を除く全ての層が埋まり最下層が左詰めの[二分木](#sq01cf)を，[配列](#06enpz)に層の順で格納した[データ構造](#y9ua1k)．要素数nに対して，挿入と取出しの[計算量](#tl94hx)がO(log n)の[優先度付きキュー](#l4awe5)を実現する．

<a id="n28uic"></a>

## 二分探索木

各頂点のキーが，左の子を根とする部分のキーより大きく，右の子を根とする部分のキーより小さい[二分木](#sq01cf)である[探索木](#jp0l0f)．

<a id="sq01cf"></a>

## 二分木

各頂点が高々2つの子をもち，それらを左の子と右の子として区別する[木](#dj2zcx)．

<a id="gczcfy"></a>

## 二相ロック

各[トランザクション](#v5hhix)が[ロック](#7x5us3)を獲得する段階と解放する段階を分け，解放を始めたのちに獲得しない[並行制御](#0brxik)の方式．実行の[直列化可能性](#p0wpt2)を保証する．[デッドロック](#rqm5zv)が生じうる．

<a id="k28z9a"></a>

## 代替データストリーム

[NTFS](#42ymz9)において，ファイルが既定の無名のデータの列に加えてもつ，名前の付いたデータの列．

<a id="h318rh"></a>

## 仮想アドレス記述子

[Windows NT](#jzpnq4)における[アドレス区間記述子](#k4ztwu)で，予約された区間を表す．対応付け先は[セクションオブジェクト](#frjmk2)と[プロセス](#lm3iq5)固有のメモリのいずれかである．区間内のアクセス権は[ページ](#05by8w)ごとに異なりうる．[EPROCESS](#ops4d2)はこれらを区間の位置で順序付けた[二分探索木](#n28uic)として保持する．

<a id="cmoqun"></a>

## 仮想アプライアンス

[ネットワーク](#uy18d2)の機能を提供するソフトウェアを動かす[仮想マシン](#uwly1k)．

<a id="cos7bu"></a>

## 仮想ネットワーク

物理的な[ネットワーク](#uy18d2)の上に論理的に構成され，同じ物理的な[ネットワーク](#uy18d2)上の他の仮想ネットワークから隔離された[ネットワーク](#uy18d2)．

<a id="gid8it"></a>

## 仮想ファイルシステム

[カーネル](#cktjwx)において，個々の[ファイルシステム](#pp17bd)の実装の差異を隠し，ファイル操作の[システムコール](#saksfm)に統一的なインターフェースを提供する層．実装ごとの処理は[操作表](#xxcrwp)を通じて呼び出す．

<a id="uwly1k"></a>

## 仮想マシン

[ハイパーバイザ](#dt1rv7)が提供する，物理計算機を模した実行環境．互いに独立して[オペレーティングシステム](#c8v8vw)を実行する．

<a id="ysrn1f"></a>

## 仮想記憶

[アドレス空間](#rygcc4)の[ページ](#05by8w)を[ページフレーム](#4qztd7)に対応付ける機構．

<a id="zyyhvv"></a>

## 例外

[割り込み](#owu45r)と異なり，実行中の命令に起因して同期的に発生し，[プロセッサ](#4ad6s1)に対応する処理を実行させる事象．

<a id="qh1hz5"></a>

## 依存アイテム

マスタアイテムと呼ぶ他の[アイテム](#as86xt)の値から，[保存前処理](#zgnkho)で値を派生させる[アイテムタイプ](#ugi5pv)．

<a id="zgnkho"></a>

## 保存前処理

[アイテム](#as86xt)の値を[ヒストリ](#s04nt7)に格納する前に適用する，変換手順の列．

<a id="qfjrzs"></a>

## 保護対象

[認可](#8esn53)により操作が制御される対象．

<a id="4xq8sn"></a>

## 保護対象側ポリシー

[保護対象](#qfjrzs)に付随し，それに対する操作を[主体](#pyjgmb)ごとに許可または拒否する[ポリシー](#d3j3nj)．

<a id="l7b2yn"></a>

## 信頼チェーン

予め信頼する[公開鍵](#7xb1uk)を起点とし，各[公開鍵](#7xb1uk)をその上位の[公開鍵](#7xb1uk)で[電子署名](#wr3566)を検証して順に信頼し，対象の[公開鍵](#7xb1uk)の信頼に至る手続き．

<a id="x633ta"></a>

## 信頼ポリシー

[IAMロール](#k1a9js)に付与され，そのロールの[IAMロール引受け](#0d235w)を許す[プリンシパル](#t8ujsy)と[アイデンティティプロバイダ](#3z77qd)を定める[リソースベースポリシー](#z6oh15)．

<a id="w6gowu"></a>

## 偽装

[Windows NT](#jzpnq4)において，[スレッド](#ou7dup)が所属する[プロセス](#lm3iq5)とは異なる[アクセストークン](#9ea3s0)で動作する[権限引受け](#5bn6hq)．

<a id="twldru"></a>

## 償却計算量

操作の列全体の[計算量](#tl94hx)を操作の数で割った，1操作あたりの[計算量](#tl94hx)．

<a id="l4awe5"></a>

## 優先度付きキュー

各要素が優先度をもち，優先度が最大または最小の要素を取り出す[抽象データ型](#wlwn4m)．

<a id="xwqhlo"></a>

## 先頭一致評価

[ポリシー](#d3j3nj)の規則を定められた順に照合し，最初に一致した規則の許可または拒否を適用する評価の方式．

<a id="vs10rb"></a>

## 公開接尾辞

その下に誰もが[ドメイン名](#d8xx9q)を登録できる[ドメイン名](#d8xx9q)．

<a id="7xb1uk"></a>

## 公開鍵

[公開鍵暗号](#g63w9e)において，[秘密鍵](#dak54j)と対をなして公開される[鍵](#atfb8r)．公開鍵から対の[秘密鍵](#dak54j)を求めることは計算上困難である．

<a id="qo4wn7"></a>

## 公開鍵基盤

[証明書](#30mc00)の階層により，[公開鍵](#7xb1uk)とその保持者の対応を保証する仕組み．

<a id="g63w9e"></a>

## 公開鍵暗号

[秘密鍵](#dak54j)と，それと対をなす[公開鍵](#7xb1uk)とを用いる[暗号](#o5aaif)．

<a id="76g0nk"></a>

## 共有メモリ

複数の[プロセス](#lm3iq5)の[アドレス空間](#rygcc4)に対応付けられた，同一の[物理メモリ](#svua87)の区域．[プロセス間通信](#vjg5ws)の手段となる．

<a id="ms7tuh"></a>

## 共用体

[C言語](#4pg9c8)において，それぞれ[データ型](#w7t735)をもつメンバーが記憶域を重ねて共有する[データ型](#w7t735)．全てのメンバーは共用体の先頭に置かれ，共用体の大きさは最大のメンバーを格納できる大きさ以上である．

<a id="sie28z"></a>

## 共通鍵

当事者の間で共有され，当事者以外に秘匿される[鍵](#atfb8r)．

<a id="6uco4b"></a>

## 共通鍵暗号

当事者が同じ[共通鍵](#sie28z)を用いる[暗号](#o5aaif)．

<a id="6cc980"></a>

## 分散システム

[ネットワーク](#uy18d2)で接続された複数の計算機が，メッセージを交換して協調し，1つのシステムとして動作するもの．

<a id="wo8tr8"></a>

## 分離レベル

並行する[トランザクション](#v5hhix)の間で許す異常の範囲を定める段階．[SQL](#v61vr0)の標準は，[ダーティリード](#ccg2j3)，[ノンリピータブルリード](#atp440)，[ファントムリード](#wgkq3s)の許容の有無により，READ UNCOMMITTED，READ COMMITTED，REPEATABLE READ，SERIALIZABLEの4段階を定める．SERIALIZABLEは[直列化可能性](#p0wpt2)を要求する．

<a id="79gxog"></a>

## 分離性

並行する[トランザクション](#v5hhix)が互いの途中の状態を観測しないという性質．その程度は[分離レベル](#wo8tr8)により緩められる．

<a id="pjlcj6"></a>

## 制限付きトークン

[Windows NT](#jzpnq4)において，既存の[アクセストークン](#9ea3s0)から，グループの無効化，権利の削除，制限する[セキュリティ識別子](#kzruy4)の追加により権限を減らして作る[アクセストークン](#9ea3s0)．

<a id="owu45r"></a>

## 割り込み

命令の実行とは非同期に発生し，[プロセッサ](#4ad6s1)に実行中の命令列を中断させて対応する処理を実行させる事象．

<a id="aiwf2j"></a>

## 割り込み要求レベル

[Windows NT](#jzpnq4)において，[プロセッサ](#4ad6s1)ごとに設定される優先度．現在の値以下の[割り込み](#owu45r)は遮断される．0をPASSIVE_LEVEL，1をAPC_LEVEL，2をDISPATCH_LEVELと呼び，3以上の値はハードウェアの[割り込み](#owu45r)に用いられる．APC_LEVEL以上では[非同期プロシージャ呼び出し](#zlguzf)の実行が遮断される．DISPATCH_LEVEL以上では[スケジューラ](#wpudzb)による[スレッド](#ou7dup)の切り替えが起こらず，[物理メモリ](#svua87)に存在しない[ページ](#05by8w)を参照できない．

<a id="imdjs3"></a>

## 動的ライブラリ

実行時に[プロセス](#lm3iq5)の[アドレス空間](#rygcc4)に読み込まれ，[サブルーチン](#y825lm)とデータを提供するファイル．

<a id="sxisir"></a>

## 動的リンカ

実行時に[動的ライブラリ](#imdjs3)を[プロセス](#lm3iq5)の[アドレス空間](#rygcc4)に読み込み，名前の参照を定義に解決する機構．

<a id="zdjtf4"></a>

## 動的型付け

変数でなく値が[データ型](#w7t735)をもち，操作との整合を実行時に検査する方式．

<a id="uo5htx"></a>

## 動的配列

容量を超える追加のとき，容量を定数倍に拡大した領域へ要素を移す[配列](#06enpz)．末尾への追加の[償却計算量](#twldru)は定数である．

<a id="7anb5g"></a>

## 原子性

[トランザクション](#v5hhix)の全ての操作が実行されるか，1つも実行されないという性質．

<a id="eo61p5"></a>

## 合意アルゴリズム

一部が故障しうる[分散システム](#6cc980)の計算機の間で同じ値の列に合意し，[レプリケーション](#rv2ppc)された状態を一致させるアルゴリズム．決定には[クォーラム](#225nin)の承認を要し，2f+1台の構成はf台の停止に耐える．

<a id="mbw8ar"></a>

## 合成

別々に[ラスタライズ](#3o1tma)した複数の[合成レイヤー](#duxj3i)を，位置，変形，透明度に従って重ね合わせ，1枚の画像を作る処理．

<a id="bi2j70"></a>

## 合成スレッド

[レンダラープロセス](#53ckw6)において，[メインスレッド](#663plp)から受け取った[合成レイヤー](#duxj3i)と[ディスプレイリスト](#2zr71h)を基に[ラスタライズ](#3o1tma)を手配し，スクロールと一部のアニメーションを[メインスレッド](#663plp)を待たずに反映した[CompositorFrame](#gyxatn)を[viz](#87mh85)へ送る[スレッド](#ou7dup)．

<a id="duxj3i"></a>

## 合成レイヤー

[合成](#mbw8ar)の単位として別々に[ラスタライズ](#3o1tma)される，[Web文書](#qbtpp4)の描画内容の部分．

<a id="q18xj8"></a>

## 同一オリジンポリシー

[Webブラウザ](#gcly3z)が，[Web文書](#qbtpp4)中の[JavaScript](#y8ql3q)に，異なる[オリジン](#3f4vd8)の[Web文書](#qbtpp4)と応答の内容の読み取りを既定で許さない規則．

<a id="lnizbx"></a>

## 名前キャッシュ

[仮想ファイルシステム](#gid8it)において，[ディレクトリ](#j1d7gn)と名前の組からその名前のファイルの[VFSノード](#pg1lac)を得る検索の結果を保持し，[パス名](#ymj65u)の解決に用いる[キャッシュ](#kj4w0z)．名前が存在しないという結果は，[VFSノード](#pg1lac)を参照しない要素で表す．

<a id="6bdul4"></a>

## 名前空間

[クラスタ](#dx7pxd)内の[オブジェクト](#8ot6zr)の名前を種類ごとに分ける[名前空間](#m7lbe4)．これに属さない種類の[オブジェクト](#8ot6zr)の名前は，[クラスタ](#dx7pxd)の中で種類ごとに一意である．[Role](#3kkitq)と[ResourceQuota](#4192cj)の適用単位となる．

<a id="m7lbe4"></a>

## 名前空間

その中で各名前が高々1つの対象を指す，名前の範囲．階層的なものでは，それ自体が上位のものの対象となって[木](#dj2zcx)をなし，対象は根からの名前の列で指される．

<a id="3or1pp"></a>

## 名前解決

[名前空間](#m7lbe4)における名前から，それが指す対象を得る手続き．

<a id="tpx3c2"></a>

## 名前解決

[DNS](#v0yvpo)における[名前解決](#3or1pp)．[ドメイン名](#d8xx9q)と型を与えて，対応する[資源レコード](#syx2b4)を得る．

<a id="utnq9w"></a>

## 周波数帯

[電波](#diiab2)の周波数の連続した範囲．範囲ごとに，利用の用途と免許の要否が法令で定められる．

<a id="0qdj5m"></a>

## 埋め込み連結リスト

要素となる[構造体](#0fq59c)に，他の要素への参照をもつ[構造体](#0fq59c)をメンバーとして埋め込んでつくる[連結リスト](#zhodwh)．要素のアドレスは，埋め込んだメンバーのアドレスから，要素内でのそのメンバーの位置を引いて得る．1つの要素は，埋め込むメンバーを複数もつことで，同時に複数のリストに属する．

<a id="00im0x"></a>

## 基地局

[セルラー通信](#fibo1z)において，[セル](#d9lgtj)内の[端末](#zw6tbw)と[電波](#diiab2)で通信し，[端末](#zw6tbw)を[コアネットワーク](#7ll5nd)に接続する固定の設備．

<a id="g8gyb5"></a>

## 外部キー

表の属性の組で，他の表の[主キー](#vgslfx)を参照するもの．値が参照先に存在する[主キー](#vgslfx)の値か空であるという[整合性制約](#u60upi)を参照整合性と呼ぶ．

<a id="kyjjof"></a>

## 多版型同時実行制御

データの更新のたびに新しい版を作り，各[トランザクション](#v5hhix)に，定められた時点の[スナップショット](#ahlapd)に属する版を読ませる[並行制御](#0brxik)の方式．読み取りが書き込みを待たせない．

<a id="q89hwf"></a>

## 大規模言語モデル

大量のテキストで訓練され，与えられた文章に続く文章を生成するモデル．

ToDo: [150](todo.md#todo-150)，[116](todo.md#todo-116)

<a id="qiqjj5"></a>

## 委任管理者

[管理アカウント](#svvkiy)が，特定の[AWSサービス](#40hiw9)について[組織](#sm4tb3)の管理を委ねるために登録した[メンバーアカウント](#yd40pa)．

<a id="rkn7hg"></a>

## 実行ロール

[Lambda関数](#v7xjp0)に関連付けられ，その実行時に[IAMロール引受け](#0d235w)の対象となる[IAMロール](#k1a9js)．

<a id="duers5"></a>

## 平衡探索木

挿入と削除のたびに構造を調整し，高さを頂点数の対数に比例する値以下に保つ[探索木](#jp0l0f)．

<a id="lhxknx"></a>

## 待ち行列

処理を待つ要素を保持し，処理する側が要素を取り出す置き場．取り出す順は追加の順とは限らず，追加の順を保つものは[キュー](#mqlfip)をなす．

<a id="zktekl"></a>

## 所有者参照

[オブジェクト](#8ot6zr)の[メタデータ](#f7of70)に含まれ，所有者である他の[オブジェクト](#8ot6zr)を種類，名前，[UID](#w2fhil)で指す参照．[名前空間](#6bdul4)に属する[オブジェクト](#8ot6zr)の所有者は，同じ[名前空間](#6bdul4)に属するか，[名前空間](#6bdul4)に属さない．所有者が削除されたとき，[propagationPolicy](#ood9pc)がOrphanでなければ，これをもつ[オブジェクト](#8ot6zr)も削除される．

<a id="wxs2uf"></a>

## 投機的実行

[プロセッサ](#4ad6s1)が，実行すべきか確定していない命令を予測に基づいて先に実行し，予測が外れたときにその結果を捨てること．

<a id="wlwn4m"></a>

## 抽象データ型

操作とその振る舞いのみで定められ，実現する[データ構造](#y9ua1k)を問わない[データ型](#w7t735)．

<a id="t93sgu"></a>

## 拒否優先評価

[ポリシー](#d3j3nj)の規則のうち拒否の規則が1つでも一致すれば，一致する許可の規則によらず拒否する評価の方式．

<a id="534jnn"></a>

## 拡張コミュニティ

型の欄をもつ8[オクテット](#yimp6h)のタグで表す[コミュニティ](#ib4lx9)の拡張．

<a id="iwj5fh"></a>

## 拡張プログラム

既存のプログラムを作り直さずに，そのプログラムに後から機能を追加するプログラム．

<a id="1erfeu"></a>

## 拡張機能

[アプリケーション](#zxvj73)に組み込む[拡張プログラム](#iwj5fh)．組み込み先が提供する[API](#9e509k)を通じて動作する．

<a id="jp0l0f"></a>

## 探索木

キーの順序に従って頂点にキーを配置し，根から比較により辿る頂点を選んでキーを探す[木](#dj2zcx)．検索，挿入，削除は高さに比例する時間を要し，[連想配列](#lkmji4)と，キーの順序に従う走査を実現する．

<a id="st4cz5"></a>

## 接続

2つの[端点](#b084uv)がデータの交換に先立って確立し，交換の間それぞれが状態を保持する関係．

<a id="d1bl1o"></a>

## 接続追跡

通過する[IPパケット](#w9btgk)を，送信元と宛先の[IPアドレス](#3ksnfe)，[ポート番号](#avetpx)，[プロトコル](#bhk5im)の組ごとに束ね，組ごとの通信の状態を保持する機構．[接続](#st4cz5)を確立しない[プロトコル](#bhk5im)の通信も束ねる．

<a id="xxcrwp"></a>

## 操作表

[サブルーチン](#y825lm)への参照を並べた[データ構造](#y9ua1k)．同じ役割を異なる実装で果たす対象がそれぞれの実装の操作表を参照し，呼び出し側は実装を区別せずに操作表を通じて処理を呼び出す．

<a id="iq5tpn"></a>

## 故障検出

対象が正常に動作しているかを，対象から届くメッセージの有無と内容により判定すること．

<a id="4e4la0"></a>

## 数値型

[アイテム](#as86xt)の値の型のうち，浮動小数または符号なし整数であるもの．

<a id="79uj26"></a>

## 整合性レベル

[Windows NT](#jzpnq4)において，[アクセストークン](#9ea3s0)と[保護対象](#qfjrzs)に付与される順序付きの信頼度．既定では，[アクセストークン](#9ea3s0)のものより高い値をもつ対象への書き込みが拒否される．

<a id="u60upi"></a>

## 整合性制約

[データベース](#vlgsmo)の状態が常に満たすべきとして宣言される条件．

<a id="kfuctl"></a>

## 既定拒否

[認可](#8esn53)において，明示的に許可されていない要求を拒否する方式．

<a id="o5aaif"></a>

## 暗号

[鍵](#atfb8r)を用いる演算により，[鍵](#atfb8r)をもたない者に対して，データの秘匿，改変の検出，作成者の確認を実現する方式．

<a id="e382sn"></a>

## 暗号化

復号に用いる[鍵](#atfb8r)を知る者のみが元に戻せるようにデータを変換すること．逆の変換を復号と呼ぶ．

<a id="lk5maz"></a>

## 最大同時アカウント数

[オペレーション設定](#fm7edw)の項目．1つの[リージョン](#1df8fw)で同時に処理する[ターゲットアカウント](#gjqg2o)の最大数を，数または割合で定める．

<a id="avov3h"></a>

## 最小接続

確立中の[接続](#st4cz5)が最も少ない[通信先](#b2znuk)を選ぶ[ロードバランサー](#v7r0tg)の方式．

<a id="raisax"></a>

## 最良経路選択

同じ[IPプレフィックス](#6rwn5e)への複数の[経路](#5433mk)から1つを選ぶ[BGP](#0ey58g)の手順．[NEXT_HOP](#2js4sd)に到達できないものを除き，次の順に比較して優劣が決まった時点で選ぶ．[LOCAL_PREF](#dalaa4)が大きい，[AS_PATH](#my3zbg)が短い，[ORIGIN](#zfmc8n)の値が小さい，[MED](#ge0o29)が小さい，[eBGP](#vz4jtn)で学習した，[NEXT_HOP](#2js4sd)までの[IGP](#sekyc5)のコストが小さい，[BGP識別子](#p2n7t4)が小さい，[CLUSTER_LIST](#1r0j49)が短い，[ピア](#7wmnel)のアドレスが小さい．[AS_PATH](#my3zbg)の長さは[AS_SET](#vqwgle)の区間を1と数える．[経路リフレクタ](#iz5p1h)が再広告したものでは，[BGP識別子](#p2n7t4)の代わりに[ORIGINATOR_ID](#rrbnra)を比較する．

<a id="0daj2w"></a>

## 最長一致

与えられた[IPアドレス](#3ksnfe)を含む[IPプレフィックス](#6rwn5e)のうち，プレフィックス長が最大のものを選ぶ規則．

<a id="c7221m"></a>

## 有効範囲

[C言語](#4pg9c8)において，識別子がその宣言の表す実体を表す，プログラムのテキストの範囲．ファイル，ブロック，関数，関数原型の4種がある．

<a id="dj2zcx"></a>

## 木

閉路をもたない連結な無向の[グラフ](#ypg0zz)．1つの頂点を根と定め，辺で隣接する2頂点のうち根に近い方を親，遠い方を子と呼ぶ．子のない頂点を葉，根から頂点までの辺の数を深さ，深さの最大値を高さと呼ぶ．

<a id="1d4gs1"></a>

## 未定義動作

[プログラミング言語](#nw9j2i)の規格が，結果に何の要件も課さないプログラムの振る舞い．[コンパイラ](#a2nw9z)はこれが生じない前提で翻訳してよい．

<a id="tva20i"></a>

## 構成マネージャ

[エグゼクティブ](#s3eb1d)において，[レジストリ](#0w2o91)を実装する構成要素．

<a id="0fq59c"></a>

## 構造体

[C言語](#4pg9c8)において，それぞれ[データ型](#w7t735)をもつメンバーの，宣言の順の並びからなる[データ型](#w7t735)．[ビットフィールド](#ouc72p)を除くメンバーは宣言の順にアドレスが増える位置に置かれ，最初のメンバーは構造体の先頭に置かれる．メンバーの間と末尾に詰め物を置くことを規格は許す．

<a id="9es8da"></a>

## 権威DNSサーバー

[DNSゾーン](#2eh0s0)の[資源レコード](#syx2b4)を保持し，その[DNSゾーン](#2eh0s0)についての問合せに権威ある応答を返す[サーバー](#uteg7y)．1つの[DNSゾーン](#2eh0s0)を複数の権威DNSサーバーが保持し，[ゾーン転送](#zil7hp)で内容を揃える．

<a id="lti67d"></a>

## 権限代行

処理が，別の処理の要求を受け，その可否を判定した上で，自身の[セキュリティ文脈](#lxnyp5)の下で要求された操作を行うこと．[権限引受け](#5bn6hq)と異なり，要求した処理の[セキュリティ文脈](#lxnyp5)は変わらない．

<a id="5bn6hq"></a>

## 権限引受け

処理が，それを開始した[主体](#pyjgmb)の[セキュリティ文脈](#lxnyp5)と異なる[セキュリティ文脈](#lxnyp5)を得て，その下で動作すること．

<a id="rzi1ck"></a>

## 権限昇格

[主体](#pyjgmb)が，本来許されない操作を行える[セキュリティ文脈](#lxnyp5)を得ること．

ToDo: [125](todo.md#todo-125)

<a id="ky7oww"></a>

## 機械語

[プロセッサ](#4ad6s1)が直接実行する命令の符号の体系．

<a id="tk8q5y"></a>

## 正規化

[リレーショナルモデル](#7y7vys)のリレーションを，ある属性の組の値が他の属性の組の値を一意に定める従属性に基づいて分解し，冗長性と更新時の不整合を除く手続き．分解の到達した段階を正規形と呼ぶ．

<a id="ihllp7"></a>

## 永続性

コミットした[トランザクション](#v5hhix)の結果が障害後も失われないという性質．

<a id="jcg0dk"></a>

## 深刻度

[Zabbix](#o6myi6)において，[トリガー](#3gz3w5)と[イベント](#przzj5)がもつ重大さの段階．低い順に未分類，情報，警告，軽度の障害，重度の障害，致命的な障害の6段階である．

<a id="1zfkze"></a>

## 無線通信

[電波](#diiab2)を媒体としてデータを伝送する通信．

<a id="six0ds"></a>

## 物理エクステント

[物理ボリューム](#uj3w47)を等分した固定長の区間で，[LVM](#9tfla3)が[記憶域](#kltl5m)を割り当てる単位．大きさは[ボリュームグループ](#um9c12)ごとに定まり，既定は4 MiBである．[論理ボリューム](#es46jv)上の対応する区間を論理エクステントと呼ぶ．

<a id="uj3w47"></a>

## 物理ボリューム

[LVM](#9tfla3)が初期化して管理下に置いた[ブロックデバイス](#1frbzb)．[物理エクステント](#six0ds)に分割される．

<a id="svua87"></a>

## 物理メモリ

[プロセッサ](#4ad6s1)が命令とデータを直接読み書きする記憶装置．

<a id="uk5ihn"></a>

## 特権モード

[ユーザーモード](#v7n2z8)では禁止される命令の実行が許される，[プロセッサ](#4ad6s1)の実行状態．

ToDo: [139](todo.md#todo-139)

<a id="u90lkn"></a>

## 特権分離

プログラムを権限の異なる複数の[プロセス](#lm3iq5)に分け，信頼できない入力を処理する[プロセス](#lm3iq5)の権限を最小にする設計．

<a id="ij6arz"></a>

## 登録可能ドメイン

[ドメイン名](#d8xx9q)の末尾に一致する最長の[公開接尾辞](#vs10rb)に，その直前の[DNSラベル](#7siuzh)を1つ加えた[ドメイン名](#d8xx9q)．

<a id="7slqlb"></a>

## 監査

対象が基準に適合しているかを，証拠に基づいて評価すること．

<a id="90keyj"></a>

## 監視主体

[Zabbix](#o6myi6)において，[ホスト](#y3ka2w)の[アイテム](#as86xt)の値を収集する[プロセス](#lm3iq5)．

<a id="pvfe2i"></a>

## 監視規則

監視対象の値または状態を条件で評価し，監視状態を定める規則．

<a id="p0wpt2"></a>

## 直列化可能性

並行に実行された[トランザクション](#v5hhix)の結果が，それらをある順序で1つずつ実行した結果と等しいという条件．

<a id="8zsqwg"></a>

## 確認応答

[障害](#ilz3yu)をユーザーが確認したことを記録する操作．

<a id="dak54j"></a>

## 秘密鍵

[公開鍵暗号](#g63w9e)において，保持者が秘匿する[鍵](#atfb8r)．

<a id="em1w73"></a>

## 移動体通信事業者

[セルラー通信](#fibo1z)の[コアネットワーク](#7ll5nd)と[基地局](#00im0x)を運用し，加入者に通信を提供する事業者．

<a id="zw6tbw"></a>

## 端末

通信を[中継](#zgr0mv)せず，利用者が通信の[端点](#b084uv)として用いる機器．

<a id="b084uv"></a>

## 端点

通信の両端にあって，データを送り出し，受け取るもの．

<a id="svvkiy"></a>

## 管理アカウント

[組織](#sm4tb3)を作成し，所有する[AWSアカウント](#r2ghkv)．[組織](#sm4tb3)ごとに1つであり，[サービスコントロールポリシー](#stc42v)は適用されない．

<a id="kh4nz4"></a>

## 管理者アカウント

[スタックセット](#9hhp5i)を作成する[AWSアカウント](#r2ghkv)．

<a id="l0kw7s"></a>

## 範囲外アクセス

[データオブジェクト](#wvtf4u)への参照を通じて，その[データオブジェクト](#wvtf4u)の範囲の外のメモリにアクセスする誤り．

<a id="sm4tb3"></a>

## 組織

[組織ルート](#9kuc7i)を根とし，[組織単位](#1wx4ge)と[組織アカウント](#4q8oz8)を根以外の頂点とする[木](#dj2zcx)である[組織リソース](#b2lxzl)．

<a id="4q8oz8"></a>

## 組織アカウント

[組織](#sm4tb3)の葉であり，1つの[AWSアカウント](#r2ghkv)を参照する[組織リソース](#b2lxzl)．

<a id="ljfr92"></a>

## 組織インスタンス

[組織](#sm4tb3)全体を管理対象とし，[管理アカウント](#svvkiy)が所有する[Identity Centerインスタンス](#5mx2oh)．[組織](#sm4tb3)ごとに最大1つ．プライマリリージョン以外の[リージョン](#1df8fw)に複製できる．

<a id="b2lxzl"></a>

## 組織リソース

[AWS Organizations](#yj1k74)の[AWSリソース](#78qg7h)．[管理アカウント](#svvkiy)が所有する[グローバルリソース](#bdchaf)である．

<a id="9kuc7i"></a>

## 組織ルート

[組織](#sm4tb3)の根である[組織リソース](#b2lxzl)．

<a id="1wx4ge"></a>

## 組織単位

[組織](#sm4tb3)の根以外の頂点であり，子をもちうる[組織リソース](#b2lxzl)．

<a id="5433mk"></a>

## 経路

宛先の[IPプレフィックス](#6rwn5e)と，そこへ向かう[IPパケット](#w9btgk)を渡す次の転送先であるネクストホップの組．

<a id="396pcu"></a>

## 経路サーバー

[IXP](#nwgavk)で，参加者から受信した[経路](#5433mk)を他の参加者へ広告する[BGPスピーカー](#v9rnch)．自身の[AS番号](#wvk6j6)を[AS_PATH](#my3zbg)に追加せず，[NEXT_HOP](#2js4sd)を変更しない．

<a id="4z8ok7"></a>

## 経路ターゲット

[経路](#5433mk)を取り込む[VRF](#3a4xlv)を定める[拡張コミュニティ](#534jnn)．[VRF](#3a4xlv)は，エクスポート用の経路ターゲットを付して[経路](#5433mk)を広告し，インポート用の経路ターゲットのいずれかをもつ[経路](#5433mk)を取り込む．

<a id="y4t1ef"></a>

## 経路ハイジャック

正当な保持者でない[自律システム](#8wkkrz)が，他者の[IPプレフィックス](#6rwn5e)またはそれより長い[IPプレフィックス](#6rwn5e)を発生源として広告し，トラフィックを引き寄せること．より長いものの広告は[最長一致](#0daj2w)により優先される．

<a id="isy0yn"></a>

## 経路フラップダンピング

広告と撤回を繰り返す[経路](#5433mk)にペナルティを累積し，抑制閾値を超えたものを使用しない手法．ペナルティは時間とともに指数的に減衰し，再使用閾値を下回ると再び用いる．

<a id="iz5p1h"></a>

## 経路リフレクタ

[iBGP](#f6yd97)の[ピア](#7wmnel)のうち反射の対象として設定したものから学習した[経路](#5433mk)を全ての[iBGP](#f6yd97)の[ピア](#7wmnel)へ，それ以外の[iBGP](#f6yd97)の[ピア](#7wmnel)から学習した[経路](#5433mk)を反射の対象へ再広告する[BGPスピーカー](#v9rnch)．再広告する[経路](#5433mk)に[ORIGINATOR_ID](#rrbnra)と[CLUSTER_LIST](#1r0j49)を付して広告の循環を防ぐ．

<a id="6kzc5c"></a>

## 経路リーク

[自律システム](#8wkkrz)が受信した[経路](#5433mk)を，[トランジット](#mcggb8)や[AS間ピアリング](#z1q1fs)の関係が想定する範囲を超えて他の[自律システム](#8wkkrz)へ広告すること．

<a id="of0ehz"></a>

## 経路反射クラスタ

1つ以上の[経路リフレクタ](#iz5p1h)と，それらが反射の対象とする[iBGP](#f6yd97)の[ピア](#7wmnel)の集まり．[クラスタID](#8rb2lo)で識別される．

<a id="476yxv"></a>

## 経路発生源検証

[ROA](#xmhp27)に基づき[経路](#5433mk)を分類する手順．その[IPプレフィックス](#6rwn5e)を包含する[ROA](#xmhp27)がなければNotFound，包含しプレフィックス長が最大プレフィックス長以下である[ROA](#xmhp27)のいずれかの[AS番号](#wvk6j6)が[AS_PATH](#my3zbg)の示す発生源に一致すればValid，それ以外はInvalidとする．

<a id="dw7079"></a>

## 経路表

[経路](#5433mk)の集合．[IPパケット](#w9btgk)の宛先の[IPアドレス](#3ksnfe)に[最長一致](#0daj2w)する要素を転送に用いる．

<a id="dlraom"></a>

## 経路識別子

[IPプレフィックス](#6rwn5e)の前に付す8[オクテット](#yimp6h)の値で，異なる[VRF](#3a4xlv)の重複する[IPプレフィックス](#6rwn5e)を区別する．これを付した[IPプレフィックス](#6rwn5e)は，[マルチプロトコル拡張](#hz8j1v)で専用の[アドレスファミリー](#zeoy6t)として交換される．

<a id="ofoz7i"></a>

## 経路集約

複数の[IPプレフィックス](#6rwn5e)を，それらを包含する1つの短い[IPプレフィックス](#6rwn5e)として広告すること．集約により[AS_PATH](#my3zbg)の情報が失われる場合はATOMIC_AGGREGATE属性を付す．集約した[BGPスピーカー](#v9rnch)は，AGGREGATOR属性で自身の[AS番号](#wvk6j6)とアドレスを示す．

<a id="wr7tbp"></a>

## 統合開発環境

[テキストエディタ](#nud9su)による編集，[ビルドシステム](#ci6jok)による変換，[デバッガ](#49baql)による欠陥の特定を，1つの[アプリケーション](#zxvj73)で行うソフトウェア開発の環境．

<a id="q83z5h"></a>

## 線形化可能性

並行に実行される各操作が，その開始から完了までの間のある一時点で瞬時に実行されたかのように見えるという，操作の結果に対する条件．

<a id="gv4jmw"></a>

## 置換更新

共有される[データ構造](#y9ua1k)を書き換えず，変更を加えた写しを作って参照を置き換えることで更新する方式．置換の前に参照を得た処理は，変更前の内容を一貫して読む．

ToDo: [144](todo.md#todo-144)

<a id="ncbdz9"></a>

## 翻訳単位

1つのソースファイルを[プリプロセッサ](#rewxde)で処理した結果．[コンパイラ](#a2nw9z)はこれを単位に翻訳する．

<a id="grye5m"></a>

## 自動登録

[Zabbix](#o6myi6)において，[アクティブチェック](#v4p3tn)を要求した[Zabbix Agent](#5l6oih)の情報に基づき，[アクション](#pfbsnf)で[ホスト](#y3ka2w)を登録する機能．

<a id="8wkkrz"></a>

## 自律システム

外部に対して一貫した[ルーティングポリシー](#4bwmon)の下で運用される[ルータ](#5f2okm)と[IPプレフィックス](#6rwn5e)の集合．[AS番号](#wvk6j6)で識別される．

<a id="rylgay"></a>

## 行

[表](#iuztvu)の要素で，各列に1つの値をもつもの．[リレーショナルモデル](#7y7vys)のタプルに当たる．

<a id="iuztvu"></a>

## 表

[SQL](#v61vr0)において，同じ列の並びをもつ[行](#rylgay)の集まり．[リレーショナルモデル](#7y7vys)のリレーションに当たるが，同じ[行](#rylgay)の重複を許す．

<a id="onqz9u"></a>

## 解放後使用

解放されたメモリの領域を，解放前に得た参照を通じて使用する誤り．

<a id="69tuqj"></a>

## 言語サーバー

[プログラミング言語](#nw9j2i)の意味を解析し，その言語に固有の編集支援の機能を[Language Server Protocol](#dfaxj3)で[テキストエディタ](#nud9su)に提供するプログラム．

<a id="z1b6lv"></a>

## 計算アイテム

他の[アイテム](#as86xt)の値から数式で値を算出する[アイテムタイプ](#ugi5pv)．

<a id="tl94hx"></a>

## 計算量

操作の実行に要する時間または記憶領域を，入力の大きさの[関数](#egp00x)として漸近的に表したもの．定数倍を無視した上界をO記法で表す．

<a id="kltl5m"></a>

## 記憶域

データを書き込み，後に読み出すために保持する容量．

<a id="uvaml5"></a>

## 記憶域期間

[Cオブジェクト](#rq1bpp)の寿命を定める区分．静的，スレッド，自動，割付けの4種があり，寿命はそれぞれ，プログラムの実行の全体，[スレッド](#ou7dup)の実行の全体，宣言を含むブロックへの進入から実行の終了まで（可変長配列は宣言から[有効範囲](#c7221m)を出るまで），[C標準ライブラリ](#oyypas)のaligned_alloc，calloc，malloc，reallocによる確保から解放までである．

ToDo: [141](todo.md#todo-141)

<a id="p7yj2k"></a>

## 許可セット

[組織インスタンス](#ljfr92)において，[AWSアカウント](#r2ghkv)で与える権限を[IAMポリシー](#let9u3)の集まりとして定めたもの．[アカウント割り当て](#n4iumx)に用いると，割り当て先の[AWSアカウント](#r2ghkv)にその権限をもつ[IAMロール](#k1a9js)が作成される．

<a id="id1pzp"></a>

## 許可上限

それ自体は許可を与えず，他の手段で与えられた許可のうち，その範囲を超えるものを無効にする制約．

<a id="kirdkx"></a>

## 許可加算評価

許可の規則のみからなる[ポリシー](#d3j3nj)を[既定拒否](#kfuctl)のもとで用い，いずれかの規則が許可するものを許可する評価の方式．規則の追加は許可を広げるのみである．

<a id="30mc00"></a>

## 証明書

[公開鍵](#7xb1uk)とその保持者を結び付ける主張に，発行者が[電子署名](#wr3566)を付したデータ．[信頼チェーン](#l7b2yn)により検証される．

<a id="8esn53"></a>

## 認可

[主体](#pyjgmb)の要求を許可するか拒否するかを決めること．

<a id="17zvxp"></a>

## 認可エンドポイント

[認可サーバー](#kvuagh)の[エンドポイント](#9i1lg3)．[フロントチャネル](#xjb5je)で[クライアントID](#rhlnw8)を含む要求を受け付け，[主体](#pyjgmb)に[認可クライアント](#47yah2)への許可または拒否を問い合わせ，結果を[フロントチャネル](#xjb5je)で[リダイレクトエンドポイント](#aodeq1)に送る．許可された場合，結果に[認可コード](#cnospa)を含める．

<a id="47yah2"></a>

## 認可クライアント

[OAuth](#2epxko)において，[認可サーバー](#kvuagh)から[アクセストークン](#8w6s21)を得て[リソースサーバー](#6lul9i)に要求を送る[クライアント](#xv4m3d)．[クライアントID](#rhlnw8)で識別される．

<a id="n1yjv8"></a>

## 認可グラント

[認可クライアント](#47yah2)が[トークンエンドポイント](#f9akzj)に示す，[アクセストークン](#8w6s21)の発行の根拠．種類は要求のgrant_typeで指定する．

<a id="cnospa"></a>

## 認可コード

[認可エンドポイント](#17zvxp)が発行し，[認可コードグラント](#sdvdsn)で一度だけ示せる短命の値．

<a id="sdvdsn"></a>

## 認可コードグラント

[認可コード](#cnospa)を示す[認可グラント](#n1yjv8)．grant_typeはauthorization_codeである．

<a id="kvuagh"></a>

## 認可サーバー

[OAuth](#2epxko)において，[リソースサーバー](#6lul9i)に代わって[認可](#8esn53)し，[認可クライアント](#47yah2)に[アクセストークン](#8w6s21)を発行する[サーバー](#uteg7y)．

<a id="l2zofw"></a>

## 認証

[識別](#mo69ip)で主張された[アイデンティティ](#8yx5pi)を確かめること．

<a id="ki350n"></a>

## 認証アサーション

[アイデンティティプロバイダ](#3z77qd)が発行し，[主体](#pyjgmb)の[認証](#l2zofw)の結果を，その[主体](#pyjgmb)を示す識別子と共に表すデータ．

<a id="p3b37s"></a>

## 認証付き暗号

[暗号化](#e382sn)と[認証子](#uft843)の作成を一度に行う[共通鍵暗号](#6uco4b)．

<a id="uft843"></a>

## 認証子

データと[鍵](#atfb8r)から作成し，その[鍵](#atfb8r)またはそれと対をなす[鍵](#atfb8r)で検証する値．検証の成功は，作成に用いた[鍵](#atfb8r)をもつ者が作成したことと，作成後にデータが改変されていないことを示す．

<a id="pyxpuc"></a>

## 認証情報

[認証](#l2zofw)において[主体](#pyjgmb)が[アイデンティティ](#8yx5pi)の証明として示す情報．

<a id="gibl6s"></a>

## 調整ループ

対象の望ましい状態を保持し，実際の状態を観測して望ましい状態との差を減らす操作を繰り返す制御の方式．

ToDo: [104](todo.md#todo-104)

<a id="es46jv"></a>

## 論理ボリューム

[ボリュームグループ](#um9c12)の[物理エクステント](#six0ds)を割り当てて構成され，[ブロックデバイス](#1frbzb)として見える[LVM](#9tfla3)の単位．複数の[物理ボリューム](#uj3w47)にまたがり，稼働中に容量を変えられる．[物理エクステント](#six0ds)の配置に，連続，複数の[物理ボリューム](#uj3w47)への交互の分散，[RAID](#1bon32)がある．シンプールと呼ぶ論理ボリュームからは，[シンプロビジョニング](#twt6a6)による論理ボリュームを切り出せる．

<a id="mo69ip"></a>

## 識別

[主体](#pyjgmb)が自身の[アイデンティティ](#8yx5pi)を主張すること．

<a id="lhc0wp"></a>

## 責任共有モデル

[Amazon Web Services](#totant)と利用者の間のセキュリティの責任の分担．[Amazon Web Services](#totant)はクラウドを構成する基盤を保護し，利用者はクラウド上に置くデータ，[IAMアイデンティティ](#ix9em5)，設定を保護する．利用者の責任の範囲は[AWSサービス](#40hiw9)ごとに異なる．

<a id="k7gc81"></a>

## 資源

[プロセス](#lm3iq5)の実行に用いられ，複数の[プロセス](#lm3iq5)の間で配分される有限の対象．

<a id="syx2b4"></a>

## 資源レコード

[DNS](#v0yvpo)において，[ドメイン名](#d8xx9q)に対応付けられる情報の単位．所有者の[ドメイン名](#d8xx9q)，型，クラス，TTL，型に応じたデータからなる．クラスは[プロトコル](#bhk5im)の体系を示す値であり，[インターネット](#3qoztf)ではINを用いる．TTLは[キャッシュ](#kj4w0z)に保持してよい秒数である．所有者，型，クラスの等しい資源レコードの集合を資源レコードセットと呼ぶ．

<a id="g9mkrr"></a>

## 資源制限

対象の集合ごとに，それが用いる[資源](#k7gc81)の量に上限を課すこと．

<a id="le79r6"></a>

## 資源要求と制限

[コンテナ](#uds0ak)ごとに指定する[資源](#k7gc81)の量．要求は[kube-scheduler](#62x28a)が[ノード](#6qrxi1)の選択に用い，制限は[cgroup](#rh5dah)により実行時に課される．[物理メモリ](#svua87)の制限を超えた[コンテナ](#uds0ak)は強制終了され，[プロセッサ](#4ad6s1)の時間の制限を超える使用は抑制される．

<a id="1sgoxr"></a>

## 資源隔離

[プロセス](#lm3iq5)の集合ごとに，見える[資源](#k7gc81)を分け，他の集合の[資源](#k7gc81)を見えなくすること．

<a id="aesepi"></a>

## 透過プロキシ

要求元に設定させず，要求元と[通信先](#b2znuk)の間で通信を横取りして[中継](#zgr0mv)する[プロキシ](#2f8683)．[Linux](#eh8l2u)では[Netfilter](#feag1h)により，宛先を自計算機に書き換える[DNAT](#x5u5e6)か，宛先を書き換えずに自計算機で受信させることで横取りする．

<a id="b2znuk"></a>

## 通信先

要求元からの通信が最終的に届けられる[端点](#b084uv)．

<a id="lkmji4"></a>

## 連想配列

一意なキーと値の組の集合を保持し，キーにより値を検索，挿入，削除する[抽象データ型](#wlwn4m)．

<a id="zhodwh"></a>

## 連結リスト

各要素が次の要素への参照をもつことで列を表す[データ構造](#y9ua1k)．参照をもつ要素の直後への挿入と削除は定数時間，先頭からi番目の要素へのアクセスはiに比例する時間を要する．各要素が前の要素への参照ももつものを双方向連結リストと呼ぶ．

<a id="ajw0fy"></a>

## 遅延プロシージャ呼び出し

[Windows NT](#jzpnq4)において，DISPATCH_LEVELの[割り込み要求レベル](#aiwf2j)で実行されるよう[待ち行列](#lhxknx)に入れられる手続き．[割り込み](#owu45r)の処理のうち，より高い[割り込み要求レベル](#aiwf2j)を要しない部分の実行に用いられる．

ToDo: [136](todo.md#todo-136)

<a id="mwtuz5"></a>

## 遅延割り当て

[資源](#k7gc81)の割り当てを，それが必要になる最初の書き込みまたは使用の時点まで遅らせる手法．必要にならなかった[資源](#k7gc81)を消費しない．

<a id="06enpz"></a>

## 配列

同じ大きさの要素を連続した記憶領域に並べ，添字から位置を計算して任意の要素に定数時間でアクセスする[データ構造](#y9ua1k)．

<a id="atfb8r"></a>

## 鍵

[暗号](#o5aaif)の演算において，入力のデータとともに出力を定める値．

<a id="u8r1ic"></a>

## 開かれたファイル記述

[ハンドル](#ib1jow)が参照する，開かれたファイルの状態．読み書きの位置と，開いたときのアクセスモードを保持し，複製された[ハンドル](#ib1jow)の間で共有される．

<a id="egp00x"></a>

## 関数

各入力にただ1つの出力を対応させる対応．

<a id="9ss4j8"></a>

## 随意アクセス制御リスト

[セキュリティ記述子](#28ts3b)において，アクセスの許可と拒否を指定する[アクセス制御エントリ](#gyqv5u)の順序付きリストである[保護対象側ポリシー](#4xq8sn)．これが存在しない場合は全てのアクセスが許可され，存在する場合は[既定拒否](#kfuctl)が適用される．

<a id="ilz3yu"></a>

## 障害

[Zabbix](#o6myi6)において，[トリガー値](#hxwb5z)が`PROBLEM`であるときに[トリガー](#3gz3w5)が生成した[イベント](#przzj5)．[トリガー](#3gz3w5)の生成モードが単一なら`PROBLEM`への変化時にのみ，複数なら条件式が真となる評価のたびに生成される．[トリガー](#3gz3w5)が許す場合は手動でクローズできる．

ToDo: [103](todo.md#todo-103)

<a id="84djzd"></a>

## 障害ドメイン

障害が他の区画に波及しないよう，電源と[ネットワーク](#uy18d2)を含む基盤を他の区画と共有しない区画．

<a id="oo8lsi"></a>

## 障害耐性

[オペレーション設定](#fm7edw)の項目．[リージョン](#1df8fw)ごとに，処理の失敗を許容する[ターゲットアカウント](#gjqg2o)の数を，数または割合で定める．失敗がこれを超えた[リージョン](#1df8fw)では処理を止め，後続の[リージョン](#1df8fw)では処理を試みない．

<a id="wr3566"></a>

## 電子署名

データに対して[秘密鍵](#dak54j)で作成し，対の[公開鍵](#7xb1uk)で検証する[認証子](#uft843)．

<a id="diiab2"></a>

## 電波

空間を伝わる，周波数3THz以下の電磁波．

<a id="c7sqk0"></a>

## 静的型付け

変数と式の[データ型](#w7t735)をプログラムの実行前に定め，操作との整合を実行前に検査する方式．

<a id="zlguzf"></a>

## 非同期プロシージャ呼び出し

[Windows NT](#jzpnq4)において，特定の[スレッド](#ou7dup)の文脈で非同期に実行されるよう，その[スレッド](#ou7dup)の[待ち行列](#lhxknx)に入れられる手続き．
