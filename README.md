# Net Chess

A simple networked chess game using Python and bindings for the [raylib](https://github.com/raysan5/raylib) game programming library.

## Downloading and Building

The expected raylib version and the [raylibpyctbg](https://github.com/overdev/raylibpyctbg) binding generator are included as git submodules. If you have already cloned the repo without the `--recurse_submodules` option, you can update these with the following:

```sh
git submodule update --init --recursive
```

Running the `build.sh` script will setup (with CMake) and build the library and then call `generate_bindings.sh` to generate the binding file. Some modification will likely be necessary to build on Windows.

## Running the Game

```sh
python src/main.py
```

By default, running `main.py` will start a local two player chess match. However, the program supports several command-line arguments that allow you to host and join networked games between a host and a client.

| Argument  | Default  | Description |
|-----------|----------|-------------|
|`-m` / `--mode`    | `None`	  | Tells the program to `host` or `join` a game. If undefined, a single client session is started and other arguments will be ignored. |
|`-a` / `--address` | `localhost` | Sets the address at which the game will be hosted or joined |
|`-p` / `--port` 	| `4242` 	  | Sets the port at which the game will be hosted or joined |	