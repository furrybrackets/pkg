# `pkg`

`pkg` is a minimal package manager focused on simplicity and efficiency. Everything is compiled from source, and it bridges the distribution gap using `translator`, a multi-lingual translator that converts package info from one manager (ex, `pacman` or AUR) to `pkg`.

## Getting started

`pkg` is a package manager similar to something like `portage`(`emerge`) in that it compiles nearly everything from scratch (excluding binary-based translated packages, such as those from `pacman`).

### Commands

#### `install`

`pkg install` is the command you will probably being using the most. The general workflow of `pkg` goes something like this:

1. User runs `pkg install $(PNAME) <-L $(LOCATION)>`
2. `pkg` gets the `$(PNAME)` package info from the specifed location (`-L` flag aka `--Loc`)
3. `pkg` repeats 2 for all dependencies that aren't installed or updated to required versions
4. `pkg` runs the build script, and then takes the compiled binary and by default puts it in `/usr/local/bin`.
5. Installation is completed.

Some general useful flags include:

* `-U` - Use flag, used to let `pkg` know what optional services it should be building for
* `-L` - Lets `pkg` know what repo to look in (default is `pkg`)
* `--CF` - Compiler flags, is appended to the generated flags made by the build
* `--CFo` - `--CFo` except it doesn't append the flags, it overrides them
* `--Od` - Duplicate output to directory
* `--O` - redirect output
* `-P` - list of different patches you want to run on the program
* `-V` - download a specific version


#### `download`

Download the package and package data without compiling it.

Useful flags:

`-P` - run a patch after download

#### `queue`

Add a downloaded package to build build queue.

Flags:

`-V` - version

#### `update`

Update the package to the newest version or the version specified with `-V`

Flags:

uses the same flags as `install`
