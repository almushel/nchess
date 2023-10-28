# Net Chess

A simple networked chess game using Python and bindings for the [Raylib](https://github.com/raysan5/raylib) game programming library.

## Building

This game requires local copy of raylib built as a shared library. The expected raylib version is included as a submodule and the `build.sh` script should setup (with CMake) and build it in the location specified in the `.raylib` file (this is referenced by the raylib.py python binding). This assumes `make` is installed, so modification is mostly likely required on Windows (e.g. `msbuild` or `nmake`).

## Running the Game

Currently, Net Chess supports two ways to play. You can play a local game with both players in the same window by running `main.py.` For a two player game, run `chess_server.py` and `chess_client.py` respectively. The order doesn't matter. They will wait for the connection before opening a window. Currently, these are both hardcoded to run at `localhost:4242`.