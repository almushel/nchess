
import sys
import re
import os
import platform
import ctypes
from enum import IntEnum
from contextlib import contextmanager
from typing import Optional as Opt, Any, Sequence as Seq, Union
from ctypes import (
    CDLL, wintypes,
    c_bool, c_char, c_byte, c_short, c_long, c_longlong, c_ubyte, c_ushort, c_ulong, c_ulonglong, c_float, c_double, c_char_p, c_void_p,
    Structure, POINTER, CFUNCTYPE, byref, cast
) 


__all__ = [
    'rlapi',
    'Bool',
    'BoolPtr',
    'Byte',
    'BytePtr',
    'Char',
    'CharPtr',
    'Short',
    'ShortPtr',
    'Int',
    'IntPtr',
    'Long',
    'LongPtr',
    'UByte',
    'UBytePtr',
    'UShort',
    'UShortPtr',
    'UInt',
    'UIntPtr',
    'ULong',
    'ULongPtr',
    'Float',
    'FloatPtr',
    'Double',
    'DoublePtr',
    'VoidPtr',
    'VoidPtrPtr',

    'Vector2',
    'Vector3',
    'Vector4',
    'Matrix',
    'Color',
    'Rectangle',
    'Image',
    'Texture',
    'RenderTexture',
    'NPatchInfo',
    'GlyphInfo',
    'Font',
    'Camera3D',
    'Camera2D',
    'Mesh',
    'Shader',
    'MaterialMap',
    'Material',
    'Transform',
    'BoneInfo',
    'Model',
    'ModelAnimation',
    'Ray',
    'RayCollision',
    'BoundingBox',
    'Wave',
    'AudioStream',
    'Sound',
    'Music',
    'VrDeviceInfo',
    'VrStereoConfig',
    'FilePathList',
    'RAYLIB_VERSION_MAJOR',
    'RAYLIB_VERSION_MINOR',
    'RAYLIB_VERSION_PATCH',
    'RAYLIB_VERSION',
    'PI',
    'DEG2RAD',
    'RAD2DEG',
    'LIGHTGRAY',
    'GRAY',
    'DARKGRAY',
    'YELLOW',
    'GOLD',
    'ORANGE',
    'PINK',
    'RED',
    'MAROON',
    'GREEN',
    'LIME',
    'DARKGREEN',
    'SKYBLUE',
    'BLUE',
    'DARKBLUE',
    'PURPLE',
    'VIOLET',
    'DARKPURPLE',
    'BEIGE',
    'BROWN',
    'DARKBROWN',
    'WHITE',
    'BLACK',
    'BLANK',
    'MAGENTA',
    'RAYWHITE',
    'Quaternion',
    'Texture2D',
    'TextureCubemap',
    'RenderTexture2D',
    'Camera',
    'ConfigFlags',
    'FLAG_VSYNC_HINT',
    'FLAG_FULLSCREEN_MODE',
    'FLAG_WINDOW_RESIZABLE',
    'FLAG_WINDOW_UNDECORATED',
    'FLAG_WINDOW_HIDDEN',
    'FLAG_WINDOW_MINIMIZED',
    'FLAG_WINDOW_MAXIMIZED',
    'FLAG_WINDOW_UNFOCUSED',
    'FLAG_WINDOW_TOPMOST',
    'FLAG_WINDOW_ALWAYS_RUN',
    'FLAG_WINDOW_TRANSPARENT',
    'FLAG_WINDOW_HIGHDPI',
    'FLAG_WINDOW_MOUSE_PASSTHROUGH',
    'FLAG_MSAA_4X_HINT',
    'FLAG_INTERLACED_HINT',
    'TraceLogLevel',
    'LOG_ALL',
    'LOG_TRACE',
    'LOG_DEBUG',
    'LOG_INFO',
    'LOG_WARNING',
    'LOG_ERROR',
    'LOG_FATAL',
    'LOG_NONE',
    'KeyboardKey',
    'KEY_NULL',
    'KEY_APOSTROPHE',
    'KEY_COMMA',
    'KEY_MINUS',
    'KEY_PERIOD',
    'KEY_SLASH',
    'KEY_ZERO',
    'KEY_ONE',
    'KEY_TWO',
    'KEY_THREE',
    'KEY_FOUR',
    'KEY_FIVE',
    'KEY_SIX',
    'KEY_SEVEN',
    'KEY_EIGHT',
    'KEY_NINE',
    'KEY_SEMICOLON',
    'KEY_EQUAL',
    'KEY_A',
    'KEY_B',
    'KEY_C',
    'KEY_D',
    'KEY_E',
    'KEY_F',
    'KEY_G',
    'KEY_H',
    'KEY_I',
    'KEY_J',
    'KEY_K',
    'KEY_L',
    'KEY_M',
    'KEY_N',
    'KEY_O',
    'KEY_P',
    'KEY_Q',
    'KEY_R',
    'KEY_S',
    'KEY_T',
    'KEY_U',
    'KEY_V',
    'KEY_W',
    'KEY_X',
    'KEY_Y',
    'KEY_Z',
    'KEY_LEFT_BRACKET',
    'KEY_BACKSLASH',
    'KEY_RIGHT_BRACKET',
    'KEY_GRAVE',
    'KEY_SPACE',
    'KEY_ESCAPE',
    'KEY_ENTER',
    'KEY_TAB',
    'KEY_BACKSPACE',
    'KEY_INSERT',
    'KEY_DELETE',
    'KEY_RIGHT',
    'KEY_LEFT',
    'KEY_DOWN',
    'KEY_UP',
    'KEY_PAGE_UP',
    'KEY_PAGE_DOWN',
    'KEY_HOME',
    'KEY_END',
    'KEY_CAPS_LOCK',
    'KEY_SCROLL_LOCK',
    'KEY_NUM_LOCK',
    'KEY_PRINT_SCREEN',
    'KEY_PAUSE',
    'KEY_F1',
    'KEY_F2',
    'KEY_F3',
    'KEY_F4',
    'KEY_F5',
    'KEY_F6',
    'KEY_F7',
    'KEY_F8',
    'KEY_F9',
    'KEY_F10',
    'KEY_F11',
    'KEY_F12',
    'KEY_LEFT_SHIFT',
    'KEY_LEFT_CONTROL',
    'KEY_LEFT_ALT',
    'KEY_LEFT_SUPER',
    'KEY_RIGHT_SHIFT',
    'KEY_RIGHT_CONTROL',
    'KEY_RIGHT_ALT',
    'KEY_RIGHT_SUPER',
    'KEY_KB_MENU',
    'KEY_KP_0',
    'KEY_KP_1',
    'KEY_KP_2',
    'KEY_KP_3',
    'KEY_KP_4',
    'KEY_KP_5',
    'KEY_KP_6',
    'KEY_KP_7',
    'KEY_KP_8',
    'KEY_KP_9',
    'KEY_KP_DECIMAL',
    'KEY_KP_DIVIDE',
    'KEY_KP_MULTIPLY',
    'KEY_KP_SUBTRACT',
    'KEY_KP_ADD',
    'KEY_KP_ENTER',
    'KEY_KP_EQUAL',
    'KEY_BACK',
    'KEY_MENU',
    'KEY_VOLUME_UP',
    'KEY_VOLUME_DOWN',
    'MouseButton',
    'MOUSE_BUTTON_LEFT',
    'MOUSE_BUTTON_RIGHT',
    'MOUSE_BUTTON_MIDDLE',
    'MOUSE_BUTTON_SIDE',
    'MOUSE_BUTTON_EXTRA',
    'MOUSE_BUTTON_FORWARD',
    'MOUSE_BUTTON_BACK',
    'MouseCursor',
    'MOUSE_CURSOR_DEFAULT',
    'MOUSE_CURSOR_ARROW',
    'MOUSE_CURSOR_IBEAM',
    'MOUSE_CURSOR_CROSSHAIR',
    'MOUSE_CURSOR_POINTING_HAND',
    'MOUSE_CURSOR_RESIZE_EW',
    'MOUSE_CURSOR_RESIZE_NS',
    'MOUSE_CURSOR_RESIZE_NWSE',
    'MOUSE_CURSOR_RESIZE_NESW',
    'MOUSE_CURSOR_RESIZE_ALL',
    'MOUSE_CURSOR_NOT_ALLOWED',
    'GamepadButton',
    'GAMEPAD_BUTTON_UNKNOWN',
    'GAMEPAD_BUTTON_LEFT_FACE_UP',
    'GAMEPAD_BUTTON_LEFT_FACE_RIGHT',
    'GAMEPAD_BUTTON_LEFT_FACE_DOWN',
    'GAMEPAD_BUTTON_LEFT_FACE_LEFT',
    'GAMEPAD_BUTTON_RIGHT_FACE_UP',
    'GAMEPAD_BUTTON_RIGHT_FACE_RIGHT',
    'GAMEPAD_BUTTON_RIGHT_FACE_DOWN',
    'GAMEPAD_BUTTON_RIGHT_FACE_LEFT',
    'GAMEPAD_BUTTON_LEFT_TRIGGER_1',
    'GAMEPAD_BUTTON_LEFT_TRIGGER_2',
    'GAMEPAD_BUTTON_RIGHT_TRIGGER_1',
    'GAMEPAD_BUTTON_RIGHT_TRIGGER_2',
    'GAMEPAD_BUTTON_MIDDLE_LEFT',
    'GAMEPAD_BUTTON_MIDDLE',
    'GAMEPAD_BUTTON_MIDDLE_RIGHT',
    'GAMEPAD_BUTTON_LEFT_THUMB',
    'GAMEPAD_BUTTON_RIGHT_THUMB',
    'GamepadAxis',
    'GAMEPAD_AXIS_LEFT_X',
    'GAMEPAD_AXIS_LEFT_Y',
    'GAMEPAD_AXIS_RIGHT_X',
    'GAMEPAD_AXIS_RIGHT_Y',
    'GAMEPAD_AXIS_LEFT_TRIGGER',
    'GAMEPAD_AXIS_RIGHT_TRIGGER',
    'MaterialMapIndex',
    'MATERIAL_MAP_ALBEDO',
    'MATERIAL_MAP_METALNESS',
    'MATERIAL_MAP_NORMAL',
    'MATERIAL_MAP_ROUGHNESS',
    'MATERIAL_MAP_OCCLUSION',
    'MATERIAL_MAP_EMISSION',
    'MATERIAL_MAP_HEIGHT',
    'MATERIAL_MAP_CUBEMAP',
    'MATERIAL_MAP_IRRADIANCE',
    'MATERIAL_MAP_PREFILTER',
    'MATERIAL_MAP_BRDF',
    'ShaderLocationIndex',
    'SHADER_LOC_VERTEX_POSITION',
    'SHADER_LOC_VERTEX_TEXCOORD01',
    'SHADER_LOC_VERTEX_TEXCOORD02',
    'SHADER_LOC_VERTEX_NORMAL',
    'SHADER_LOC_VERTEX_TANGENT',
    'SHADER_LOC_VERTEX_COLOR',
    'SHADER_LOC_MATRIX_MVP',
    'SHADER_LOC_MATRIX_VIEW',
    'SHADER_LOC_MATRIX_PROJECTION',
    'SHADER_LOC_MATRIX_MODEL',
    'SHADER_LOC_MATRIX_NORMAL',
    'SHADER_LOC_VECTOR_VIEW',
    'SHADER_LOC_COLOR_DIFFUSE',
    'SHADER_LOC_COLOR_SPECULAR',
    'SHADER_LOC_COLOR_AMBIENT',
    'SHADER_LOC_MAP_ALBEDO',
    'SHADER_LOC_MAP_METALNESS',
    'SHADER_LOC_MAP_NORMAL',
    'SHADER_LOC_MAP_ROUGHNESS',
    'SHADER_LOC_MAP_OCCLUSION',
    'SHADER_LOC_MAP_EMISSION',
    'SHADER_LOC_MAP_HEIGHT',
    'SHADER_LOC_MAP_CUBEMAP',
    'SHADER_LOC_MAP_IRRADIANCE',
    'SHADER_LOC_MAP_PREFILTER',
    'SHADER_LOC_MAP_BRDF',
    'ShaderUniformDataType',
    'SHADER_UNIFORM_FLOAT',
    'SHADER_UNIFORM_VEC2',
    'SHADER_UNIFORM_VEC3',
    'SHADER_UNIFORM_VEC4',
    'SHADER_UNIFORM_INT',
    'SHADER_UNIFORM_IVEC2',
    'SHADER_UNIFORM_IVEC3',
    'SHADER_UNIFORM_IVEC4',
    'SHADER_UNIFORM_SAMPLER2D',
    'ShaderAttributeDataType',
    'SHADER_ATTRIB_FLOAT',
    'SHADER_ATTRIB_VEC2',
    'SHADER_ATTRIB_VEC3',
    'SHADER_ATTRIB_VEC4',
    'PixelFormat',
    'PIXELFORMAT_UNCOMPRESSED_GRAYSCALE',
    'PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA',
    'PIXELFORMAT_UNCOMPRESSED_R5G6B5',
    'PIXELFORMAT_UNCOMPRESSED_R8G8B8',
    'PIXELFORMAT_UNCOMPRESSED_R5G5B5A1',
    'PIXELFORMAT_UNCOMPRESSED_R4G4B4A4',
    'PIXELFORMAT_UNCOMPRESSED_R8G8B8A8',
    'PIXELFORMAT_UNCOMPRESSED_R32',
    'PIXELFORMAT_UNCOMPRESSED_R32G32B32',
    'PIXELFORMAT_UNCOMPRESSED_R32G32B32A32',
    'PIXELFORMAT_COMPRESSED_DXT1_RGB',
    'PIXELFORMAT_COMPRESSED_DXT1_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT3_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT5_RGBA',
    'PIXELFORMAT_COMPRESSED_ETC1_RGB',
    'PIXELFORMAT_COMPRESSED_ETC2_RGB',
    'PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA',
    'PIXELFORMAT_COMPRESSED_PVRT_RGB',
    'PIXELFORMAT_COMPRESSED_PVRT_RGBA',
    'PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA',
    'PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA',
    'TextureFilter',
    'TEXTURE_FILTER_POINT',
    'TEXTURE_FILTER_BILINEAR',
    'TEXTURE_FILTER_TRILINEAR',
    'TEXTURE_FILTER_ANISOTROPIC_4X',
    'TEXTURE_FILTER_ANISOTROPIC_8X',
    'TEXTURE_FILTER_ANISOTROPIC_16X',
    'TextureWrap',
    'TEXTURE_WRAP_REPEAT',
    'TEXTURE_WRAP_CLAMP',
    'TEXTURE_WRAP_MIRROR_REPEAT',
    'TEXTURE_WRAP_MIRROR_CLAMP',
    'CubemapLayout',
    'CUBEMAP_LAYOUT_AUTO_DETECT',
    'CUBEMAP_LAYOUT_LINE_VERTICAL',
    'CUBEMAP_LAYOUT_LINE_HORIZONTAL',
    'CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR',
    'CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE',
    'CUBEMAP_LAYOUT_PANORAMA',
    'FontType',
    'FONT_DEFAULT',
    'FONT_BITMAP',
    'FONT_SDF',
    'BlendMode',
    'BLEND_ALPHA',
    'BLEND_ADDITIVE',
    'BLEND_MULTIPLIED',
    'BLEND_ADD_COLORS',
    'BLEND_SUBTRACT_COLORS',
    'BLEND_ALPHA_PREMULTIPLY',
    'BLEND_CUSTOM',
    'BLEND_CUSTOM_SEPARATE',
    'Gesture',
    'GESTURE_NONE',
    'GESTURE_TAP',
    'GESTURE_DOUBLETAP',
    'GESTURE_HOLD',
    'GESTURE_DRAG',
    'GESTURE_SWIPE_RIGHT',
    'GESTURE_SWIPE_LEFT',
    'GESTURE_SWIPE_UP',
    'GESTURE_SWIPE_DOWN',
    'GESTURE_PINCH_IN',
    'GESTURE_PINCH_OUT',
    'CameraMode',
    'CAMERA_CUSTOM',
    'CAMERA_FREE',
    'CAMERA_ORBITAL',
    'CAMERA_FIRST_PERSON',
    'CAMERA_THIRD_PERSON',
    'CameraProjection',
    'CAMERA_PERSPECTIVE',
    'CAMERA_ORTHOGRAPHIC',
    'NPatchLayout',
    'NPATCH_NINE_PATCH',
    'NPATCH_THREE_PATCH_VERTICAL',
    'NPATCH_THREE_PATCH_HORIZONTAL',
    'TraceLogCallback',
    'LoadFileDataCallback',
    'SaveFileDataCallback',
    'LoadFileTextCallback',
    'SaveFileTextCallback',
    'AudioCallback',
    'InitWindow',
    'WindowShouldClose',
    'CloseWindow',
    'IsWindowReady',
    'IsWindowFullscreen',
    'IsWindowHidden',
    'IsWindowMinimized',
    'IsWindowMaximized',
    'IsWindowFocused',
    'IsWindowResized',
    'IsWindowState',
    'SetWindowState',
    'ClearWindowState',
    'ToggleFullscreen',
    'MaximizeWindow',
    'MinimizeWindow',
    'RestoreWindow',
    'SetWindowIcon',
    'SetWindowIcons',
    'SetWindowTitle',
    'SetWindowPosition',
    'SetWindowMonitor',
    'SetWindowMinSize',
    'SetWindowSize',
    'SetWindowOpacity',
    'GetWindowHandle',
    'GetScreenWidth',
    'GetScreenHeight',
    'GetRenderWidth',
    'GetRenderHeight',
    'GetMonitorCount',
    'GetCurrentMonitor',
    'GetMonitorPosition',
    'GetMonitorWidth',
    'GetMonitorHeight',
    'GetMonitorPhysicalWidth',
    'GetMonitorPhysicalHeight',
    'GetMonitorRefreshRate',
    'GetWindowPosition',
    'GetWindowScaleDPI',
    'GetMonitorName',
    'SetClipboardText',
    'GetClipboardText',
    'EnableEventWaiting',
    'DisableEventWaiting',
    'SwapScreenBuffer',
    'PollInputEvents',
    'WaitTime',
    'ShowCursor',
    'HideCursor',
    'IsCursorHidden',
    'EnableCursor',
    'DisableCursor',
    'IsCursorOnScreen',
    'ClearBackground',
    'BeginDrawing',
    'EndDrawing',
    'BeginMode2D',
    'EndMode2D',
    'BeginMode3D',
    'EndMode3D',
    'BeginTextureMode',
    'EndTextureMode',
    'BeginShaderMode',
    'EndShaderMode',
    'BeginBlendMode',
    'EndBlendMode',
    'BeginScissorMode',
    'EndScissorMode',
    'BeginVrStereoMode',
    'EndVrStereoMode',
    'LoadVrStereoConfig',
    'UnloadVrStereoConfig',
    'LoadShader',
    'LoadShaderFromMemory',
    'IsShaderReady',
    'GetShaderLocation',
    'GetShaderLocationAttrib',
    'SetShaderValue',
    'SetShaderValueV',
    'SetShaderValueMatrix',
    'SetShaderValueTexture',
    'UnloadShader',
    'GetMouseRay',
    'GetCameraMatrix',
    'GetCameraMatrix2D',
    'GetWorldToScreen',
    'GetScreenToWorld2D',
    'GetWorldToScreenEx',
    'GetWorldToScreen2D',
    'SetTargetFPS',
    'GetFPS',
    'GetFrameTime',
    'GetTime',
    'GetRandomValue',
    'SetRandomSeed',
    'TakeScreenshot',
    'SetConfigFlags',
    'TraceLog',
    'SetTraceLogLevel',
    'MemAlloc',
    'MemRealloc',
    'MemFree',
    'OpenURL',
    'SetTraceLogCallback',
    'SetLoadFileDataCallback',
    'SetSaveFileDataCallback',
    'SetLoadFileTextCallback',
    'SetSaveFileTextCallback',
    'LoadFileData',
    'UnloadFileData',
    'SaveFileData',
    'ExportDataAsCode',
    'LoadFileText',
    'UnloadFileText',
    'SaveFileText',
    'FileExists',
    'DirectoryExists',
    'IsFileExtension',
    'GetFileLength',
    'GetFileExtension',
    'GetFileName',
    'GetFileNameWithoutExt',
    'GetDirectoryPath',
    'GetPrevDirectoryPath',
    'GetWorkingDirectory',
    'GetApplicationDirectory',
    'ChangeDirectory',
    'IsPathFile',
    'LoadDirectoryFiles',
    'LoadDirectoryFilesEx',
    'UnloadDirectoryFiles',
    'IsFileDropped',
    'LoadDroppedFiles',
    'UnloadDroppedFiles',
    'GetFileModTime',
    'CompressData',
    'DecompressData',
    'EncodeDataBase64',
    'DecodeDataBase64',
    'IsKeyPressed',
    'IsKeyDown',
    'IsKeyReleased',
    'IsKeyUp',
    'SetExitKey',
    'GetKeyPressed',
    'GetCharPressed',
    'IsGamepadAvailable',
    'GetGamepadName',
    'IsGamepadButtonPressed',
    'IsGamepadButtonDown',
    'IsGamepadButtonReleased',
    'IsGamepadButtonUp',
    'GetGamepadButtonPressed',
    'GetGamepadAxisCount',
    'GetGamepadAxisMovement',
    'SetGamepadMappings',
    'IsMouseButtonPressed',
    'IsMouseButtonDown',
    'IsMouseButtonReleased',
    'IsMouseButtonUp',
    'GetMouseX',
    'GetMouseY',
    'GetMousePosition',
    'GetMouseDelta',
    'SetMousePosition',
    'SetMouseOffset',
    'SetMouseScale',
    'GetMouseWheelMove',
    'GetMouseWheelMoveV',
    'SetMouseCursor',
    'GetTouchX',
    'GetTouchY',
    'GetTouchPosition',
    'GetTouchPointId',
    'GetTouchPointCount',
    'SetGesturesEnabled',
    'IsGestureDetected',
    'GetGestureDetected',
    'GetGestureHoldDuration',
    'GetGestureDragVector',
    'GetGestureDragAngle',
    'GetGesturePinchVector',
    'GetGesturePinchAngle',
    'UpdateCamera',
    'UpdateCameraPro',
    'SetShapesTexture',
    'DrawPixel',
    'DrawPixelV',
    'DrawLine',
    'DrawLineV',
    'DrawLineEx',
    'DrawLineBezier',
    'DrawLineBezierQuad',
    'DrawLineBezierCubic',
    'DrawLineStrip',
    'DrawCircle',
    'DrawCircleSector',
    'DrawCircleSectorLines',
    'DrawCircleGradient',
    'DrawCircleV',
    'DrawCircleLines',
    'DrawEllipse',
    'DrawEllipseLines',
    'DrawRing',
    'DrawRingLines',
    'DrawRectangle',
    'DrawRectangleV',
    'DrawRectangleRec',
    'DrawRectanglePro',
    'DrawRectangleGradientV',
    'DrawRectangleGradientH',
    'DrawRectangleGradientEx',
    'DrawRectangleLines',
    'DrawRectangleLinesEx',
    'DrawRectangleRounded',
    'DrawRectangleRoundedLines',
    'DrawTriangle',
    'DrawTriangleLines',
    'DrawTriangleFan',
    'DrawTriangleStrip',
    'DrawPoly',
    'DrawPolyLines',
    'DrawPolyLinesEx',
    'CheckCollisionRecs',
    'CheckCollisionCircles',
    'CheckCollisionCircleRec',
    'CheckCollisionPointRec',
    'CheckCollisionPointCircle',
    'CheckCollisionPointTriangle',
    'CheckCollisionPointPoly',
    'CheckCollisionLines',
    'CheckCollisionPointLine',
    'GetCollisionRec',
    'LoadImage',
    'LoadImageRaw',
    'LoadImageAnim',
    'LoadImageFromMemory',
    'LoadImageFromTexture',
    'LoadImageFromScreen',
    'IsImageReady',
    'UnloadImage',
    'ExportImage',
    'ExportImageAsCode',
    'GenImageColor',
    'GenImageGradientV',
    'GenImageGradientH',
    'GenImageGradientRadial',
    'GenImageChecked',
    'GenImageWhiteNoise',
    'GenImagePerlinNoise',
    'GenImageCellular',
    'GenImageText',
    'ImageCopy',
    'ImageFromImage',
    'ImageText',
    'ImageTextEx',
    'ImageFormat',
    'ImageToPOT',
    'ImageCrop',
    'ImageAlphaCrop',
    'ImageAlphaClear',
    'ImageAlphaMask',
    'ImageAlphaPremultiply',
    'ImageBlurGaussian',
    'ImageResize',
    'ImageResizeNN',
    'ImageResizeCanvas',
    'ImageMipmaps',
    'ImageDither',
    'ImageFlipVertical',
    'ImageFlipHorizontal',
    'ImageRotateCW',
    'ImageRotateCCW',
    'ImageColorTint',
    'ImageColorInvert',
    'ImageColorGrayscale',
    'ImageColorContrast',
    'ImageColorBrightness',
    'ImageColorReplace',
    'LoadImageColors',
    'LoadImagePalette',
    'UnloadImageColors',
    'UnloadImagePalette',
    'GetImageAlphaBorder',
    'GetImageColor',
    'ImageClearBackground',
    'ImageDrawPixel',
    'ImageDrawPixelV',
    'ImageDrawLine',
    'ImageDrawLineV',
    'ImageDrawCircle',
    'ImageDrawCircleV',
    'ImageDrawCircleLines',
    'ImageDrawCircleLinesV',
    'ImageDrawRectangle',
    'ImageDrawRectangleV',
    'ImageDrawRectangleRec',
    'ImageDrawRectangleLines',
    'ImageDraw',
    'ImageDrawText',
    'ImageDrawTextEx',
    'LoadTexture',
    'LoadTextureFromImage',
    'LoadTextureCubemap',
    'LoadRenderTexture',
    'IsTextureReady',
    'UnloadTexture',
    'IsRenderTextureReady',
    'UnloadRenderTexture',
    'UpdateTexture',
    'UpdateTextureRec',
    'GenTextureMipmaps',
    'SetTextureFilter',
    'SetTextureWrap',
    'DrawTexture',
    'DrawTextureV',
    'DrawTextureEx',
    'DrawTextureRec',
    'DrawTexturePro',
    'DrawTextureNPatch',
    'Fade',
    'ColorToInt',
    'ColorNormalize',
    'ColorFromNormalized',
    'ColorToHSV',
    'ColorFromHSV',
    'ColorTint',
    'ColorBrightness',
    'ColorContrast',
    'ColorAlpha',
    'ColorAlphaBlend',
    'GetColor',
    'GetPixelColor',
    'SetPixelColor',
    'GetPixelDataSize',
    'GetFontDefault',
    'LoadFont',
    'LoadFontEx',
    'LoadFontFromImage',
    'LoadFontFromMemory',
    'IsFontReady',
    'LoadFontData',
    'GenImageFontAtlas',
    'UnloadFontData',
    'UnloadFont',
    'ExportFontAsCode',
    'DrawFPS',
    'DrawText',
    'DrawTextEx',
    'DrawTextPro',
    'DrawTextCodepoint',
    'DrawTextCodepoints',
    'MeasureText',
    'MeasureTextEx',
    'GetGlyphIndex',
    'GetGlyphInfo',
    'GetGlyphAtlasRec',
    'LoadUTF8',
    'UnloadUTF8',
    'LoadCodepoints',
    'UnloadCodepoints',
    'GetCodepointCount',
    'GetCodepoint',
    'GetCodepointNext',
    'GetCodepointPrevious',
    'CodepointToUTF8',
    'TextCopy',
    'TextIsEqual',
    'TextLength',
    'TextFormat',
    'TextSubtext',
    'TextReplace',
    'TextInsert',
    'TextJoin',
    'TextSplit',
    'TextAppend',
    'TextFindIndex',
    'TextToUpper',
    'TextToLower',
    'TextToPascal',
    'TextToInteger',
    'DrawLine3D',
    'DrawPoint3D',
    'DrawCircle3D',
    'DrawTriangle3D',
    'DrawTriangleStrip3D',
    'DrawCube',
    'DrawCubeV',
    'DrawCubeWires',
    'DrawCubeWiresV',
    'DrawSphere',
    'DrawSphereEx',
    'DrawSphereWires',
    'DrawCylinder',
    'DrawCylinderEx',
    'DrawCylinderWires',
    'DrawCylinderWiresEx',
    'DrawCapsule',
    'DrawCapsuleWires',
    'DrawPlane',
    'DrawRay',
    'DrawGrid',
    'LoadModel',
    'LoadModelFromMesh',
    'IsModelReady',
    'UnloadModel',
    'GetModelBoundingBox',
    'DrawModel',
    'DrawModelEx',
    'DrawModelWires',
    'DrawModelWiresEx',
    'DrawBoundingBox',
    'DrawBillboard',
    'DrawBillboardRec',
    'DrawBillboardPro',
    'UploadMesh',
    'UpdateMeshBuffer',
    'UnloadMesh',
    'DrawMesh',
    'DrawMeshInstanced',
    'ExportMesh',
    'GetMeshBoundingBox',
    'GenMeshTangents',
    'GenMeshPoly',
    'GenMeshPlane',
    'GenMeshCube',
    'GenMeshSphere',
    'GenMeshHemiSphere',
    'GenMeshCylinder',
    'GenMeshCone',
    'GenMeshTorus',
    'GenMeshKnot',
    'GenMeshHeightmap',
    'GenMeshCubicmap',
    'LoadMaterials',
    'LoadMaterialDefault',
    'IsMaterialReady',
    'UnloadMaterial',
    'SetMaterialTexture',
    'SetModelMeshMaterial',
    'LoadModelAnimations',
    'UpdateModelAnimation',
    'UnloadModelAnimation',
    'UnloadModelAnimations',
    'IsModelAnimationValid',
    'CheckCollisionSpheres',
    'CheckCollisionBoxes',
    'CheckCollisionBoxSphere',
    'GetRayCollisionSphere',
    'GetRayCollisionBox',
    'GetRayCollisionMesh',
    'GetRayCollisionTriangle',
    'GetRayCollisionQuad',
    'InitAudioDevice',
    'CloseAudioDevice',
    'IsAudioDeviceReady',
    'SetMasterVolume',
    'LoadWave',
    'LoadWaveFromMemory',
    'IsWaveReady',
    'LoadSound',
    'LoadSoundFromWave',
    'IsSoundReady',
    'UpdateSound',
    'UnloadWave',
    'UnloadSound',
    'ExportWave',
    'ExportWaveAsCode',
    'PlaySound',
    'StopSound',
    'PauseSound',
    'ResumeSound',
    'IsSoundPlaying',
    'SetSoundVolume',
    'SetSoundPitch',
    'SetSoundPan',
    'WaveCopy',
    'WaveCrop',
    'WaveFormat',
    'LoadWaveSamples',
    'UnloadWaveSamples',
    'LoadMusicStream',
    'LoadMusicStreamFromMemory',
    'IsMusicReady',
    'UnloadMusicStream',
    'PlayMusicStream',
    'IsMusicStreamPlaying',
    'UpdateMusicStream',
    'StopMusicStream',
    'PauseMusicStream',
    'ResumeMusicStream',
    'SeekMusicStream',
    'SetMusicVolume',
    'SetMusicPitch',
    'SetMusicPan',
    'GetMusicTimeLength',
    'GetMusicTimePlayed',
    'LoadAudioStream',
    'IsAudioStreamReady',
    'UnloadAudioStream',
    'UpdateAudioStream',
    'IsAudioStreamProcessed',
    'PlayAudioStream',
    'PauseAudioStream',
    'ResumeAudioStream',
    'IsAudioStreamPlaying',
    'StopAudioStream',
    'SetAudioStreamVolume',
    'SetAudioStreamPitch',
    'SetAudioStreamPan',
    'SetAudioStreamBufferSizeDefault',
    'SetAudioStreamCallback',
    'AttachAudioStreamProcessor',
    'DetachAudioStreamProcessor',
    'AttachAudioMixedProcessor',
    'DetachAudioMixedProcessor',
#    'Drawing',
#    'ScissorMode',
#    'Mode2D',
#    'Mode3D',
#    'ShaderMode',
#    'TextureMode',
#    'VrStereoMode',
]

# region LIBRARY LOADING

# region CDLLEX

