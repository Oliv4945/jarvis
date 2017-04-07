# Jarvis [![Version-shield]](CHANGELOG.md) [![License-shield]](LICENSE.md)

![Banner]

## ![English][English] English
> Jarvis.sh is a lightweight configurable multi-lang jarvis-like bot.
Meant for home automation running on slow computer (ex: Raspberry Pi 2 & 3).  
It installs automatically speech recognition & synthesis engines of your choice.  
It works with a [plugin store](http://domotiquefacile.fr/jarvis/plugins) to add some cool features.

This project is multilingual, which means that you may receive assistance, at least in French and in English.

---
This branch is a port to OpenWrt (tested on Respeaker)  

Some OpenWrt packages are not provided and must be compiled : whiptail, mpg1213, jq. For that I am tring to cross compile them thanks to [Respeaker's github](https://github.com/respeaker/openwrt) repository.  
Steps required on my setup (Debian Stretch)
* `git clone https://github.com/respeaker/openwrt.git`
* cd openwrt
* `cp respeaker.config .config`
* `make tools/install`. I had two errors solved by
  - Manually add `compiler-gcc6.h` to `build_dir/host/u-boot-2014.10/include/linux/`
  - Patch uboot `rsa-sign.c` with [this patch](https://git.lede-project.org/?p=source.git;a=blob;f=tools/mkimage/patches/210-openssl-1.1.x-compat.patch;h=fa7c99f39b0a65f0d784473ca9b8fde836e4fa6e;hb=70b104f98c0657323b28fce140b73a94bf3eb756)
* `make toolchain/install`
  - If required, download [linux-3.18.23.tar.xz](https://www.linux-mips.org/pub/linux/mips/kernel/v3.x/linux-3.18.23.tar.xz) into `./dl`
  - If gcc>=6 is used, a weird error appears while compiling...gcc :-)
So I switched to a virtual machine with gcc 4.9, it works out of the box except Linux sources files download

Packages compilation:
* jq Use this (Makefile)[https://github.com/zz090923610/jq-openwrt], with [this patch](https://github.com/eq-3/occu/blob/master/CCU2/buildroot-2014.11/package/jq/jq-0001-libm.h-comment-j0-j1-y0-and-y1.patch)
* mpg123 from official OpenWrt packages
* whiptail from [here](https://dev.openwrt.org/browser/packages/libs/newt/Makefile) - Still got an error "missing slang.h"
---
<details>
	<summary id="TOC"><strong>Table Of Contents</strong></summary>
- [Requirements]
 - [Compatible equipment]
 - [Compatible OS]
 - [Essential Tools]
- [Supported Languages]
- [Getting started]
- [Contributing]
- [Changelog]
- [Disclaimer & License]

</details>

### Requirements

#### Compatible equipment

<details open>
	<summary id="equipment"><strong>Tested on these compatible equipment</strong></summary>
- *Raspberry Pi 2 Model B*
- *Raspberry Pi 3 Model B*
</details>

#### Compatible OS
Compatible with any Linux distribution that has installed the tools needed. The script checks for them at the beginning.

<details open>
	<summary id="distroslinux"><strong>Tested on these compatible Linux distributions</strong></summary>
- *Raspbian 7 (Wheezy) and 8 (Jessie) (Raspberry Pi)*
</details>

#### Essential tools &#8592; The script does not work if you don't have installed all of them

 Command     | Possible package name | 
:------------|:----------------------|
 git         | git                   |
 
 
### Supported Languages

![English][English] English <br/>
![French][French] French <br/>

---

### Getting started

**Getting started with Jarvis (Core & Plugins)**

Overview & full documentation available on http://domotiquefacile.fr/jarvis/
Please, take a look at [Docs](http://domotiquefacile.fr/jarvis/content/installation) and [Issues](https://github.com/alexylem/jarvis/issues) (mostly [question](https://github.com/alexylem/jarvis/issues?utf8=%E2%9C%93&q=is%3Aissue%20label%3Aquestion%20),  [help wanted](https://github.com/alexylem/jarvis/issues?utf8=%E2%9C%93&q=is%3Aissue%20label%3A%22help%20wanted%22%20) and [plugin request](https://github.com/alexylem/jarvis/issues?q=is%3Aissue+label%3A%22plugin+request%22)) before opening a new issue.


### Contributing

- Translations into other languages
- More distribution and equipment support compatibility
- New features
- Testing and feedback

#### Getting started with Git and GitHub

 * [Setting up Git for Windows and connecting to GitHub](http://help.github.com/win-set-up-git/)
 * [Forking a GitHub repository](http://help.github.com/fork-a-repo/)
 * [The simple guide to GIT guide](http://rogerdudler.github.com/git-guide/)

Once you're familiar with Git and GitHub, you'll be able to clone the repository and contribute.

Read the [Contributing File] for more details on the process of project collaborating and on our code of conduct.

### Changelog

Read the [Changelog File] to review changes.

### Disclaimer & License

Use this script on your own networks and equipment.<br/>
`Jarvis` staff is not responsible of its use in any case.

### License

[![License-shield]](LICENSE.md) Please, refer to [LICENSE.md](https://github.com/alexylem/jarvis/blob/master/LICENSE.md) file.

<!-- Links To Images -->
[Banner]: /imgs/banners/jarvis_banner.png "Simple configurable multi-lang assistant"
[English]: /imgs/flags/us.png "English"
[French]: /imgs/flags/fr.png "French"
<!-- Links To MDs -->
[Changelog File]: CHANGELOG.md
[Contributing File]: CONTRIBUTING.md
[License File]: LICENSE.md
<!-- Badges URLs -->
[Version-shield]: https://img.shields.io/badge/version-17.04.01-blue.svg?style=flat-square&colorA=273133&colorB=0093ee "Latest version"
[License-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square&colorA=273133&colorB=bd0000 "MIT"
