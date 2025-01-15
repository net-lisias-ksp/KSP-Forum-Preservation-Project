# KSP's Forum Preservation Project :: Install Instructions

This document explains how to set up this circus and make some profit.


## Installing `python` and `virtualenv`

### Linux

wip

#### Linux on ARM (Debian ARM Bookworm)

I recently acquired a nice Raspberry PI5 that I could use on this project and, so, I did. :)

The thing works very well, however... `lzrip`, a key item on this toolchain, is broken on Debian (and almost surely all other ARM distributions). It's a pain in the ass, but it's survivable as the problem was [already diagnosed](https://andrei600.wordpress.com/2016/04/11/project-improving-lrzip-phase-two/). TL;DR: `lrzip` makes use or a JIT code that only works on x86, but a flaw on the source code is activating the JIT while compiling in ARM.

The workaround I used is the one proposed by `andrei600` in the document I linked above. Edit `libzpaq.cpp`:

from:

```c
#include "libzpaq.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#ifndef NOJIT
#ifndef _WIN32
#include <sys/mman.h>
#else
#include <windows.h>
#endif
#endif
```

to:

```c
#include "libzpaq.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// GNU
#ifdef __arm__
#define NOJIT 1
#endif
#ifdef __aarch64__
#define NOJIT 1
#endif

#ifndef NOJIT
#ifndef _WIN32
#include <sys/mman.h>
#else
#include <windows.h>
#endif
#endif
```

And recompile the damn thing. On Debian, do as follows:

```bash
sudo dpkg -r lrzip
sudo apt-get install build-essential fakeroot devscripts
sudo apt install liblz4-dev liblzo2-dev libbz2-dev
cd ~
mkdir code
cd code
git clone https://github.com/ckolivas/lrzip.git
cd lrzip

** EDIT libzpaq/libzpaq.cpp as instructed above **

./autogen.sh
./configure
make
sudo make install
```

This will uninstall the stock `lrzip`, install all necessary tools and libs and then will build and install your custom `lzzip` into `/usr/local/bin`.

From this point, everything just works.


### MacOS

wip

### Windows

Dude, you should be masochist. :)

wip


## Installing remaining tools

wip


## Downloading this repository

wip


## Configuring to your environment

wip


## Firing up the whole thing

wip

### Using the Steam Deck

```
sudo systemctl start sshd
systemd-run --scope --user tmux
```

Não esquecer o SWAP!!!