if sys.platform == 'win32':
    DONT_RESOLVE_DLL_REFERENCES = 0x00000001
    LOAD_LIBRARY_AS_DATAFILE = 0x00000002
    LOAD_WITH_ALTERED_SEARCH_PATH = 0x00000008
    LOAD_IGNORE_CODE_AUTHZ_LEVEL = 0x00000010  # NT 6.1
    LOAD_LIBRARY_AS_IMAGE_RESOURCE = 0x00000020  # NT 6.0
    LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE = 0x00000040  # NT 6.0

    # These cannot be combined with LOAD_WITH_ALTERED_SEARCH_PATH.
    # Install update KB2533623 for NT 6.0 & 6.1.
    LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR = 0x00000100
    LOAD_LIBRARY_SEARCH_APPLICATION_DIR = 0x00000200
    LOAD_LIBRARY_SEARCH_USER_DIRS = 0x00000400
    LOAD_LIBRARY_SEARCH_SYSTEM32 = 0x00000800
    LOAD_LIBRARY_SEARCH_DEFAULT_DIRS = 0x00001000

    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)


    def check_bool(result, func, args):
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return args


    kernel32.LoadLibraryExW.errcheck = check_bool
    kernel32.LoadLibraryExW.restype = wintypes.HMODULE
    kernel32.LoadLibraryExW.argtypes = (wintypes.LPCWSTR,
                                        wintypes.HANDLE,
                                        wintypes.DWORD)


    class CDLLEx(ctypes.CDLL):
        def __init__(self, name, mode=0, handle=None,
                    use_errno=True, use_last_error=False):
            if handle is None:
                handle = kernel32.LoadLibraryExW(name, None, mode)
            super(CDLLEx, self).__init__(name, mode, handle,
                                        use_errno, use_last_error)


    class WinDLLEx(ctypes.WinDLL):
        def __init__(self, name, mode=0, handle=None,
                    use_errno=False, use_last_error=True):
            if handle is None:
                handle = kernel32.LoadLibraryExW(name, None, mode)
            super(WinDLLEx, self).__init__(name, mode, handle,
                                        use_errno, use_last_error)


# endregion (cdllex)

# check for .raylib file in CWD

#
# example of .raylib file contents:
# ```json
# { 
#     "win32": {
#         "32bit": "path/to/raylib/filename.dll",
#         "64bit": "path/to/raylib/filename.dll",
#     },
#     "linux": {
#         "32bit": "path/to/raylib/filename.so",
#         "64bit": "path/to/raylib/filename.so",
#     },
#     "darwin": {
#         "64bit": "path/to/raylib/filename.dylib",
#     },
# }
# ```
#

_dotraylib_used = False
_dotraylib_loadinfo = None
_dotraylib = os.path.join(os.getcwd(), '.raylib')
_dotraylib_config = {}
if os.path.exists(_dotraylib) and os.path.isfile(_dotraylib):
    _dotraylib_used = True
    import json
    with open(_dotraylib, 'r', encoding='utf8') as fp:
        try:
            _dotraylib_config = json.load(fp)
        except json.JSONDecodeError:
            _dotraylib_loadinfo = "Could not decode .raylib file"
            _dotraylib_used = False

    del json

_lib_fname = {
    'win32': 'raylib.dll',
    'linux': 'libraylib.so',
    'darwin': 'libraylib.4.5.0.dylib'
}

_lib_platform = sys.platform

if _lib_platform == 'win32':
    _bitness = platform.architecture()[0]
elif _lib_platform == 'darwin':
    _bitness = '64bit'
else:
    _bitness = '64bit' if sys.maxsize > 2 ** 32 else '32bit'

_lib_default = os.path.join('../lib', 'bin', _bitness, _lib_fname[_lib_platform])

if _dotraylib_used:
    try:
        _lib_default = os.path.abspath(_dotraylib_config[_lib_platform][_bitness])

    except (KeyError, ValueError):
        _dotraylib_loadinfo = "Platform ({}) and bitness ({}) not specified in .raylib file".format(_lib_platform, _bitness)

_lib_fname_abspath = os.path.normcase(os.path.normpath(_lib_default))

_cwd_info = "\n    current working dir: {}".format(os.getcwd()) if _dotraylib_used else ""
_load_info = "\n    .raylib load info: {}".format(_dotraylib_loadinfo) if _dotraylib_loadinfo else ""

print(
    """Library loading info:
    platform: {}
    bitness: {}{}{}
    absolute path: {}
    using .raylib file: {}
    exists: {}
    is file: {}
    """.format(
        _lib_platform,
        _bitness,
        _cwd_info,
        _load_info,
        _lib_fname_abspath,
        'yes' if _dotraylib_used else 'no',
        'yes' if os.path.exists(_lib_fname_abspath) else 'no',
        'yes' if os.path.isfile(_lib_fname_abspath) else 'no'
    )
)

rlapi = None
if _lib_platform == 'win32':

    try:
        rlapi = CDLLEx(_lib_fname_abspath, LOAD_WITH_ALTERED_SEARCH_PATH)
    except OSError:
        print("Unable to load {}.".format(_lib_fname[_lib_platform]))
        rlapi = None
else:
    rlapi = CDLL(_lib_fname_abspath)

if rlapi is None:
    print("Failed to load shared library.")
    exit()
else:
    print("Shared library loaded succesfully.", rlapi)



Bool = c_bool
BoolPtr = POINTER(c_bool)
Byte = c_byte
BytePtr = POINTER(c_byte)
Char = c_char
CharPtr = POINTER(c_char)
Short = c_short
ShortPtr = POINTER(c_short)
Int = c_long
IntPtr = POINTER(c_long)
Long = c_long
LongPtr = POINTER(c_long)
LongLong = c_longlong
LongLongPtr = POINTER(c_longlong)
UChar = c_ubyte
UCharPtr = POINTER(c_ubyte)
UByte = c_ubyte
UBytePtr = POINTER(c_ubyte)
UShort = c_ushort
UShortPtr = POINTER(c_ushort)
UInt = c_ulong
UIntPtr = POINTER(c_ulong)
ULong = c_ulong
ULongPtr = POINTER(c_ulong)
ULongLong = c_ulonglong
ULongLongPtr = POINTER(c_ulonglong)
Float = c_float
FloatPtr = POINTER(c_float)
Double = c_double
DoublePtr = POINTER(c_double)
VoidPtr = c_void_p
VoidPtrPtr = POINTER(c_void_p)
CharPtr = c_char_p
CharPtrPtr = POINTER(c_char_p)


# Vector component swizzling helppers
_VEC2_GET_SWZL = re.compile(r'[xy]{,4}')
_VEC3_GET_SWZL = re.compile(r'[xyz]{,4}')
_VEC4_GET_SWZL = re.compile(r'[xyzw]{,4}')
_RGBA_GET_SWZL = re.compile(r'[rgba]{1,4}')
_RECT_GET_SWZL = re.compile(r'(width|height|[xywhcmrb]{,4})')

_VEC2_SET_SWZL = re.compile(r'[xy]{,2}')
_VEC3_SET_SWZL = re.compile(r'[xyz]{,3}')
_VEC4_SET_SWZL = re.compile(r'[xyzw]{,4}')
_RGBA_SET_SWZL = re.compile(r'[rgba]{1,4}')
_RECT_SET_SWZL = re.compile(r'(width|height|[xywhcmrb]{,4})')

# region FUNCTIONS


def _clsname(obj):
    return obj.__class__.__name__


def is_number(obj):
    return isinstance(obj, (int, float))


def is_component(value):
    return isinstance(value, int) and 0 <= value <= 255


def _clamp_rgba(*args):
    return tuple(value & 255 for value in args)


def _str_in(value):
    return value.encode('utf-8', 'ignore') if isinstance(value, str) else value


def _str_in2(values):
    return _arr_in(CharPtr, tuple(_str_in(value) for value in values))


def _str_out(value):
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


def _arr_in(typ, data):
    if isinstance(data, POINTER(typ)):
        return data
    return (typ * len(data))(*data)


def _arr2_in(typ, data):
    arr = typ * len(data[0])
    return (arr * len(data))(*data)


def _arr_out(data):
    return data.values


def _ptr_out(ptr, length=0):
    [ptr.contents] if length == 1 else ([] if not length else ptr[:length])

# region TYPE CAST FUNCS


def _float(value):
    return float(value)


def _int(value, ranged=None):
    if ranged:
        return max(ranged[0], min(int(value), ranged[1]))
    return int(value)


def _vec2(seq):
    if isinstance(seq, Vector2):
        return seq
    x, y = seq
    return Vector2(_float(x), _float(y))


def _vec3(seq):
    if isinstance(seq, Vector3):
        return seq
    x, y, z = seq
    return Vector3(float(x), float(y), float(z))


def _vec4(seq):
    if isinstance(seq, Vector4):
        return seq
    x, y, z, w = seq
    return Vector4(float(x), float(y), float(z), float(w))


def _rect(seq):
    if isinstance(seq, Rectangle):
        return seq
    x, y, w, h = seq
    return Rectangle(float(x), float(y), float(w), float(h))


def _color(seq):
    if isinstance(seq, Color):
        return seq
    r, g, b, q = seq
    rng = 0, 255
    return Color(_int(r, rng), _int(g, rng), _int(b, rng), _int(q, rng))

# endregion (type cast funcs)


def _wrap(api, argtypes, restype):
    api.argtypes = argtypes
    api.restype = restype
    return api

# endregion (functions)


# Struct not exposed in raylib.h
class rAudioBufferPtr(Structure):
    pass


# Struct not exposed in raylib.h
class rAudioProcessorPtr(Structure):
    pass



