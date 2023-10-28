# Net Chess

A simple networked chess game using Python and bindings for the [raylib](https://github.com/raysan5/raylib) game programming library.

## Building

The expected raylib version and the [raylibpyctbg](https://github.com/overdev/raylibpyctbg) binding generator are included as git submodules. The `build.sh` script will setup (with CMake) and build the library and then generate the binding file. Some modification will likely be necessary to build on Windows.

## Running the Game

Currently, Net Chess supports two ways to play:

1. You can play a local game with both players in the same window by running `main.py.`

2. For a two player game, run `chess_server.py` and `chess_client.py` respectively. The order doesn't matter. They will wait for a connection before opening a window. Currently, these are both hardcoded to run at `localhost:4242`.