from raylib import *

# NOTE: Currently raises AttributeError on import, which can be fixed by removing attributes after and including "Drawing" in __all__

def main():
	InitWindow(800, 600, "Net Chess")
	
	while not WindowShouldClose():
		BeginDrawing()
		
		ClearBackground(RAYWHITE)
		text = "Chess With Raylib and Python(?)!"
		font_size = 16
		width = MeasureText(text, font_size)
		DrawText(text, 400-width/2, 300-font_size/2, font_size, RED)

		EndDrawing()

	CloseWindow()

main()