class Vector2(Structure):
    '''Vector2, 2 components'''
    _fields_ = [
        ('x', Float),
        ('y', Float),
    ]


    @classmethod
    def array_of(cls, vector2_sequence):
        '''Creates and returns an array of Vector2s'''
        arr = cls * len(vector2_sequence)
        return arr(*vector2_sequence)


    def __init__(self, x=None, y=None):
        '''Initializes this Vector2 struct'''
        super(Vector2, self).__init__(
            x or 0.0,
            y or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Vector2 instance'''
        return byref(self)


    def __len__(self):
        return 2

    def __getitem__(self, key):
        return (self.x, self.y).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC2_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector2 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC2_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector2 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector2, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector2, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector2's components'''
        return {'x': self.x, 'y': self.y}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector2's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))


    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Vector2{}".format(self.__str__())


# Pointer type to Vector2s
Vector2Ptr = POINTER(Vector2)



class Vector3(Structure):
    '''Vector3, 3 components'''
    _fields_ = [
        ('x', Float),
        ('y', Float),
        ('z', Float),
    ]


    @classmethod
    def array_of(cls, vector3_sequence):
        '''Creates and returns an array of Vector3s'''
        arr = cls * len(vector3_sequence)
        return arr(*vector3_sequence)


    def __init__(self, x=None, y=None, z=None):
        '''Initializes this Vector3 struct'''
        super(Vector3, self).__init__(
            x or 0.0,
            y or 0.0,
            z or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Vector3 instance'''
        return byref(self)


    def __len__(self):
        return 3

    def __getitem__(self, key):
        return (self.x, self.y, self.z).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC3_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector3 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC3_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector3 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector3, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector3, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector3's components'''
        return {'x': self.x, 'y': self.y, 'z': self.z}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector3's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.z = float(d.get('z', self.z))

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Vector3{}".format(self.__str__())


# Pointer type to Vector3s
Vector3Ptr = POINTER(Vector3)



class Vector4(Structure):
    '''Vector4, 4 components'''
    _fields_ = [
        ('x', Float),
        ('y', Float),
        ('z', Float),
        ('w', Float),
    ]


    @classmethod
    def array_of(cls, vector4_sequence):
        '''Creates and returns an array of Vector4s'''
        arr = cls * len(vector4_sequence)
        return arr(*vector4_sequence)


    def __init__(self, x=None, y=None, z=None, w=None):
        '''Initializes this Vector4 struct'''
        super(Vector4, self).__init__(
            x or 0.0,
            y or 0.0,
            z or 0.0,
            w or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Vector4 instance'''
        return byref(self)


    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self.x, self.y. self.z, self.w).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector4 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC4_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector4 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector4, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector4, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector4's components'''
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector4's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.z = float(d.get('z', self.z))
        self.w = float(d.get('w', self.w))


    def __str__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)

    def __repr__(self):
        return "Vector4{}".format(self.__str__())


# Pointer type to Vector4s
Vector4Ptr = POINTER(Vector4)


# Quaternion, 4 components (Vector4 alias)
Quaternion = Vector4
QuaternionPtr = Vector4Ptr

class Matrix(Structure):
    '''Matrix, 4x4 components, column major, OpenGL style, right-handed'''
    _fields_ = [
        ('m0', Float),
        ('m4', Float),
        ('m8', Float),
        ('m12', Float),
        ('m1', Float),
        ('m5', Float),
        ('m9', Float),
        ('m13', Float),
        ('m2', Float),
        ('m6', Float),
        ('m10', Float),
        ('m14', Float),
        ('m3', Float),
        ('m7', Float),
        ('m11', Float),
        ('m15', Float),
    ]


    @classmethod
    def array_of(cls, matrix_sequence):
        '''Creates and returns an array of Matrixs'''
        arr = cls * len(matrix_sequence)
        return arr(*matrix_sequence)


    def __init__(self, m0=None,
                 m4=None,
                 m8=None,
                 m12=None,
                 m1=None,
                 m5=None,
                 m9=None,
                 m13=None,
                 m2=None,
                 m6=None,
                 m10=None,
                 m14=None,
                 m3=None,
                 m7=None,
                 m11=None,
                 m15=None):
        '''Initializes this Matrix struct'''
        super(Matrix, self).__init__(
            m0 or 0.0,
            m4 or 0.0,
            m8 or 0.0,
            m12 or 0.0,
            m1 or 0.0,
            m5 or 0.0,
            m9 or 0.0,
            m13 or 0.0,
            m2 or 0.0,
            m6 or 0.0,
            m10 or 0.0,
            m14 or 0.0,
            m3 or 0.0,
            m7 or 0.0,
            m11 or 0.0,
            m15 or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Matrix instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Matrixs
MatrixPtr = POINTER(Matrix)



class Color(Structure):
    '''Color, 4 components, R8G8B8A8 (32bit)'''
    _fields_ = [
        ('r', UChar),
        ('g', UChar),
        ('b', UChar),
        ('a', UChar),
    ]


    @classmethod
    def array_of(cls, color_sequence):
        '''Creates and returns an array of Colors'''
        arr = cls * len(color_sequence)
        return arr(*color_sequence)


    def __init__(self, r=None, g=None, b=None, a=None):
        '''Initializes this Color struct'''
        super(Color, self).__init__(
            r or 0,
            g or 0,
            b or 0,
            a or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Color instance'''
        return byref(self)


    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self.r, self.g, self.b, self.a).__getitem__(key)

    def __getattr__(self, attr):
        m = _RGBA_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Color object does not have attribute '{}'.".format(attr))
        cls = {1: int, 4: Color}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _RGBA_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Color object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Color, self).__setattr__(attr, int(value))
        else:
            for i, ch in enumerate(attr):
                super(Color, self).__setattr__(ch, int(value[i]))

    def todict(self):
        '''Returns a dict mapping this Color's components'''
        return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Color's components'''
        self.r = int(d.get('r', self.r))
        self.g = int(d.get('g', self.g))
        self.b = int(d.get('b', self.b))
        self.a = int(d.get('a', self.a))


    def __str__(self):
        return "({: 3}, {: 3}, {: 3}, {: 3})".format(self.r, self.g, self.b, self.a)

    def __repr__(self):
        return "Color{}".format(self.__str__())


# Pointer type to Colors
ColorPtr = POINTER(Color)



class Rectangle(Structure):
    '''Rectangle, 4 components'''
    _fields_ = [
        ('x', Float),
        ('y', Float),
        ('width', Float),
        ('height', Float),
    ]


    @classmethod
    def array_of(cls, rectangle_sequence):
        '''Creates and returns an array of Rectangles'''
        arr = cls * len(rectangle_sequence)
        return arr(*rectangle_sequence)


    def __init__(self, x=None, y=None, width=None, height=None):
        '''Initializes this Rectangle struct'''
        super(Rectangle, self).__init__(
            x or 0.0,
            y or 0.0,
            width or 0.0,
            height or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Rectangle instance'''
        return byref(self)


    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self.x, self.y. self.width, self.height).__getitem__(key)

    def __getattr__(self, attr):
        m = _RECT_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Rectangle object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Rectangle}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _RECT_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Rectangle object does not have attribute '{}'.".format(attr))
        w = self.width
        h = self.height
        if attr in ('width', 'height') or len(attr) == 1:
            if attr == 'c':
                super(Rectangle, self).__setattr__('x', float(value - w * 0.5))
            elif attr == 'r':
                super(Rectangle, self).__setattr__('x', float(value - w))
            elif attr == 'm':
                super(Rectangle, self).__setattr__('y', float(value - h * 0.5))
            elif attr == 'b':
                super(Rectangle, self).__setattr__('y', float(value - h))
            else:
                super(Rectangle, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                if ch in 'xywh':
                    super(Rectangle, self).__setattr__(ch, float(value[i]))
                elif ch == 'c':
                    super(Rectangle, self).__setattr__('x', float(value[i] - w * 0.5))
                elif ch == 'r':
                    super(Rectangle, self).__setattr__('x', float(value[i] - w))
                elif ch == 'm':
                    super(Rectangle, self).__setattr__('y', float(value[i] - h * 0.5))
                elif ch == 'b':
                    super(Rectangle, self).__setattr__('y', float(value[i] - h))

    def todict(self):
        '''Returns a dict mapping this Rectangle's components'''
        return {'x': self.x, 'y': self.y, 'w': self.width, 'h': self.height,
                'c': self.x + self.width * 0.5, 'm': self.y + self.height * 0.5,
                'r': self.x + self.width, 'b': self.y + self.height}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Rectangle's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.width = float(d.get('w', self.width))
        self.height = float(d.get('h', self.height))


    def __str__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.width, self.height)

    def __repr__(self):
        return "Rectangle{}".format(self.__str__())


# Pointer type to Rectangles
RectanglePtr = POINTER(Rectangle)



class Image(Structure):
    '''Image, pixel data stored in CPU memory (RAM)'''
    _fields_ = [
        ('data', VoidPtr),
        ('width', Int),
        ('height', Int),
        ('mipmaps', Int),
        ('format', Int),
    ]


    @classmethod
    def array_of(cls, image_sequence):
        '''Creates and returns an array of Images'''
        arr = cls * len(image_sequence)
        return arr(*image_sequence)


    def __init__(self, data=None,
                 width=None,
                 height=None,
                 mipmaps=None,
                 format=None):
        '''Initializes this Image struct'''
        super(Image, self).__init__(
            data,
            width or 0,
            height or 0,
            mipmaps or 0,
            format or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Image instance'''
        return byref(self)



# Pointer type to Images
ImagePtr = POINTER(Image)



class Texture(Structure):
    '''Texture, tex data stored in GPU memory (VRAM)'''
    _fields_ = [
        ('id', UInt),
        ('width', Int),
        ('height', Int),
        ('mipmaps', Int),
        ('format', Int),
    ]


    @classmethod
    def array_of(cls, texture_sequence):
        '''Creates and returns an array of Textures'''
        arr = cls * len(texture_sequence)
        return arr(*texture_sequence)


    def __init__(self, id=None,
                 width=None,
                 height=None,
                 mipmaps=None,
                 format=None):
        '''Initializes this Texture struct'''
        super(Texture, self).__init__(
            id or 0,
            width or 0,
            height or 0,
            mipmaps or 0,
            format or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Texture instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Textures
TexturePtr = POINTER(Texture)


# Texture2D, same as Texture
Texture2D = Texture
Texture2DPtr = TexturePtr
# TextureCubemap, same as Texture
TextureCubemap = Texture
TextureCubemapPtr = TexturePtr

class RenderTexture(Structure):
    '''RenderTexture, fbo for texture rendering'''
    _fields_ = [
        ('id', UInt),
        ('texture', Texture),
        ('depth', Texture),
    ]


    @classmethod
    def array_of(cls, render_texture_sequence):
        '''Creates and returns an array of RenderTextures'''
        arr = cls * len(render_texture_sequence)
        return arr(*render_texture_sequence)


    def __init__(self, id=None, texture=None, depth=None):
        '''Initializes this RenderTexture struct'''
        super(RenderTexture, self).__init__(
            id or 0,
            texture or Texture(),
            depth or Texture()
        )


    @property
    def byref(self):
        '''Gets a reference to this RenderTexture instance'''
        return byref(self)



# Pointer type to RenderTextures
RenderTexturePtr = POINTER(RenderTexture)


# RenderTexture2D, same as RenderTexture
RenderTexture2D = RenderTexture
RenderTexture2DPtr = RenderTexturePtr

class NPatchInfo(Structure):
    '''NPatchInfo, n-patch layout info'''
    _fields_ = [
        ('source', Rectangle),
        ('left', Int),
        ('top', Int),
        ('right', Int),
        ('bottom', Int),
        ('layout', Int),
    ]


    @classmethod
    def array_of(cls, npatch_info_sequence):
        '''Creates and returns an array of NPatchInfos'''
        arr = cls * len(npatch_info_sequence)
        return arr(*npatch_info_sequence)


    def __init__(self, source=None,
                 left=None,
                 top=None,
                 right=None,
                 bottom=None,
                 layout=None):
        '''Initializes this NPatchInfo struct'''
        super(NPatchInfo, self).__init__(
            source or Rectangle(),
            left or 0,
            top or 0,
            right or 0,
            bottom or 0,
            layout or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this NPatchInfo instance'''
        return byref(self)



# Pointer type to NPatchInfos
NPatchInfoPtr = POINTER(NPatchInfo)



class GlyphInfo(Structure):
    '''GlyphInfo, font characters glyphs info'''
    _fields_ = [
        ('value', Int),
        ('offsetX', Int),
        ('offsetY', Int),
        ('advanceX', Int),
        ('image', Image),
    ]


    @classmethod
    def array_of(cls, glyph_info_sequence):
        '''Creates and returns an array of GlyphInfos'''
        arr = cls * len(glyph_info_sequence)
        return arr(*glyph_info_sequence)


    def __init__(self, value=None,
                 offsetX=None,
                 offsetY=None,
                 advanceX=None,
                 image=None):
        '''Initializes this GlyphInfo struct'''
        super(GlyphInfo, self).__init__(
            value or 0,
            offsetX or 0,
            offsetY or 0,
            advanceX or 0,
            image or Image()
        )


    @property
    def byref(self):
        '''Gets a reference to this GlyphInfo instance'''
        return byref(self)



# Pointer type to GlyphInfos
GlyphInfoPtr = POINTER(GlyphInfo)



class Font(Structure):
    '''Font, font texture and GlyphInfo array data'''
    _fields_ = [
        ('baseSize', Int),
        ('glyphCount', Int),
        ('glyphPadding', Int),
        ('texture', Texture2D),
        ('recs', RectanglePtr),
        ('glyphs', GlyphInfoPtr),
    ]


    @classmethod
    def array_of(cls, font_sequence):
        '''Creates and returns an array of Fonts'''
        arr = cls * len(font_sequence)
        return arr(*font_sequence)


    def __init__(self, baseSize=None,
                 glyphCount=None,
                 glyphPadding=None,
                 texture=None,
                 recs=None,
                 glyphs=None):
        '''Initializes this Font struct'''
        super(Font, self).__init__(
            baseSize or 0,
            glyphCount or 0,
            glyphPadding or 0,
            texture or Texture2D(),
            recs,
            glyphs
        )


    @property
    def byref(self):
        '''Gets a reference to this Font instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Fonts
FontPtr = POINTER(Font)



class Camera3D(Structure):
    '''Camera, defines position/orientation in 3d space'''
    _fields_ = [
        ('position', Vector3),
        ('target', Vector3),
        ('up', Vector3),
        ('fovy', Float),
        ('projection', Int),
    ]


    @classmethod
    def array_of(cls, camera3d_sequence):
        '''Creates and returns an array of Camera3Ds'''
        arr = cls * len(camera3d_sequence)
        return arr(*camera3d_sequence)


    def __init__(self, position=None,
                 target=None,
                 up=None,
                 fovy=None,
                 projection=None):
        '''Initializes this Camera3D struct'''
        super(Camera3D, self).__init__(
            position or Vector3(),
            target or Vector3(),
            up or Vector3(),
            fovy or 0.0,
            projection or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Camera3D instance'''
        return byref(self)



# Pointer type to Camera3Ds
Camera3DPtr = POINTER(Camera3D)


# Camera type fallback, defaults to Camera3D
Camera = Camera3D
CameraPtr = Camera3DPtr

class Camera2D(Structure):
    '''Camera2D, defines position/orientation in 2d space'''
    _fields_ = [
        ('offset', Vector2),
        ('target', Vector2),
        ('rotation', Float),
        ('zoom', Float),
    ]


    @classmethod
    def array_of(cls, camera2d_sequence):
        '''Creates and returns an array of Camera2Ds'''
        arr = cls * len(camera2d_sequence)
        return arr(*camera2d_sequence)


    def __init__(self, offset=None, target=None, rotation=None, zoom=None):
        '''Initializes this Camera2D struct'''
        super(Camera2D, self).__init__(
            offset or Vector2(),
            target or Vector2(),
            rotation or 0.0,
            zoom or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Camera2D instance'''
        return byref(self)



# Pointer type to Camera2Ds
Camera2DPtr = POINTER(Camera2D)



class Mesh(Structure):
    '''Mesh, vertex data and vao/vbo'''
    _fields_ = [
        ('vertexCount', Int),
        ('triangleCount', Int),
        ('vertices', FloatPtr),
        ('texcoords', FloatPtr),
        ('texcoords2', FloatPtr),
        ('normals', FloatPtr),
        ('tangents', FloatPtr),
        ('colors', UCharPtr),
        ('indices', UShortPtr),
        ('animVertices', FloatPtr),
        ('animNormals', FloatPtr),
        ('boneIds', UCharPtr),
        ('boneWeights', FloatPtr),
        ('vaoId', UInt),
        ('vboId', UIntPtr),
    ]


    @classmethod
    def array_of(cls, mesh_sequence):
        '''Creates and returns an array of Meshs'''
        arr = cls * len(mesh_sequence)
        return arr(*mesh_sequence)


    def __init__(self, vertexCount=None,
                 triangleCount=None,
                 vertices=None,
                 texcoords=None,
                 texcoords2=None,
                 normals=None,
                 tangents=None,
                 colors=None,
                 indices=None,
                 animVertices=None,
                 animNormals=None,
                 boneIds=None,
                 boneWeights=None,
                 vaoId=None,
                 vboId=None):
        '''Initializes this Mesh struct'''
        super(Mesh, self).__init__(
            vertexCount or 0,
            triangleCount or 0,
            vertices,
            texcoords,
            texcoords2,
            normals,
            tangents,
            colors,
            indices,
            animVertices,
            animNormals,
            boneIds,
            boneWeights,
            vaoId or 0,
            vboId
        )


    @property
    def byref(self):
        '''Gets a reference to this Mesh instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Meshs
MeshPtr = POINTER(Mesh)



class Shader(Structure):
    '''Shader'''
    _fields_ = [
        ('id', UInt),
        ('locs', IntPtr),
    ]


    @classmethod
    def array_of(cls, shader_sequence):
        '''Creates and returns an array of Shaders'''
        arr = cls * len(shader_sequence)
        return arr(*shader_sequence)


    def __init__(self, id=None, locs=None):
        '''Initializes this Shader struct'''
        super(Shader, self).__init__(
            id or 0,
            locs
        )


    @property
    def byref(self):
        '''Gets a reference to this Shader instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Shaders
ShaderPtr = POINTER(Shader)



class MaterialMap(Structure):
    '''MaterialMap'''
    _fields_ = [
        ('texture', Texture2D),
        ('color', Color),
        ('value', Float),
    ]


    @classmethod
    def array_of(cls, material_map_sequence):
        '''Creates and returns an array of MaterialMaps'''
        arr = cls * len(material_map_sequence)
        return arr(*material_map_sequence)


    def __init__(self, texture=None, color=None, value=None):
        '''Initializes this MaterialMap struct'''
        super(MaterialMap, self).__init__(
            texture or Texture2D(),
            color or Color(),
            value or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this MaterialMap instance'''
        return byref(self)



# Pointer type to MaterialMaps
MaterialMapPtr = POINTER(MaterialMap)



class Material(Structure):
    '''Material, includes shader and maps'''
    _fields_ = [
        ('shader', Shader),
        ('maps', MaterialMapPtr),
        ('params', Float * 4),
    ]


    @classmethod
    def array_of(cls, material_sequence):
        '''Creates and returns an array of Materials'''
        arr = cls * len(material_sequence)
        return arr(*material_sequence)


    def __init__(self, shader=None, maps=None, params=None):
        '''Initializes this Material struct'''
        super(Material, self).__init__(
            shader or Shader(),
            maps,
            params
        )


    @property
    def byref(self):
        '''Gets a reference to this Material instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Materials
MaterialPtr = POINTER(Material)



class Transform(Structure):
    '''Transform, vertex transformation data'''
    _fields_ = [
        ('translation', Vector3),
        ('rotation', Quaternion),
        ('scale', Vector3),
    ]


    @classmethod
    def array_of(cls, transform_sequence):
        '''Creates and returns an array of Transforms'''
        arr = cls * len(transform_sequence)
        return arr(*transform_sequence)


    def __init__(self, translation=None, rotation=None, scale=None):
        '''Initializes this Transform struct'''
        super(Transform, self).__init__(
            translation or Vector3(),
            rotation or Quaternion(),
            scale or Vector3()
        )


    @property
    def byref(self):
        '''Gets a reference to this Transform instance'''
        return byref(self)



# Pointer type to Transforms
TransformPtr = POINTER(Transform)



class BoneInfo(Structure):
    '''Bone, skeletal animation bone'''
    _fields_ = [
        ('name', CharPtr),
        ('parent', Int),
    ]


    @classmethod
    def array_of(cls, bone_info_sequence):
        '''Creates and returns an array of BoneInfos'''
        arr = cls * len(bone_info_sequence)
        return arr(*bone_info_sequence)


    def __init__(self, name=None, parent=None):
        '''Initializes this BoneInfo struct'''
        super(BoneInfo, self).__init__(
            name,
            parent or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this BoneInfo instance'''
        return byref(self)



# Pointer type to BoneInfos
BoneInfoPtr = POINTER(BoneInfo)



class Model(Structure):
    '''Model, meshes, materials and animation data'''
    _fields_ = [
        ('transform', Matrix),
        ('meshCount', Int),
        ('materialCount', Int),
        ('meshes', MeshPtr),
        ('materials', MaterialPtr),
        ('meshMaterial', IntPtr),
        ('boneCount', Int),
        ('bones', BoneInfoPtr),
        ('bindPose', TransformPtr),
    ]


    @classmethod
    def array_of(cls, model_sequence):
        '''Creates and returns an array of Models'''
        arr = cls * len(model_sequence)
        return arr(*model_sequence)


    def __init__(self, transform=None,
                 meshCount=None,
                 materialCount=None,
                 meshes=None,
                 materials=None,
                 meshMaterial=None,
                 boneCount=None,
                 bones=None,
                 bindPose=None):
        '''Initializes this Model struct'''
        super(Model, self).__init__(
            transform or Matrix(),
            meshCount or 0,
            materialCount or 0,
            meshes,
            materials,
            meshMaterial,
            boneCount or 0,
            bones,
            bindPose
        )


    @property
    def byref(self):
        '''Gets a reference to this Model instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Models
ModelPtr = POINTER(Model)



class ModelAnimation(Structure):
    '''ModelAnimation'''
    _fields_ = [
        ('boneCount', Int),
        ('frameCount', Int),
        ('bones', BoneInfoPtr),
        ('framePoses', TransformPtr),
    ]


    @classmethod
    def array_of(cls, model_animation_sequence):
        '''Creates and returns an array of ModelAnimations'''
        arr = cls * len(model_animation_sequence)
        return arr(*model_animation_sequence)


    def __init__(self, boneCount=None, frameCount=None, bones=None, framePoses=None):
        '''Initializes this ModelAnimation struct'''
        super(ModelAnimation, self).__init__(
            boneCount or 0,
            frameCount or 0,
            bones,
            framePoses
        )


    @property
    def byref(self):
        '''Gets a reference to this ModelAnimation instance'''
        return byref(self)



# Pointer type to ModelAnimations
ModelAnimationPtr = POINTER(ModelAnimation)



class Ray(Structure):
    '''Ray, ray for raycasting'''
    _fields_ = [
        ('position', Vector3),
        ('direction', Vector3),
    ]


    @classmethod
    def array_of(cls, ray_sequence):
        '''Creates and returns an array of Rays'''
        arr = cls * len(ray_sequence)
        return arr(*ray_sequence)


    def __init__(self, position=None, direction=None):
        '''Initializes this Ray struct'''
        super(Ray, self).__init__(
            position or Vector3(),
            direction or Vector3()
        )


    @property
    def byref(self):
        '''Gets a reference to this Ray instance'''
        return byref(self)



# Pointer type to Rays
RayPtr = POINTER(Ray)



class RayCollision(Structure):
    '''RayCollision, ray hit information'''
    _fields_ = [
        ('hit', Bool),
        ('distance', Float),
        ('point', Vector3),
        ('normal', Vector3),
    ]


    @classmethod
    def array_of(cls, ray_collision_sequence):
        '''Creates and returns an array of RayCollisions'''
        arr = cls * len(ray_collision_sequence)
        return arr(*ray_collision_sequence)


    def __init__(self, hit=None, distance=None, point=None, normal=None):
        '''Initializes this RayCollision struct'''
        super(RayCollision, self).__init__(
            hit or False,
            distance or 0.0,
            point or Vector3(),
            normal or Vector3()
        )


    @property
    def byref(self):
        '''Gets a reference to this RayCollision instance'''
        return byref(self)



# Pointer type to RayCollisions
RayCollisionPtr = POINTER(RayCollision)



class BoundingBox(Structure):
    '''BoundingBox'''
    _fields_ = [
        ('min', Vector3),
        ('max', Vector3),
    ]


    @classmethod
    def array_of(cls, bounding_box_sequence):
        '''Creates and returns an array of BoundingBoxs'''
        arr = cls * len(bounding_box_sequence)
        return arr(*bounding_box_sequence)


    def __init__(self, min=None, max=None):
        '''Initializes this BoundingBox struct'''
        super(BoundingBox, self).__init__(
            min or Vector3(),
            max or Vector3()
        )


    @property
    def byref(self):
        '''Gets a reference to this BoundingBox instance'''
        return byref(self)



# Pointer type to BoundingBoxs
BoundingBoxPtr = POINTER(BoundingBox)



class Wave(Structure):
    '''Wave, audio wave data'''
    _fields_ = [
        ('frameCount', UInt),
        ('sampleRate', UInt),
        ('sampleSize', UInt),
        ('channels', UInt),
        ('data', VoidPtr),
    ]


    @classmethod
    def array_of(cls, wave_sequence):
        '''Creates and returns an array of Waves'''
        arr = cls * len(wave_sequence)
        return arr(*wave_sequence)


    def __init__(self, frameCount=None,
                 sampleRate=None,
                 sampleSize=None,
                 channels=None,
                 data=None):
        '''Initializes this Wave struct'''
        super(Wave, self).__init__(
            frameCount or 0,
            sampleRate or 0,
            sampleSize or 0,
            channels or 0,
            data
        )


    @property
    def byref(self):
        '''Gets a reference to this Wave instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Waves
WavePtr = POINTER(Wave)



class AudioStream(Structure):
    '''AudioStream, custom audio stream'''
    _fields_ = [
        ('buffer', rAudioBufferPtr),
        ('processor', rAudioProcessorPtr),
        ('sampleRate', UInt),
        ('sampleSize', UInt),
        ('channels', UInt),
    ]


    @classmethod
    def array_of(cls, audio_stream_sequence):
        '''Creates and returns an array of AudioStreams'''
        arr = cls * len(audio_stream_sequence)
        return arr(*audio_stream_sequence)


    def __init__(self, buffer=None,
                 processor=None,
                 sampleRate=None,
                 sampleSize=None,
                 channels=None):
        '''Initializes this AudioStream struct'''
        super(AudioStream, self).__init__(
            buffer,
            processor,
            sampleRate or 0,
            sampleSize or 0,
            channels or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this AudioStream instance'''
        return byref(self)


    def __str__(self):
        return "[{} Playing: {}]".format(self.__class__.__name__, _IsAudioStreamPlaying(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to AudioStreams
AudioStreamPtr = POINTER(AudioStream)



class Sound(Structure):
    '''Sound'''
    _fields_ = [
        ('stream', AudioStream),
        ('frameCount', UInt),
    ]


    @classmethod
    def array_of(cls, sound_sequence):
        '''Creates and returns an array of Sounds'''
        arr = cls * len(sound_sequence)
        return arr(*sound_sequence)


    def __init__(self, stream=None, frameCount=None):
        '''Initializes this Sound struct'''
        super(Sound, self).__init__(
            stream or AudioStream(),
            frameCount or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Sound instance'''
        return byref(self)


    def __str__(self):
        return "[{} Playing: {}]".format(self.__class__.__name__, _IsSoundPlaying(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Sounds
SoundPtr = POINTER(Sound)



class Music(Structure):
    '''Music, audio stream, anything longer than ~10 seconds should be streamed'''
    _fields_ = [
        ('stream', AudioStream),
        ('frameCount', UInt),
        ('looping', Bool),
        ('ctxType', Int),
        ('ctxData', VoidPtr),
    ]


    @classmethod
    def array_of(cls, music_sequence):
        '''Creates and returns an array of Musics'''
        arr = cls * len(music_sequence)
        return arr(*music_sequence)


    def __init__(self, stream=None,
                 frameCount=None,
                 looping=None,
                 ctxType=None,
                 ctxData=None):
        '''Initializes this Music struct'''
        super(Music, self).__init__(
            stream or AudioStream(),
            frameCount or 0,
            looping or False,
            ctxType or 0,
            ctxData
        )


    @property
    def byref(self):
        '''Gets a reference to this Music instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()


# Pointer type to Musics
MusicPtr = POINTER(Music)



class VrDeviceInfo(Structure):
    '''VrDeviceInfo, Head-Mounted-Display device parameters'''
    _fields_ = [
        ('hResolution', Int),
        ('vResolution', Int),
        ('hScreenSize', Float),
        ('vScreenSize', Float),
        ('vScreenCenter', Float),
        ('eyeToScreenDistance', Float),
        ('lensSeparationDistance', Float),
        ('interpupillaryDistance', Float),
        ('lensDistortionValues', Float * 4),
        ('chromaAbCorrection', Float * 4),
    ]


    @classmethod
    def array_of(cls, vr_device_info_sequence):
        '''Creates and returns an array of VrDeviceInfos'''
        arr = cls * len(vr_device_info_sequence)
        return arr(*vr_device_info_sequence)


    def __init__(self, hResolution=None,
                 vResolution=None,
                 hScreenSize=None,
                 vScreenSize=None,
                 vScreenCenter=None,
                 eyeToScreenDistance=None,
                 lensSeparationDistance=None,
                 interpupillaryDistance=None,
                 lensDistortionValues=None,
                 chromaAbCorrection=None):
        '''Initializes this VrDeviceInfo struct'''
        super(VrDeviceInfo, self).__init__(
            hResolution or 0,
            vResolution or 0,
            hScreenSize or 0.0,
            vScreenSize or 0.0,
            vScreenCenter or 0.0,
            eyeToScreenDistance or 0.0,
            lensSeparationDistance or 0.0,
            interpupillaryDistance or 0.0,
            lensDistortionValues,
            chromaAbCorrection
        )


    @property
    def byref(self):
        '''Gets a reference to this VrDeviceInfo instance'''
        return byref(self)



# Pointer type to VrDeviceInfos
VrDeviceInfoPtr = POINTER(VrDeviceInfo)



class VrStereoConfig(Structure):
    '''VrStereoConfig, VR stereo rendering configuration for simulator'''
    _fields_ = [
        ('projection', Matrix * 2),
        ('viewOffset', Matrix * 2),
        ('leftLensCenter', Float * 2),
        ('rightLensCenter', Float * 2),
        ('leftScreenCenter', Float * 2),
        ('rightScreenCenter', Float * 2),
        ('scale', Float * 2),
        ('scaleIn', Float * 2),
    ]


    @classmethod
    def array_of(cls, vr_stereo_config_sequence):
        '''Creates and returns an array of VrStereoConfigs'''
        arr = cls * len(vr_stereo_config_sequence)
        return arr(*vr_stereo_config_sequence)


    def __init__(self, projection=None,
                 viewOffset=None,
                 leftLensCenter=None,
                 rightLensCenter=None,
                 leftScreenCenter=None,
                 rightScreenCenter=None,
                 scale=None,
                 scaleIn=None):
        '''Initializes this VrStereoConfig struct'''
        super(VrStereoConfig, self).__init__(
            projection,
            viewOffset,
            leftLensCenter,
            rightLensCenter,
            leftScreenCenter,
            rightScreenCenter,
            scale,
            scaleIn
        )


    @property
    def byref(self):
        '''Gets a reference to this VrStereoConfig instance'''
        return byref(self)



# Pointer type to VrStereoConfigs
VrStereoConfigPtr = POINTER(VrStereoConfig)



class FilePathList(Structure):
    '''File path list'''
    _fields_ = [
        ('capacity', UInt),
        ('count', UInt),
        ('paths', CharPtrPtr),
    ]


    @classmethod
    def array_of(cls, file_path_list_sequence):
        '''Creates and returns an array of FilePathLists'''
        arr = cls * len(file_path_list_sequence)
        return arr(*file_path_list_sequence)


    def __init__(self, capacity=None, count=None, paths=None):
        '''Initializes this FilePathList struct'''
        super(FilePathList, self).__init__(
            capacity or 0,
            count or 0,
            paths
        )


    @property
    def byref(self):
        '''Gets a reference to this FilePathList instance'''
        return byref(self)



# Pointer type to FilePathLists
FilePathListPtr = POINTER(FilePathList)


class ConfigFlags(IntEnum):
    """System/Window config flags"""

    FLAG_VSYNC_HINT = 64
    """Set to try enabling V-Sync on GPU"""

    FLAG_FULLSCREEN_MODE = 2
    """Set to run program in fullscreen"""

    FLAG_WINDOW_RESIZABLE = 4
    """Set to allow resizable window"""

    FLAG_WINDOW_UNDECORATED = 8
    """Set to disable window decoration (frame and buttons)"""

    FLAG_WINDOW_HIDDEN = 128
    """Set to hide window"""

    FLAG_WINDOW_MINIMIZED = 512
    """Set to minimize window (iconify)"""

    FLAG_WINDOW_MAXIMIZED = 1024
    """Set to maximize window (expanded to monitor)"""

    FLAG_WINDOW_UNFOCUSED = 2048
    """Set to window non focused"""

    FLAG_WINDOW_TOPMOST = 4096
    """Set to window always on top"""

    FLAG_WINDOW_ALWAYS_RUN = 256
    """Set to allow windows running while minimized"""

    FLAG_WINDOW_TRANSPARENT = 16
    """Set to allow transparent framebuffer"""

    FLAG_WINDOW_HIGHDPI = 8192
    """Set to support HighDPI"""

    FLAG_WINDOW_MOUSE_PASSTHROUGH = 16384
    """Set to support mouse passthrough, only supported when FLAG_WINDOW_UNDECORATED"""

    FLAG_MSAA_4X_HINT = 32
    """Set to try enabling MSAA 4X"""

    FLAG_INTERLACED_HINT = 65536
    """Set to try enabling interlaced video format (for V3D)"""



FLAG_VSYNC_HINT = ConfigFlags.FLAG_VSYNC_HINT
FLAG_FULLSCREEN_MODE = ConfigFlags.FLAG_FULLSCREEN_MODE
FLAG_WINDOW_RESIZABLE = ConfigFlags.FLAG_WINDOW_RESIZABLE
FLAG_WINDOW_UNDECORATED = ConfigFlags.FLAG_WINDOW_UNDECORATED
FLAG_WINDOW_HIDDEN = ConfigFlags.FLAG_WINDOW_HIDDEN
FLAG_WINDOW_MINIMIZED = ConfigFlags.FLAG_WINDOW_MINIMIZED
FLAG_WINDOW_MAXIMIZED = ConfigFlags.FLAG_WINDOW_MAXIMIZED
FLAG_WINDOW_UNFOCUSED = ConfigFlags.FLAG_WINDOW_UNFOCUSED
FLAG_WINDOW_TOPMOST = ConfigFlags.FLAG_WINDOW_TOPMOST
FLAG_WINDOW_ALWAYS_RUN = ConfigFlags.FLAG_WINDOW_ALWAYS_RUN
FLAG_WINDOW_TRANSPARENT = ConfigFlags.FLAG_WINDOW_TRANSPARENT
FLAG_WINDOW_HIGHDPI = ConfigFlags.FLAG_WINDOW_HIGHDPI
FLAG_WINDOW_MOUSE_PASSTHROUGH = ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH
FLAG_MSAA_4X_HINT = ConfigFlags.FLAG_MSAA_4X_HINT
FLAG_INTERLACED_HINT = ConfigFlags.FLAG_INTERLACED_HINT


class TraceLogLevel(IntEnum):
    """Trace log level"""

    LOG_ALL = 0
    """Display all logs"""

    LOG_TRACE = 1
    """Trace logging, intended for internal use only"""

    LOG_DEBUG = 2
    """Debug logging, used for internal debugging, it should be disabled on release builds"""

    LOG_INFO = 3
    """Info logging, used for program execution info"""

    LOG_WARNING = 4
    """Warning logging, used on recoverable failures"""

    LOG_ERROR = 5
    """Error logging, used on unrecoverable failures"""

    LOG_FATAL = 6
    """Fatal logging, used to abort program: exit(EXIT_FAILURE)"""

    LOG_NONE = 7
    """Disable logging"""



LOG_ALL = TraceLogLevel.LOG_ALL
LOG_TRACE = TraceLogLevel.LOG_TRACE
LOG_DEBUG = TraceLogLevel.LOG_DEBUG
LOG_INFO = TraceLogLevel.LOG_INFO
LOG_WARNING = TraceLogLevel.LOG_WARNING
LOG_ERROR = TraceLogLevel.LOG_ERROR
LOG_FATAL = TraceLogLevel.LOG_FATAL
LOG_NONE = TraceLogLevel.LOG_NONE


class KeyboardKey(IntEnum):
    """Keyboard keys (US keyboard layout)"""

    KEY_NULL = 0
    """Key: NULL, used for no key pressed"""

    KEY_APOSTROPHE = 39
    """Key: '"""

    KEY_COMMA = 44
    """Key: ,"""

    KEY_MINUS = 45
    """Key: -"""

    KEY_PERIOD = 46
    """Key: ."""

    KEY_SLASH = 47
    """Key: /"""

    KEY_ZERO = 48
    """Key: 0"""

    KEY_ONE = 49
    """Key: 1"""

    KEY_TWO = 50
    """Key: 2"""

    KEY_THREE = 51
    """Key: 3"""

    KEY_FOUR = 52
    """Key: 4"""

    KEY_FIVE = 53
    """Key: 5"""

    KEY_SIX = 54
    """Key: 6"""

    KEY_SEVEN = 55
    """Key: 7"""

    KEY_EIGHT = 56
    """Key: 8"""

    KEY_NINE = 57
    """Key: 9"""

    KEY_SEMICOLON = 59
    """Key: ;"""

    KEY_EQUAL = 61
    """Key: ="""

    KEY_A = 65
    """Key: A | a"""

    KEY_B = 66
    """Key: B | b"""

    KEY_C = 67
    """Key: C | c"""

    KEY_D = 68
    """Key: D | d"""

    KEY_E = 69
    """Key: E | e"""

    KEY_F = 70
    """Key: F | f"""

    KEY_G = 71
    """Key: G | g"""

    KEY_H = 72
    """Key: H | h"""

    KEY_I = 73
    """Key: I | i"""

    KEY_J = 74
    """Key: J | j"""

    KEY_K = 75
    """Key: K | k"""

    KEY_L = 76
    """Key: L | l"""

    KEY_M = 77
    """Key: M | m"""

    KEY_N = 78
    """Key: N | n"""

    KEY_O = 79
    """Key: O | o"""

    KEY_P = 80
    """Key: P | p"""

    KEY_Q = 81
    """Key: Q | q"""

    KEY_R = 82
    """Key: R | r"""

    KEY_S = 83
    """Key: S | s"""

    KEY_T = 84
    """Key: T | t"""

    KEY_U = 85
    """Key: U | u"""

    KEY_V = 86
    """Key: V | v"""

    KEY_W = 87
    """Key: W | w"""

    KEY_X = 88
    """Key: X | x"""

    KEY_Y = 89
    """Key: Y | y"""

    KEY_Z = 90
    """Key: Z | z"""

    KEY_LEFT_BRACKET = 91
    """Key: ["""

    KEY_BACKSLASH = 92
    """Key: '\'"""

    KEY_RIGHT_BRACKET = 93
    """Key: ]"""

    KEY_GRAVE = 96
    """Key: `"""

    KEY_SPACE = 32
    """Key: Space"""

    KEY_ESCAPE = 256
    """Key: Esc"""

    KEY_ENTER = 257
    """Key: Enter"""

    KEY_TAB = 258
    """Key: Tab"""

    KEY_BACKSPACE = 259
    """Key: Backspace"""

    KEY_INSERT = 260
    """Key: Ins"""

    KEY_DELETE = 261
    """Key: Del"""

    KEY_RIGHT = 262
    """Key: Cursor right"""

    KEY_LEFT = 263
    """Key: Cursor left"""

    KEY_DOWN = 264
    """Key: Cursor down"""

    KEY_UP = 265
    """Key: Cursor up"""

    KEY_PAGE_UP = 266
    """Key: Page up"""

    KEY_PAGE_DOWN = 267
    """Key: Page down"""

    KEY_HOME = 268
    """Key: Home"""

    KEY_END = 269
    """Key: End"""

    KEY_CAPS_LOCK = 280
    """Key: Caps lock"""

    KEY_SCROLL_LOCK = 281
    """Key: Scroll down"""

    KEY_NUM_LOCK = 282
    """Key: Num lock"""

    KEY_PRINT_SCREEN = 283
    """Key: Print screen"""

    KEY_PAUSE = 284
    """Key: Pause"""

    KEY_F1 = 290
    """Key: F1"""

    KEY_F2 = 291
    """Key: F2"""

    KEY_F3 = 292
    """Key: F3"""

    KEY_F4 = 293
    """Key: F4"""

    KEY_F5 = 294
    """Key: F5"""

    KEY_F6 = 295
    """Key: F6"""

    KEY_F7 = 296
    """Key: F7"""

    KEY_F8 = 297
    """Key: F8"""

    KEY_F9 = 298
    """Key: F9"""

    KEY_F10 = 299
    """Key: F10"""

    KEY_F11 = 300
    """Key: F11"""

    KEY_F12 = 301
    """Key: F12"""

    KEY_LEFT_SHIFT = 340
    """Key: Shift left"""

    KEY_LEFT_CONTROL = 341
    """Key: Control left"""

    KEY_LEFT_ALT = 342
    """Key: Alt left"""

    KEY_LEFT_SUPER = 343
    """Key: Super left"""

    KEY_RIGHT_SHIFT = 344
    """Key: Shift right"""

    KEY_RIGHT_CONTROL = 345
    """Key: Control right"""

    KEY_RIGHT_ALT = 346
    """Key: Alt right"""

    KEY_RIGHT_SUPER = 347
    """Key: Super right"""

    KEY_KB_MENU = 348
    """Key: KB menu"""

    KEY_KP_0 = 320
    """Key: Keypad 0"""

    KEY_KP_1 = 321
    """Key: Keypad 1"""

    KEY_KP_2 = 322
    """Key: Keypad 2"""

    KEY_KP_3 = 323
    """Key: Keypad 3"""

    KEY_KP_4 = 324
    """Key: Keypad 4"""

    KEY_KP_5 = 325
    """Key: Keypad 5"""

    KEY_KP_6 = 326
    """Key: Keypad 6"""

    KEY_KP_7 = 327
    """Key: Keypad 7"""

    KEY_KP_8 = 328
    """Key: Keypad 8"""

    KEY_KP_9 = 329
    """Key: Keypad 9"""

    KEY_KP_DECIMAL = 330
    """Key: Keypad ."""

    KEY_KP_DIVIDE = 331
    """Key: Keypad /"""

    KEY_KP_MULTIPLY = 332
    """Key: Keypad *"""

    KEY_KP_SUBTRACT = 333
    """Key: Keypad -"""

    KEY_KP_ADD = 334
    """Key: Keypad +"""

    KEY_KP_ENTER = 335
    """Key: Keypad Enter"""

    KEY_KP_EQUAL = 336
    """Key: Keypad ="""

    KEY_BACK = 4
    """Key: Android back button"""

    KEY_MENU = 82
    """Key: Android menu button"""

    KEY_VOLUME_UP = 24
    """Key: Android volume up button"""

    KEY_VOLUME_DOWN = 25
    """Key: Android volume down button"""



KEY_NULL = KeyboardKey.KEY_NULL
KEY_APOSTROPHE = KeyboardKey.KEY_APOSTROPHE
KEY_COMMA = KeyboardKey.KEY_COMMA
KEY_MINUS = KeyboardKey.KEY_MINUS
KEY_PERIOD = KeyboardKey.KEY_PERIOD
KEY_SLASH = KeyboardKey.KEY_SLASH
KEY_ZERO = KeyboardKey.KEY_ZERO
KEY_ONE = KeyboardKey.KEY_ONE
KEY_TWO = KeyboardKey.KEY_TWO
KEY_THREE = KeyboardKey.KEY_THREE
KEY_FOUR = KeyboardKey.KEY_FOUR
KEY_FIVE = KeyboardKey.KEY_FIVE
KEY_SIX = KeyboardKey.KEY_SIX
KEY_SEVEN = KeyboardKey.KEY_SEVEN
KEY_EIGHT = KeyboardKey.KEY_EIGHT
KEY_NINE = KeyboardKey.KEY_NINE
KEY_SEMICOLON = KeyboardKey.KEY_SEMICOLON
KEY_EQUAL = KeyboardKey.KEY_EQUAL
KEY_A = KeyboardKey.KEY_A
KEY_B = KeyboardKey.KEY_B
KEY_C = KeyboardKey.KEY_C
KEY_D = KeyboardKey.KEY_D
KEY_E = KeyboardKey.KEY_E
KEY_F = KeyboardKey.KEY_F
KEY_G = KeyboardKey.KEY_G
KEY_H = KeyboardKey.KEY_H
KEY_I = KeyboardKey.KEY_I
KEY_J = KeyboardKey.KEY_J
KEY_K = KeyboardKey.KEY_K
KEY_L = KeyboardKey.KEY_L
KEY_M = KeyboardKey.KEY_M
KEY_N = KeyboardKey.KEY_N
KEY_O = KeyboardKey.KEY_O
KEY_P = KeyboardKey.KEY_P
KEY_Q = KeyboardKey.KEY_Q
KEY_R = KeyboardKey.KEY_R
KEY_S = KeyboardKey.KEY_S
KEY_T = KeyboardKey.KEY_T
KEY_U = KeyboardKey.KEY_U
KEY_V = KeyboardKey.KEY_V
KEY_W = KeyboardKey.KEY_W
KEY_X = KeyboardKey.KEY_X
KEY_Y = KeyboardKey.KEY_Y
KEY_Z = KeyboardKey.KEY_Z
KEY_LEFT_BRACKET = KeyboardKey.KEY_LEFT_BRACKET
KEY_BACKSLASH = KeyboardKey.KEY_BACKSLASH
KEY_RIGHT_BRACKET = KeyboardKey.KEY_RIGHT_BRACKET
KEY_GRAVE = KeyboardKey.KEY_GRAVE
KEY_SPACE = KeyboardKey.KEY_SPACE
KEY_ESCAPE = KeyboardKey.KEY_ESCAPE
KEY_ENTER = KeyboardKey.KEY_ENTER
KEY_TAB = KeyboardKey.KEY_TAB
KEY_BACKSPACE = KeyboardKey.KEY_BACKSPACE
KEY_INSERT = KeyboardKey.KEY_INSERT
KEY_DELETE = KeyboardKey.KEY_DELETE
KEY_RIGHT = KeyboardKey.KEY_RIGHT
KEY_LEFT = KeyboardKey.KEY_LEFT
KEY_DOWN = KeyboardKey.KEY_DOWN
KEY_UP = KeyboardKey.KEY_UP
KEY_PAGE_UP = KeyboardKey.KEY_PAGE_UP
KEY_PAGE_DOWN = KeyboardKey.KEY_PAGE_DOWN
KEY_HOME = KeyboardKey.KEY_HOME
KEY_END = KeyboardKey.KEY_END
KEY_CAPS_LOCK = KeyboardKey.KEY_CAPS_LOCK
KEY_SCROLL_LOCK = KeyboardKey.KEY_SCROLL_LOCK
KEY_NUM_LOCK = KeyboardKey.KEY_NUM_LOCK
KEY_PRINT_SCREEN = KeyboardKey.KEY_PRINT_SCREEN
KEY_PAUSE = KeyboardKey.KEY_PAUSE
KEY_F1 = KeyboardKey.KEY_F1
KEY_F2 = KeyboardKey.KEY_F2
KEY_F3 = KeyboardKey.KEY_F3
KEY_F4 = KeyboardKey.KEY_F4
KEY_F5 = KeyboardKey.KEY_F5
KEY_F6 = KeyboardKey.KEY_F6
KEY_F7 = KeyboardKey.KEY_F7
KEY_F8 = KeyboardKey.KEY_F8
KEY_F9 = KeyboardKey.KEY_F9
KEY_F10 = KeyboardKey.KEY_F10
KEY_F11 = KeyboardKey.KEY_F11
KEY_F12 = KeyboardKey.KEY_F12
KEY_LEFT_SHIFT = KeyboardKey.KEY_LEFT_SHIFT
KEY_LEFT_CONTROL = KeyboardKey.KEY_LEFT_CONTROL
KEY_LEFT_ALT = KeyboardKey.KEY_LEFT_ALT
KEY_LEFT_SUPER = KeyboardKey.KEY_LEFT_SUPER
KEY_RIGHT_SHIFT = KeyboardKey.KEY_RIGHT_SHIFT
KEY_RIGHT_CONTROL = KeyboardKey.KEY_RIGHT_CONTROL
KEY_RIGHT_ALT = KeyboardKey.KEY_RIGHT_ALT
KEY_RIGHT_SUPER = KeyboardKey.KEY_RIGHT_SUPER
KEY_KB_MENU = KeyboardKey.KEY_KB_MENU
KEY_KP_0 = KeyboardKey.KEY_KP_0
KEY_KP_1 = KeyboardKey.KEY_KP_1
KEY_KP_2 = KeyboardKey.KEY_KP_2
KEY_KP_3 = KeyboardKey.KEY_KP_3
KEY_KP_4 = KeyboardKey.KEY_KP_4
KEY_KP_5 = KeyboardKey.KEY_KP_5
KEY_KP_6 = KeyboardKey.KEY_KP_6
KEY_KP_7 = KeyboardKey.KEY_KP_7
KEY_KP_8 = KeyboardKey.KEY_KP_8
KEY_KP_9 = KeyboardKey.KEY_KP_9
KEY_KP_DECIMAL = KeyboardKey.KEY_KP_DECIMAL
KEY_KP_DIVIDE = KeyboardKey.KEY_KP_DIVIDE
KEY_KP_MULTIPLY = KeyboardKey.KEY_KP_MULTIPLY
KEY_KP_SUBTRACT = KeyboardKey.KEY_KP_SUBTRACT
KEY_KP_ADD = KeyboardKey.KEY_KP_ADD
KEY_KP_ENTER = KeyboardKey.KEY_KP_ENTER
KEY_KP_EQUAL = KeyboardKey.KEY_KP_EQUAL
KEY_BACK = KeyboardKey.KEY_BACK
KEY_MENU = KeyboardKey.KEY_MENU
KEY_VOLUME_UP = KeyboardKey.KEY_VOLUME_UP
KEY_VOLUME_DOWN = KeyboardKey.KEY_VOLUME_DOWN


class MouseButton(IntEnum):
    """Mouse buttons"""

    MOUSE_BUTTON_LEFT = 0
    """Mouse button left"""

    MOUSE_BUTTON_RIGHT = 1
    """Mouse button right"""

    MOUSE_BUTTON_MIDDLE = 2
    """Mouse button middle (pressed wheel)"""

    MOUSE_BUTTON_SIDE = 3
    """Mouse button side (advanced mouse device)"""

    MOUSE_BUTTON_EXTRA = 4
    """Mouse button extra (advanced mouse device)"""

    MOUSE_BUTTON_FORWARD = 5
    """Mouse button forward (advanced mouse device)"""

    MOUSE_BUTTON_BACK = 6
    """Mouse button back (advanced mouse device)"""



MOUSE_BUTTON_LEFT = MouseButton.MOUSE_BUTTON_LEFT
MOUSE_BUTTON_RIGHT = MouseButton.MOUSE_BUTTON_RIGHT
MOUSE_BUTTON_MIDDLE = MouseButton.MOUSE_BUTTON_MIDDLE
MOUSE_BUTTON_SIDE = MouseButton.MOUSE_BUTTON_SIDE
MOUSE_BUTTON_EXTRA = MouseButton.MOUSE_BUTTON_EXTRA
MOUSE_BUTTON_FORWARD = MouseButton.MOUSE_BUTTON_FORWARD
MOUSE_BUTTON_BACK = MouseButton.MOUSE_BUTTON_BACK


class MouseCursor(IntEnum):
    """Mouse cursor"""

    MOUSE_CURSOR_DEFAULT = 0
    """Default pointer shape"""

    MOUSE_CURSOR_ARROW = 1
    """Arrow shape"""

    MOUSE_CURSOR_IBEAM = 2
    """Text writing cursor shape"""

    MOUSE_CURSOR_CROSSHAIR = 3
    """Cross shape"""

    MOUSE_CURSOR_POINTING_HAND = 4
    """Pointing hand cursor"""

    MOUSE_CURSOR_RESIZE_EW = 5
    """Horizontal resize/move arrow shape"""

    MOUSE_CURSOR_RESIZE_NS = 6
    """Vertical resize/move arrow shape"""

    MOUSE_CURSOR_RESIZE_NWSE = 7
    """Top-left to bottom-right diagonal resize/move arrow shape"""

    MOUSE_CURSOR_RESIZE_NESW = 8
    """The top-right to bottom-left diagonal resize/move arrow shape"""

    MOUSE_CURSOR_RESIZE_ALL = 9
    """The omnidirectional resize/move cursor shape"""

    MOUSE_CURSOR_NOT_ALLOWED = 10
    """The operation-not-allowed shape"""



MOUSE_CURSOR_DEFAULT = MouseCursor.MOUSE_CURSOR_DEFAULT
MOUSE_CURSOR_ARROW = MouseCursor.MOUSE_CURSOR_ARROW
MOUSE_CURSOR_IBEAM = MouseCursor.MOUSE_CURSOR_IBEAM
MOUSE_CURSOR_CROSSHAIR = MouseCursor.MOUSE_CURSOR_CROSSHAIR
MOUSE_CURSOR_POINTING_HAND = MouseCursor.MOUSE_CURSOR_POINTING_HAND
MOUSE_CURSOR_RESIZE_EW = MouseCursor.MOUSE_CURSOR_RESIZE_EW
MOUSE_CURSOR_RESIZE_NS = MouseCursor.MOUSE_CURSOR_RESIZE_NS
MOUSE_CURSOR_RESIZE_NWSE = MouseCursor.MOUSE_CURSOR_RESIZE_NWSE
MOUSE_CURSOR_RESIZE_NESW = MouseCursor.MOUSE_CURSOR_RESIZE_NESW
MOUSE_CURSOR_RESIZE_ALL = MouseCursor.MOUSE_CURSOR_RESIZE_ALL
MOUSE_CURSOR_NOT_ALLOWED = MouseCursor.MOUSE_CURSOR_NOT_ALLOWED


class GamepadButton(IntEnum):
    """Gamepad buttons"""

    GAMEPAD_BUTTON_UNKNOWN = 0
    """Unknown button, just for error checking"""

    GAMEPAD_BUTTON_LEFT_FACE_UP = 1
    """Gamepad left DPAD up button"""

    GAMEPAD_BUTTON_LEFT_FACE_RIGHT = 2
    """Gamepad left DPAD right button"""

    GAMEPAD_BUTTON_LEFT_FACE_DOWN = 3
    """Gamepad left DPAD down button"""

    GAMEPAD_BUTTON_LEFT_FACE_LEFT = 4
    """Gamepad left DPAD left button"""

    GAMEPAD_BUTTON_RIGHT_FACE_UP = 5
    """Gamepad right button up (i.e. PS3: Triangle, Xbox: Y)"""

    GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = 6
    """Gamepad right button right (i.e. PS3: Square, Xbox: X)"""

    GAMEPAD_BUTTON_RIGHT_FACE_DOWN = 7
    """Gamepad right button down (i.e. PS3: Cross, Xbox: A)"""

    GAMEPAD_BUTTON_RIGHT_FACE_LEFT = 8
    """Gamepad right button left (i.e. PS3: Circle, Xbox: B)"""

    GAMEPAD_BUTTON_LEFT_TRIGGER_1 = 9
    """Gamepad top/back trigger left (first), it could be a trailing button"""

    GAMEPAD_BUTTON_LEFT_TRIGGER_2 = 10
    """Gamepad top/back trigger left (second), it could be a trailing button"""

    GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = 11
    """Gamepad top/back trigger right (one), it could be a trailing button"""

    GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = 12
    """Gamepad top/back trigger right (second), it could be a trailing button"""

    GAMEPAD_BUTTON_MIDDLE_LEFT = 13
    """Gamepad center buttons, left one (i.e. PS3: Select)"""

    GAMEPAD_BUTTON_MIDDLE = 14
    """Gamepad center buttons, middle one (i.e. PS3: PS, Xbox: XBOX)"""

    GAMEPAD_BUTTON_MIDDLE_RIGHT = 15
    """Gamepad center buttons, right one (i.e. PS3: Start)"""

    GAMEPAD_BUTTON_LEFT_THUMB = 16
    """Gamepad joystick pressed button left"""

    GAMEPAD_BUTTON_RIGHT_THUMB = 17
    """Gamepad joystick pressed button right"""



GAMEPAD_BUTTON_UNKNOWN = GamepadButton.GAMEPAD_BUTTON_UNKNOWN
GAMEPAD_BUTTON_LEFT_FACE_UP = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_UP
GAMEPAD_BUTTON_LEFT_FACE_RIGHT = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_RIGHT
GAMEPAD_BUTTON_LEFT_FACE_DOWN = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_DOWN
GAMEPAD_BUTTON_LEFT_FACE_LEFT = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_LEFT
GAMEPAD_BUTTON_RIGHT_FACE_UP = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_UP
GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_RIGHT
GAMEPAD_BUTTON_RIGHT_FACE_DOWN = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_DOWN
GAMEPAD_BUTTON_RIGHT_FACE_LEFT = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_LEFT
GAMEPAD_BUTTON_LEFT_TRIGGER_1 = GamepadButton.GAMEPAD_BUTTON_LEFT_TRIGGER_1
GAMEPAD_BUTTON_LEFT_TRIGGER_2 = GamepadButton.GAMEPAD_BUTTON_LEFT_TRIGGER_2
GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = GamepadButton.GAMEPAD_BUTTON_RIGHT_TRIGGER_1
GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = GamepadButton.GAMEPAD_BUTTON_RIGHT_TRIGGER_2
GAMEPAD_BUTTON_MIDDLE_LEFT = GamepadButton.GAMEPAD_BUTTON_MIDDLE_LEFT
GAMEPAD_BUTTON_MIDDLE = GamepadButton.GAMEPAD_BUTTON_MIDDLE
GAMEPAD_BUTTON_MIDDLE_RIGHT = GamepadButton.GAMEPAD_BUTTON_MIDDLE_RIGHT
GAMEPAD_BUTTON_LEFT_THUMB = GamepadButton.GAMEPAD_BUTTON_LEFT_THUMB
GAMEPAD_BUTTON_RIGHT_THUMB = GamepadButton.GAMEPAD_BUTTON_RIGHT_THUMB


class GamepadAxis(IntEnum):
    """Gamepad axis"""

    GAMEPAD_AXIS_LEFT_X = 0
    """Gamepad left stick X axis"""

    GAMEPAD_AXIS_LEFT_Y = 1
    """Gamepad left stick Y axis"""

    GAMEPAD_AXIS_RIGHT_X = 2
    """Gamepad right stick X axis"""

    GAMEPAD_AXIS_RIGHT_Y = 3
    """Gamepad right stick Y axis"""

    GAMEPAD_AXIS_LEFT_TRIGGER = 4
    """Gamepad back trigger left, pressure level: [1..-1]"""

    GAMEPAD_AXIS_RIGHT_TRIGGER = 5
    """Gamepad back trigger right, pressure level: [1..-1]"""



GAMEPAD_AXIS_LEFT_X = GamepadAxis.GAMEPAD_AXIS_LEFT_X
GAMEPAD_AXIS_LEFT_Y = GamepadAxis.GAMEPAD_AXIS_LEFT_Y
GAMEPAD_AXIS_RIGHT_X = GamepadAxis.GAMEPAD_AXIS_RIGHT_X
GAMEPAD_AXIS_RIGHT_Y = GamepadAxis.GAMEPAD_AXIS_RIGHT_Y
GAMEPAD_AXIS_LEFT_TRIGGER = GamepadAxis.GAMEPAD_AXIS_LEFT_TRIGGER
GAMEPAD_AXIS_RIGHT_TRIGGER = GamepadAxis.GAMEPAD_AXIS_RIGHT_TRIGGER


class MaterialMapIndex(IntEnum):
    """Material map index"""

    MATERIAL_MAP_ALBEDO = 0
    """Albedo material (same as: MATERIAL_MAP_DIFFUSE)"""

    MATERIAL_MAP_METALNESS = 1
    """Metalness material (same as: MATERIAL_MAP_SPECULAR)"""

    MATERIAL_MAP_NORMAL = 2
    """Normal material"""

    MATERIAL_MAP_ROUGHNESS = 3
    """Roughness material"""

    MATERIAL_MAP_OCCLUSION = 4
    """Ambient occlusion material"""

    MATERIAL_MAP_EMISSION = 5
    """Emission material"""

    MATERIAL_MAP_HEIGHT = 6
    """Heightmap material"""

    MATERIAL_MAP_CUBEMAP = 7
    """Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)"""

    MATERIAL_MAP_IRRADIANCE = 8
    """Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)"""

    MATERIAL_MAP_PREFILTER = 9
    """Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)"""

    MATERIAL_MAP_BRDF = 10
    """Brdf material"""



MATERIAL_MAP_ALBEDO = MaterialMapIndex.MATERIAL_MAP_ALBEDO
MATERIAL_MAP_METALNESS = MaterialMapIndex.MATERIAL_MAP_METALNESS
MATERIAL_MAP_NORMAL = MaterialMapIndex.MATERIAL_MAP_NORMAL
MATERIAL_MAP_ROUGHNESS = MaterialMapIndex.MATERIAL_MAP_ROUGHNESS
MATERIAL_MAP_OCCLUSION = MaterialMapIndex.MATERIAL_MAP_OCCLUSION
MATERIAL_MAP_EMISSION = MaterialMapIndex.MATERIAL_MAP_EMISSION
MATERIAL_MAP_HEIGHT = MaterialMapIndex.MATERIAL_MAP_HEIGHT
MATERIAL_MAP_CUBEMAP = MaterialMapIndex.MATERIAL_MAP_CUBEMAP
MATERIAL_MAP_IRRADIANCE = MaterialMapIndex.MATERIAL_MAP_IRRADIANCE
MATERIAL_MAP_PREFILTER = MaterialMapIndex.MATERIAL_MAP_PREFILTER
MATERIAL_MAP_BRDF = MaterialMapIndex.MATERIAL_MAP_BRDF


class ShaderLocationIndex(IntEnum):
    """Shader location index"""

    SHADER_LOC_VERTEX_POSITION = 0
    """Shader location: vertex attribute: position"""

    SHADER_LOC_VERTEX_TEXCOORD01 = 1
    """Shader location: vertex attribute: texcoord01"""

    SHADER_LOC_VERTEX_TEXCOORD02 = 2
    """Shader location: vertex attribute: texcoord02"""

    SHADER_LOC_VERTEX_NORMAL = 3
    """Shader location: vertex attribute: normal"""

    SHADER_LOC_VERTEX_TANGENT = 4
    """Shader location: vertex attribute: tangent"""

    SHADER_LOC_VERTEX_COLOR = 5
    """Shader location: vertex attribute: color"""

    SHADER_LOC_MATRIX_MVP = 6
    """Shader location: matrix uniform: model-view-projection"""

    SHADER_LOC_MATRIX_VIEW = 7
    """Shader location: matrix uniform: view (camera transform)"""

    SHADER_LOC_MATRIX_PROJECTION = 8
    """Shader location: matrix uniform: projection"""

    SHADER_LOC_MATRIX_MODEL = 9
    """Shader location: matrix uniform: model (transform)"""

    SHADER_LOC_MATRIX_NORMAL = 10
    """Shader location: matrix uniform: normal"""

    SHADER_LOC_VECTOR_VIEW = 11
    """Shader location: vector uniform: view"""

    SHADER_LOC_COLOR_DIFFUSE = 12
    """Shader location: vector uniform: diffuse color"""

    SHADER_LOC_COLOR_SPECULAR = 13
    """Shader location: vector uniform: specular color"""

    SHADER_LOC_COLOR_AMBIENT = 14
    """Shader location: vector uniform: ambient color"""

    SHADER_LOC_MAP_ALBEDO = 15
    """Shader location: sampler2d texture: albedo (same as: SHADER_LOC_MAP_DIFFUSE)"""

    SHADER_LOC_MAP_METALNESS = 16
    """Shader location: sampler2d texture: metalness (same as: SHADER_LOC_MAP_SPECULAR)"""

    SHADER_LOC_MAP_NORMAL = 17
    """Shader location: sampler2d texture: normal"""

    SHADER_LOC_MAP_ROUGHNESS = 18
    """Shader location: sampler2d texture: roughness"""

    SHADER_LOC_MAP_OCCLUSION = 19
    """Shader location: sampler2d texture: occlusion"""

    SHADER_LOC_MAP_EMISSION = 20
    """Shader location: sampler2d texture: emission"""

    SHADER_LOC_MAP_HEIGHT = 21
    """Shader location: sampler2d texture: height"""

    SHADER_LOC_MAP_CUBEMAP = 22
    """Shader location: samplerCube texture: cubemap"""

    SHADER_LOC_MAP_IRRADIANCE = 23
    """Shader location: samplerCube texture: irradiance"""

    SHADER_LOC_MAP_PREFILTER = 24
    """Shader location: samplerCube texture: prefilter"""

    SHADER_LOC_MAP_BRDF = 25
    """Shader location: sampler2d texture: brdf"""



SHADER_LOC_VERTEX_POSITION = ShaderLocationIndex.SHADER_LOC_VERTEX_POSITION
SHADER_LOC_VERTEX_TEXCOORD01 = ShaderLocationIndex.SHADER_LOC_VERTEX_TEXCOORD01
SHADER_LOC_VERTEX_TEXCOORD02 = ShaderLocationIndex.SHADER_LOC_VERTEX_TEXCOORD02
SHADER_LOC_VERTEX_NORMAL = ShaderLocationIndex.SHADER_LOC_VERTEX_NORMAL
SHADER_LOC_VERTEX_TANGENT = ShaderLocationIndex.SHADER_LOC_VERTEX_TANGENT
SHADER_LOC_VERTEX_COLOR = ShaderLocationIndex.SHADER_LOC_VERTEX_COLOR
SHADER_LOC_MATRIX_MVP = ShaderLocationIndex.SHADER_LOC_MATRIX_MVP
SHADER_LOC_MATRIX_VIEW = ShaderLocationIndex.SHADER_LOC_MATRIX_VIEW
SHADER_LOC_MATRIX_PROJECTION = ShaderLocationIndex.SHADER_LOC_MATRIX_PROJECTION
SHADER_LOC_MATRIX_MODEL = ShaderLocationIndex.SHADER_LOC_MATRIX_MODEL
SHADER_LOC_MATRIX_NORMAL = ShaderLocationIndex.SHADER_LOC_MATRIX_NORMAL
SHADER_LOC_VECTOR_VIEW = ShaderLocationIndex.SHADER_LOC_VECTOR_VIEW
SHADER_LOC_COLOR_DIFFUSE = ShaderLocationIndex.SHADER_LOC_COLOR_DIFFUSE
SHADER_LOC_COLOR_SPECULAR = ShaderLocationIndex.SHADER_LOC_COLOR_SPECULAR
SHADER_LOC_COLOR_AMBIENT = ShaderLocationIndex.SHADER_LOC_COLOR_AMBIENT
SHADER_LOC_MAP_ALBEDO = ShaderLocationIndex.SHADER_LOC_MAP_ALBEDO
SHADER_LOC_MAP_METALNESS = ShaderLocationIndex.SHADER_LOC_MAP_METALNESS
SHADER_LOC_MAP_NORMAL = ShaderLocationIndex.SHADER_LOC_MAP_NORMAL
SHADER_LOC_MAP_ROUGHNESS = ShaderLocationIndex.SHADER_LOC_MAP_ROUGHNESS
SHADER_LOC_MAP_OCCLUSION = ShaderLocationIndex.SHADER_LOC_MAP_OCCLUSION
SHADER_LOC_MAP_EMISSION = ShaderLocationIndex.SHADER_LOC_MAP_EMISSION
SHADER_LOC_MAP_HEIGHT = ShaderLocationIndex.SHADER_LOC_MAP_HEIGHT
SHADER_LOC_MAP_CUBEMAP = ShaderLocationIndex.SHADER_LOC_MAP_CUBEMAP
SHADER_LOC_MAP_IRRADIANCE = ShaderLocationIndex.SHADER_LOC_MAP_IRRADIANCE
SHADER_LOC_MAP_PREFILTER = ShaderLocationIndex.SHADER_LOC_MAP_PREFILTER
SHADER_LOC_MAP_BRDF = ShaderLocationIndex.SHADER_LOC_MAP_BRDF


class ShaderUniformDataType(IntEnum):
    """Shader uniform data type"""

    SHADER_UNIFORM_FLOAT = 0
    """Shader uniform type: float"""

    SHADER_UNIFORM_VEC2 = 1
    """Shader uniform type: vec2 (2 float)"""

    SHADER_UNIFORM_VEC3 = 2
    """Shader uniform type: vec3 (3 float)"""

    SHADER_UNIFORM_VEC4 = 3
    """Shader uniform type: vec4 (4 float)"""

    SHADER_UNIFORM_INT = 4
    """Shader uniform type: int"""

    SHADER_UNIFORM_IVEC2 = 5
    """Shader uniform type: ivec2 (2 int)"""

    SHADER_UNIFORM_IVEC3 = 6
    """Shader uniform type: ivec3 (3 int)"""

    SHADER_UNIFORM_IVEC4 = 7
    """Shader uniform type: ivec4 (4 int)"""

    SHADER_UNIFORM_SAMPLER2D = 8
    """Shader uniform type: sampler2d"""



SHADER_UNIFORM_FLOAT = ShaderUniformDataType.SHADER_UNIFORM_FLOAT
SHADER_UNIFORM_VEC2 = ShaderUniformDataType.SHADER_UNIFORM_VEC2
SHADER_UNIFORM_VEC3 = ShaderUniformDataType.SHADER_UNIFORM_VEC3
SHADER_UNIFORM_VEC4 = ShaderUniformDataType.SHADER_UNIFORM_VEC4
SHADER_UNIFORM_INT = ShaderUniformDataType.SHADER_UNIFORM_INT
SHADER_UNIFORM_IVEC2 = ShaderUniformDataType.SHADER_UNIFORM_IVEC2
SHADER_UNIFORM_IVEC3 = ShaderUniformDataType.SHADER_UNIFORM_IVEC3
SHADER_UNIFORM_IVEC4 = ShaderUniformDataType.SHADER_UNIFORM_IVEC4
SHADER_UNIFORM_SAMPLER2D = ShaderUniformDataType.SHADER_UNIFORM_SAMPLER2D


class ShaderAttributeDataType(IntEnum):
    """Shader attribute data types"""

    SHADER_ATTRIB_FLOAT = 0
    """Shader attribute type: float"""

    SHADER_ATTRIB_VEC2 = 1
    """Shader attribute type: vec2 (2 float)"""

    SHADER_ATTRIB_VEC3 = 2
    """Shader attribute type: vec3 (3 float)"""

    SHADER_ATTRIB_VEC4 = 3
    """Shader attribute type: vec4 (4 float)"""



SHADER_ATTRIB_FLOAT = ShaderAttributeDataType.SHADER_ATTRIB_FLOAT
SHADER_ATTRIB_VEC2 = ShaderAttributeDataType.SHADER_ATTRIB_VEC2
SHADER_ATTRIB_VEC3 = ShaderAttributeDataType.SHADER_ATTRIB_VEC3
SHADER_ATTRIB_VEC4 = ShaderAttributeDataType.SHADER_ATTRIB_VEC4


class PixelFormat(IntEnum):
    """Pixel formats"""

    PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1
    """8 bit per pixel (no alpha)"""

    PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2
    """8*2 bpp (2 channels)"""

    PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3
    """16 bpp"""

    PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4
    """24 bpp"""

    PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5
    """16 bpp (1 bit alpha)"""

    PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6
    """16 bpp (4 bit alpha)"""

    PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7
    """32 bpp"""

    PIXELFORMAT_UNCOMPRESSED_R32 = 8
    """32 bpp (1 channel - float)"""

    PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9
    """32*3 bpp (3 channels - float)"""

    PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10
    """32*4 bpp (4 channels - float)"""

    PIXELFORMAT_COMPRESSED_DXT1_RGB = 11
    """4 bpp (no alpha)"""

    PIXELFORMAT_COMPRESSED_DXT1_RGBA = 12
    """4 bpp (1 bit alpha)"""

    PIXELFORMAT_COMPRESSED_DXT3_RGBA = 13
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_DXT5_RGBA = 14
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_ETC1_RGB = 15
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ETC2_RGB = 16
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 17
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_PVRT_RGB = 18
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_PVRT_RGBA = 19
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 20
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 21
    """2 bpp"""



PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = PixelFormat.PIXELFORMAT_UNCOMPRESSED_GRAYSCALE
PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = PixelFormat.PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA
PIXELFORMAT_UNCOMPRESSED_R5G6B5 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R5G6B5
PIXELFORMAT_UNCOMPRESSED_R8G8B8 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R8G8B8
PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R5G5B5A1
PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R4G4B4A4
PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R8G8B8A8
PIXELFORMAT_UNCOMPRESSED_R32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32
PIXELFORMAT_UNCOMPRESSED_R32G32B32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32G32B32
PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32G32B32A32
PIXELFORMAT_COMPRESSED_DXT1_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_DXT1_RGB
PIXELFORMAT_COMPRESSED_DXT1_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT1_RGBA
PIXELFORMAT_COMPRESSED_DXT3_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT3_RGBA
PIXELFORMAT_COMPRESSED_DXT5_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT5_RGBA
PIXELFORMAT_COMPRESSED_ETC1_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_ETC1_RGB
PIXELFORMAT_COMPRESSED_ETC2_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_ETC2_RGB
PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA
PIXELFORMAT_COMPRESSED_PVRT_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_PVRT_RGB
PIXELFORMAT_COMPRESSED_PVRT_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_PVRT_RGBA
PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA
PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA


class TextureFilter(IntEnum):
    """Texture parameters: filter mode"""

    TEXTURE_FILTER_POINT = 0
    """No filter, just pixel approximation"""

    TEXTURE_FILTER_BILINEAR = 1
    """Linear filtering"""

    TEXTURE_FILTER_TRILINEAR = 2
    """Trilinear filtering (linear with mipmaps)"""

    TEXTURE_FILTER_ANISOTROPIC_4X = 3
    """Anisotropic filtering 4x"""

    TEXTURE_FILTER_ANISOTROPIC_8X = 4
    """Anisotropic filtering 8x"""

    TEXTURE_FILTER_ANISOTROPIC_16X = 5
    """Anisotropic filtering 16x"""



TEXTURE_FILTER_POINT = TextureFilter.TEXTURE_FILTER_POINT
TEXTURE_FILTER_BILINEAR = TextureFilter.TEXTURE_FILTER_BILINEAR
TEXTURE_FILTER_TRILINEAR = TextureFilter.TEXTURE_FILTER_TRILINEAR
TEXTURE_FILTER_ANISOTROPIC_4X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_4X
TEXTURE_FILTER_ANISOTROPIC_8X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_8X
TEXTURE_FILTER_ANISOTROPIC_16X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_16X


class TextureWrap(IntEnum):
    """Texture parameters: wrap mode"""

    TEXTURE_WRAP_REPEAT = 0
    """Repeats texture in tiled mode"""

    TEXTURE_WRAP_CLAMP = 1
    """Clamps texture to edge pixel in tiled mode"""

    TEXTURE_WRAP_MIRROR_REPEAT = 2
    """Mirrors and repeats the texture in tiled mode"""

    TEXTURE_WRAP_MIRROR_CLAMP = 3
    """Mirrors and clamps to border the texture in tiled mode"""



TEXTURE_WRAP_REPEAT = TextureWrap.TEXTURE_WRAP_REPEAT
TEXTURE_WRAP_CLAMP = TextureWrap.TEXTURE_WRAP_CLAMP
TEXTURE_WRAP_MIRROR_REPEAT = TextureWrap.TEXTURE_WRAP_MIRROR_REPEAT
TEXTURE_WRAP_MIRROR_CLAMP = TextureWrap.TEXTURE_WRAP_MIRROR_CLAMP


class CubemapLayout(IntEnum):
    """Cubemap layouts"""

    CUBEMAP_LAYOUT_AUTO_DETECT = 0
    """Automatically detect layout type"""

    CUBEMAP_LAYOUT_LINE_VERTICAL = 1
    """Layout is defined by a vertical line with faces"""

    CUBEMAP_LAYOUT_LINE_HORIZONTAL = 2
    """Layout is defined by a horizontal line with faces"""

    CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = 3
    """Layout is defined by a 3x4 cross with cubemap faces"""

    CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = 4
    """Layout is defined by a 4x3 cross with cubemap faces"""

    CUBEMAP_LAYOUT_PANORAMA = 5
    """Layout is defined by a panorama image (equirrectangular map)"""



CUBEMAP_LAYOUT_AUTO_DETECT = CubemapLayout.CUBEMAP_LAYOUT_AUTO_DETECT
CUBEMAP_LAYOUT_LINE_VERTICAL = CubemapLayout.CUBEMAP_LAYOUT_LINE_VERTICAL
CUBEMAP_LAYOUT_LINE_HORIZONTAL = CubemapLayout.CUBEMAP_LAYOUT_LINE_HORIZONTAL
CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = CubemapLayout.CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR
CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = CubemapLayout.CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE
CUBEMAP_LAYOUT_PANORAMA = CubemapLayout.CUBEMAP_LAYOUT_PANORAMA


class FontType(IntEnum):
    """Font type, defines generation method"""

    FONT_DEFAULT = 0
    """Default font generation, anti-aliased"""

    FONT_BITMAP = 1
    """Bitmap font generation, no anti-aliasing"""

    FONT_SDF = 2
    """SDF font generation, requires external shader"""



FONT_DEFAULT = FontType.FONT_DEFAULT
FONT_BITMAP = FontType.FONT_BITMAP
FONT_SDF = FontType.FONT_SDF


class BlendMode(IntEnum):
    """Color blending modes (pre-defined)"""

    BLEND_ALPHA = 0
    """Blend textures considering alpha (default)"""

    BLEND_ADDITIVE = 1
    """Blend textures adding colors"""

    BLEND_MULTIPLIED = 2
    """Blend textures multiplying colors"""

    BLEND_ADD_COLORS = 3
    """Blend textures adding colors (alternative)"""

    BLEND_SUBTRACT_COLORS = 4
    """Blend textures subtracting colors (alternative)"""

    BLEND_ALPHA_PREMULTIPLY = 5
    """Blend premultiplied textures considering alpha"""

    BLEND_CUSTOM = 6
    """Blend textures using custom src/dst factors (use rlSetBlendFactors())"""

    BLEND_CUSTOM_SEPARATE = 7
    """Blend textures using custom rgb/alpha separate src/dst factors (use rlSetBlendFactorsSeparate())"""



BLEND_ALPHA = BlendMode.BLEND_ALPHA
BLEND_ADDITIVE = BlendMode.BLEND_ADDITIVE
BLEND_MULTIPLIED = BlendMode.BLEND_MULTIPLIED
BLEND_ADD_COLORS = BlendMode.BLEND_ADD_COLORS
BLEND_SUBTRACT_COLORS = BlendMode.BLEND_SUBTRACT_COLORS
BLEND_ALPHA_PREMULTIPLY = BlendMode.BLEND_ALPHA_PREMULTIPLY
BLEND_CUSTOM = BlendMode.BLEND_CUSTOM
BLEND_CUSTOM_SEPARATE = BlendMode.BLEND_CUSTOM_SEPARATE


class Gesture(IntEnum):
    """Gesture"""

    GESTURE_NONE = 0
    """No gesture"""

    GESTURE_TAP = 1
    """Tap gesture"""

    GESTURE_DOUBLETAP = 2
    """Double tap gesture"""

    GESTURE_HOLD = 4
    """Hold gesture"""

    GESTURE_DRAG = 8
    """Drag gesture"""

    GESTURE_SWIPE_RIGHT = 16
    """Swipe right gesture"""

    GESTURE_SWIPE_LEFT = 32
    """Swipe left gesture"""

    GESTURE_SWIPE_UP = 64
    """Swipe up gesture"""

    GESTURE_SWIPE_DOWN = 128
    """Swipe down gesture"""

    GESTURE_PINCH_IN = 256
    """Pinch in gesture"""

    GESTURE_PINCH_OUT = 512
    """Pinch out gesture"""



GESTURE_NONE = Gesture.GESTURE_NONE
GESTURE_TAP = Gesture.GESTURE_TAP
GESTURE_DOUBLETAP = Gesture.GESTURE_DOUBLETAP
GESTURE_HOLD = Gesture.GESTURE_HOLD
GESTURE_DRAG = Gesture.GESTURE_DRAG
GESTURE_SWIPE_RIGHT = Gesture.GESTURE_SWIPE_RIGHT
GESTURE_SWIPE_LEFT = Gesture.GESTURE_SWIPE_LEFT
GESTURE_SWIPE_UP = Gesture.GESTURE_SWIPE_UP
GESTURE_SWIPE_DOWN = Gesture.GESTURE_SWIPE_DOWN
GESTURE_PINCH_IN = Gesture.GESTURE_PINCH_IN
GESTURE_PINCH_OUT = Gesture.GESTURE_PINCH_OUT


class CameraMode(IntEnum):
    """Camera system modes"""

    CAMERA_CUSTOM = 0
    """Custom camera"""

    CAMERA_FREE = 1
    """Free camera"""

    CAMERA_ORBITAL = 2
    """Orbital camera"""

    CAMERA_FIRST_PERSON = 3
    """First person camera"""

    CAMERA_THIRD_PERSON = 4
    """Third person camera"""



CAMERA_CUSTOM = CameraMode.CAMERA_CUSTOM
CAMERA_FREE = CameraMode.CAMERA_FREE
CAMERA_ORBITAL = CameraMode.CAMERA_ORBITAL
CAMERA_FIRST_PERSON = CameraMode.CAMERA_FIRST_PERSON
CAMERA_THIRD_PERSON = CameraMode.CAMERA_THIRD_PERSON


class CameraProjection(IntEnum):
    """Camera projection"""

    CAMERA_PERSPECTIVE = 0
    """Perspective projection"""

    CAMERA_ORTHOGRAPHIC = 1
    """Orthographic projection"""



CAMERA_PERSPECTIVE = CameraProjection.CAMERA_PERSPECTIVE
CAMERA_ORTHOGRAPHIC = CameraProjection.CAMERA_ORTHOGRAPHIC


class NPatchLayout(IntEnum):
    """N-patch layout"""

    NPATCH_NINE_PATCH = 0
    """Npatch layout: 3x3 tiles"""

    NPATCH_THREE_PATCH_VERTICAL = 1
    """Npatch layout: 1x3 tiles"""

    NPATCH_THREE_PATCH_HORIZONTAL = 2
    """Npatch layout: 3x1 tiles"""



NPATCH_NINE_PATCH = NPatchLayout.NPATCH_NINE_PATCH
NPATCH_THREE_PATCH_VERTICAL = NPatchLayout.NPATCH_THREE_PATCH_VERTICAL
NPATCH_THREE_PATCH_HORIZONTAL = NPatchLayout.NPATCH_THREE_PATCH_HORIZONTAL



RAYLIB_VERSION_MAJOR = 4

RAYLIB_VERSION_MINOR = 5

RAYLIB_VERSION_PATCH = 0

RAYLIB_VERSION = '4.5'

PI = 3.141592653589793

DEG2RAD = (PI / 180.0)

RAD2DEG = (180.0 / PI)
# Light Gray
LIGHTGRAY = Color( 200, 200, 200, 255 )
# Gray
GRAY = Color( 130, 130, 130, 255 )
# Dark Gray
DARKGRAY = Color( 80, 80, 80, 255 )
# Yellow
YELLOW = Color( 253, 249, 0, 255 )
# Gold
GOLD = Color( 255, 203, 0, 255 )
# Orange
ORANGE = Color( 255, 161, 0, 255 )
# Pink
PINK = Color( 255, 109, 194, 255 )
# Red
RED = Color( 230, 41, 55, 255 )
# Maroon
MAROON = Color( 190, 33, 55, 255 )
# Green
GREEN = Color( 0, 228, 48, 255 )
# Lime
LIME = Color( 0, 158, 47, 255 )
# Dark Green
DARKGREEN = Color( 0, 117, 44, 255 )
# Sky Blue
SKYBLUE = Color( 102, 191, 255, 255 )
# Blue
BLUE = Color( 0, 121, 241, 255 )
# Dark Blue
DARKBLUE = Color( 0, 82, 172, 255 )
# Purple
PURPLE = Color( 200, 122, 255, 255 )
# Violet
VIOLET = Color( 135, 60, 190, 255 )
# Dark Purple
DARKPURPLE = Color( 112, 31, 126, 255 )
# Beige
BEIGE = Color( 211, 176, 131, 255 )
# Brown
BROWN = Color( 127, 106, 79, 255 )
# Dark Brown
DARKBROWN = Color( 76, 63, 47, 255 )
# White
WHITE = Color( 255, 255, 255, 255 )
# Black
BLACK = Color( 0, 0, 0, 255 )
# Blank (Transparent)
BLANK = Color( 0, 0, 0, 0 )
# Magenta
MAGENTA = Color( 255, 0, 255, 255 )
# My own White (raylib logo)
RAYWHITE = Color( 245, 245, 245, 255 )

# Logging: Redirect trace log messages
TraceLogCallback = CFUNCTYPE(None, Int, CharPtr, VoidPtr)

# FileIO: Load binary data
LoadFileDataCallback = CFUNCTYPE(UCharPtr, CharPtr, UIntPtr)

# FileIO: Save binary data
SaveFileDataCallback = CFUNCTYPE(Bool, CharPtr, VoidPtr, UInt)

# FileIO: Load text data
LoadFileTextCallback = CFUNCTYPE(CharPtr, CharPtr)

# FileIO: Save text data
SaveFileTextCallback = CFUNCTYPE(Bool, CharPtr, CharPtr)

# 
AudioCallback = CFUNCTYPE(None, VoidPtr, UInt)
_InitWindow = _wrap(rlapi.InitWindow, [Int, Int, CharPtr], None)
_WindowShouldClose = _wrap(rlapi.WindowShouldClose, [], Bool)
_CloseWindow = _wrap(rlapi.CloseWindow, [], None)
_IsWindowReady = _wrap(rlapi.IsWindowReady, [], Bool)
_IsWindowFullscreen = _wrap(rlapi.IsWindowFullscreen, [], Bool)
_IsWindowHidden = _wrap(rlapi.IsWindowHidden, [], Bool)
_IsWindowMinimized = _wrap(rlapi.IsWindowMinimized, [], Bool)
_IsWindowMaximized = _wrap(rlapi.IsWindowMaximized, [], Bool)
_IsWindowFocused = _wrap(rlapi.IsWindowFocused, [], Bool)
_IsWindowResized = _wrap(rlapi.IsWindowResized, [], Bool)
_IsWindowState = _wrap(rlapi.IsWindowState, [UInt], Bool)
_SetWindowState = _wrap(rlapi.SetWindowState, [UInt], None)
_ClearWindowState = _wrap(rlapi.ClearWindowState, [UInt], None)
_ToggleFullscreen = _wrap(rlapi.ToggleFullscreen, [], None)
_MaximizeWindow = _wrap(rlapi.MaximizeWindow, [], None)
_MinimizeWindow = _wrap(rlapi.MinimizeWindow, [], None)
_RestoreWindow = _wrap(rlapi.RestoreWindow, [], None)
_SetWindowIcon = _wrap(rlapi.SetWindowIcon, [Image], None)
_SetWindowIcons = _wrap(rlapi.SetWindowIcons, [ImagePtr, Int], None)
_SetWindowTitle = _wrap(rlapi.SetWindowTitle, [CharPtr], None)
_SetWindowPosition = _wrap(rlapi.SetWindowPosition, [Int, Int], None)
_SetWindowMonitor = _wrap(rlapi.SetWindowMonitor, [Int], None)
_SetWindowMinSize = _wrap(rlapi.SetWindowMinSize, [Int, Int], None)
_SetWindowSize = _wrap(rlapi.SetWindowSize, [Int, Int], None)
_SetWindowOpacity = _wrap(rlapi.SetWindowOpacity, [Float], None)
_GetWindowHandle = _wrap(rlapi.GetWindowHandle, [], VoidPtr)
_GetScreenWidth = _wrap(rlapi.GetScreenWidth, [], Int)
_GetScreenHeight = _wrap(rlapi.GetScreenHeight, [], Int)
_GetRenderWidth = _wrap(rlapi.GetRenderWidth, [], Int)
_GetRenderHeight = _wrap(rlapi.GetRenderHeight, [], Int)
_GetMonitorCount = _wrap(rlapi.GetMonitorCount, [], Int)
_GetCurrentMonitor = _wrap(rlapi.GetCurrentMonitor, [], Int)
_GetMonitorPosition = _wrap(rlapi.GetMonitorPosition, [Int], Vector2)
_GetMonitorWidth = _wrap(rlapi.GetMonitorWidth, [Int], Int)
_GetMonitorHeight = _wrap(rlapi.GetMonitorHeight, [Int], Int)
_GetMonitorPhysicalWidth = _wrap(rlapi.GetMonitorPhysicalWidth, [Int], Int)
_GetMonitorPhysicalHeight = _wrap(rlapi.GetMonitorPhysicalHeight, [Int], Int)
_GetMonitorRefreshRate = _wrap(rlapi.GetMonitorRefreshRate, [Int], Int)
_GetWindowPosition = _wrap(rlapi.GetWindowPosition, [], Vector2)
_GetWindowScaleDPI = _wrap(rlapi.GetWindowScaleDPI, [], Vector2)
_GetMonitorName = _wrap(rlapi.GetMonitorName, [Int], CharPtr)
_SetClipboardText = _wrap(rlapi.SetClipboardText, [CharPtr], None)
_GetClipboardText = _wrap(rlapi.GetClipboardText, [], CharPtr)
_EnableEventWaiting = _wrap(rlapi.EnableEventWaiting, [], None)
_DisableEventWaiting = _wrap(rlapi.DisableEventWaiting, [], None)
_SwapScreenBuffer = _wrap(rlapi.SwapScreenBuffer, [], None)
_PollInputEvents = _wrap(rlapi.PollInputEvents, [], None)
_WaitTime = _wrap(rlapi.WaitTime, [Double], None)
_ShowCursor = _wrap(rlapi.ShowCursor, [], None)
_HideCursor = _wrap(rlapi.HideCursor, [], None)
_IsCursorHidden = _wrap(rlapi.IsCursorHidden, [], Bool)
_EnableCursor = _wrap(rlapi.EnableCursor, [], None)
_DisableCursor = _wrap(rlapi.DisableCursor, [], None)
_IsCursorOnScreen = _wrap(rlapi.IsCursorOnScreen, [], Bool)
_ClearBackground = _wrap(rlapi.ClearBackground, [Color], None)
_BeginDrawing = _wrap(rlapi.BeginDrawing, [], None)
_EndDrawing = _wrap(rlapi.EndDrawing, [], None)
_BeginMode2D = _wrap(rlapi.BeginMode2D, [Camera2D], None)
_EndMode2D = _wrap(rlapi.EndMode2D, [], None)
_BeginMode3D = _wrap(rlapi.BeginMode3D, [Camera3D], None)
_EndMode3D = _wrap(rlapi.EndMode3D, [], None)
_BeginTextureMode = _wrap(rlapi.BeginTextureMode, [RenderTexture2D], None)
_EndTextureMode = _wrap(rlapi.EndTextureMode, [], None)
_BeginShaderMode = _wrap(rlapi.BeginShaderMode, [Shader], None)
_EndShaderMode = _wrap(rlapi.EndShaderMode, [], None)
_BeginBlendMode = _wrap(rlapi.BeginBlendMode, [Int], None)
_EndBlendMode = _wrap(rlapi.EndBlendMode, [], None)
_BeginScissorMode = _wrap(rlapi.BeginScissorMode, [Int, Int, Int, Int], None)
_EndScissorMode = _wrap(rlapi.EndScissorMode, [], None)
_BeginVrStereoMode = _wrap(rlapi.BeginVrStereoMode, [VrStereoConfig], None)
_EndVrStereoMode = _wrap(rlapi.EndVrStereoMode, [], None)
_LoadVrStereoConfig = _wrap(rlapi.LoadVrStereoConfig, [VrDeviceInfo], VrStereoConfig)
_UnloadVrStereoConfig = _wrap(rlapi.UnloadVrStereoConfig, [VrStereoConfig], None)
_LoadShader = _wrap(rlapi.LoadShader, [CharPtr, CharPtr], Shader)
_LoadShaderFromMemory = _wrap(rlapi.LoadShaderFromMemory, [CharPtr, CharPtr], Shader)
_IsShaderReady = _wrap(rlapi.IsShaderReady, [Shader], Bool)
_GetShaderLocation = _wrap(rlapi.GetShaderLocation, [Shader, CharPtr], Int)
_GetShaderLocationAttrib = _wrap(rlapi.GetShaderLocationAttrib, [Shader, CharPtr], Int)
_SetShaderValue = _wrap(rlapi.SetShaderValue, [Shader, Int, VoidPtr, Int], None)
_SetShaderValueV = _wrap(rlapi.SetShaderValueV, [Shader, Int, VoidPtr, Int, Int], None)
_SetShaderValueMatrix = _wrap(rlapi.SetShaderValueMatrix, [Shader, Int, Matrix], None)
_SetShaderValueTexture = _wrap(rlapi.SetShaderValueTexture, [Shader, Int, Texture2D], None)
_UnloadShader = _wrap(rlapi.UnloadShader, [Shader], None)
_GetMouseRay = _wrap(rlapi.GetMouseRay, [Vector2, Camera], Ray)
_GetCameraMatrix = _wrap(rlapi.GetCameraMatrix, [Camera], Matrix)
_GetCameraMatrix2D = _wrap(rlapi.GetCameraMatrix2D, [Camera2D], Matrix)
_GetWorldToScreen = _wrap(rlapi.GetWorldToScreen, [Vector3, Camera], Vector2)
_GetScreenToWorld2D = _wrap(rlapi.GetScreenToWorld2D, [Vector2, Camera2D], Vector2)
_GetWorldToScreenEx = _wrap(rlapi.GetWorldToScreenEx, [Vector3, Camera, Int, Int], Vector2)
_GetWorldToScreen2D = _wrap(rlapi.GetWorldToScreen2D, [Vector2, Camera2D], Vector2)
_SetTargetFPS = _wrap(rlapi.SetTargetFPS, [Int], None)
_GetFPS = _wrap(rlapi.GetFPS, [], Int)
_GetFrameTime = _wrap(rlapi.GetFrameTime, [], Float)
_GetTime = _wrap(rlapi.GetTime, [], Double)
_GetRandomValue = _wrap(rlapi.GetRandomValue, [Int, Int], Int)
_SetRandomSeed = _wrap(rlapi.SetRandomSeed, [UInt], None)
_TakeScreenshot = _wrap(rlapi.TakeScreenshot, [CharPtr], None)
_SetConfigFlags = _wrap(rlapi.SetConfigFlags, [UInt], None)
_TraceLog = _wrap(rlapi.TraceLog, [Int, CharPtr, VoidPtr], None)
_SetTraceLogLevel = _wrap(rlapi.SetTraceLogLevel, [Int], None)
_MemAlloc = _wrap(rlapi.MemAlloc, [UInt], VoidPtr)
_MemRealloc = _wrap(rlapi.MemRealloc, [VoidPtr, UInt], VoidPtr)
_MemFree = _wrap(rlapi.MemFree, [VoidPtr], None)
_OpenURL = _wrap(rlapi.OpenURL, [CharPtr], None)
_SetTraceLogCallback = _wrap(rlapi.SetTraceLogCallback, [TraceLogCallback], None)
_SetLoadFileDataCallback = _wrap(rlapi.SetLoadFileDataCallback, [LoadFileDataCallback], None)
_SetSaveFileDataCallback = _wrap(rlapi.SetSaveFileDataCallback, [SaveFileDataCallback], None)
_SetLoadFileTextCallback = _wrap(rlapi.SetLoadFileTextCallback, [LoadFileTextCallback], None)
_SetSaveFileTextCallback = _wrap(rlapi.SetSaveFileTextCallback, [SaveFileTextCallback], None)
_LoadFileData = _wrap(rlapi.LoadFileData, [CharPtr, UIntPtr], UCharPtr)
_UnloadFileData = _wrap(rlapi.UnloadFileData, [UCharPtr], None)
_SaveFileData = _wrap(rlapi.SaveFileData, [CharPtr, VoidPtr, UInt], Bool)
_ExportDataAsCode = _wrap(rlapi.ExportDataAsCode, [UCharPtr, UInt, CharPtr], Bool)
_LoadFileText = _wrap(rlapi.LoadFileText, [CharPtr], CharPtr)
_UnloadFileText = _wrap(rlapi.UnloadFileText, [CharPtr], None)
_SaveFileText = _wrap(rlapi.SaveFileText, [CharPtr, CharPtr], Bool)
_FileExists = _wrap(rlapi.FileExists, [CharPtr], Bool)
_DirectoryExists = _wrap(rlapi.DirectoryExists, [CharPtr], Bool)
_IsFileExtension = _wrap(rlapi.IsFileExtension, [CharPtr, CharPtr], Bool)
_GetFileLength = _wrap(rlapi.GetFileLength, [CharPtr], Int)
_GetFileExtension = _wrap(rlapi.GetFileExtension, [CharPtr], CharPtr)
_GetFileName = _wrap(rlapi.GetFileName, [CharPtr], CharPtr)
_GetFileNameWithoutExt = _wrap(rlapi.GetFileNameWithoutExt, [CharPtr], CharPtr)
_GetDirectoryPath = _wrap(rlapi.GetDirectoryPath, [CharPtr], CharPtr)
_GetPrevDirectoryPath = _wrap(rlapi.GetPrevDirectoryPath, [CharPtr], CharPtr)
_GetWorkingDirectory = _wrap(rlapi.GetWorkingDirectory, [], CharPtr)
_GetApplicationDirectory = _wrap(rlapi.GetApplicationDirectory, [], CharPtr)
_ChangeDirectory = _wrap(rlapi.ChangeDirectory, [CharPtr], Bool)
_IsPathFile = _wrap(rlapi.IsPathFile, [CharPtr], Bool)
_LoadDirectoryFiles = _wrap(rlapi.LoadDirectoryFiles, [CharPtr], FilePathList)
_LoadDirectoryFilesEx = _wrap(rlapi.LoadDirectoryFilesEx, [CharPtr, CharPtr, Bool], FilePathList)
_UnloadDirectoryFiles = _wrap(rlapi.UnloadDirectoryFiles, [FilePathList], None)
_IsFileDropped = _wrap(rlapi.IsFileDropped, [], Bool)
_LoadDroppedFiles = _wrap(rlapi.LoadDroppedFiles, [], FilePathList)
_UnloadDroppedFiles = _wrap(rlapi.UnloadDroppedFiles, [FilePathList], None)
_GetFileModTime = _wrap(rlapi.GetFileModTime, [CharPtr], Long)
_CompressData = _wrap(rlapi.CompressData, [UCharPtr, Int, IntPtr], UCharPtr)
_DecompressData = _wrap(rlapi.DecompressData, [UCharPtr, Int, IntPtr], UCharPtr)
_EncodeDataBase64 = _wrap(rlapi.EncodeDataBase64, [UCharPtr, Int, IntPtr], CharPtr)
_DecodeDataBase64 = _wrap(rlapi.DecodeDataBase64, [UCharPtr, IntPtr], UCharPtr)
_IsKeyPressed = _wrap(rlapi.IsKeyPressed, [Int], Bool)
_IsKeyDown = _wrap(rlapi.IsKeyDown, [Int], Bool)
_IsKeyReleased = _wrap(rlapi.IsKeyReleased, [Int], Bool)
_IsKeyUp = _wrap(rlapi.IsKeyUp, [Int], Bool)
_SetExitKey = _wrap(rlapi.SetExitKey, [Int], None)
_GetKeyPressed = _wrap(rlapi.GetKeyPressed, [], Int)
_GetCharPressed = _wrap(rlapi.GetCharPressed, [], Int)
_IsGamepadAvailable = _wrap(rlapi.IsGamepadAvailable, [Int], Bool)
_GetGamepadName = _wrap(rlapi.GetGamepadName, [Int], CharPtr)
_IsGamepadButtonPressed = _wrap(rlapi.IsGamepadButtonPressed, [Int, Int], Bool)
_IsGamepadButtonDown = _wrap(rlapi.IsGamepadButtonDown, [Int, Int], Bool)
_IsGamepadButtonReleased = _wrap(rlapi.IsGamepadButtonReleased, [Int, Int], Bool)
_IsGamepadButtonUp = _wrap(rlapi.IsGamepadButtonUp, [Int, Int], Bool)
_GetGamepadButtonPressed = _wrap(rlapi.GetGamepadButtonPressed, [], Int)
_GetGamepadAxisCount = _wrap(rlapi.GetGamepadAxisCount, [Int], Int)
_GetGamepadAxisMovement = _wrap(rlapi.GetGamepadAxisMovement, [Int, Int], Float)
_SetGamepadMappings = _wrap(rlapi.SetGamepadMappings, [CharPtr], Int)
_IsMouseButtonPressed = _wrap(rlapi.IsMouseButtonPressed, [Int], Bool)
_IsMouseButtonDown = _wrap(rlapi.IsMouseButtonDown, [Int], Bool)
_IsMouseButtonReleased = _wrap(rlapi.IsMouseButtonReleased, [Int], Bool)
_IsMouseButtonUp = _wrap(rlapi.IsMouseButtonUp, [Int], Bool)
_GetMouseX = _wrap(rlapi.GetMouseX, [], Int)
_GetMouseY = _wrap(rlapi.GetMouseY, [], Int)
_GetMousePosition = _wrap(rlapi.GetMousePosition, [], Vector2)
_GetMouseDelta = _wrap(rlapi.GetMouseDelta, [], Vector2)
_SetMousePosition = _wrap(rlapi.SetMousePosition, [Int, Int], None)
_SetMouseOffset = _wrap(rlapi.SetMouseOffset, [Int, Int], None)
_SetMouseScale = _wrap(rlapi.SetMouseScale, [Float, Float], None)
_GetMouseWheelMove = _wrap(rlapi.GetMouseWheelMove, [], Float)
_GetMouseWheelMoveV = _wrap(rlapi.GetMouseWheelMoveV, [], Vector2)
_SetMouseCursor = _wrap(rlapi.SetMouseCursor, [Int], None)
_GetTouchX = _wrap(rlapi.GetTouchX, [], Int)
_GetTouchY = _wrap(rlapi.GetTouchY, [], Int)
_GetTouchPosition = _wrap(rlapi.GetTouchPosition, [Int], Vector2)
_GetTouchPointId = _wrap(rlapi.GetTouchPointId, [Int], Int)
_GetTouchPointCount = _wrap(rlapi.GetTouchPointCount, [], Int)
_SetGesturesEnabled = _wrap(rlapi.SetGesturesEnabled, [UInt], None)
_IsGestureDetected = _wrap(rlapi.IsGestureDetected, [Int], Bool)
_GetGestureDetected = _wrap(rlapi.GetGestureDetected, [], Int)
_GetGestureHoldDuration = _wrap(rlapi.GetGestureHoldDuration, [], Float)
_GetGestureDragVector = _wrap(rlapi.GetGestureDragVector, [], Vector2)
_GetGestureDragAngle = _wrap(rlapi.GetGestureDragAngle, [], Float)
_GetGesturePinchVector = _wrap(rlapi.GetGesturePinchVector, [], Vector2)
_GetGesturePinchAngle = _wrap(rlapi.GetGesturePinchAngle, [], Float)
_UpdateCamera = _wrap(rlapi.UpdateCamera, [CameraPtr, Int], None)
_UpdateCameraPro = _wrap(rlapi.UpdateCameraPro, [CameraPtr, Vector3, Vector3, Float], None)
_SetShapesTexture = _wrap(rlapi.SetShapesTexture, [Texture2D, Rectangle], None)
_DrawPixel = _wrap(rlapi.DrawPixel, [Int, Int, Color], None)
_DrawPixelV = _wrap(rlapi.DrawPixelV, [Vector2, Color], None)
_DrawLine = _wrap(rlapi.DrawLine, [Int, Int, Int, Int, Color], None)
_DrawLineV = _wrap(rlapi.DrawLineV, [Vector2, Vector2, Color], None)
_DrawLineEx = _wrap(rlapi.DrawLineEx, [Vector2, Vector2, Float, Color], None)
_DrawLineBezier = _wrap(rlapi.DrawLineBezier, [Vector2, Vector2, Float, Color], None)
_DrawLineBezierQuad = _wrap(rlapi.DrawLineBezierQuad, [Vector2, Vector2, Vector2, Float, Color], None)
_DrawLineBezierCubic = _wrap(rlapi.DrawLineBezierCubic, [Vector2, Vector2, Vector2, Vector2, Float, Color], None)
_DrawLineStrip = _wrap(rlapi.DrawLineStrip, [Vector2Ptr, Int, Color], None)
_DrawCircle = _wrap(rlapi.DrawCircle, [Int, Int, Float, Color], None)
_DrawCircleSector = _wrap(rlapi.DrawCircleSector, [Vector2, Float, Float, Float, Int, Color], None)
_DrawCircleSectorLines = _wrap(rlapi.DrawCircleSectorLines, [Vector2, Float, Float, Float, Int, Color], None)
_DrawCircleGradient = _wrap(rlapi.DrawCircleGradient, [Int, Int, Float, Color, Color], None)
_DrawCircleV = _wrap(rlapi.DrawCircleV, [Vector2, Float, Color], None)
_DrawCircleLines = _wrap(rlapi.DrawCircleLines, [Int, Int, Float, Color], None)
_DrawEllipse = _wrap(rlapi.DrawEllipse, [Int, Int, Float, Float, Color], None)
_DrawEllipseLines = _wrap(rlapi.DrawEllipseLines, [Int, Int, Float, Float, Color], None)
_DrawRing = _wrap(rlapi.DrawRing, [Vector2, Float, Float, Float, Float, Int, Color], None)
_DrawRingLines = _wrap(rlapi.DrawRingLines, [Vector2, Float, Float, Float, Float, Int, Color], None)
_DrawRectangle = _wrap(rlapi.DrawRectangle, [Int, Int, Int, Int, Color], None)
_DrawRectangleV = _wrap(rlapi.DrawRectangleV, [Vector2, Vector2, Color], None)
_DrawRectangleRec = _wrap(rlapi.DrawRectangleRec, [Rectangle, Color], None)
_DrawRectanglePro = _wrap(rlapi.DrawRectanglePro, [Rectangle, Vector2, Float, Color], None)
_DrawRectangleGradientV = _wrap(rlapi.DrawRectangleGradientV, [Int, Int, Int, Int, Color, Color], None)
_DrawRectangleGradientH = _wrap(rlapi.DrawRectangleGradientH, [Int, Int, Int, Int, Color, Color], None)
_DrawRectangleGradientEx = _wrap(rlapi.DrawRectangleGradientEx, [Rectangle, Color, Color, Color, Color], None)
_DrawRectangleLines = _wrap(rlapi.DrawRectangleLines, [Int, Int, Int, Int, Color], None)
_DrawRectangleLinesEx = _wrap(rlapi.DrawRectangleLinesEx, [Rectangle, Float, Color], None)
_DrawRectangleRounded = _wrap(rlapi.DrawRectangleRounded, [Rectangle, Float, Int, Color], None)
_DrawRectangleRoundedLines = _wrap(rlapi.DrawRectangleRoundedLines, [Rectangle, Float, Int, Float, Color], None)
_DrawTriangle = _wrap(rlapi.DrawTriangle, [Vector2, Vector2, Vector2, Color], None)
_DrawTriangleLines = _wrap(rlapi.DrawTriangleLines, [Vector2, Vector2, Vector2, Color], None)
_DrawTriangleFan = _wrap(rlapi.DrawTriangleFan, [Vector2Ptr, Int, Color], None)
_DrawTriangleStrip = _wrap(rlapi.DrawTriangleStrip, [Vector2Ptr, Int, Color], None)
_DrawPoly = _wrap(rlapi.DrawPoly, [Vector2, Int, Float, Float, Color], None)
_DrawPolyLines = _wrap(rlapi.DrawPolyLines, [Vector2, Int, Float, Float, Color], None)
_DrawPolyLinesEx = _wrap(rlapi.DrawPolyLinesEx, [Vector2, Int, Float, Float, Float, Color], None)
_CheckCollisionRecs = _wrap(rlapi.CheckCollisionRecs, [Rectangle, Rectangle], Bool)
_CheckCollisionCircles = _wrap(rlapi.CheckCollisionCircles, [Vector2, Float, Vector2, Float], Bool)
_CheckCollisionCircleRec = _wrap(rlapi.CheckCollisionCircleRec, [Vector2, Float, Rectangle], Bool)
_CheckCollisionPointRec = _wrap(rlapi.CheckCollisionPointRec, [Vector2, Rectangle], Bool)
_CheckCollisionPointCircle = _wrap(rlapi.CheckCollisionPointCircle, [Vector2, Vector2, Float], Bool)
_CheckCollisionPointTriangle = _wrap(rlapi.CheckCollisionPointTriangle, [Vector2, Vector2, Vector2, Vector2], Bool)
_CheckCollisionPointPoly = _wrap(rlapi.CheckCollisionPointPoly, [Vector2, Vector2Ptr, Int], Bool)
_CheckCollisionLines = _wrap(rlapi.CheckCollisionLines, [Vector2, Vector2, Vector2, Vector2, Vector2Ptr], Bool)
_CheckCollisionPointLine = _wrap(rlapi.CheckCollisionPointLine, [Vector2, Vector2, Vector2, Int], Bool)
_GetCollisionRec = _wrap(rlapi.GetCollisionRec, [Rectangle, Rectangle], Rectangle)
_LoadImage = _wrap(rlapi.LoadImage, [CharPtr], Image)
_LoadImageRaw = _wrap(rlapi.LoadImageRaw, [CharPtr, Int, Int, Int, Int], Image)
_LoadImageAnim = _wrap(rlapi.LoadImageAnim, [CharPtr, IntPtr], Image)
_LoadImageFromMemory = _wrap(rlapi.LoadImageFromMemory, [CharPtr, UCharPtr, Int], Image)
_LoadImageFromTexture = _wrap(rlapi.LoadImageFromTexture, [Texture2D], Image)
_LoadImageFromScreen = _wrap(rlapi.LoadImageFromScreen, [], Image)
_IsImageReady = _wrap(rlapi.IsImageReady, [Image], Bool)
_UnloadImage = _wrap(rlapi.UnloadImage, [Image], None)
_ExportImage = _wrap(rlapi.ExportImage, [Image, CharPtr], Bool)
_ExportImageAsCode = _wrap(rlapi.ExportImageAsCode, [Image, CharPtr], Bool)
_GenImageColor = _wrap(rlapi.GenImageColor, [Int, Int, Color], Image)
_GenImageGradientV = _wrap(rlapi.GenImageGradientV, [Int, Int, Color, Color], Image)
_GenImageGradientH = _wrap(rlapi.GenImageGradientH, [Int, Int, Color, Color], Image)
_GenImageGradientRadial = _wrap(rlapi.GenImageGradientRadial, [Int, Int, Float, Color, Color], Image)
_GenImageChecked = _wrap(rlapi.GenImageChecked, [Int, Int, Int, Int, Color, Color], Image)
_GenImageWhiteNoise = _wrap(rlapi.GenImageWhiteNoise, [Int, Int, Float], Image)
_GenImagePerlinNoise = _wrap(rlapi.GenImagePerlinNoise, [Int, Int, Int, Int, Float], Image)
_GenImageCellular = _wrap(rlapi.GenImageCellular, [Int, Int, Int], Image)
_GenImageText = _wrap(rlapi.GenImageText, [Int, Int, CharPtr], Image)
_ImageCopy = _wrap(rlapi.ImageCopy, [Image], Image)
_ImageFromImage = _wrap(rlapi.ImageFromImage, [Image, Rectangle], Image)
_ImageText = _wrap(rlapi.ImageText, [CharPtr, Int, Color], Image)
_ImageTextEx = _wrap(rlapi.ImageTextEx, [Font, CharPtr, Float, Float, Color], Image)
_ImageFormat = _wrap(rlapi.ImageFormat, [ImagePtr, Int], None)
_ImageToPOT = _wrap(rlapi.ImageToPOT, [ImagePtr, Color], None)
_ImageCrop = _wrap(rlapi.ImageCrop, [ImagePtr, Rectangle], None)
_ImageAlphaCrop = _wrap(rlapi.ImageAlphaCrop, [ImagePtr, Float], None)
_ImageAlphaClear = _wrap(rlapi.ImageAlphaClear, [ImagePtr, Color, Float], None)
_ImageAlphaMask = _wrap(rlapi.ImageAlphaMask, [ImagePtr, Image], None)
_ImageAlphaPremultiply = _wrap(rlapi.ImageAlphaPremultiply, [ImagePtr], None)
_ImageBlurGaussian = _wrap(rlapi.ImageBlurGaussian, [ImagePtr, Int], None)
_ImageResize = _wrap(rlapi.ImageResize, [ImagePtr, Int, Int], None)
_ImageResizeNN = _wrap(rlapi.ImageResizeNN, [ImagePtr, Int, Int], None)
_ImageResizeCanvas = _wrap(rlapi.ImageResizeCanvas, [ImagePtr, Int, Int, Int, Int, Color], None)
_ImageMipmaps = _wrap(rlapi.ImageMipmaps, [ImagePtr], None)
_ImageDither = _wrap(rlapi.ImageDither, [ImagePtr, Int, Int, Int, Int], None)
_ImageFlipVertical = _wrap(rlapi.ImageFlipVertical, [ImagePtr], None)
_ImageFlipHorizontal = _wrap(rlapi.ImageFlipHorizontal, [ImagePtr], None)
_ImageRotateCW = _wrap(rlapi.ImageRotateCW, [ImagePtr], None)
_ImageRotateCCW = _wrap(rlapi.ImageRotateCCW, [ImagePtr], None)
_ImageColorTint = _wrap(rlapi.ImageColorTint, [ImagePtr, Color], None)
_ImageColorInvert = _wrap(rlapi.ImageColorInvert, [ImagePtr], None)
_ImageColorGrayscale = _wrap(rlapi.ImageColorGrayscale, [ImagePtr], None)
_ImageColorContrast = _wrap(rlapi.ImageColorContrast, [ImagePtr, Float], None)
_ImageColorBrightness = _wrap(rlapi.ImageColorBrightness, [ImagePtr, Int], None)
_ImageColorReplace = _wrap(rlapi.ImageColorReplace, [ImagePtr, Color, Color], None)
_LoadImageColors = _wrap(rlapi.LoadImageColors, [Image], ColorPtr)
_LoadImagePalette = _wrap(rlapi.LoadImagePalette, [Image, Int, IntPtr], ColorPtr)
_UnloadImageColors = _wrap(rlapi.UnloadImageColors, [ColorPtr], None)
_UnloadImagePalette = _wrap(rlapi.UnloadImagePalette, [ColorPtr], None)
_GetImageAlphaBorder = _wrap(rlapi.GetImageAlphaBorder, [Image, Float], Rectangle)
_GetImageColor = _wrap(rlapi.GetImageColor, [Image, Int, Int], Color)
_ImageClearBackground = _wrap(rlapi.ImageClearBackground, [ImagePtr, Color], None)
_ImageDrawPixel = _wrap(rlapi.ImageDrawPixel, [ImagePtr, Int, Int, Color], None)
_ImageDrawPixelV = _wrap(rlapi.ImageDrawPixelV, [ImagePtr, Vector2, Color], None)
_ImageDrawLine = _wrap(rlapi.ImageDrawLine, [ImagePtr, Int, Int, Int, Int, Color], None)
_ImageDrawLineV = _wrap(rlapi.ImageDrawLineV, [ImagePtr, Vector2, Vector2, Color], None)
_ImageDrawCircle = _wrap(rlapi.ImageDrawCircle, [ImagePtr, Int, Int, Int, Color], None)
_ImageDrawCircleV = _wrap(rlapi.ImageDrawCircleV, [ImagePtr, Vector2, Int, Color], None)
_ImageDrawCircleLines = _wrap(rlapi.ImageDrawCircleLines, [ImagePtr, Int, Int, Int, Color], None)
_ImageDrawCircleLinesV = _wrap(rlapi.ImageDrawCircleLinesV, [ImagePtr, Vector2, Int, Color], None)
_ImageDrawRectangle = _wrap(rlapi.ImageDrawRectangle, [ImagePtr, Int, Int, Int, Int, Color], None)
_ImageDrawRectangleV = _wrap(rlapi.ImageDrawRectangleV, [ImagePtr, Vector2, Vector2, Color], None)
_ImageDrawRectangleRec = _wrap(rlapi.ImageDrawRectangleRec, [ImagePtr, Rectangle, Color], None)
_ImageDrawRectangleLines = _wrap(rlapi.ImageDrawRectangleLines, [ImagePtr, Rectangle, Int, Color], None)
_ImageDraw = _wrap(rlapi.ImageDraw, [ImagePtr, Image, Rectangle, Rectangle, Color], None)
_ImageDrawText = _wrap(rlapi.ImageDrawText, [ImagePtr, CharPtr, Int, Int, Int, Color], None)
_ImageDrawTextEx = _wrap(rlapi.ImageDrawTextEx, [ImagePtr, Font, CharPtr, Vector2, Float, Float, Color], None)
_LoadTexture = _wrap(rlapi.LoadTexture, [CharPtr], Texture2D)
_LoadTextureFromImage = _wrap(rlapi.LoadTextureFromImage, [Image], Texture2D)
_LoadTextureCubemap = _wrap(rlapi.LoadTextureCubemap, [Image, Int], TextureCubemap)
_LoadRenderTexture = _wrap(rlapi.LoadRenderTexture, [Int, Int], RenderTexture2D)
_IsTextureReady = _wrap(rlapi.IsTextureReady, [Texture2D], Bool)
_UnloadTexture = _wrap(rlapi.UnloadTexture, [Texture2D], None)
_IsRenderTextureReady = _wrap(rlapi.IsRenderTextureReady, [RenderTexture2D], Bool)
_UnloadRenderTexture = _wrap(rlapi.UnloadRenderTexture, [RenderTexture2D], None)
_UpdateTexture = _wrap(rlapi.UpdateTexture, [Texture2D, VoidPtr], None)
_UpdateTextureRec = _wrap(rlapi.UpdateTextureRec, [Texture2D, Rectangle, VoidPtr], None)
_GenTextureMipmaps = _wrap(rlapi.GenTextureMipmaps, [Texture2DPtr], None)
_SetTextureFilter = _wrap(rlapi.SetTextureFilter, [Texture2D, Int], None)
_SetTextureWrap = _wrap(rlapi.SetTextureWrap, [Texture2D, Int], None)
_DrawTexture = _wrap(rlapi.DrawTexture, [Texture2D, Int, Int, Color], None)
_DrawTextureV = _wrap(rlapi.DrawTextureV, [Texture2D, Vector2, Color], None)
_DrawTextureEx = _wrap(rlapi.DrawTextureEx, [Texture2D, Vector2, Float, Float, Color], None)
_DrawTextureRec = _wrap(rlapi.DrawTextureRec, [Texture2D, Rectangle, Vector2, Color], None)
_DrawTexturePro = _wrap(rlapi.DrawTexturePro, [Texture2D, Rectangle, Rectangle, Vector2, Float, Color], None)
_DrawTextureNPatch = _wrap(rlapi.DrawTextureNPatch, [Texture2D, NPatchInfo, Rectangle, Vector2, Float, Color], None)
_Fade = _wrap(rlapi.Fade, [Color, Float], Color)
_ColorToInt = _wrap(rlapi.ColorToInt, [Color], Int)
_ColorNormalize = _wrap(rlapi.ColorNormalize, [Color], Vector4)
_ColorFromNormalized = _wrap(rlapi.ColorFromNormalized, [Vector4], Color)
_ColorToHSV = _wrap(rlapi.ColorToHSV, [Color], Vector3)
_ColorFromHSV = _wrap(rlapi.ColorFromHSV, [Float, Float, Float], Color)
_ColorTint = _wrap(rlapi.ColorTint, [Color, Color], Color)
_ColorBrightness = _wrap(rlapi.ColorBrightness, [Color, Float], Color)
_ColorContrast = _wrap(rlapi.ColorContrast, [Color, Float], Color)
_ColorAlpha = _wrap(rlapi.ColorAlpha, [Color, Float], Color)
_ColorAlphaBlend = _wrap(rlapi.ColorAlphaBlend, [Color, Color, Color], Color)
_GetColor = _wrap(rlapi.GetColor, [UInt], Color)
_GetPixelColor = _wrap(rlapi.GetPixelColor, [VoidPtr, Int], Color)
_SetPixelColor = _wrap(rlapi.SetPixelColor, [VoidPtr, Color, Int], None)
_GetPixelDataSize = _wrap(rlapi.GetPixelDataSize, [Int, Int, Int], Int)
_GetFontDefault = _wrap(rlapi.GetFontDefault, [], Font)
_LoadFont = _wrap(rlapi.LoadFont, [CharPtr], Font)
_LoadFontEx = _wrap(rlapi.LoadFontEx, [CharPtr, Int, IntPtr, Int], Font)
_LoadFontFromImage = _wrap(rlapi.LoadFontFromImage, [Image, Color, Int], Font)
_LoadFontFromMemory = _wrap(rlapi.LoadFontFromMemory, [CharPtr, UCharPtr, Int, Int, IntPtr, Int], Font)
_IsFontReady = _wrap(rlapi.IsFontReady, [Font], Bool)
_LoadFontData = _wrap(rlapi.LoadFontData, [UCharPtr, Int, Int, IntPtr, Int, Int], GlyphInfoPtr)
_GenImageFontAtlas = _wrap(rlapi.GenImageFontAtlas, [GlyphInfoPtr, RectanglePtr, Int, Int, Int, Int], Image)
_UnloadFontData = _wrap(rlapi.UnloadFontData, [GlyphInfoPtr, Int], None)
_UnloadFont = _wrap(rlapi.UnloadFont, [Font], None)
_ExportFontAsCode = _wrap(rlapi.ExportFontAsCode, [Font, CharPtr], Bool)
_DrawFPS = _wrap(rlapi.DrawFPS, [Int, Int], None)
_DrawText = _wrap(rlapi.DrawText, [CharPtr, Int, Int, Int, Color], None)
_DrawTextEx = _wrap(rlapi.DrawTextEx, [Font, CharPtr, Vector2, Float, Float, Color], None)
_DrawTextPro = _wrap(rlapi.DrawTextPro, [Font, CharPtr, Vector2, Vector2, Float, Float, Float, Color], None)
_DrawTextCodepoint = _wrap(rlapi.DrawTextCodepoint, [Font, Int, Vector2, Float, Color], None)
_DrawTextCodepoints = _wrap(rlapi.DrawTextCodepoints, [Font, IntPtr, Int, Vector2, Float, Float, Color], None)
_MeasureText = _wrap(rlapi.MeasureText, [CharPtr, Int], Int)
_MeasureTextEx = _wrap(rlapi.MeasureTextEx, [Font, CharPtr, Float, Float], Vector2)
_GetGlyphIndex = _wrap(rlapi.GetGlyphIndex, [Font, Int], Int)
_GetGlyphInfo = _wrap(rlapi.GetGlyphInfo, [Font, Int], GlyphInfo)
_GetGlyphAtlasRec = _wrap(rlapi.GetGlyphAtlasRec, [Font, Int], Rectangle)
_LoadUTF8 = _wrap(rlapi.LoadUTF8, [IntPtr, Int], CharPtr)
_UnloadUTF8 = _wrap(rlapi.UnloadUTF8, [CharPtr], None)
_LoadCodepoints = _wrap(rlapi.LoadCodepoints, [CharPtr, IntPtr], IntPtr)
_UnloadCodepoints = _wrap(rlapi.UnloadCodepoints, [IntPtr], None)
_GetCodepointCount = _wrap(rlapi.GetCodepointCount, [CharPtr], Int)
_GetCodepoint = _wrap(rlapi.GetCodepoint, [CharPtr, IntPtr], Int)
_GetCodepointNext = _wrap(rlapi.GetCodepointNext, [CharPtr, IntPtr], Int)
_GetCodepointPrevious = _wrap(rlapi.GetCodepointPrevious, [CharPtr, IntPtr], Int)
_CodepointToUTF8 = _wrap(rlapi.CodepointToUTF8, [Int, IntPtr], CharPtr)
_TextCopy = _wrap(rlapi.TextCopy, [CharPtr, CharPtr], Int)
_TextIsEqual = _wrap(rlapi.TextIsEqual, [CharPtr, CharPtr], Bool)
_TextLength = _wrap(rlapi.TextLength, [CharPtr], UInt)
_TextFormat = _wrap(rlapi.TextFormat, [CharPtr, VoidPtr], CharPtr)
_TextSubtext = _wrap(rlapi.TextSubtext, [CharPtr, Int, Int], CharPtr)
_TextReplace = _wrap(rlapi.TextReplace, [CharPtr, CharPtr, CharPtr], CharPtr)
_TextInsert = _wrap(rlapi.TextInsert, [CharPtr, CharPtr, Int], CharPtr)
_TextJoin = _wrap(rlapi.TextJoin, [CharPtrPtr, Int, CharPtr], CharPtr)
_TextSplit = _wrap(rlapi.TextSplit, [CharPtr, Char, IntPtr], CharPtrPtr)
_TextAppend = _wrap(rlapi.TextAppend, [CharPtr, CharPtr, IntPtr], None)
_TextFindIndex = _wrap(rlapi.TextFindIndex, [CharPtr, CharPtr], Int)
_TextToUpper = _wrap(rlapi.TextToUpper, [CharPtr], CharPtr)
_TextToLower = _wrap(rlapi.TextToLower, [CharPtr], CharPtr)
_TextToPascal = _wrap(rlapi.TextToPascal, [CharPtr], CharPtr)
_TextToInteger = _wrap(rlapi.TextToInteger, [CharPtr], Int)
_DrawLine3D = _wrap(rlapi.DrawLine3D, [Vector3, Vector3, Color], None)
_DrawPoint3D = _wrap(rlapi.DrawPoint3D, [Vector3, Color], None)
_DrawCircle3D = _wrap(rlapi.DrawCircle3D, [Vector3, Float, Vector3, Float, Color], None)
_DrawTriangle3D = _wrap(rlapi.DrawTriangle3D, [Vector3, Vector3, Vector3, Color], None)
_DrawTriangleStrip3D = _wrap(rlapi.DrawTriangleStrip3D, [Vector3Ptr, Int, Color], None)
_DrawCube = _wrap(rlapi.DrawCube, [Vector3, Float, Float, Float, Color], None)
_DrawCubeV = _wrap(rlapi.DrawCubeV, [Vector3, Vector3, Color], None)
_DrawCubeWires = _wrap(rlapi.DrawCubeWires, [Vector3, Float, Float, Float, Color], None)
_DrawCubeWiresV = _wrap(rlapi.DrawCubeWiresV, [Vector3, Vector3, Color], None)
_DrawSphere = _wrap(rlapi.DrawSphere, [Vector3, Float, Color], None)
_DrawSphereEx = _wrap(rlapi.DrawSphereEx, [Vector3, Float, Int, Int, Color], None)
_DrawSphereWires = _wrap(rlapi.DrawSphereWires, [Vector3, Float, Int, Int, Color], None)
_DrawCylinder = _wrap(rlapi.DrawCylinder, [Vector3, Float, Float, Float, Int, Color], None)
_DrawCylinderEx = _wrap(rlapi.DrawCylinderEx, [Vector3, Vector3, Float, Float, Int, Color], None)
_DrawCylinderWires = _wrap(rlapi.DrawCylinderWires, [Vector3, Float, Float, Float, Int, Color], None)
_DrawCylinderWiresEx = _wrap(rlapi.DrawCylinderWiresEx, [Vector3, Vector3, Float, Float, Int, Color], None)
_DrawCapsule = _wrap(rlapi.DrawCapsule, [Vector3, Vector3, Float, Int, Int, Color], None)
_DrawCapsuleWires = _wrap(rlapi.DrawCapsuleWires, [Vector3, Vector3, Float, Int, Int, Color], None)
_DrawPlane = _wrap(rlapi.DrawPlane, [Vector3, Vector2, Color], None)
_DrawRay = _wrap(rlapi.DrawRay, [Ray, Color], None)
_DrawGrid = _wrap(rlapi.DrawGrid, [Int, Float], None)
_LoadModel = _wrap(rlapi.LoadModel, [CharPtr], Model)
_LoadModelFromMesh = _wrap(rlapi.LoadModelFromMesh, [Mesh], Model)
_IsModelReady = _wrap(rlapi.IsModelReady, [Model], Bool)
_UnloadModel = _wrap(rlapi.UnloadModel, [Model], None)
_GetModelBoundingBox = _wrap(rlapi.GetModelBoundingBox, [Model], BoundingBox)
_DrawModel = _wrap(rlapi.DrawModel, [Model, Vector3, Float, Color], None)
_DrawModelEx = _wrap(rlapi.DrawModelEx, [Model, Vector3, Vector3, Float, Vector3, Color], None)
_DrawModelWires = _wrap(rlapi.DrawModelWires, [Model, Vector3, Float, Color], None)
_DrawModelWiresEx = _wrap(rlapi.DrawModelWiresEx, [Model, Vector3, Vector3, Float, Vector3, Color], None)
_DrawBoundingBox = _wrap(rlapi.DrawBoundingBox, [BoundingBox, Color], None)
_DrawBillboard = _wrap(rlapi.DrawBillboard, [Camera, Texture2D, Vector3, Float, Color], None)
_DrawBillboardRec = _wrap(rlapi.DrawBillboardRec, [Camera, Texture2D, Rectangle, Vector3, Vector2, Color], None)
_DrawBillboardPro = _wrap(rlapi.DrawBillboardPro, [Camera, Texture2D, Rectangle, Vector3, Vector3, Vector2, Vector2, Float, Color], None)
_UploadMesh = _wrap(rlapi.UploadMesh, [MeshPtr, Bool], None)
_UpdateMeshBuffer = _wrap(rlapi.UpdateMeshBuffer, [Mesh, Int, VoidPtr, Int, Int], None)
_UnloadMesh = _wrap(rlapi.UnloadMesh, [Mesh], None)
_DrawMesh = _wrap(rlapi.DrawMesh, [Mesh, Material, Matrix], None)
_DrawMeshInstanced = _wrap(rlapi.DrawMeshInstanced, [Mesh, Material, MatrixPtr, Int], None)
_ExportMesh = _wrap(rlapi.ExportMesh, [Mesh, CharPtr], Bool)
_GetMeshBoundingBox = _wrap(rlapi.GetMeshBoundingBox, [Mesh], BoundingBox)
_GenMeshTangents = _wrap(rlapi.GenMeshTangents, [MeshPtr], None)
_GenMeshPoly = _wrap(rlapi.GenMeshPoly, [Int, Float], Mesh)
_GenMeshPlane = _wrap(rlapi.GenMeshPlane, [Float, Float, Int, Int], Mesh)
_GenMeshCube = _wrap(rlapi.GenMeshCube, [Float, Float, Float], Mesh)
_GenMeshSphere = _wrap(rlapi.GenMeshSphere, [Float, Int, Int], Mesh)
_GenMeshHemiSphere = _wrap(rlapi.GenMeshHemiSphere, [Float, Int, Int], Mesh)
_GenMeshCylinder = _wrap(rlapi.GenMeshCylinder, [Float, Float, Int], Mesh)
_GenMeshCone = _wrap(rlapi.GenMeshCone, [Float, Float, Int], Mesh)
_GenMeshTorus = _wrap(rlapi.GenMeshTorus, [Float, Float, Int, Int], Mesh)
_GenMeshKnot = _wrap(rlapi.GenMeshKnot, [Float, Float, Int, Int], Mesh)
_GenMeshHeightmap = _wrap(rlapi.GenMeshHeightmap, [Image, Vector3], Mesh)
_GenMeshCubicmap = _wrap(rlapi.GenMeshCubicmap, [Image, Vector3], Mesh)
_LoadMaterials = _wrap(rlapi.LoadMaterials, [CharPtr, IntPtr], MaterialPtr)
_LoadMaterialDefault = _wrap(rlapi.LoadMaterialDefault, [], Material)
_IsMaterialReady = _wrap(rlapi.IsMaterialReady, [Material], Bool)
_UnloadMaterial = _wrap(rlapi.UnloadMaterial, [Material], None)
_SetMaterialTexture = _wrap(rlapi.SetMaterialTexture, [MaterialPtr, Int, Texture2D], None)
_SetModelMeshMaterial = _wrap(rlapi.SetModelMeshMaterial, [ModelPtr, Int, Int], None)
_LoadModelAnimations = _wrap(rlapi.LoadModelAnimations, [CharPtr, UIntPtr], ModelAnimationPtr)
_UpdateModelAnimation = _wrap(rlapi.UpdateModelAnimation, [Model, ModelAnimation, Int], None)
_UnloadModelAnimation = _wrap(rlapi.UnloadModelAnimation, [ModelAnimation], None)
_UnloadModelAnimations = _wrap(rlapi.UnloadModelAnimations, [ModelAnimationPtr, UInt], None)
_IsModelAnimationValid = _wrap(rlapi.IsModelAnimationValid, [Model, ModelAnimation], Bool)
_CheckCollisionSpheres = _wrap(rlapi.CheckCollisionSpheres, [Vector3, Float, Vector3, Float], Bool)
_CheckCollisionBoxes = _wrap(rlapi.CheckCollisionBoxes, [BoundingBox, BoundingBox], Bool)
_CheckCollisionBoxSphere = _wrap(rlapi.CheckCollisionBoxSphere, [BoundingBox, Vector3, Float], Bool)
_GetRayCollisionSphere = _wrap(rlapi.GetRayCollisionSphere, [Ray, Vector3, Float], RayCollision)
_GetRayCollisionBox = _wrap(rlapi.GetRayCollisionBox, [Ray, BoundingBox], RayCollision)
_GetRayCollisionMesh = _wrap(rlapi.GetRayCollisionMesh, [Ray, Mesh, Matrix], RayCollision)
_GetRayCollisionTriangle = _wrap(rlapi.GetRayCollisionTriangle, [Ray, Vector3, Vector3, Vector3], RayCollision)
_GetRayCollisionQuad = _wrap(rlapi.GetRayCollisionQuad, [Ray, Vector3, Vector3, Vector3, Vector3], RayCollision)
_InitAudioDevice = _wrap(rlapi.InitAudioDevice, [], None)
_CloseAudioDevice = _wrap(rlapi.CloseAudioDevice, [], None)
_IsAudioDeviceReady = _wrap(rlapi.IsAudioDeviceReady, [], Bool)
_SetMasterVolume = _wrap(rlapi.SetMasterVolume, [Float], None)
_LoadWave = _wrap(rlapi.LoadWave, [CharPtr], Wave)
_LoadWaveFromMemory = _wrap(rlapi.LoadWaveFromMemory, [CharPtr, UCharPtr, Int], Wave)
_IsWaveReady = _wrap(rlapi.IsWaveReady, [Wave], Bool)
_LoadSound = _wrap(rlapi.LoadSound, [CharPtr], Sound)
_LoadSoundFromWave = _wrap(rlapi.LoadSoundFromWave, [Wave], Sound)
_IsSoundReady = _wrap(rlapi.IsSoundReady, [Sound], Bool)
_UpdateSound = _wrap(rlapi.UpdateSound, [Sound, VoidPtr, Int], None)
_UnloadWave = _wrap(rlapi.UnloadWave, [Wave], None)
_UnloadSound = _wrap(rlapi.UnloadSound, [Sound], None)
_ExportWave = _wrap(rlapi.ExportWave, [Wave, CharPtr], Bool)
_ExportWaveAsCode = _wrap(rlapi.ExportWaveAsCode, [Wave, CharPtr], Bool)
_PlaySound = _wrap(rlapi.PlaySound, [Sound], None)
_StopSound = _wrap(rlapi.StopSound, [Sound], None)
_PauseSound = _wrap(rlapi.PauseSound, [Sound], None)
_ResumeSound = _wrap(rlapi.ResumeSound, [Sound], None)
_IsSoundPlaying = _wrap(rlapi.IsSoundPlaying, [Sound], Bool)
_SetSoundVolume = _wrap(rlapi.SetSoundVolume, [Sound, Float], None)
_SetSoundPitch = _wrap(rlapi.SetSoundPitch, [Sound, Float], None)
_SetSoundPan = _wrap(rlapi.SetSoundPan, [Sound, Float], None)
_WaveCopy = _wrap(rlapi.WaveCopy, [Wave], Wave)
_WaveCrop = _wrap(rlapi.WaveCrop, [WavePtr, Int, Int], None)
_WaveFormat = _wrap(rlapi.WaveFormat, [WavePtr, Int, Int, Int], None)
_LoadWaveSamples = _wrap(rlapi.LoadWaveSamples, [Wave], FloatPtr)
_UnloadWaveSamples = _wrap(rlapi.UnloadWaveSamples, [FloatPtr], None)
_LoadMusicStream = _wrap(rlapi.LoadMusicStream, [CharPtr], Music)
_LoadMusicStreamFromMemory = _wrap(rlapi.LoadMusicStreamFromMemory, [CharPtr, UCharPtr, Int], Music)
_IsMusicReady = _wrap(rlapi.IsMusicReady, [Music], Bool)
_UnloadMusicStream = _wrap(rlapi.UnloadMusicStream, [Music], None)
_PlayMusicStream = _wrap(rlapi.PlayMusicStream, [Music], None)
_IsMusicStreamPlaying = _wrap(rlapi.IsMusicStreamPlaying, [Music], Bool)
_UpdateMusicStream = _wrap(rlapi.UpdateMusicStream, [Music], None)
_StopMusicStream = _wrap(rlapi.StopMusicStream, [Music], None)
_PauseMusicStream = _wrap(rlapi.PauseMusicStream, [Music], None)
_ResumeMusicStream = _wrap(rlapi.ResumeMusicStream, [Music], None)
_SeekMusicStream = _wrap(rlapi.SeekMusicStream, [Music, Float], None)
_SetMusicVolume = _wrap(rlapi.SetMusicVolume, [Music, Float], None)
_SetMusicPitch = _wrap(rlapi.SetMusicPitch, [Music, Float], None)
_SetMusicPan = _wrap(rlapi.SetMusicPan, [Music, Float], None)
_GetMusicTimeLength = _wrap(rlapi.GetMusicTimeLength, [Music], Float)
_GetMusicTimePlayed = _wrap(rlapi.GetMusicTimePlayed, [Music], Float)
_LoadAudioStream = _wrap(rlapi.LoadAudioStream, [UInt, UInt, UInt], AudioStream)
_IsAudioStreamReady = _wrap(rlapi.IsAudioStreamReady, [AudioStream], Bool)
_UnloadAudioStream = _wrap(rlapi.UnloadAudioStream, [AudioStream], None)
_UpdateAudioStream = _wrap(rlapi.UpdateAudioStream, [AudioStream, VoidPtr, Int], None)
_IsAudioStreamProcessed = _wrap(rlapi.IsAudioStreamProcessed, [AudioStream], Bool)
_PlayAudioStream = _wrap(rlapi.PlayAudioStream, [AudioStream], None)
_PauseAudioStream = _wrap(rlapi.PauseAudioStream, [AudioStream], None)
_ResumeAudioStream = _wrap(rlapi.ResumeAudioStream, [AudioStream], None)
_IsAudioStreamPlaying = _wrap(rlapi.IsAudioStreamPlaying, [AudioStream], Bool)
_StopAudioStream = _wrap(rlapi.StopAudioStream, [AudioStream], None)
_SetAudioStreamVolume = _wrap(rlapi.SetAudioStreamVolume, [AudioStream, Float], None)
_SetAudioStreamPitch = _wrap(rlapi.SetAudioStreamPitch, [AudioStream, Float], None)
_SetAudioStreamPan = _wrap(rlapi.SetAudioStreamPan, [AudioStream, Float], None)
_SetAudioStreamBufferSizeDefault = _wrap(rlapi.SetAudioStreamBufferSizeDefault, [Int], None)
_SetAudioStreamCallback = _wrap(rlapi.SetAudioStreamCallback, [AudioStream, AudioCallback], None)
_AttachAudioStreamProcessor = _wrap(rlapi.AttachAudioStreamProcessor, [AudioStream, AudioCallback], None)
_DetachAudioStreamProcessor = _wrap(rlapi.DetachAudioStreamProcessor, [AudioStream, AudioCallback], None)
_AttachAudioMixedProcessor = _wrap(rlapi.AttachAudioMixedProcessor, [AudioCallback], None)
_DetachAudioMixedProcessor = _wrap(rlapi.DetachAudioMixedProcessor, [AudioCallback], None)


def InitWindow(width, height, title):
    """Initialize window and OpenGL context"""
    _InitWindow(int(width), int(height), _str_in(title))


def WindowShouldClose():
    """Check if KEY_ESCAPE pressed or Close icon pressed"""
    result = _WindowShouldClose()
    return result


def CloseWindow():
    """Close window and unload OpenGL context"""
    _CloseWindow()


def IsWindowReady():
    """Check if window has been initialized successfully"""
    result = _IsWindowReady()
    return result


def IsWindowFullscreen():
    """Check if window is currently fullscreen"""
    result = _IsWindowFullscreen()
    return result


def IsWindowHidden():
    """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
    result = _IsWindowHidden()
    return result


def IsWindowMinimized():
    """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
    result = _IsWindowMinimized()
    return result


def IsWindowMaximized():
    """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
    result = _IsWindowMaximized()
    return result


def IsWindowFocused():
    """Check if window is currently focused (only PLATFORM_DESKTOP)"""
    result = _IsWindowFocused()
    return result


def IsWindowResized():
    """Check if window has been resized last frame"""
    result = _IsWindowResized()
    return result


def IsWindowState(flag):
    """Check if one specific window flag is enabled"""
    result = _IsWindowState(flag)
    return result


def SetWindowState(flags):
    """Set window configuration state using flags (only PLATFORM_DESKTOP)"""
    _SetWindowState(flags)


def ClearWindowState(flags):
    """Clear window configuration state flags"""
    _ClearWindowState(flags)


def ToggleFullscreen():
    """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
    _ToggleFullscreen()


def MaximizeWindow():
    """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
    _MaximizeWindow()


def MinimizeWindow():
    """Set window state: minimized, if resizable (only PLATFORM_DESKTOP)"""
    _MinimizeWindow()


def RestoreWindow():
    """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
    _RestoreWindow()


def SetWindowIcon(image):
    """Set icon for window (single image, RGBA 32bit, only PLATFORM_DESKTOP)"""
    _SetWindowIcon(image)


def SetWindowIcons(images, count):
    """Set icon for window (multiple images, RGBA 32bit, only PLATFORM_DESKTOP)"""
    _SetWindowIcons(images, int(count))


def SetWindowTitle(title):
    """Set title for window (only PLATFORM_DESKTOP)"""
    _SetWindowTitle(_str_in(title))


def SetWindowPosition(x, y):
    """Set window position on screen (only PLATFORM_DESKTOP)"""
    _SetWindowPosition(int(x), int(y))


def SetWindowMonitor(monitor):
    """Set monitor for the current window (fullscreen mode)"""
    _SetWindowMonitor(int(monitor))


def SetWindowMinSize(width, height):
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
    _SetWindowMinSize(int(width), int(height))


def SetWindowSize(width, height):
    """Set window dimensions"""
    _SetWindowSize(int(width), int(height))


def SetWindowOpacity(opacity):
    """Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)"""
    _SetWindowOpacity(float(opacity))


def GetWindowHandle():
    """Get native window handle"""
    _GetWindowHandle()


def GetScreenWidth():
    """Get current screen width"""
    result = _GetScreenWidth()
    return result


def GetScreenHeight():
    """Get current screen height"""
    result = _GetScreenHeight()
    return result


def GetRenderWidth():
    """Get current render width (it considers HiDPI)"""
    result = _GetRenderWidth()
    return result


def GetRenderHeight():
    """Get current render height (it considers HiDPI)"""
    result = _GetRenderHeight()
    return result


def GetMonitorCount():
    """Get number of connected monitors"""
    result = _GetMonitorCount()
    return result


def GetCurrentMonitor():
    """Get current connected monitor"""
    result = _GetCurrentMonitor()
    return result


def GetMonitorPosition(monitor):
    """Get specified monitor position"""
    result = _GetMonitorPosition(int(monitor))
    return result


def GetMonitorWidth(monitor):
    """Get specified monitor width (current video mode used by monitor)"""
    result = _GetMonitorWidth(int(monitor))
    return result


def GetMonitorHeight(monitor):
    """Get specified monitor height (current video mode used by monitor)"""
    result = _GetMonitorHeight(int(monitor))
    return result


def GetMonitorPhysicalWidth(monitor):
    """Get specified monitor physical width in millimetres"""
    result = _GetMonitorPhysicalWidth(int(monitor))
    return result


def GetMonitorPhysicalHeight(monitor):
    """Get specified monitor physical height in millimetres"""
    result = _GetMonitorPhysicalHeight(int(monitor))
    return result


def GetMonitorRefreshRate(monitor):
    """Get specified monitor refresh rate"""
    result = _GetMonitorRefreshRate(int(monitor))
    return result


def GetWindowPosition():
    """Get window position XY on monitor"""
    result = _GetWindowPosition()
    return result


def GetWindowScaleDPI():
    """Get window scale DPI factor"""
    result = _GetWindowScaleDPI()
    return result


def GetMonitorName(monitor):
    """Get the human-readable, UTF-8 encoded name of the primary monitor"""
    result = _ptr_out(_GetMonitorName(int(monitor)))
    return result


def SetClipboardText(text):
    """Set clipboard text content"""
    _SetClipboardText(_str_in(text))


def GetClipboardText():
    """Get clipboard text content"""
    result = _ptr_out(_GetClipboardText())
    return result


def EnableEventWaiting():
    """Enable waiting for events on EndDrawing(), no automatic event polling"""
    _EnableEventWaiting()


def DisableEventWaiting():
    """Disable waiting for events on EndDrawing(), automatic events polling"""
    _DisableEventWaiting()


def SwapScreenBuffer():
    """Swap back buffer with front buffer (screen drawing)"""
    _SwapScreenBuffer()


def PollInputEvents():
    """Register all input events"""
    _PollInputEvents()


def WaitTime(seconds):
    """Wait for some time (halt program execution)"""
    _WaitTime(float(seconds))


def ShowCursor():
    """Shows cursor"""
    _ShowCursor()


def HideCursor():
    """Hides cursor"""
    _HideCursor()


def IsCursorHidden():
    """Check if cursor is not visible"""
    result = _IsCursorHidden()
    return result


def EnableCursor():
    """Enables cursor (unlock cursor)"""
    _EnableCursor()


def DisableCursor():
    """Disables cursor (lock cursor)"""
    _DisableCursor()


def IsCursorOnScreen():
    """Check if cursor is on the screen"""
    result = _IsCursorOnScreen()
    return result


def ClearBackground(color):
    """Set background color (framebuffer clear color)"""
    _ClearBackground(_color(color))


def BeginDrawing():
    """Setup canvas (framebuffer) to start drawing"""
    _BeginDrawing()


def EndDrawing():
    """End canvas drawing and swap buffers (double buffering)"""
    _EndDrawing()


def BeginMode2D(camera):
    """Begin 2D mode with custom camera (2D)"""
    _BeginMode2D(camera)


def EndMode2D():
    """Ends 2D mode with custom camera"""
    _EndMode2D()


def BeginMode3D(camera):
    """Begin 3D mode with custom camera (3D)"""
    _BeginMode3D(camera)


def EndMode3D():
    """Ends 3D mode and returns to default 2D orthographic mode"""
    _EndMode3D()


def BeginTextureMode(target):
    """Begin drawing to render texture"""
    _BeginTextureMode(target)


def EndTextureMode():
    """Ends drawing to render texture"""
    _EndTextureMode()


def BeginShaderMode(shader):
    """Begin custom shader drawing"""
    _BeginShaderMode(shader)


def EndShaderMode():
    """End custom shader drawing (use default shader)"""
    _EndShaderMode()


def BeginBlendMode(mode):
    """Begin blending mode (alpha, additive, multiplied, subtract, custom)"""
    _BeginBlendMode(int(mode))


def EndBlendMode():
    """End blending mode (reset to default: alpha blending)"""
    _EndBlendMode()


def BeginScissorMode(x, y, width, height):
    """Begin scissor mode (define screen area for following drawing)"""
    _BeginScissorMode(int(x), int(y), int(width), int(height))


def EndScissorMode():
    """End scissor mode"""
    _EndScissorMode()


def BeginVrStereoMode(config):
    """Begin stereo rendering (requires VR simulator)"""
    _BeginVrStereoMode(config)


def EndVrStereoMode():
    """End stereo rendering (requires VR simulator)"""
    _EndVrStereoMode()


def LoadVrStereoConfig(device):
    """Load VR stereo config for VR simulator device parameters"""
    result = _LoadVrStereoConfig(device)
    return result


def UnloadVrStereoConfig(config):
    """Unload VR stereo config"""
    _UnloadVrStereoConfig(config)


def LoadShader(vsFileName, fsFileName):
    """Load shader from files and bind default locations"""
    result = _LoadShader(_str_in(vsFileName), _str_in(fsFileName))
    return result


def LoadShaderFromMemory(vsCode, fsCode):
    """Load shader from code strings and bind default locations"""
    result = _LoadShaderFromMemory(_str_in(vsCode), _str_in(fsCode))
    return result


def IsShaderReady(shader):
    """Check if a shader is ready"""
    result = _IsShaderReady(shader)
    return result


def GetShaderLocation(shader, uniformName):
    """Get shader uniform location"""
    result = _GetShaderLocation(shader, _str_in(uniformName))
    return result


def GetShaderLocationAttrib(shader, attribName):
    """Get shader attribute location"""
    result = _GetShaderLocationAttrib(shader, _str_in(attribName))
    return result


def SetShaderValue(shader, locIndex, value, uniformType):
    """Set shader uniform value"""
    _SetShaderValue(shader, int(locIndex), value, int(uniformType))


def SetShaderValueV(shader, locIndex, value, uniformType, count):
    """Set shader uniform value vector"""
    _SetShaderValueV(shader, int(locIndex), value, int(uniformType), int(count))


def SetShaderValueMatrix(shader, locIndex, mat):
    """Set shader uniform value (matrix 4x4)"""
    _SetShaderValueMatrix(shader, int(locIndex), mat)


def SetShaderValueTexture(shader, locIndex, texture):
    """Set shader uniform value for texture (sampler2d)"""
    _SetShaderValueTexture(shader, int(locIndex), texture)


def UnloadShader(shader):
    """Unload shader from GPU memory (VRAM)"""
    _UnloadShader(shader)


def GetMouseRay(mousePosition, camera):
    """Get a ray trace from mouse position"""
    result = _GetMouseRay(_vec2(mousePosition), camera)
    return result


def GetCameraMatrix(camera):
    """Get camera transform matrix (view matrix)"""
    result = _GetCameraMatrix(camera)
    return result


def GetCameraMatrix2D(camera):
    """Get camera 2d transform matrix"""
    result = _GetCameraMatrix2D(camera)
    return result


def GetWorldToScreen(position, camera):
    """Get the screen space position for a 3d world space position"""
    result = _GetWorldToScreen(_vec3(position), camera)
    return result


def GetScreenToWorld2D(position, camera):
    """Get the world space position for a 2d camera screen space position"""
    result = _GetScreenToWorld2D(_vec2(position), camera)
    return result


def GetWorldToScreenEx(position, camera, width, height):
    """Get size position for a 3d world space position"""
    result = _GetWorldToScreenEx(_vec3(position), camera, int(width), int(height))
    return result


def GetWorldToScreen2D(position, camera):
    """Get the screen space position for a 2d camera world space position"""
    result = _GetWorldToScreen2D(_vec2(position), camera)
    return result


def SetTargetFPS(fps):
    """Set target FPS (maximum)"""
    _SetTargetFPS(int(fps))


def GetFPS():
    """Get current FPS"""
    result = _GetFPS()
    return result


def GetFrameTime():
    """Get time in seconds for last frame drawn (delta time)"""
    result = _GetFrameTime()
    return result


def GetTime():
    """Get elapsed time in seconds since InitWindow()"""
    result = _GetTime()
    return result


def GetRandomValue(min, max):
    """Get a random value between min and max (both included)"""
    result = _GetRandomValue(int(min), int(max))
    return result


def SetRandomSeed(seed):
    """Set the seed for the random number generator"""
    _SetRandomSeed(seed)


def TakeScreenshot(fileName):
    """Takes a screenshot of current screen (filename extension defines format)"""
    _TakeScreenshot(_str_in(fileName))


def SetConfigFlags(flags):
    """Setup init configuration flags (view FLAGS)"""
    _SetConfigFlags(flags)


def TraceLog(logLevel, text, args):
    """Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)"""
    _TraceLog(int(logLevel), _str_in(text), args)


def SetTraceLogLevel(logLevel):
    """Set the current threshold (minimum) log level"""
    _SetTraceLogLevel(int(logLevel))


def MemAlloc(size):
    """Internal memory allocator"""
    _MemAlloc(size)


def MemRealloc(ptr, size):
    """Internal memory reallocator"""
    _MemRealloc(ptr, size)


def MemFree(ptr):
    """Internal memory free"""
    _MemFree(ptr)


def OpenURL(url):
    """Open URL with default system browser (if available)"""
    _OpenURL(_str_in(url))


def SetTraceLogCallback(callback):
    """Set custom trace log"""
    _SetTraceLogCallback(callback)


def SetLoadFileDataCallback(callback):
    """Set custom file binary data loader"""
    _SetLoadFileDataCallback(callback)


def SetSaveFileDataCallback(callback):
    """Set custom file binary data saver"""
    _SetSaveFileDataCallback(callback)


def SetLoadFileTextCallback(callback):
    """Set custom file text data loader"""
    _SetLoadFileTextCallback(callback)


def SetSaveFileTextCallback(callback):
    """Set custom file text data saver"""
    _SetSaveFileTextCallback(callback)


def LoadFileData(fileName, bytesRead):
    """Load file data as byte array (read)"""
    result = _ptr_out(_LoadFileData(_str_in(fileName), bytesRead))
    return result


def UnloadFileData(data):
    """Unload file data allocated by LoadFileData()"""
    _UnloadFileData(_str_in(data))


def SaveFileData(fileName, data, bytesToWrite):
    """Save data to file from byte array (write), returns true on success"""
    result = _SaveFileData(_str_in(fileName), data, bytesToWrite)
    return result


def ExportDataAsCode(data, size, fileName):
    """Export data to code (.h), returns true on success"""
    result = _ExportDataAsCode(_str_in(data), size, _str_in(fileName))
    return result


def LoadFileText(fileName):
    """Load text data from file (read), returns a '\0' terminated string"""
    result = _ptr_out(_LoadFileText(_str_in(fileName)))
    return result


def UnloadFileText(text):
    """Unload file text data allocated by LoadFileText()"""
    _UnloadFileText(_str_in(text))


def SaveFileText(fileName, text):
    """Save text data to file (write), string must be '\0' terminated, returns true on success"""
    result = _SaveFileText(_str_in(fileName), _str_in(text))
    return result


def FileExists(fileName):
    """Check if file exists"""
    result = _FileExists(_str_in(fileName))
    return result


def DirectoryExists(dirPath):
    """Check if a directory path exists"""
    result = _DirectoryExists(_str_in(dirPath))
    return result


def IsFileExtension(fileName, ext):
    """Check file extension (including point: .png, .wav)"""
    result = _IsFileExtension(_str_in(fileName), _str_in(ext))
    return result


def GetFileLength(fileName):
    """Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)"""
    result = _GetFileLength(_str_in(fileName))
    return result


def GetFileExtension(fileName):
    """Get pointer to extension for a filename string (includes dot: '.png')"""
    result = _ptr_out(_GetFileExtension(_str_in(fileName)))
    return result


def GetFileName(filePath):
    """Get pointer to filename for a path string"""
    result = _ptr_out(_GetFileName(_str_in(filePath)))
    return result


def GetFileNameWithoutExt(filePath):
    """Get filename string without extension (uses static string)"""
    result = _ptr_out(_GetFileNameWithoutExt(_str_in(filePath)))
    return result


def GetDirectoryPath(filePath):
    """Get full path for a given fileName with path (uses static string)"""
    result = _ptr_out(_GetDirectoryPath(_str_in(filePath)))
    return result


def GetPrevDirectoryPath(dirPath):
    """Get previous directory path for a given path (uses static string)"""
    result = _ptr_out(_GetPrevDirectoryPath(_str_in(dirPath)))
    return result


def GetWorkingDirectory():
    """Get current working directory (uses static string)"""
    result = _ptr_out(_GetWorkingDirectory())
    return result


def GetApplicationDirectory():
    """Get the directory if the running application (uses static string)"""
    result = _ptr_out(_GetApplicationDirectory())
    return result


def ChangeDirectory(dir):
    """Change working directory, return true on success"""
    result = _ChangeDirectory(_str_in(dir))
    return result


def IsPathFile(path):
    """Check if a given path is a file or a directory"""
    result = _IsPathFile(_str_in(path))
    return result


def LoadDirectoryFiles(dirPath):
    """Load directory filepaths"""
    result = _LoadDirectoryFiles(_str_in(dirPath))
    return result


def LoadDirectoryFilesEx(basePath, filter, scanSubdirs):
    """Load directory filepaths with extension filtering and recursive directory scan"""
    result = _LoadDirectoryFilesEx(_str_in(basePath), _str_in(filter), bool(scanSubdirs))
    return result


def UnloadDirectoryFiles(files):
    """Unload filepaths"""
    _UnloadDirectoryFiles(files)


def IsFileDropped():
    """Check if a file has been dropped into window"""
    result = _IsFileDropped()
    return result


def LoadDroppedFiles():
    """Load dropped filepaths"""
    result = _LoadDroppedFiles()
    return result


def UnloadDroppedFiles(files):
    """Unload dropped filepaths"""
    _UnloadDroppedFiles(files)


def GetFileModTime(fileName):
    """Get file modification time (last write time)"""
    result = _GetFileModTime(_str_in(fileName))
    return result


def CompressData(data, dataSize, compDataSize):
    """Compress data (DEFLATE algorithm), memory must be MemFree()"""
    result = _ptr_out(_CompressData(_str_in(data), int(dataSize), compDataSize))
    return result


def DecompressData(compData, compDataSize, dataSize):
    """Decompress data (DEFLATE algorithm), memory must be MemFree()"""
    result = _ptr_out(_DecompressData(_str_in(compData), int(compDataSize), dataSize))
    return result


def EncodeDataBase64(data, dataSize, outputSize):
    """Encode data to Base64 string, memory must be MemFree()"""
    result = _ptr_out(_EncodeDataBase64(_str_in(data), int(dataSize), outputSize))
    return result


def DecodeDataBase64(data, outputSize):
    """Decode Base64 string data, memory must be MemFree()"""
    result = _ptr_out(_DecodeDataBase64(_str_in(data), outputSize))
    return result


def IsKeyPressed(key):
    """Check if a key has been pressed once"""
    result = _IsKeyPressed(int(key))
    return result


def IsKeyDown(key):
    """Check if a key is being pressed"""
    result = _IsKeyDown(int(key))
    return result


def IsKeyReleased(key):
    """Check if a key has been released once"""
    result = _IsKeyReleased(int(key))
    return result


def IsKeyUp(key):
    """Check if a key is NOT being pressed"""
    result = _IsKeyUp(int(key))
    return result


def SetExitKey(key):
    """Set a custom key to exit program (default is ESC)"""
    _SetExitKey(int(key))


def GetKeyPressed():
    """Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty"""
    result = _GetKeyPressed()
    return result


def GetCharPressed():
    """Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty"""
    result = _GetCharPressed()
    return result


def IsGamepadAvailable(gamepad):
    """Check if a gamepad is available"""
    result = _IsGamepadAvailable(int(gamepad))
    return result


def GetGamepadName(gamepad):
    """Get gamepad internal name id"""
    result = _ptr_out(_GetGamepadName(int(gamepad)))
    return result


def IsGamepadButtonPressed(gamepad, button):
    """Check if a gamepad button has been pressed once"""
    result = _IsGamepadButtonPressed(int(gamepad), int(button))
    return result


def IsGamepadButtonDown(gamepad, button):
    """Check if a gamepad button is being pressed"""
    result = _IsGamepadButtonDown(int(gamepad), int(button))
    return result


def IsGamepadButtonReleased(gamepad, button):
    """Check if a gamepad button has been released once"""
    result = _IsGamepadButtonReleased(int(gamepad), int(button))
    return result


def IsGamepadButtonUp(gamepad, button):
    """Check if a gamepad button is NOT being pressed"""
    result = _IsGamepadButtonUp(int(gamepad), int(button))
    return result


def GetGamepadButtonPressed():
    """Get the last gamepad button pressed"""
    result = _GetGamepadButtonPressed()
    return result


def GetGamepadAxisCount(gamepad):
    """Get gamepad axis count for a gamepad"""
    result = _GetGamepadAxisCount(int(gamepad))
    return result


def GetGamepadAxisMovement(gamepad, axis):
    """Get axis movement value for a gamepad axis"""
    result = _GetGamepadAxisMovement(int(gamepad), int(axis))
    return result


def SetGamepadMappings(mappings):
    """Set internal gamepad mappings (SDL_GameControllerDB)"""
    result = _SetGamepadMappings(_str_in(mappings))
    return result


def IsMouseButtonPressed(button):
    """Check if a mouse button has been pressed once"""
    result = _IsMouseButtonPressed(int(button))
    return result


def IsMouseButtonDown(button):
    """Check if a mouse button is being pressed"""
    result = _IsMouseButtonDown(int(button))
    return result


def IsMouseButtonReleased(button):
    """Check if a mouse button has been released once"""
    result = _IsMouseButtonReleased(int(button))
    return result


def IsMouseButtonUp(button):
    """Check if a mouse button is NOT being pressed"""
    result = _IsMouseButtonUp(int(button))
    return result


def GetMouseX():
    """Get mouse position X"""
    result = _GetMouseX()
    return result


def GetMouseY():
    """Get mouse position Y"""
    result = _GetMouseY()
    return result


def GetMousePosition():
    """Get mouse position XY"""
    result = _GetMousePosition()
    return result


def GetMouseDelta():
    """Get mouse delta between frames"""
    result = _GetMouseDelta()
    return result


def SetMousePosition(x, y):
    """Set mouse position XY"""
    _SetMousePosition(int(x), int(y))


def SetMouseOffset(offsetX, offsetY):
    """Set mouse offset"""
    _SetMouseOffset(int(offsetX), int(offsetY))


def SetMouseScale(scaleX, scaleY):
    """Set mouse scaling"""
    _SetMouseScale(float(scaleX), float(scaleY))


def GetMouseWheelMove():
    """Get mouse wheel movement for X or Y, whichever is larger"""
    result = _GetMouseWheelMove()
    return result


def GetMouseWheelMoveV():
    """Get mouse wheel movement for both X and Y"""
    result = _GetMouseWheelMoveV()
    return result


def SetMouseCursor(cursor):
    """Set mouse cursor"""
    _SetMouseCursor(int(cursor))


def GetTouchX():
    """Get touch position X for touch point 0 (relative to screen size)"""
    result = _GetTouchX()
    return result


def GetTouchY():
    """Get touch position Y for touch point 0 (relative to screen size)"""
    result = _GetTouchY()
    return result


def GetTouchPosition(index):
    """Get touch position XY for a touch point index (relative to screen size)"""
    result = _GetTouchPosition(int(index))
    return result


def GetTouchPointId(index):
    """Get touch point identifier for given index"""
    result = _GetTouchPointId(int(index))
    return result


def GetTouchPointCount():
    """Get number of touch points"""
    result = _GetTouchPointCount()
    return result


def SetGesturesEnabled(flags):
    """Enable a set of gestures using flags"""
    _SetGesturesEnabled(flags)


def IsGestureDetected(gesture):
    """Check if a gesture have been detected"""
    result = _IsGestureDetected(int(gesture))
    return result


def GetGestureDetected():
    """Get latest detected gesture"""
    result = _GetGestureDetected()
    return result


def GetGestureHoldDuration():
    """Get gesture hold time in milliseconds"""
    result = _GetGestureHoldDuration()
    return result


def GetGestureDragVector():
    """Get gesture drag vector"""
    result = _GetGestureDragVector()
    return result


def GetGestureDragAngle():
    """Get gesture drag angle"""
    result = _GetGestureDragAngle()
    return result


def GetGesturePinchVector():
    """Get gesture pinch delta"""
    result = _GetGesturePinchVector()
    return result


def GetGesturePinchAngle():
    """Get gesture pinch angle"""
    result = _GetGesturePinchAngle()
    return result


def UpdateCamera(camera, mode):
    """Update camera position for selected mode"""
    _UpdateCamera(camera, int(mode))


def UpdateCameraPro(camera, movement, rotation, zoom):
    """Update camera movement/rotation"""
    _UpdateCameraPro(camera, _vec3(movement), _vec3(rotation), float(zoom))


def SetShapesTexture(texture, source):
    """Set texture and rectangle to be used on shapes drawing"""
    _SetShapesTexture(texture, _rect(source))


def DrawPixel(posX, posY, color):
    """Draw a pixel"""
    _DrawPixel(int(posX), int(posY), _color(color))


def DrawPixelV(position, color):
    """Draw a pixel (Vector version)"""
    _DrawPixelV(_vec2(position), _color(color))


def DrawLine(startPosX, startPosY, endPosX, endPosY, color):
    """Draw a line"""
    _DrawLine(int(startPosX), int(startPosY), int(endPosX), int(endPosY), _color(color))


def DrawLineV(startPos, endPos, color):
    """Draw a line (Vector version)"""
    _DrawLineV(_vec2(startPos), _vec2(endPos), _color(color))


def DrawLineEx(startPos, endPos, thick, color):
    """Draw a line defining thickness"""
    _DrawLineEx(_vec2(startPos), _vec2(endPos), float(thick), _color(color))


def DrawLineBezier(startPos, endPos, thick, color):
    """Draw a line using cubic-bezier curves in-out"""
    _DrawLineBezier(_vec2(startPos), _vec2(endPos), float(thick), _color(color))


def DrawLineBezierQuad(startPos, endPos, controlPos, thick, color):
    """Draw line using quadratic bezier curves with a control point"""
    _DrawLineBezierQuad(_vec2(startPos), _vec2(endPos), _vec2(controlPos), float(thick), _color(color))


def DrawLineBezierCubic(startPos, endPos, startControlPos, endControlPos, thick, color):
    """Draw line using cubic bezier curves with 2 control points"""
    _DrawLineBezierCubic(_vec2(startPos), _vec2(endPos), _vec2(startControlPos), _vec2(endControlPos), float(thick), _color(color))


def DrawLineStrip(points, color):
    """Draw lines sequence"""
    _DrawLineStrip(_arr_in(Vector2, points), len(points), _color(color))


def DrawCircle(centerX, centerY, radius, color):
    """Draw a color-filled circle"""
    _DrawCircle(int(centerX), int(centerY), float(radius), _color(color))


def DrawCircleSector(center, radius, startAngle, endAngle, segments, color):
    """Draw a piece of a circle"""
    _DrawCircleSector(_vec2(center), float(radius), float(startAngle), float(endAngle), int(segments), _color(color))


def DrawCircleSectorLines(center, radius, startAngle, endAngle, segments, color):
    """Draw circle sector outline"""
    _DrawCircleSectorLines(_vec2(center), float(radius), float(startAngle), float(endAngle), int(segments), _color(color))


def DrawCircleGradient(centerX, centerY, radius, color1, color2):
    """Draw a gradient-filled circle"""
    _DrawCircleGradient(int(centerX), int(centerY), float(radius), _color(color1), _color(color2))


def DrawCircleV(center, radius, color):
    """Draw a color-filled circle (Vector version)"""
    _DrawCircleV(_vec2(center), float(radius), _color(color))


def DrawCircleLines(centerX, centerY, radius, color):
    """Draw circle outline"""
    _DrawCircleLines(int(centerX), int(centerY), float(radius), _color(color))


def DrawEllipse(centerX, centerY, radiusH, radiusV, color):
    """Draw ellipse"""
    _DrawEllipse(int(centerX), int(centerY), float(radiusH), float(radiusV), _color(color))


def DrawEllipseLines(centerX, centerY, radiusH, radiusV, color):
    """Draw ellipse outline"""
    _DrawEllipseLines(int(centerX), int(centerY), float(radiusH), float(radiusV), _color(color))


def DrawRing(center, innerRadius, outerRadius, startAngle, endAngle, segments, color):
    """Draw ring"""
    _DrawRing(_vec2(center), float(innerRadius), float(outerRadius), float(startAngle), float(endAngle), int(segments), _color(color))


def DrawRingLines(center, innerRadius, outerRadius, startAngle, endAngle, segments, color):
    """Draw ring outline"""
    _DrawRingLines(_vec2(center), float(innerRadius), float(outerRadius), float(startAngle), float(endAngle), int(segments), _color(color))


def DrawRectangle(posX, posY, width, height, color):
    """Draw a color-filled rectangle"""
    _DrawRectangle(int(posX), int(posY), int(width), int(height), _color(color))


def DrawRectangleV(position, size, color):
    """Draw a color-filled rectangle (Vector version)"""
    _DrawRectangleV(_vec2(position), _vec2(size), _color(color))


def DrawRectangleRec(rec, color):
    """Draw a color-filled rectangle"""
    _DrawRectangleRec(_rect(rec), _color(color))


def DrawRectanglePro(rec, origin, rotation, color):
    """Draw a color-filled rectangle with pro parameters"""
    _DrawRectanglePro(_rect(rec), _vec2(origin), float(rotation), _color(color))


def DrawRectangleGradientV(posX, posY, width, height, color1, color2):
    """Draw a vertical-gradient-filled rectangle"""
    _DrawRectangleGradientV(int(posX), int(posY), int(width), int(height), _color(color1), _color(color2))


def DrawRectangleGradientH(posX, posY, width, height, color1, color2):
    """Draw a horizontal-gradient-filled rectangle"""
    _DrawRectangleGradientH(int(posX), int(posY), int(width), int(height), _color(color1), _color(color2))


def DrawRectangleGradientEx(rec, col1, col2, col3, col4):
    """Draw a gradient-filled rectangle with custom vertex colors"""
    _DrawRectangleGradientEx(_rect(rec), _color(col1), _color(col2), _color(col3), _color(col4))


def DrawRectangleLines(posX, posY, width, height, color):
    """Draw rectangle outline"""
    _DrawRectangleLines(int(posX), int(posY), int(width), int(height), _color(color))


def DrawRectangleLinesEx(rec, lineThick, color):
    """Draw rectangle outline with extended parameters"""
    _DrawRectangleLinesEx(_rect(rec), float(lineThick), _color(color))


def DrawRectangleRounded(rec, roundness, segments, color):
    """Draw rectangle with rounded edges"""
    _DrawRectangleRounded(_rect(rec), float(roundness), int(segments), _color(color))


def DrawRectangleRoundedLines(rec, roundness, segments, lineThick, color):
    """Draw rectangle with rounded edges outline"""
    _DrawRectangleRoundedLines(_rect(rec), float(roundness), int(segments), float(lineThick), _color(color))


def DrawTriangle(v1, v2, v3, color):
    """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
    _DrawTriangle(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


def DrawTriangleLines(v1, v2, v3, color):
    """Draw triangle outline (vertex in counter-clockwise order!)"""
    _DrawTriangleLines(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


def DrawTriangleFan(points, color):
    """Draw a triangle fan defined by points (first vertex is the center)"""
    _DrawTriangleFan(_arr_in(Vector2, points), len(points), _color(color))


def DrawTriangleStrip(points, color):
    """Draw a triangle strip defined by points"""
    _DrawTriangleStrip(_arr_in(Vector2, points), len(points), _color(color))


def DrawPoly(center, sides, radius, rotation, color):
    """Draw a regular polygon (Vector version)"""
    _DrawPoly(_vec2(center), int(sides), float(radius), float(rotation), _color(color))


def DrawPolyLines(center, sides, radius, rotation, color):
    """Draw a polygon outline of n sides"""
    _DrawPolyLines(_vec2(center), int(sides), float(radius), float(rotation), _color(color))


def DrawPolyLinesEx(center, sides, radius, rotation, lineThick, color):
    """Draw a polygon outline of n sides with extended parameters"""
    _DrawPolyLinesEx(_vec2(center), int(sides), float(radius), float(rotation), float(lineThick), _color(color))


def CheckCollisionRecs(rec1, rec2):
    """Check collision between two rectangles"""
    result = _CheckCollisionRecs(_rect(rec1), _rect(rec2))
    return result


def CheckCollisionCircles(center1, radius1, center2, radius2):
    """Check collision between two circles"""
    result = _CheckCollisionCircles(_vec2(center1), float(radius1), _vec2(center2), float(radius2))
    return result


def CheckCollisionCircleRec(center, radius, rec):
    """Check collision between circle and rectangle"""
    result = _CheckCollisionCircleRec(_vec2(center), float(radius), _rect(rec))
    return result


def CheckCollisionPointRec(point, rec):
    """Check if point is inside rectangle"""
    result = _CheckCollisionPointRec(_vec2(point), _rect(rec))
    return result


def CheckCollisionPointCircle(point, center, radius):
    """Check if point is inside circle"""
    result = _CheckCollisionPointCircle(_vec2(point), _vec2(center), float(radius))
    return result


def CheckCollisionPointTriangle(point, p1, p2, p3):
    """Check if point is inside a triangle"""
    result = _CheckCollisionPointTriangle(_vec2(point), _vec2(p1), _vec2(p2), _vec2(p3))
    return result


def CheckCollisionPointPoly(point, points, pointCount):
    """Check if point is within a polygon described by array of vertices"""
    result = _CheckCollisionPointPoly(_vec2(point), _vec2(points), int(pointCount))
    return result


def CheckCollisionLines(startPos1, endPos1, startPos2, endPos2, collisionPoint):
    """Check the collision between two lines defined by two points each, returns collision point by reference"""
    result = _CheckCollisionLines(_vec2(startPos1), _vec2(endPos1), _vec2(startPos2), _vec2(endPos2), _vec2(collisionPoint))
    return result


def CheckCollisionPointLine(point, p1, p2, threshold):
    """Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]"""
    result = _CheckCollisionPointLine(_vec2(point), _vec2(p1), _vec2(p2), int(threshold))
    return result


def GetCollisionRec(rec1, rec2):
    """Get collision rectangle for two rectangles collision"""
    result = _GetCollisionRec(_rect(rec1), _rect(rec2))
    return result


def LoadImage(fileName):
    """Load image from file into CPU memory (RAM)"""
    result = _LoadImage(_str_in(fileName))
    return result


def LoadImageRaw(fileName, width, height, format, headerSize):
    """Load image from RAW file data"""
    result = _LoadImageRaw(_str_in(fileName), int(width), int(height), int(format), int(headerSize))
    return result


def LoadImageAnim(fileName, frames):
    """Load image sequence from file (frames appended to image.data)"""
    result = _LoadImageAnim(_str_in(fileName), frames)
    return result


def LoadImageFromMemory(fileType, fileData, dataSize):
    """Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
    result = _LoadImageFromMemory(_str_in(fileType), _str_in(fileData), int(dataSize))
    return result


def LoadImageFromTexture(texture):
    """Load image from GPU texture data"""
    result = _LoadImageFromTexture(texture)
    return result


def LoadImageFromScreen():
    """Load image from screen buffer and (screenshot)"""
    result = _LoadImageFromScreen()
    return result


def IsImageReady(image):
    """Check if an image is ready"""
    result = _IsImageReady(image)
    return result


def UnloadImage(image):
    """Unload image from CPU memory (RAM)"""
    _UnloadImage(image)


def ExportImage(image, fileName):
    """Export image data to file, returns true on success"""
    result = _ExportImage(image, _str_in(fileName))
    return result


def ExportImageAsCode(image, fileName):
    """Export image as code file defining an array of bytes, returns true on success"""
    result = _ExportImageAsCode(image, _str_in(fileName))
    return result


def GenImageColor(width, height, color):
    """Generate image: plain color"""
    result = _GenImageColor(int(width), int(height), _color(color))
    return result


def GenImageGradientV(width, height, top, bottom):
    """Generate image: vertical gradient"""
    result = _GenImageGradientV(int(width), int(height), _color(top), _color(bottom))
    return result


def GenImageGradientH(width, height, left, right):
    """Generate image: horizontal gradient"""
    result = _GenImageGradientH(int(width), int(height), _color(left), _color(right))
    return result


def GenImageGradientRadial(width, height, density, inner, outer):
    """Generate image: radial gradient"""
    result = _GenImageGradientRadial(int(width), int(height), float(density), _color(inner), _color(outer))
    return result


def GenImageChecked(width, height, checksX, checksY, col1, col2):
    """Generate image: checked"""
    result = _GenImageChecked(int(width), int(height), int(checksX), int(checksY), _color(col1), _color(col2))
    return result


def GenImageWhiteNoise(width, height, factor):
    """Generate image: white noise"""
    result = _GenImageWhiteNoise(int(width), int(height), float(factor))
    return result


def GenImagePerlinNoise(width, height, offsetX, offsetY, scale):
    """Generate image: perlin noise"""
    result = _GenImagePerlinNoise(int(width), int(height), int(offsetX), int(offsetY), float(scale))
    return result


def GenImageCellular(width, height, tileSize):
    """Generate image: cellular algorithm, bigger tileSize means bigger cells"""
    result = _GenImageCellular(int(width), int(height), int(tileSize))
    return result


def GenImageText(width, height, text):
    """Generate image: grayscale image from text data"""
    result = _GenImageText(int(width), int(height), _str_in(text))
    return result


def ImageCopy(image):
    """Create an image duplicate (useful for transformations)"""
    result = _ImageCopy(image)
    return result


def ImageFromImage(image, rec):
    """Create an image from another image piece"""
    result = _ImageFromImage(image, _rect(rec))
    return result


def ImageText(text, fontSize, color):
    """Create an image from text (default font)"""
    result = _ImageText(_str_in(text), int(fontSize), _color(color))
    return result


def ImageTextEx(font, text, fontSize, spacing, tint):
    """Create an image from text (custom sprite font)"""
    result = _ImageTextEx(font, _str_in(text), float(fontSize), float(spacing), _color(tint))
    return result


def ImageFormat(image, newFormat):
    """Convert image data to desired format"""
    _ImageFormat(image, int(newFormat))


def ImageToPOT(image, fill):
    """Convert image to POT (power-of-two)"""
    _ImageToPOT(image, _color(fill))


def ImageCrop(image, crop):
    """Crop an image to a defined rectangle"""
    _ImageCrop(image, _rect(crop))


def ImageAlphaCrop(image, threshold):
    """Crop image depending on alpha value"""
    _ImageAlphaCrop(image, float(threshold))


def ImageAlphaClear(image, color, threshold):
    """Clear alpha channel to desired color"""
    _ImageAlphaClear(image, _color(color), float(threshold))


def ImageAlphaMask(image, alphaMask):
    """Apply alpha mask to image"""
    _ImageAlphaMask(image, alphaMask)


def ImageAlphaPremultiply(image):
    """Premultiply alpha channel"""
    _ImageAlphaPremultiply(image)


def ImageBlurGaussian(image, blurSize):
    """Apply Gaussian blur using a box blur approximation"""
    _ImageBlurGaussian(image, int(blurSize))


def ImageResize(image, newWidth, newHeight):
    """Resize image (Bicubic scaling algorithm)"""
    _ImageResize(image, int(newWidth), int(newHeight))


def ImageResizeNN(image, newWidth, newHeight):
    """Resize image (Nearest-Neighbor scaling algorithm)"""
    _ImageResizeNN(image, int(newWidth), int(newHeight))


def ImageResizeCanvas(image, newWidth, newHeight, offsetX, offsetY, fill):
    """Resize canvas and fill with color"""
    _ImageResizeCanvas(image, int(newWidth), int(newHeight), int(offsetX), int(offsetY), _color(fill))


def ImageMipmaps(image):
    """Compute all mipmap levels for a provided image"""
    _ImageMipmaps(image)


def ImageDither(image, rBpp, gBpp, bBpp, aBpp):
    """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
    _ImageDither(image, int(rBpp), int(gBpp), int(bBpp), int(aBpp))


def ImageFlipVertical(image):
    """Flip image vertically"""
    _ImageFlipVertical(image)


def ImageFlipHorizontal(image):
    """Flip image horizontally"""
    _ImageFlipHorizontal(image)


def ImageRotateCW(image):
    """Rotate image clockwise 90deg"""
    _ImageRotateCW(image)


def ImageRotateCCW(image):
    """Rotate image counter-clockwise 90deg"""
    _ImageRotateCCW(image)


def ImageColorTint(image, color):
    """Modify image color: tint"""
    _ImageColorTint(image, _color(color))


def ImageColorInvert(image):
    """Modify image color: invert"""
    _ImageColorInvert(image)


def ImageColorGrayscale(image):
    """Modify image color: grayscale"""
    _ImageColorGrayscale(image)


def ImageColorContrast(image, contrast):
    """Modify image color: contrast (-100 to 100)"""
    _ImageColorContrast(image, float(contrast))


def ImageColorBrightness(image, brightness):
    """Modify image color: brightness (-255 to 255)"""
    _ImageColorBrightness(image, int(brightness))


def ImageColorReplace(image, color, replace):
    """Modify image color: replace color"""
    _ImageColorReplace(image, _color(color), _color(replace))


def LoadImageColors(image):
    """Load color data from image as a Color array (RGBA - 32bit)"""
    result = _ptr_out(_LoadImageColors(image))
    return result


def LoadImagePalette(image, maxPaletteSize):
    """Load colors palette from image as a Color array (RGBA - 32bit)"""
    colorCount = Int(0)
    result = _ptr_out(_LoadImagePalette(image, int(maxPaletteSize), byref(colorCount)), colorCount.value)
    return result


def UnloadImageColors(colors):
    """Unload color data loaded with LoadImageColors()"""
    _UnloadImageColors(_color(colors))


def UnloadImagePalette(colors):
    """Unload colors palette loaded with LoadImagePalette()"""
    _UnloadImagePalette(_color(colors))


def GetImageAlphaBorder(image, threshold):
    """Get image alpha border rectangle"""
    result = _GetImageAlphaBorder(image, float(threshold))
    return result


def GetImageColor(image, x, y):
    """Get image pixel color at (x, y) position"""
    result = _GetImageColor(image, int(x), int(y))
    return result


def ImageClearBackground(dst, color):
    """Clear image background with given color"""
    _ImageClearBackground(dst, _color(color))


def ImageDrawPixel(dst, posX, posY, color):
    """Draw pixel within an image"""
    _ImageDrawPixel(dst, int(posX), int(posY), _color(color))


def ImageDrawPixelV(dst, position, color):
    """Draw pixel within an image (Vector version)"""
    _ImageDrawPixelV(dst, _vec2(position), _color(color))


def ImageDrawLine(dst, startPosX, startPosY, endPosX, endPosY, color):
    """Draw line within an image"""
    _ImageDrawLine(dst, int(startPosX), int(startPosY), int(endPosX), int(endPosY), _color(color))


def ImageDrawLineV(dst, start, end, color):
    """Draw line within an image (Vector version)"""
    _ImageDrawLineV(dst, _vec2(start), _vec2(end), _color(color))


def ImageDrawCircle(dst, centerX, centerY, radius, color):
    """Draw a filled circle within an image"""
    _ImageDrawCircle(dst, int(centerX), int(centerY), int(radius), _color(color))


def ImageDrawCircleV(dst, center, radius, color):
    """Draw a filled circle within an image (Vector version)"""
    _ImageDrawCircleV(dst, _vec2(center), int(radius), _color(color))


def ImageDrawCircleLines(dst, centerX, centerY, radius, color):
    """Draw circle outline within an image"""
    _ImageDrawCircleLines(dst, int(centerX), int(centerY), int(radius), _color(color))


def ImageDrawCircleLinesV(dst, center, radius, color):
    """Draw circle outline within an image (Vector version)"""
    _ImageDrawCircleLinesV(dst, _vec2(center), int(radius), _color(color))


def ImageDrawRectangle(dst, posX, posY, width, height, color):
    """Draw rectangle within an image"""
    _ImageDrawRectangle(dst, int(posX), int(posY), int(width), int(height), _color(color))


def ImageDrawRectangleV(dst, position, size, color):
    """Draw rectangle within an image (Vector version)"""
    _ImageDrawRectangleV(dst, _vec2(position), _vec2(size), _color(color))


def ImageDrawRectangleRec(dst, rec, color):
    """Draw rectangle within an image"""
    _ImageDrawRectangleRec(dst, _rect(rec), _color(color))


def ImageDrawRectangleLines(dst, rec, thick, color):
    """Draw rectangle lines within an image"""
    _ImageDrawRectangleLines(dst, _rect(rec), int(thick), _color(color))


def ImageDraw(dst, src, srcRec, dstRec, tint):
    """Draw a source image within a destination image (tint applied to source)"""
    _ImageDraw(dst, src, _rect(srcRec), _rect(dstRec), _color(tint))


def ImageDrawText(dst, text, posX, posY, fontSize, color):
    """Draw text (using default font) within an image (destination)"""
    _ImageDrawText(dst, _str_in(text), int(posX), int(posY), int(fontSize), _color(color))


def ImageDrawTextEx(dst, font, text, position, fontSize, spacing, tint):
    """Draw text (custom sprite font) within an image (destination)"""
    _ImageDrawTextEx(dst, font, _str_in(text), _vec2(position), float(fontSize), float(spacing), _color(tint))


def LoadTexture(fileName):
    """Load texture from file into GPU memory (VRAM)"""
    result = _LoadTexture(_str_in(fileName))
    return result


def LoadTextureFromImage(image):
    """Load texture from image data"""
    result = _LoadTextureFromImage(image)
    return result


def LoadTextureCubemap(image, layout):
    """Load cubemap from image, multiple image cubemap layouts supported"""
    result = _LoadTextureCubemap(image, int(layout))
    return result


def LoadRenderTexture(width, height):
    """Load texture for rendering (framebuffer)"""
    result = _LoadRenderTexture(int(width), int(height))
    return result


def IsTextureReady(texture):
    """Check if a texture is ready"""
    result = _IsTextureReady(texture)
    return result


def UnloadTexture(texture):
    """Unload texture from GPU memory (VRAM)"""
    _UnloadTexture(texture)


def IsRenderTextureReady(target):
    """Check if a render texture is ready"""
    result = _IsRenderTextureReady(target)
    return result


def UnloadRenderTexture(target):
    """Unload render texture from GPU memory (VRAM)"""
    _UnloadRenderTexture(target)


def UpdateTexture(texture, pixels):
    """Update GPU texture with new data"""
    _UpdateTexture(texture, pixels)


def UpdateTextureRec(texture, rec, pixels):
    """Update GPU texture rectangle with new data"""
    _UpdateTextureRec(texture, _rect(rec), pixels)


def GenTextureMipmaps(texture):
    """Generate GPU mipmaps for a texture"""
    _GenTextureMipmaps(texture)


def SetTextureFilter(texture, filter):
    """Set texture scaling filter mode"""
    _SetTextureFilter(texture, int(filter))


def SetTextureWrap(texture, wrap):
    """Set texture wrapping mode"""
    _SetTextureWrap(texture, int(wrap))


def DrawTexture(texture, posX, posY, tint):
    """Draw a Texture2D"""
    _DrawTexture(texture, int(posX), int(posY), _color(tint))


def DrawTextureV(texture, position, tint):
    """Draw a Texture2D with position defined as Vector2"""
    _DrawTextureV(texture, _vec2(position), _color(tint))


def DrawTextureEx(texture, position, rotation, scale, tint):
    """Draw a Texture2D with extended parameters"""
    _DrawTextureEx(texture, _vec2(position), float(rotation), float(scale), _color(tint))


def DrawTextureRec(texture, source, position, tint):
    """Draw a part of a texture defined by a rectangle"""
    _DrawTextureRec(texture, _rect(source), _vec2(position), _color(tint))


def DrawTexturePro(texture, source, dest, origin, rotation, tint):
    """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
    _DrawTexturePro(texture, _rect(source), _rect(dest), _vec2(origin), float(rotation), _color(tint))


def DrawTextureNPatch(texture, nPatchInfo, dest, origin, rotation, tint):
    """Draws a texture (or part of it) that stretches or shrinks nicely"""
    _DrawTextureNPatch(texture, nPatchInfo, _rect(dest), _vec2(origin), float(rotation), _color(tint))


def Fade(color, alpha):
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
    result = _Fade(_color(color), float(alpha))
    return result


def ColorToInt(color):
    """Get hexadecimal value for a Color"""
    result = _ColorToInt(_color(color))
    return result


def ColorNormalize(color):
    """Get Color normalized as float [0..1]"""
    result = _ColorNormalize(_color(color))
    return result


def ColorFromNormalized(normalized):
    """Get Color from normalized values [0..1]"""
    result = _ColorFromNormalized(_vec4(normalized))
    return result


def ColorToHSV(color):
    """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
    result = _ColorToHSV(_color(color))
    return result


def ColorFromHSV(hue, saturation, value):
    """Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
    result = _ColorFromHSV(float(hue), float(saturation), float(value))
    return result


def ColorTint(color, tint):
    """Get color multiplied with another color"""
    result = _ColorTint(_color(color), _color(tint))
    return result


def ColorBrightness(color, factor):
    """Get color with brightness correction, brightness factor goes from -1.0f to 1.0f"""
    result = _ColorBrightness(_color(color), float(factor))
    return result


def ColorContrast(color, contrast):
    """Get color with contrast correction, contrast values between -1.0f and 1.0f"""
    result = _ColorContrast(_color(color), float(contrast))
    return result


def ColorAlpha(color, alpha):
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
    result = _ColorAlpha(_color(color), float(alpha))
    return result


def ColorAlphaBlend(dst, src, tint):
    """Get src alpha-blended into dst color with tint"""
    result = _ColorAlphaBlend(_color(dst), _color(src), _color(tint))
    return result


def GetColor(hexValue):
    """Get Color structure from hexadecimal value"""
    result = _GetColor(hexValue)
    return result


def GetPixelColor(srcPtr, format):
    """Get Color from a source pixel pointer of certain format"""
    result = _GetPixelColor(srcPtr, int(format))
    return result


def SetPixelColor(dstPtr, color, format):
    """Set color formatted into destination pixel pointer"""
    _SetPixelColor(dstPtr, _color(color), int(format))


def GetPixelDataSize(width, height, format):
    """Get pixel data size in bytes for certain format"""
    result = _GetPixelDataSize(int(width), int(height), int(format))
    return result


def GetFontDefault():
    """Get the default Font"""
    result = _GetFontDefault()
    return result


def LoadFont(fileName):
    """Load font from file into GPU memory (VRAM)"""
    result = _LoadFont(_str_in(fileName))
    return result


def LoadFontEx(fileName, fontSize, fontChars, glyphCount):
    """Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set"""
    result = _LoadFontEx(_str_in(fileName), int(fontSize), fontChars, int(glyphCount))
    return result


def LoadFontFromImage(image, key, firstChar):
    """Load font from Image (XNA style)"""
    result = _LoadFontFromImage(image, _color(key), int(firstChar))
    return result


def LoadFontFromMemory(fileType, fileData, dataSize, fontSize, fontChars, glyphCount):
    """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
    result = _LoadFontFromMemory(_str_in(fileType), _str_in(fileData), int(dataSize), int(fontSize), fontChars, int(glyphCount))
    return result


def IsFontReady(font):
    """Check if a font is ready"""
    result = _IsFontReady(font)
    return result


def LoadFontData(fileData, dataSize, fontSize, fontChars, glyphCount, type):
    """Load font data for further use"""
    result = _ptr_out(_LoadFontData(_str_in(fileData), int(dataSize), int(fontSize), fontChars, int(glyphCount), int(type)))
    return result


def GenImageFontAtlas(chars, recs, glyphCount, fontSize, padding, packMethod):
    """Generate image font atlas using chars info"""
    result = _GenImageFontAtlas(chars, recs, int(glyphCount), int(fontSize), int(padding), int(packMethod))
    return result


def UnloadFontData(chars, glyphCount):
    """Unload font chars info data (RAM)"""
    _UnloadFontData(chars, int(glyphCount))


def UnloadFont(font):
    """Unload font from GPU memory (VRAM)"""
    _UnloadFont(font)


def ExportFontAsCode(font, fileName):
    """Export font as code file, returns true on success"""
    result = _ExportFontAsCode(font, _str_in(fileName))
    return result


def DrawFPS(posX, posY):
    """Draw current FPS"""
    _DrawFPS(int(posX), int(posY))


def DrawText(text, posX, posY, fontSize, color):
    """Draw text (using default font)"""
    _DrawText(_str_in(text), int(posX), int(posY), int(fontSize), _color(color))


def DrawTextEx(font, text, position, fontSize, spacing, tint):
    """Draw text using font and additional parameters"""
    _DrawTextEx(font, _str_in(text), _vec2(position), float(fontSize), float(spacing), _color(tint))


def DrawTextPro(font, text, position, origin, rotation, fontSize, spacing, tint):
    """Draw text using Font and pro parameters (rotation)"""
    _DrawTextPro(font, _str_in(text), _vec2(position), _vec2(origin), float(rotation), float(fontSize), float(spacing), _color(tint))


def DrawTextCodepoint(font, codepoint, position, fontSize, tint):
    """Draw one character (codepoint)"""
    _DrawTextCodepoint(font, int(codepoint), _vec2(position), float(fontSize), _color(tint))


def DrawTextCodepoints(font, codepoints, position, fontSize, spacing, tint):
    """Draw multiple character (codepoint)"""
    _DrawTextCodepoints(font, _str_in(codepoints), len(codepoints), _vec2(position), float(fontSize), float(spacing), _color(tint))


def MeasureText(text, fontSize):
    """Measure string width for default font"""
    result = _MeasureText(_str_in(text), int(fontSize))
    return result


def MeasureTextEx(font, text, fontSize, spacing):
    """Measure string size for Font"""
    result = _MeasureTextEx(font, _str_in(text), float(fontSize), float(spacing))
    return result


def GetGlyphIndex(font, codepoint):
    """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
    result = _GetGlyphIndex(font, int(codepoint))
    return result


def GetGlyphInfo(font, codepoint):
    """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
    result = _GetGlyphInfo(font, int(codepoint))
    return result


def GetGlyphAtlasRec(font, codepoint):
    """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
    result = _GetGlyphAtlasRec(font, int(codepoint))
    return result


def LoadUTF8(codepoints, length):
    """Load UTF-8 text encoded from codepoints array"""
    result = _ptr_out(_LoadUTF8(codepoints, int(length)))
    return result


def UnloadUTF8(text):
    """Unload UTF-8 text encoded from codepoints array"""
    _UnloadUTF8(_str_in(text))


def LoadCodepoints(text, count):
    """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
    result = _ptr_out(_LoadCodepoints(_str_in(text), count))
    return result


def UnloadCodepoints(codepoints):
    """Unload codepoints data from memory"""
    _UnloadCodepoints(codepoints)


def GetCodepointCount(text):
    """Get total number of codepoints in a UTF-8 encoded string"""
    result = _GetCodepointCount(_str_in(text))
    return result


def GetCodepoint(text, codepointSize):
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
    result = _GetCodepoint(_str_in(text), codepointSize)
    return result


def GetCodepointNext(text, codepointSize):
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
    result = _GetCodepointNext(_str_in(text), codepointSize)
    return result


def GetCodepointPrevious(text, codepointSize):
    """Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
    result = _GetCodepointPrevious(_str_in(text), codepointSize)
    return result


def CodepointToUTF8(codepoint, utf8Size):
    """Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
    result = _ptr_out(_CodepointToUTF8(int(codepoint), utf8Size))
    return result


def TextCopy(dst, src):
    """Copy one string to another, returns bytes copied"""
    result = _TextCopy(_str_in(dst), _str_in(src))
    return result


def TextIsEqual(text1, text2):
    """Check if two text string are equal"""
    result = _TextIsEqual(_str_in(text1), _str_in(text2))
    return result


def TextLength(text):
    """Get text length, checks for '\0' ending"""
    result = _TextLength(_str_in(text))
    return result


def TextFormat(text, args):
    """Text formatting with variables (sprintf() style)"""
    result = _ptr_out(_TextFormat(_str_in(text), args))
    return result


def TextSubtext(text, position, length):
    """Get a piece of a text string"""
    result = _ptr_out(_TextSubtext(_str_in(text), int(position), int(length)))
    return result


def TextReplace(text, replace, by):
    """Replace text string (WARNING: memory must be freed!)"""
    result = _ptr_out(_TextReplace(_str_in(text), _str_in(replace), _str_in(by)))
    return result


def TextInsert(text, insert, position):
    """Insert text in a position (WARNING: memory must be freed!)"""
    result = _ptr_out(_TextInsert(_str_in(text), _str_in(insert), int(position)))
    return result


def TextJoin(textList, count, delimiter):
    """Join text strings with delimiter"""
    result = _ptr_out(_TextJoin(_str_in2(textList), int(count), _str_in(delimiter)))
    return result


def TextSplit(text, delimiter, count):
    """Split text into multiple strings"""
    result = _ptr_out(_TextSplit(_str_in(text), int(delimiter), count))
    return result


def TextAppend(text, append, position):
    """Append text at specific position and move cursor!"""
    _TextAppend(_str_in(text), _str_in(append), position)


def TextFindIndex(text, find):
    """Find first text occurrence within a string"""
    result = _TextFindIndex(_str_in(text), _str_in(find))
    return result


def TextToUpper(text):
    """Get upper case version of provided string"""
    result = _ptr_out(_TextToUpper(_str_in(text)))
    return result


def TextToLower(text):
    """Get lower case version of provided string"""
    result = _ptr_out(_TextToLower(_str_in(text)))
    return result


def TextToPascal(text):
    """Get Pascal case notation version of provided string"""
    result = _ptr_out(_TextToPascal(_str_in(text)))
    return result


def TextToInteger(text):
    """Get integer value from text (negative values not supported)"""
    result = _TextToInteger(_str_in(text))
    return result


def DrawLine3D(startPos, endPos, color):
    """Draw a line in 3D world space"""
    _DrawLine3D(_vec3(startPos), _vec3(endPos), _color(color))


def DrawPoint3D(position, color):
    """Draw a point in 3D space, actually a small line"""
    _DrawPoint3D(_vec3(position), _color(color))


def DrawCircle3D(center, radius, rotationAxis, rotationAngle, color):
    """Draw a circle in 3D world space"""
    _DrawCircle3D(_vec3(center), float(radius), _vec3(rotationAxis), float(rotationAngle), _color(color))


def DrawTriangle3D(v1, v2, v3, color):
    """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
    _DrawTriangle3D(_vec3(v1), _vec3(v2), _vec3(v3), _color(color))


def DrawTriangleStrip3D(points, color):
    """Draw a triangle strip defined by points"""
    _DrawTriangleStrip3D(_arr_in(Vector3, points), len(points), _color(color))


def DrawCube(position, width, height, length, color):
    """Draw cube"""
    _DrawCube(_vec3(position), float(width), float(height), float(length), _color(color))


def DrawCubeV(position, size, color):
    """Draw cube (Vector version)"""
    _DrawCubeV(_vec3(position), _vec3(size), _color(color))


def DrawCubeWires(position, width, height, length, color):
    """Draw cube wires"""
    _DrawCubeWires(_vec3(position), float(width), float(height), float(length), _color(color))


def DrawCubeWiresV(position, size, color):
    """Draw cube wires (Vector version)"""
    _DrawCubeWiresV(_vec3(position), _vec3(size), _color(color))


def DrawSphere(centerPos, radius, color):
    """Draw sphere"""
    _DrawSphere(_vec3(centerPos), float(radius), _color(color))


def DrawSphereEx(centerPos, radius, rings, slices, color):
    """Draw sphere with extended parameters"""
    _DrawSphereEx(_vec3(centerPos), float(radius), int(rings), int(slices), _color(color))


def DrawSphereWires(centerPos, radius, rings, slices, color):
    """Draw sphere wires"""
    _DrawSphereWires(_vec3(centerPos), float(radius), int(rings), int(slices), _color(color))


def DrawCylinder(position, radiusTop, radiusBottom, height, slices, color):
    """Draw a cylinder/cone"""
    _DrawCylinder(_vec3(position), float(radiusTop), float(radiusBottom), float(height), int(slices), _color(color))


def DrawCylinderEx(startPos, endPos, startRadius, endRadius, sides, color):
    """Draw a cylinder with base at startPos and top at endPos"""
    _DrawCylinderEx(_vec3(startPos), _vec3(endPos), float(startRadius), float(endRadius), int(sides), _color(color))


def DrawCylinderWires(position, radiusTop, radiusBottom, height, slices, color):
    """Draw a cylinder/cone wires"""
    _DrawCylinderWires(_vec3(position), float(radiusTop), float(radiusBottom), float(height), int(slices), _color(color))


def DrawCylinderWiresEx(startPos, endPos, startRadius, endRadius, sides, color):
    """Draw a cylinder wires with base at startPos and top at endPos"""
    _DrawCylinderWiresEx(_vec3(startPos), _vec3(endPos), float(startRadius), float(endRadius), int(sides), _color(color))


def DrawCapsule(startPos, endPos, radius, slices, rings, color):
    """Draw a capsule with the center of its sphere caps at startPos and endPos"""
    _DrawCapsule(_vec3(startPos), _vec3(endPos), float(radius), int(slices), int(rings), _color(color))


def DrawCapsuleWires(startPos, endPos, radius, slices, rings, color):
    """Draw capsule wireframe with the center of its sphere caps at startPos and endPos"""
    _DrawCapsuleWires(_vec3(startPos), _vec3(endPos), float(radius), int(slices), int(rings), _color(color))


def DrawPlane(centerPos, size, color):
    """Draw a plane XZ"""
    _DrawPlane(_vec3(centerPos), _vec2(size), _color(color))


def DrawRay(ray, color):
    """Draw a ray line"""
    _DrawRay(ray, _color(color))


def DrawGrid(slices, spacing):
    """Draw a grid (centered at (0, 0, 0))"""
    _DrawGrid(int(slices), float(spacing))


def LoadModel(fileName):
    """Load model from files (meshes and materials)"""
    result = _LoadModel(_str_in(fileName))
    return result


def LoadModelFromMesh(mesh):
    """Load model from generated mesh (default material)"""
    result = _LoadModelFromMesh(mesh)
    return result


def IsModelReady(model):
    """Check if a model is ready"""
    result = _IsModelReady(model)
    return result


def UnloadModel(model):
    """Unload model (including meshes) from memory (RAM and/or VRAM)"""
    _UnloadModel(model)


def GetModelBoundingBox(model):
    """Compute model bounding box limits (considers all meshes)"""
    result = _GetModelBoundingBox(model)
    return result


def DrawModel(model, position, scale, tint):
    """Draw a model (with texture if set)"""
    _DrawModel(model, _vec3(position), float(scale), _color(tint))


def DrawModelEx(model, position, rotationAxis, rotationAngle, scale, tint):
    """Draw a model with extended parameters"""
    _DrawModelEx(model, _vec3(position), _vec3(rotationAxis), float(rotationAngle), _vec3(scale), _color(tint))


def DrawModelWires(model, position, scale, tint):
    """Draw a model wires (with texture if set)"""
    _DrawModelWires(model, _vec3(position), float(scale), _color(tint))


def DrawModelWiresEx(model, position, rotationAxis, rotationAngle, scale, tint):
    """Draw a model wires (with texture if set) with extended parameters"""
    _DrawModelWiresEx(model, _vec3(position), _vec3(rotationAxis), float(rotationAngle), _vec3(scale), _color(tint))


def DrawBoundingBox(box, color):
    """Draw bounding box (wires)"""
    _DrawBoundingBox(box, _color(color))


def DrawBillboard(camera, texture, position, size, tint):
    """Draw a billboard texture"""
    _DrawBillboard(camera, texture, _vec3(position), float(size), _color(tint))


def DrawBillboardRec(camera, texture, source, position, size, tint):
    """Draw a billboard texture defined by source"""
    _DrawBillboardRec(camera, texture, _rect(source), _vec3(position), _vec2(size), _color(tint))


def DrawBillboardPro(camera, texture, source, position, up, size, origin, rotation, tint):
    """Draw a billboard texture defined by source and rotation"""
    _DrawBillboardPro(camera, texture, _rect(source), _vec3(position), _vec3(up), _vec2(size), _vec2(origin), float(rotation), _color(tint))


def UploadMesh(mesh, dynamic):
    """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
    _UploadMesh(mesh, bool(dynamic))


def UpdateMeshBuffer(mesh, index, data, dataSize, offset):
    """Update mesh vertex data in GPU for a specific buffer index"""
    _UpdateMeshBuffer(mesh, int(index), data, int(dataSize), int(offset))


def UnloadMesh(mesh):
    """Unload mesh data from CPU and GPU"""
    _UnloadMesh(mesh)


def DrawMesh(mesh, material, transform):
    """Draw a 3d mesh with material and transform"""
    _DrawMesh(mesh, material, transform)


def DrawMeshInstanced(mesh, material, transforms, instances):
    """Draw multiple mesh instances with material and different transforms"""
    _DrawMeshInstanced(mesh, material, transforms, int(instances))


def ExportMesh(mesh, fileName):
    """Export mesh data to file, returns true on success"""
    result = _ExportMesh(mesh, _str_in(fileName))
    return result


def GetMeshBoundingBox(mesh):
    """Compute mesh bounding box limits"""
    result = _GetMeshBoundingBox(mesh)
    return result


def GenMeshTangents(mesh):
    """Compute mesh tangents"""
    _GenMeshTangents(mesh)


def GenMeshPoly(sides, radius):
    """Generate polygonal mesh"""
    result = _GenMeshPoly(int(sides), float(radius))
    return result


def GenMeshPlane(width, length, resX, resZ):
    """Generate plane mesh (with subdivisions)"""
    result = _GenMeshPlane(float(width), float(length), int(resX), int(resZ))
    return result


def GenMeshCube(width, height, length):
    """Generate cuboid mesh"""
    result = _GenMeshCube(float(width), float(height), float(length))
    return result


def GenMeshSphere(radius, rings, slices):
    """Generate sphere mesh (standard sphere)"""
    result = _GenMeshSphere(float(radius), int(rings), int(slices))
    return result


def GenMeshHemiSphere(radius, rings, slices):
    """Generate half-sphere mesh (no bottom cap)"""
    result = _GenMeshHemiSphere(float(radius), int(rings), int(slices))
    return result


def GenMeshCylinder(radius, height, slices):
    """Generate cylinder mesh"""
    result = _GenMeshCylinder(float(radius), float(height), int(slices))
    return result


def GenMeshCone(radius, height, slices):
    """Generate cone/pyramid mesh"""
    result = _GenMeshCone(float(radius), float(height), int(slices))
    return result


def GenMeshTorus(radius, size, radSeg, sides):
    """Generate torus mesh"""
    result = _GenMeshTorus(float(radius), float(size), int(radSeg), int(sides))
    return result


def GenMeshKnot(radius, size, radSeg, sides):
    """Generate trefoil knot mesh"""
    result = _GenMeshKnot(float(radius), float(size), int(radSeg), int(sides))
    return result


def GenMeshHeightmap(heightmap, size):
    """Generate heightmap mesh from image data"""
    result = _GenMeshHeightmap(heightmap, _vec3(size))
    return result


def GenMeshCubicmap(cubicmap, cubeSize):
    """Generate cubes-based map mesh from image data"""
    result = _GenMeshCubicmap(cubicmap, _vec3(cubeSize))
    return result


def LoadMaterials(fileName):
    """Load materials from model file"""
    materialCount = Int(0)
    result = _ptr_out(_LoadMaterials(_str_in(fileName), byref(materialCount)), materialCount.value)
    return result


def LoadMaterialDefault():
    """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
    result = _LoadMaterialDefault()
    return result


def IsMaterialReady(material):
    """Check if a material is ready"""
    result = _IsMaterialReady(material)
    return result


def UnloadMaterial(material):
    """Unload material from GPU memory (VRAM)"""
    _UnloadMaterial(material)


def SetMaterialTexture(material, mapType, texture):
    """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
    _SetMaterialTexture(material, int(mapType), texture)


def SetModelMeshMaterial(model, meshId, materialId):
    """Set material for a mesh"""
    _SetModelMeshMaterial(model, int(meshId), int(materialId))


def LoadModelAnimations(fileName):
    """Load model animations from file"""
    animCount = UInt(0)
    result = _ptr_out(_LoadModelAnimations(_str_in(fileName), byref(animCount)), animCount.value)
    return result


def UpdateModelAnimation(model, anim, frame):
    """Update model animation pose"""
    _UpdateModelAnimation(model, anim, int(frame))


def UnloadModelAnimation(anim):
    """Unload animation data"""
    _UnloadModelAnimation(anim)


def UnloadModelAnimations(animations, count):
    """Unload animation array data"""
    _UnloadModelAnimations(animations, count)


def IsModelAnimationValid(model, anim):
    """Check model animation skeleton match"""
    result = _IsModelAnimationValid(model, anim)
    return result


def CheckCollisionSpheres(center1, radius1, center2, radius2):
    """Check collision between two spheres"""
    result = _CheckCollisionSpheres(_vec3(center1), float(radius1), _vec3(center2), float(radius2))
    return result


def CheckCollisionBoxes(box1, box2):
    """Check collision between two bounding boxes"""
    result = _CheckCollisionBoxes(box1, box2)
    return result


def CheckCollisionBoxSphere(box, center, radius):
    """Check collision between box and sphere"""
    result = _CheckCollisionBoxSphere(box, _vec3(center), float(radius))
    return result


def GetRayCollisionSphere(ray, center, radius):
    """Get collision info between ray and sphere"""
    result = _GetRayCollisionSphere(ray, _vec3(center), float(radius))
    return result


def GetRayCollisionBox(ray, box):
    """Get collision info between ray and box"""
    result = _GetRayCollisionBox(ray, box)
    return result


def GetRayCollisionMesh(ray, mesh, transform):
    """Get collision info between ray and mesh"""
    result = _GetRayCollisionMesh(ray, mesh, transform)
    return result


def GetRayCollisionTriangle(ray, p1, p2, p3):
    """Get collision info between ray and triangle"""
    result = _GetRayCollisionTriangle(ray, _vec3(p1), _vec3(p2), _vec3(p3))
    return result


def GetRayCollisionQuad(ray, p1, p2, p3, p4):
    """Get collision info between ray and quad"""
    result = _GetRayCollisionQuad(ray, _vec3(p1), _vec3(p2), _vec3(p3), _vec3(p4))
    return result


def InitAudioDevice():
    """Initialize audio device and context"""
    _InitAudioDevice()


def CloseAudioDevice():
    """Close the audio device and context"""
    _CloseAudioDevice()


def IsAudioDeviceReady():
    """Check if audio device has been initialized successfully"""
    result = _IsAudioDeviceReady()
    return result


def SetMasterVolume(volume):
    """Set master volume (listener)"""
    _SetMasterVolume(float(volume))


def LoadWave(fileName):
    """Load wave data from file"""
    result = _LoadWave(_str_in(fileName))
    return result


def LoadWaveFromMemory(fileType, fileData, dataSize):
    """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
    result = _LoadWaveFromMemory(_str_in(fileType), _str_in(fileData), int(dataSize))
    return result


def IsWaveReady(wave):
    """Checks if wave data is ready"""
    result = _IsWaveReady(wave)
    return result


def LoadSound(fileName):
    """Load sound from file"""
    result = _LoadSound(_str_in(fileName))
    return result


def LoadSoundFromWave(wave):
    """Load sound from wave data"""
    result = _LoadSoundFromWave(wave)
    return result


def IsSoundReady(sound):
    """Checks if a sound is ready"""
    result = _IsSoundReady(sound)
    return result


def UpdateSound(sound, data, sampleCount):
    """Update sound buffer with new data"""
    _UpdateSound(sound, data, int(sampleCount))


def UnloadWave(wave):
    """Unload wave data"""
    _UnloadWave(wave)


def UnloadSound(sound):
    """Unload sound"""
    _UnloadSound(sound)


def ExportWave(wave, fileName):
    """Export wave data to file, returns true on success"""
    result = _ExportWave(wave, _str_in(fileName))
    return result


def ExportWaveAsCode(wave, fileName):
    """Export wave sample data to code (.h), returns true on success"""
    result = _ExportWaveAsCode(wave, _str_in(fileName))
    return result


def PlaySound(sound):
    """Play a sound"""
    _PlaySound(sound)


def StopSound(sound):
    """Stop playing a sound"""
    _StopSound(sound)


def PauseSound(sound):
    """Pause a sound"""
    _PauseSound(sound)


def ResumeSound(sound):
    """Resume a paused sound"""
    _ResumeSound(sound)


def IsSoundPlaying(sound):
    """Check if a sound is currently playing"""
    result = _IsSoundPlaying(sound)
    return result


def SetSoundVolume(sound, volume):
    """Set volume for a sound (1.0 is max level)"""
    _SetSoundVolume(sound, float(volume))


def SetSoundPitch(sound, pitch):
    """Set pitch for a sound (1.0 is base level)"""
    _SetSoundPitch(sound, float(pitch))


def SetSoundPan(sound, pan):
    """Set pan for a sound (0.5 is center)"""
    _SetSoundPan(sound, float(pan))


def WaveCopy(wave):
    """Copy a wave to a new wave"""
    result = _WaveCopy(wave)
    return result


def WaveCrop(wave, initSample, finalSample):
    """Crop a wave to defined samples range"""
    _WaveCrop(wave, int(initSample), int(finalSample))


def WaveFormat(wave, sampleRate, sampleSize, channels):
    """Convert wave data to desired format"""
    _WaveFormat(wave, int(sampleRate), int(sampleSize), int(channels))


def LoadWaveSamples(wave):
    """Load samples data from wave as a 32bit float data array"""
    result = _ptr_out(_LoadWaveSamples(wave))
    return result


def UnloadWaveSamples(samples):
    """Unload samples data loaded with LoadWaveSamples()"""
    _UnloadWaveSamples(samples)


def LoadMusicStream(fileName):
    """Load music stream from file"""
    result = _LoadMusicStream(_str_in(fileName))
    return result


def LoadMusicStreamFromMemory(fileType, data, dataSize):
    """Load music stream from data"""
    result = _LoadMusicStreamFromMemory(_str_in(fileType), _str_in(data), int(dataSize))
    return result


def IsMusicReady(music):
    """Checks if a music stream is ready"""
    result = _IsMusicReady(music)
    return result


def UnloadMusicStream(music):
    """Unload music stream"""
    _UnloadMusicStream(music)


def PlayMusicStream(music):
    """Start music playing"""
    _PlayMusicStream(music)


def IsMusicStreamPlaying(music):
    """Check if music is playing"""
    result = _IsMusicStreamPlaying(music)
    return result


def UpdateMusicStream(music):
    """Updates buffers for music streaming"""
    _UpdateMusicStream(music)


def StopMusicStream(music):
    """Stop music playing"""
    _StopMusicStream(music)


def PauseMusicStream(music):
    """Pause music playing"""
    _PauseMusicStream(music)


def ResumeMusicStream(music):
    """Resume playing paused music"""
    _ResumeMusicStream(music)


def SeekMusicStream(music, position):
    """Seek music to a position (in seconds)"""
    _SeekMusicStream(music, float(position))


def SetMusicVolume(music, volume):
    """Set volume for music (1.0 is max level)"""
    _SetMusicVolume(music, float(volume))


def SetMusicPitch(music, pitch):
    """Set pitch for a music (1.0 is base level)"""
    _SetMusicPitch(music, float(pitch))


def SetMusicPan(music, pan):
    """Set pan for a music (0.5 is center)"""
    _SetMusicPan(music, float(pan))


def GetMusicTimeLength(music):
    """Get music time length (in seconds)"""
    result = _GetMusicTimeLength(music)
    return result


def GetMusicTimePlayed(music):
    """Get current music time played (in seconds)"""
    result = _GetMusicTimePlayed(music)
    return result


def LoadAudioStream(sampleRate, sampleSize, channels):
    """Load audio stream (to stream raw audio pcm data)"""
    result = _LoadAudioStream(sampleRate, sampleSize, channels)
    return result


def IsAudioStreamReady(stream):
    """Checks if an audio stream is ready"""
    result = _IsAudioStreamReady(stream)
    return result


def UnloadAudioStream(stream):
    """Unload audio stream and free memory"""
    _UnloadAudioStream(stream)


def UpdateAudioStream(stream, data, frameCount):
    """Update audio stream buffers with data"""
    _UpdateAudioStream(stream, data, int(frameCount))


def IsAudioStreamProcessed(stream):
    """Check if any audio stream buffers requires refill"""
    result = _IsAudioStreamProcessed(stream)
    return result


def PlayAudioStream(stream):
    """Play audio stream"""
    _PlayAudioStream(stream)


def PauseAudioStream(stream):
    """Pause audio stream"""
    _PauseAudioStream(stream)


def ResumeAudioStream(stream):
    """Resume audio stream"""
    _ResumeAudioStream(stream)


def IsAudioStreamPlaying(stream):
    """Check if audio stream is playing"""
    result = _IsAudioStreamPlaying(stream)
    return result


def StopAudioStream(stream):
    """Stop audio stream"""
    _StopAudioStream(stream)


def SetAudioStreamVolume(stream, volume):
    """Set volume for audio stream (1.0 is max level)"""
    _SetAudioStreamVolume(stream, float(volume))


def SetAudioStreamPitch(stream, pitch):
    """Set pitch for audio stream (1.0 is base level)"""
    _SetAudioStreamPitch(stream, float(pitch))


def SetAudioStreamPan(stream, pan):
    """Set pan for audio stream (0.5 is centered)"""
    _SetAudioStreamPan(stream, float(pan))


def SetAudioStreamBufferSizeDefault(size):
    """Default size for new audio streams"""
    _SetAudioStreamBufferSizeDefault(int(size))


def SetAudioStreamCallback(stream, callback):
    """Audio thread callback to request new data"""
    _SetAudioStreamCallback(stream, callback)


def AttachAudioStreamProcessor(stream, processor):
    """Attach audio stream processor to stream"""
    _AttachAudioStreamProcessor(stream, processor)


def DetachAudioStreamProcessor(stream, processor):
    """Detach audio stream processor from stream"""
    _DetachAudioStreamProcessor(stream, processor)


def AttachAudioMixedProcessor(processor):
    """Attach audio stream processor to the entire audio pipeline"""
    _AttachAudioMixedProcessor(processor)


def DetachAudioMixedProcessor(processor):
    """Detach audio stream processor from the entire audio pipeline"""
    _DetachAudioMixedProcessor(processor)
