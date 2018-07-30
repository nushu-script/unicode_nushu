Unicode 女书输入法是 [Unicode 女书词典](https://chromezh.github.io/nushu-dictionary/)的一部分。

# Unicode 女书输入法 [![Build status](https://ci.appveyor.com/api/projects/status/877sevtm8mpdayot?svg=true)](https://ci.appveyor.com/project/chromezh/unicode-nushu) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

**使用 Unicode 女书输入法，简便地输入 Unicode 编码的 396 个女书字符。**

![Unicode 女书输入法](https://chromezh.github.io/unicode_nushu/demo/weasel_unicode_nushu0.png)

![Unicode 女书输入法](https://chromezh.github.io/unicode_nushu/demo/weasel_unicode_nushu1.png)

| Unicode 女书输入法必要文件 | 最新版本 |
| :- | :- |
| unicode_nushu_romanization.dict.yaml | 20180506 V1.1.04 |
| unicode_nushu_romanization.schema.yaml | 20180506 V1.0.03 |
| luna_pinyin_nushu.schema.yaml | 20180506 V1.0.01 |
| s2nushu.json | 20180506 |
| s2nushu.txt | 20180528 ![new](https://chromezh.github.io/unicode_nushu/demo/new_6.png) |

## 安装与更新

* [安装方法](https://chromezh.github.io/unicode_nushu/install)
* [Unicode 女书输入法更新](https://chromezh.github.io/unicode_nushu/update)

## 使用方法

### 使用普通话拼音输入女书（汉字对照）

　　首先，将输入法切换到「小狼毫（TSF）」。

　　按 `F4` 或 ```Ctrl+` ``` 唤出菜单，选择「朙月拼音·Unicode 女书」，即可通过普通话输入女书。

　　目前支持 1760 个汉字，其他汉字尚不能转换为对应的女书。

![](https://chromezh.github.io/unicode_nushu/demo/weasel_unicode_nushu1.png)

### 使用女书拼音输入女书

　　首先，将输入法切换到「小狼毫（TSF）」。

　　按 `F4` 或 ```Ctrl+` ``` 唤出菜单，选择「朙月拼音·Unicode 女书」。

　　按下 &#96; 键（在键盘的左上角）， 进入女书拼音输入模式。

![](https://chromezh.github.io/unicode_nushu/demo/weasel_unicode_nushu3.png)

　　继续输入字母，即可通过女书拼音输入女书。

![](https://chromezh.github.io/unicode_nushu/demo/weasel_unicode_nushu0.png)

　　另外，按 `F4` 或 ```Ctrl+` ``` 唤出菜单，选择「Unicode 女书拼音」，可以在不按 &#96; 键的情况下，通过女书拼音输入女书。

### 退出女书输入模式（只得到汉字）

　　使用「朙月拼音·Unicode 女书」时，有两种方法退出女书模式。退出女书输入模式后，仍然是使用普通话拼音进行输入，但得到的是汉字，而不是女书。

![](https://chromezh.github.io/unicode_nushu/demo/weasel_unicode_nushu2.png)

　　可以按 `F4` 或 ```Ctrl+` ``` 唤出菜单，再按 4 选择「女书 -> 汉字」选项退出女书模式，也可以按 `Ctrl+Shift+4` 快捷键退出女书模式。

![](https://chromezh.github.io/unicode_nushu/demo/weasel_unicode_nushu4.png)

## 女书拼音

> 注：此处的女书拼音不是完整的江永城关话音系，仅是为了输入女书字符而设定。

### 声母

| 国际音标 | p | p' | m | f | v | t | t' | n | l | ts | ts' | s | tɕ | tɕ' | ȵ | k | k' | ŋ | h | ∅ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| NushuSources | p | ph | m | f | v | t | th | n | l | ts | tsh | s | tc | tch | nj | k | kh | ng | h | &nbsp; |
| Unicode 女书输入法拼音 | b | p | m | f | v | d | t | n | l | z | c | s | j | q | nj | g | k | ng | h | &nbsp; |

> 说明：Unicode 女书输入法的声母表记类似普通话拼音方案。

### 韵母

| 国际音标 | a | ua | ya | ie | ø | uø | yø | uə | yə | ɯə | i | iu | u | yu | y | ɯ | ai | uai | yai | au | iau | ou | iou | əɯ | uoɯ | yoɯ | uɯ | yn | aŋ | iaŋ | uaŋ | yaŋ | əŋ | oŋ | ioŋ | iŋ | ŋ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| NushuSources 及 Unicode 女书输入法拼音 | a | ua | ya | ie | oe | uoe | yoe | ue | ye | we | i | iu | u | yu | y | w | ai | uai | yai | au | iau | ou | iou | ew | uow | yow | uw | yn | ang | iang | uang | yang | eng | ong | iong | ing | ng |

> 注意：
> 1. `y` 代表普通话拼音中 `ü` 的发音；
> 1. `w` 代表不圆唇的 `u`；
> 1. `ue`, `ye`, `we` 中的 `e` 读如普通话「饿」，不是普通话「夜」（ye）中的 `e`。

### 声调

　　声调 7 个，其中平上去分阴阳，入声不分。

　　调值：阴平 **44** 阳平 **42** 阴上 **35** 阳上 **13** 阴去 **21** 阳去 **33** 入声 **5**。

　　其中，声调使用「五度标调法」表示，数字表示的是声调的调值，即将音高分为 5 度，最高为 `5`，最低为 `1`。例如 `35` 表示升调，且音高由中等到最高。入声读音短促，故用单数字表示。

## Unicode 编码-女书发音对照表

　　本表修订于 2018 年 5 月 6 日。

![Unicode 编码-女书发音对照表](https://chromezh.github.io/unicode_nushu/demo/unicode-nushu-pronunciation_table.png)

## 致谢

　　本项目利用了以下项目的成果：

* [RIME &brvbar; 中州韻輸入法引擎](http://rime.im/)
* [開放中文轉換 (Open Chinese Convert)](https://github.com/BYVoid/OpenCC)
* [天珩全字库](http://cheonhyeong.com/Simplified/download.html)

　　本项目参考了以下资料：

* 赵丽明，徐焰著《女书规范字书法字帖》
* **Unicode Character Database** 中的 [NushuSources-11.0.0d1.txt](http://www.unicode.org/Public/11.0.0/ucd/NushuSources-11.0.0d1.txt)


## 开发指南

　　欢迎更多的人参与到 Unicode 女书输入法的开发中，为本项目的完善贡献力量。

　　Unicode 女书输入法各组件的关系参见[简介](https://chromezh.github.io/unicode_nushu/intro)。

　　若您发现 Unicode 女书输入法的任何问题，或有任何功能建议，请在[本页面 (https://github.com/chromezh/unicode_nushu)](https://github.com/chromezh/unicode_nushu) 上方点击 Issues -> New Issue，发起反馈。若已有解决方案，欢迎发起 Pull Request。

　　本项目是 Unicode 女书词典的一部分。若您想参与词库的修改和补充，请访问 [Unicode 女书词典](https://chromezh.github.io/nushu-dictionary/)。

　　若您有 GitHub 账号，且本项目对您有帮助，请在页面右上角为本项目点击 `Star` 按钮～
