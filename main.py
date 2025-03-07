import asyncio
from camoufox import AsyncCamoufox

inject = {
    "navigator.userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D5055b [FBAN/FBIOS;FBAV/496.0.0.23.103;FBBV/684558567;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/18.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/687045607;IABMV/1]",
    "navigator.appName": "Netscape",
    "navigator.platform": "iPhone",
    "navigator.maxTouchPoints": 5,
    "navigator.hardwareConcurrency": 4,
    "navigator.appVersion": "5.1.2",
    "navigator.appCodeName": "Mozilla",
    "navigator.productSub": "496.0.0.23.103",

    "screen.height": 932,
    "screen.width": 430,
    "screen.availWidth": 430,
    "screen.availHeight": 932,
    "screen.colorDepth": 24,

    "window.devicePixelRatio": 3,
    "window.innerWidth": 430,
    "window.innerHeight": 932,
    "window.outerWidth": 430,
    "window.outerHeight": 932,
    "window.screenX": 430,
    "window.screenY": 932,

    "webGl:renderer": "Apple GPU",
    "webGl:vendor": "Apple Inc.",
    "webGl:contextAttributes": {
        "alpha": True,
        "antialias": True,
        "depth": True,
        "failIfMajorPerformanceCaveat": False,
        "powerPreference": "default",
        "premultipliedAlpha": True,
        "preserveDrawingBuffer": False,
        "stencil": False
    },
    "webGl:supportedExtensions": [
        "ANGLE_instanced_arrays",
        "EXT_blend_minmax",
        "EXT_clip_control",
        "EXT_color_buffer_half_float",
        "EXT_depth_clamp",
        "EXT_frag_depth",
        "EXT_polygon_offset_clamp",
        "EXT_shader_texture_lod",
        "EXT_texture_filter_anisotropic",
        "EXT_texture_mirror_clamp_to_edge",
        "EXT_sRGB",
        "KHR_parallel_shader_compile",
        "OES_element_index_uint",
        "OES_fbo_render_mipmap",
        "OES_standard_derivatives",
        "OES_texture_float",
        "OES_texture_half_float",
        "OES_texture_half_float_linear",
        "OES_vertex_array_object",
        "WEBGL_blend_func_extended",
        "WEBGL_color_buffer_float",
        "WEBGL_compressed_texture_astc",
        "WEBGL_compressed_texture_etc",
        "WEBGL_compressed_texture_etc1",
        "WEBGL_compressed_texture_pvrtc",
        "WEBKIT_WEBGL_compressed_texture_pvrtc",
        "WEBGL_debug_renderer_info",
        "WEBGL_debug_shaders",
        "WEBGL_depth_texture",
        "WEBGL_draw_buffers",
        "WEBGL_lose_context",
        "WEBGL_multi_draw",
        "WEBGL_polygon_mode"
    ],
    "webGl:parameters": {
        "2849": 1,
        "2884": False,
        "2885": 1029,
        "2886": 2305,
        "2928": [
            0,
            1
        ],
        "2929": False,
        "2930": True,
        "2931": 1,
        "2932": 513,
        "2960": False,
        "2961": 0,
        "2962": 519,
        "2963": 2147483647,
        "2964": 7680,
        "2965": 7680,
        "2966": 7680,
        "2967": 0,
        "2968": 2147483647,
        "2978": [
            0,
            0,
            256,
            256
        ],
        "3024": True,
        "3042": False,
        "3074": None,
        "3088": [
            0,
            0,
            256,
            256
        ],
        "3089": False,
        "3106": [
            0,
            0,
            0,
            0
        ],
        "3107": [
            True,
            True,
            True,
            True
        ],
        "3314": None,
        "3315": None,
        "3316": None,
        "3317": 4,
        "3330": None,
        "3331": None,
        "3332": None,
        "3333": 4,
        "3379": 16384,
        "3386": [
            16384,
            16384
        ],
        "3408": 4,
        "3410": 8,
        "3411": 8,
        "3412": 8,
        "3413": 8,
        "3414": 24,
        "3415": 0,
        "7936": "WebKit",
        "7937": "WebKit WebGL",
        "7938": "WebGL 1.0",
        "10752": 0,
        "32773": [
            0,
            0,
            0,
            0
        ],
        "32777": 32774,
        "32823": False,
        "32824": 0,
        "32873": None,
        "32877": None,
        "32878": None,
        "32883": None,
        "32926": False,
        "32928": False,
        "32936": 1,
        "32937": 4,
        "32938": 1,
        "32939": False,
        "32968": 0,
        "32969": 1,
        "32970": 0,
        "32971": 1,
        "33000": None,
        "33001": None,
        "33170": 4352,
        "33901": [
            1,
            511
        ],
        "33902": [
            1,
            1
        ],
        "34016": 33984,
        "34024": 16384,
        "34045": None,
        "34047": None,
        "34068": None,
        "34076": 16384,
        "34467": None,
        "34816": 519,
        "34817": 7680,
        "34818": 7680,
        "34819": 7680,
        "34852": None,
        "34853": None,
        "34854": None,
        "34855": None,
        "34856": None,
        "34857": None,
        "34858": None,
        "34859": None,
        "34860": None,
        "34877": 32774,
        "34921": 16,
        "34930": 16,
        "34964": None,
        "34965": None,
        "35071": None,
        "35076": None,
        "35077": None,
        "35371": None,
        "35373": None,
        "35374": None,
        "35375": None,
        "35376": None,
        "35377": None,
        "35379": None,
        "35380": None,
        "35657": None,
        "35658": None,
        "35659": None,
        "35660": 16,
        "35661": 32,
        "35723": None,
        "35724": "WebGL GLSL ES 1.0 (1.0)",
        "35725": None,
        "35738": 5121,
        "35739": 6408,
        "35968": None,
        "35977": None,
        "35978": None,
        "35979": None,
        "36003": 0,
        "36004": 2147483647,
        "36005": 2147483647,
        "36006": None,
        "36007": None,
        "36063": None,
        "36183": None,
        "36203": None,
        "36345": 0,
        "36347": 1024,
        "36348": 31,
        "36349": 1024,
        "36387": None,
        "36388": None,
        "36392": None,
        "36795": None,
        "37137": None,
        "37154": None,
        "37157": None,
        "37440": False,
        "37441": False,
        "37443": 37444,
        "37444": None,
        "37445": "Apple Inc.",
        "37446": "Apple GPU",
        "37447": None,
        "38449": None
    },
    "webGl:shaderPrecisionFormats": {
        "35633,36336": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35633,36337": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35633,36338": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35633,36339": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35633,36340": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35633,36341": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35632,36336": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35632,36337": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35632,36338": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35632,36339": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35632,36340": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35632,36341": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        }
    },
    "webGl2:contextAttributes": {
        "alpha": True,
        "antialias": True,
        "depth": True,
        "failIfMajorPerformanceCaveat": False,
        "powerPreference": "default",
        "premultipliedAlpha": True,
        "preserveDrawingBuffer": False,
        "stencil": False
    },
    "webGl2:supportedExtensions": [
        "EXT_clip_control",
        "EXT_color_buffer_float",
        "EXT_color_buffer_half_float",
        "EXT_conservative_depth",
        "EXT_depth_clamp",
        "EXT_polygon_offset_clamp",
        "EXT_render_snorm",
        "EXT_texture_filter_anisotropic",
        "EXT_texture_mirror_clamp_to_edge",
        "EXT_texture_norm16",
        "KHR_parallel_shader_compile",
        "NV_shader_noperspective_interpolation",
        "OES_draw_buffers_indexed",
        "OES_sample_variables",
        "OES_shader_multisample_interpolation",
        "WEBGL_blend_func_extended",
        "WEBGL_clip_cull_distance",
        "WEBGL_compressed_texture_astc",
        "WEBGL_compressed_texture_etc",
        "WEBGL_compressed_texture_etc1",
        "WEBGL_compressed_texture_pvrtc",
        "WEBKIT_WEBGL_compressed_texture_pvrtc",
        "WEBGL_debug_renderer_info",
        "WEBGL_debug_shaders",
        "WEBGL_lose_context",
        "WEBGL_multi_draw",
        "WEBGL_polygon_mode",
        "WEBGL_provoking_vertex",
        "WEBGL_render_shared_exponent",
        "WEBGL_stencil_texturing"
    ],
    "webGl2:parameters": {
        "2849": 1,
        "2884": False,
        "2885": 1029,
        "2886": 2305,
        "2928": [
            0,
            1
        ],
        "2929": False,
        "2930": True,
        "2931": 1,
        "2932": 513,
        "2960": False,
        "2961": 0,
        "2962": 519,
        "2963": 2147483647,
        "2964": 7680,
        "2965": 7680,
        "2966": 7680,
        "2967": 0,
        "2968": 2147483647,
        "2978": [
            0,
            0,
            256,
            256
        ],
        "3024": True,
        "3042": False,
        "3074": 1029,
        "3088": [
            0,
            0,
            256,
            256
        ],
        "3089": False,
        "3106": [
            0,
            0,
            0,
            0
        ],
        "3107": [
            True,
            True,
            True,
            True
        ],
        "3314": 0,
        "3315": 0,
        "3316": 0,
        "3317": 4,
        "3330": 0,
        "3331": 0,
        "3332": 0,
        "3333": 4,
        "3379": 16384,
        "3386": [
            16384,
            16384
        ],
        "3408": 4,
        "3410": 8,
        "3411": 8,
        "3412": 8,
        "3413": 8,
        "3414": 24,
        "3415": 0,
        "7936": "WebKit",
        "7937": "WebKit WebGL",
        "7938": "WebGL 2.0",
        "10752": 0,
        "32773": [
            0,
            0,
            0,
            0
        ],
        "32777": 32774,
        "32823": False,
        "32824": 0,
        "32873": None,
        "32877": 0,
        "32878": 0,
        "32883": 2048,
        "32926": False,
        "32928": False,
        "32936": 1,
        "32937": 4,
        "32938": 1,
        "32939": False,
        "32968": 0,
        "32969": 1,
        "32970": 0,
        "32971": 1,
        "33000": 2147483647,
        "33001": 2147483647,
        "33170": 4352,
        "33901": [
            1,
            511
        ],
        "33902": [
            1,
            1
        ],
        "34016": 33984,
        "34024": 16384,
        "34045": 15,
        "34047": None,
        "34068": None,
        "34076": 16384,
        "34467": None,
        "34816": 519,
        "34817": 7680,
        "34818": 7680,
        "34819": 7680,
        "34852": 8,
        "34853": 1029,
        "34854": 1029,
        "34855": 1029,
        "34856": 1029,
        "34857": 1029,
        "34858": 1029,
        "34859": 1029,
        "34860": 1029,
        "34877": 32774,
        "34921": 16,
        "34930": 16,
        "34964": None,
        "34965": None,
        "35071": 2048,
        "35076": -8,
        "35077": 7,
        "35371": 12,
        "35373": 12,
        "35374": 24,
        "35375": 24,
        "35376": 16384,
        "35377": 53248,
        "35379": 53248,
        "35380": 16,
        "35657": 4096,
        "35658": 4096,
        "35659": 124,
        "35660": 16,
        "35661": 32,
        "35723": 4352,
        "35724": "WebGL GLSL ES 3.00",
        "35725": None,
        "35738": 5121,
        "35739": 6408,
        "35968": 4,
        "35977": False,
        "35978": 128,
        "35979": 4,
        "36003": 0,
        "36004": 2147483647,
        "36005": 2147483647,
        "36006": None,
        "36007": None,
        "36063": 8,
        "36183": 4,
        "36203": 4294967294,
        "36345": 0,
        "36347": 1024,
        "36348": 31,
        "36349": 1024,
        "36387": False,
        "36388": False,
        "36392": None,
        "36795": None,
        "37137": 0,
        "37154": 124,
        "37157": 124,
        "37440": False,
        "37441": False,
        "37443": 37444,
        "37444": None,
        "37445": "Apple Inc.",
        "37446": "Apple GPU",
        "37447": 0,
        "38449": None
    },
    "webGl2:shaderPrecisionFormats": {
        "35633,36336": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35633,36337": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35633,36338": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35633,36339": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35633,36340": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35633,36341": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35632,36336": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35632,36337": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35632,36338": {
            "rangeMin": 127,
            "rangeMax": 127,
            "precision": 23
        },
        "35632,36339": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35632,36340": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        },
        "35632,36341": {
            "rangeMin": 31,
            "rangeMax": 30,
            "precision": 0
        }
    }
}

# Camoufox浏览器线程
async def handle_url(url):
    async with AsyncCamoufox(
            os="macos",
            config=inject,
            fonts=[".Al Bayan PUA", ".Al Nile PUA", ".Al Tarikh PUA", ".Apple Color Emoji UI",
                   ".Apple SD Gothic NeoI", ".Aqua Kana", ".Aqua Kana Bold", ".Aqua かな", ".Aqua かな ボールド",
                   ".Arial Hebrew Desk Interface", ".Baghdad PUA", ".Beirut PUA", ".Damascus PUA",
                   ".DecoType Naskh PUA", ".Diwan Kufi PUA", ".Farah PUA", ".Geeza Pro Interface", ".Geeza Pro PUA",
                   ".Helvetica LT MM", ".Hiragino Kaku Gothic Interface", ".Hiragino Sans GB Interface",
                   ".Keyboard", ".KufiStandardGK PUA", ".LastResort", ".Lucida Grande UI", ".Muna PUA",
                   ".Nadeem PUA", ".New York", ".Noto Nastaliq Urdu UI", ".PingFang HK", ".PingFang SC",
                   ".PingFang TC", ".SF Arabic", ".SF Arabic Rounded", ".SF Compact", ".SF Compact Rounded",
                   ".SF NS", ".SF NS Mono", ".SF NS Rounded", ".Sana PUA", ".Savoye LET CC.", ".ThonburiUI",
                   ".ThonburiUIWatch", ".苹方-港", ".苹方-简", ".苹方-繁", ".蘋方-港", ".蘋方-簡", ".蘋方-繁",
                   "Academy Engraved LET", "Al Bayan", "Al Nile", "Al Tarikh", "American Typewriter", "Andale Mono",
                   "Apple Braille", "Apple Chancery", "Apple Color Emoji", "Apple SD Gothic Neo",
                   "Apple SD 산돌고딕 Neo", "Apple Symbols", "AppleGothic", "AppleMyungjo", "Arial", "Arial Black",
                   "Arial Hebrew", "Arial Hebrew Scholar", "Arial Narrow", "Arial Rounded MT Bold",
                   "Arial Unicode MS", "Athelas", "Avenir", "Avenir Black", "Avenir Black Oblique", "Avenir Book",
                   "Avenir Heavy", "Avenir Light", "Avenir Medium", "Avenir Next", "Avenir Next Condensed",
                   "Avenir Next Condensed Demi Bold", "Avenir Next Condensed Heavy", "Avenir Next Condensed Medium",
                   "Avenir Next Condensed Ultra Light", "Avenir Next Demi Bold", "Avenir Next Heavy",
                   "Avenir Next Medium", "Avenir Next Ultra Light", "Ayuthaya", "Baghdad", "Bangla MN",
                   "Bangla Sangam MN", "Baskerville", "Beirut", "Big Caslon", "Bodoni 72", "Bodoni 72 Oldstyle",
                   "Bodoni 72 Smallcaps", "Bodoni Ornaments", "Bradley Hand", "Brush Script MT", "Chalkboard",
                   "Chalkboard SE", "Chalkduster", "Charter", "Charter Black", "Cochin", "Comic Sans MS",
                   "Copperplate", "Corsiva Hebrew", "Courier", "Courier New", "Czcionka systemowa", "DIN Alternate",
                   "DIN Condensed", "Damascus", "DecoType Naskh", "Devanagari MT", "Devanagari Sangam MN", "Didot",
                   "Diwan Kufi", "Diwan Thuluth", "Euphemia UCAS", "Farah", "Farisi", "Font Sistem",
                   "Font de sistem", "Font di sistema", "Font sustava", "Fonte do Sistema", "Futura",
                   "GB18030 Bitmap", "Galvji", "Geeza Pro", "Geneva", "Georgia", "Gill Sans", "Grantha Sangam MN",
                   "Gujarati MT", "Gujarati Sangam MN", "Gurmukhi MN", "Gurmukhi MT", "Gurmukhi Sangam MN",
                   "Heiti SC", "Heiti TC", "Heiti-간체", "Heiti-번체", "Helvetica", "Helvetica Neue", "Herculanum",
                   "Hiragino Kaku Gothic Pro", "Hiragino Kaku Gothic Pro W3", "Hiragino Kaku Gothic Pro W6",
                   "Hiragino Kaku Gothic ProN", "Hiragino Kaku Gothic ProN W3", "Hiragino Kaku Gothic ProN W6",
                   "Hiragino Kaku Gothic Std", "Hiragino Kaku Gothic Std W8", "Hiragino Kaku Gothic StdN",
                   "Hiragino Kaku Gothic StdN W8", "Hiragino Maru Gothic Pro", "Hiragino Maru Gothic Pro W4",
                   "Hiragino Maru Gothic ProN", "Hiragino Maru Gothic ProN W4", "Hiragino Mincho Pro",
                   "Hiragino Mincho Pro W3", "Hiragino Mincho Pro W6", "Hiragino Mincho ProN",
                   "Hiragino Mincho ProN W3", "Hiragino Mincho ProN W6", "Hiragino Sans", "Hiragino Sans GB",
                   "Hiragino Sans GB W3", "Hiragino Sans GB W6", "Hiragino Sans W0", "Hiragino Sans W1",
                   "Hiragino Sans W2", "Hiragino Sans W3", "Hiragino Sans W4", "Hiragino Sans W5",
                   "Hiragino Sans W6", "Hiragino Sans W7", "Hiragino Sans W8", "Hiragino Sans W9", "Hoefler Text",
                   "Hoefler Text Ornaments", "ITF Devanagari", "ITF Devanagari Marathi", "Impact", "InaiMathi",
                   "Iowan Old Style", "Iowan Old Style Black", "Järjestelmäfontti", "Kailasa", "Kannada MN",
                   "Kannada Sangam MN", "Kefa", "Khmer MN", "Khmer Sangam MN", "Kohinoor Bangla",
                   "Kohinoor Devanagari", "Kohinoor Gujarati", "Kohinoor Telugu", "Kokonor", "Krungthep",
                   "KufiStandardGK", "Lao MN", "Lao Sangam MN", "Lucida Grande", "Luminari", "Malayalam MN",
                   "Malayalam Sangam MN", "Marion", "Marker Felt", "Menlo", "Microsoft Sans Serif", "Mishafi",
                   "Mishafi Gold", "Monaco", "Mshtakan", "Mukta Mahee", "MuktaMahee Bold", "MuktaMahee ExtraBold",
                   "MuktaMahee ExtraLight", "MuktaMahee Light", "MuktaMahee Medium", "MuktaMahee Regular",
                   "MuktaMahee SemiBold", "Muna", "Myanmar MN", "Myanmar Sangam MN", "Nadeem", "New Peninim MT",
                   "Noteworthy", "Noto Nastaliq Urdu", "Noto Sans Adlam", "Noto Sans Armenian",
                   "Noto Sans Armenian Blk", "Noto Sans Armenian ExtBd", "Noto Sans Armenian ExtLt",
                   "Noto Sans Armenian Light", "Noto Sans Armenian Med", "Noto Sans Armenian SemBd",
                   "Noto Sans Armenian Thin", "Noto Sans Avestan", "Noto Sans Bamum", "Noto Sans Bassa Vah",
                   "Noto Sans Batak", "Noto Sans Bhaiksuki", "Noto Sans Brahmi", "Noto Sans Buginese",
                   "Noto Sans Buhid", "Noto Sans CanAborig", "Noto Sans Canadian Aboriginal", "Noto Sans Carian",
                   "Noto Sans CaucAlban", "Noto Sans Caucasian Albanian", "Noto Sans Chakma", "Noto Sans Cham",
                   "Noto Sans Coptic", "Noto Sans Cuneiform", "Noto Sans Cypriot", "Noto Sans Duployan",
                   "Noto Sans EgyptHiero", "Noto Sans Egyptian Hieroglyphs", "Noto Sans Elbasan",
                   "Noto Sans Glagolitic", "Noto Sans Gothic", "Noto Sans Gunjala Gondi",
                   "Noto Sans Hanifi Rohingya", "Noto Sans HanifiRohg", "Noto Sans Hanunoo", "Noto Sans Hatran",
                   "Noto Sans ImpAramaic", "Noto Sans Imperial Aramaic", "Noto Sans InsPahlavi",
                   "Noto Sans InsParthi", "Noto Sans Inscriptional Pahlavi", "Noto Sans Inscriptional Parthian",
                   "Noto Sans Javanese", "Noto Sans Kaithi", "Noto Sans Kannada", "Noto Sans Kannada Black",
                   "Noto Sans Kannada ExtraBold", "Noto Sans Kannada ExtraLight", "Noto Sans Kannada Light",
                   "Noto Sans Kannada Medium", "Noto Sans Kannada SemiBold", "Noto Sans Kannada Thin",
                   "Noto Sans Kayah Li", "Noto Sans Kharoshthi", "Noto Sans Khojki", "Noto Sans Khudawadi",
                   "Noto Sans Lepcha", "Noto Sans Limbu", "Noto Sans Linear A", "Noto Sans Linear B",
                   "Noto Sans Lisu", "Noto Sans Lycian", "Noto Sans Lydian", "Noto Sans Mahajani",
                   "Noto Sans Mandaic", "Noto Sans Manichaean", "Noto Sans Marchen", "Noto Sans Masaram Gondi",
                   "Noto Sans Meetei Mayek", "Noto Sans Mende Kikakui", "Noto Sans Meroitic", "Noto Sans Miao",
                   "Noto Sans Modi", "Noto Sans Mongolian", "Noto Sans Mro", "Noto Sans Multani",
                   "Noto Sans Myanmar", "Noto Sans Myanmar Blk", "Noto Sans Myanmar ExtBd",
                   "Noto Sans Myanmar ExtLt", "Noto Sans Myanmar Light", "Noto Sans Myanmar Med",
                   "Noto Sans Myanmar SemBd", "Noto Sans Myanmar Thin", "Noto Sans NKo", "Noto Sans Nabataean",
                   "Noto Sans New Tai Lue", "Noto Sans Newa", "Noto Sans Ol Chiki", "Noto Sans Old Hungarian",
                   "Noto Sans Old Italic", "Noto Sans Old North Arabian", "Noto Sans Old Permic",
                   "Noto Sans Old Persian", "Noto Sans Old South Arabian", "Noto Sans Old Turkic",
                   "Noto Sans OldHung", "Noto Sans OldNorArab", "Noto Sans OldSouArab", "Noto Sans Oriya",
                   "Noto Sans Osage", "Noto Sans Osmanya", "Noto Sans Pahawh Hmong", "Noto Sans Palmyrene",
                   "Noto Sans Pau Cin Hau", "Noto Sans PhagsPa", "Noto Sans Phoenician", "Noto Sans PsaPahlavi",
                   "Noto Sans Psalter Pahlavi", "Noto Sans Rejang", "Noto Sans Samaritan", "Noto Sans Saurashtra",
                   "Noto Sans Sharada", "Noto Sans Siddham", "Noto Sans Sora Sompeng", "Noto Sans SoraSomp",
                   "Noto Sans Sundanese", "Noto Sans Syloti Nagri", "Noto Sans Syriac", "Noto Sans Tagalog",
                   "Noto Sans Tagbanwa", "Noto Sans Tai Le", "Noto Sans Tai Tham", "Noto Sans Tai Viet",
                   "Noto Sans Takri", "Noto Sans Thaana", "Noto Sans Tifinagh", "Noto Sans Tirhuta",
                   "Noto Sans Ugaritic", "Noto Sans Vai", "Noto Sans Wancho", "Noto Sans Warang Citi",
                   "Noto Sans Yi", "Noto Sans Zawgyi", "Noto Sans Zawgyi Blk", "Noto Sans Zawgyi ExtBd",
                   "Noto Sans Zawgyi ExtLt", "Noto Sans Zawgyi Light", "Noto Sans Zawgyi Med",
                   "Noto Sans Zawgyi SemBd", "Noto Sans Zawgyi Thin", "Noto Serif Ahom", "Noto Serif Balinese",
                   "Noto Serif Hmong Nyiakeng", "Noto Serif Myanmar", "Noto Serif Myanmar Blk",
                   "Noto Serif Myanmar ExtBd", "Noto Serif Myanmar ExtLt", "Noto Serif Myanmar Light",
                   "Noto Serif Myanmar Med", "Noto Serif Myanmar SemBd", "Noto Serif Myanmar Thin",
                   "Noto Serif Yezidi", "Optima", "Oriya MN", "Oriya Sangam MN", "PT Mono", "PT Sans",
                   "PT Sans Caption", "PT Sans Narrow", "PT Serif", "PT Serif Caption", "Palatino", "Papyrus",
                   "Party LET", "Phosphate", "Phông chữ Hệ thống", "PingFang HK", "PingFang SC", "PingFang TC",
                   "Plantagenet Cherokee", "Police système", "Raanana", "Rendszerbetűtípus", "Rockwell",
                   "STIX Two Math", "STIX Two Text", "STIXGeneral", "STIXIntegralsD", "STIXIntegralsSm",
                   "STIXIntegralsUp", "STIXIntegralsUpD", "STIXIntegralsUpSm", "STIXNonUnicode", "STIXSizeFiveSym",
                   "STIXSizeFourSym", "STIXSizeOneSym", "STIXSizeThreeSym", "STIXSizeTwoSym", "STIXVariants",
                   "STSong", "Sana", "Sathu", "Savoye LET", "Seravek", "Seravek ExtraLight", "Seravek Light",
                   "Seravek Medium", "Shree Devanagari 714", "SignPainter", "SignPainter-HouseScript", "Silom",
                   "Sinhala MN", "Sinhala Sangam MN", "Sistem Fontu", "Skia", "Snell Roundhand", "Songti SC",
                   "Songti TC", "Sukhumvit Set", "Superclarendon", "Symbol", "Systeemlettertype", "System Font",
                   "Systemschrift", "Systemskrift", "Systemtypsnitt", "Systémové písmo", "Tahoma", "Tamil MN",
                   "Tamil Sangam MN", "Telugu MN", "Telugu Sangam MN", "Thonburi", "Times", "Times New Roman",
                   "Tipo de letra del sistema", "Tipo de letra do sistema", "Tipus de lletra del sistema",
                   "Trattatello", "Trebuchet MS", "Verdana", "Waseem", "Webdings", "Wingdings", "Wingdings 2",
                   "Wingdings 3", "Zapf Dingbats", "Zapfino", "Γραμματοσειρά συστήματος", "Системний шрифт",
                   "Системный шрифт", "גופן מערכת", "البيان", "التاريخ", "النيل", "بغداد", "بيروت", "جيزة",
                   "خط النظام", "دمشق", "ديوان ثلث", "ديوان كوفي", "صنعاء", "فارسي", "فرح", "كوفي", "منى", "مِصحفي",
                   "مِصحفي ذهبي", "نديم", "نسخ", "وسيم", "आई॰टी॰एफ़॰ देवनागरी", "आई॰टी॰एफ़॰ देवनागरी मराठी",
                   "कोहिनूर देवनागरी", "देवनागरी एम॰टी॰", "देवनागरी संगम एम॰एन॰", "श्री देवनागरी ७१४",
                   "แบบอักษรระบบ", "⹁煵愠芩苈", "システムフォント", "ヒラギノ丸ゴ Pro", "ヒラギノ丸ゴ Pro W4",
                   "ヒラギノ丸ゴ ProN", "ヒラギノ丸ゴ ProN W4", "ヒラギノ明朝 Pro", "ヒラギノ明朝 Pro W3",
                   "ヒラギノ明朝 Pro W6", "ヒラギノ明朝 ProN", "ヒラギノ明朝 ProN W3", "ヒラギノ明朝 ProN W6",
                   "ヒラギノ角ゴ Pro", "ヒラギノ角ゴ Pro W3", "ヒラギノ角ゴ Pro W6", "ヒラギノ角ゴ ProN",
                   "ヒラギノ角ゴ ProN W3", "ヒラギノ角ゴ ProN W6", "ヒラギノ角ゴ Std", "ヒラギノ角ゴ Std W8",
                   "ヒラギノ角ゴ StdN", "ヒラギノ角ゴ StdN W8", "ヒラギノ角ゴ 簡体中文", "ヒラギノ角ゴ 簡体中文 W3",
                   "ヒラギノ角ゴ 簡体中文 W6", "ヒラギノ角ゴシック", "ヒラギノ角ゴシック W0",
                   "ヒラギノ角ゴシック W1", "ヒラギノ角ゴシック W2", "ヒラギノ角ゴシック W3",
                   "ヒラギノ角ゴシック W4", "ヒラギノ角ゴシック W5", "ヒラギノ角ゴシック W6",
                   "ヒラギノ角 ゴシック W7", "ヒラギノ角ゴシック W8", "ヒラギノ角ゴシック W9", "冬青黑体简体中文",
                   "冬青黑体简体中文 W3", "冬青黑体简体中文 W6", "冬青黑體簡體中文", "冬青黑體簡體中文 W3",
                   "冬青黑體簡體中文 W6", "宋体-简", "宋体-繁", "宋體-簡", "宋體-繁", "系統字體", "系统字体",
                   "苹方-港", "苹方-简", "苹方-繁", "荱莉荍荭詰荓⁐牯", "荱莉荍荭詰荓⁓瑤", "荱莉荍荭詰荓荖荢荎",
                   "荱莉荍荭諛荓⁐牯", "荱莉荍荭难銩⁐牯", "蘋方-港", "蘋方-簡", "蘋方-繁", "黑体-简", "黑体-繁",
                   "黑體-簡", "黑體-繁", "黒体-簡", "黒体-繁", "시스템 서체"],
            enable_cache=True,
            geoip=True,
            proxy={
                'server': 'as.lumiproxy.com:5888',
                'username': 'lumi-lewis007_area-US_state-Newyork',
                'password': 'lewis1719',
            },
            window=(1282, 955),
            locale="en-US",
            block_images=True,
            block_webrtc=True,
            humanize=True,
            headless=False,
            firefox_user_prefs={
                "network.protocol-handler.external.whatsapp": True,
                "network.protocol-handler.warn-external.whatsapp": True,
            }
    ) as browser:
        context = await browser.new_context(
            extra_http_headers={
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Upgrade-Insecure-Requests': '1'
            },
            bypass_csp=True,
            reduced_motion='no-preference',
            accept_downloads=True,
            permissions=['geolocation', 'notifications'],
            java_script_enabled=True,
        )
        await context.set_extra_http_headers(
            {
                # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                # 'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'X-Requested-With': 'com.facebook.Facebook',
                'FBAPP-BROWSER-VERSION': '492.0.0.101.111',
                'X-FB-HTTP-Engine': 'Liger',
                "Origin": 'https://m.facebook.com',
                "Referer": 'https://m.facebook.com/'
            }
        )
        try:
            return await _process_page(context, url, visited=set())
        finally:
            await context.close()

async def _process_page(context, url, visited, depth=0):
    if depth > 2:  # 防止无限递归
        print("⚠️ 达到最大递归深度")
        return None

    if url in visited:
        return None
    visited.add(url)

    page = await context.new_page()

    page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "stylesheet", "font"] else route.continue_())

    try:

        await dismiss_modal(page)

        # 注册事件监听器，用于捕获真正的导航事件
        target_future = asyncio.get_event_loop().create_future()

        async def handle_request(request):
            if request.resource_type == "document":
                new_url = request.url
                print(f"[方法1] 主框架跳转至: {new_url}")
                if "chat.whatsapp.com" in new_url and not target_future.done():
                    target_future.set_result(new_url)

        def on_frame_navigated(frame):
            # 仅关注主框架的跳转
            if frame == page.main_frame:
                new_url = frame.url
                print(f"[方法1] 主框架跳转至: {new_url}")
                if "chat.whatsapp.com" in new_url and not target_future.done():
                    target_future.set_result(new_url)

        def on_response(response):
            if response.request.resource_type == "document":
                new_url = response.url
                print(f"[方法2] 导航完成: {new_url}")
                if "chat.whatsapp.com" in new_url and not target_future.done():
                    target_future.set_result(new_url)

        page.on("request", handle_request)
        page.on("framenavigated", on_frame_navigated)
        page.on("response", on_response)


        # 导航至指定 URL，等待网络空闲状态

        await asyncio.gather(
            page.goto(url, wait_until="networkidle", timeout=60000),
            page.wait_for_selector("css=*", timeout=60000)
        )

        await asyncio.sleep(10)

        # 尝试等待短暂时间，捕获页面 goto 后的真实跳转
        try:
            new_url = await asyncio.wait_for(target_future, timeout=10)
            if new_url:
                print(f"✅ 已到目标页面：{new_url}")
                return new_url
        except asyncio.TimeoutError:
            pass
        finally:
            page.remove_listener("framenavigated", on_frame_navigated)
            page.remove_listener("response", on_response)

        # 如果 goto 后页面 URL 已包含目标字符串，直接返回
        if "chat.whatsapp.com" in page.url:
            print(f"✅ 已到目标页面：{page.url}")
            return page.url

        # 如果页面中有弹窗（例如 alert）覆盖页面，也尝试关闭
        await dismiss_modal(page)

        # 使用多种策略查找 Join 按钮
        buttons = await _find_join_buttons(page)
        print(f"🔍 发现 {len(buttons)} 个候选按钮")

        # 遍历候选按钮，依次尝试点击
        for btn in buttons:
            try:
                try:
                    btn_text = await btn.text_content() or "<无文本>"
                except Exception:
                    btn_text = "<无法获取文本>"
                print(f"🔄 尝试点击按钮：{btn_text}")
                result = await _click_and_track(context, page, btn, visited, depth)
                await asyncio.sleep(5)  # 使用 asyncio.sleep 而不是阻塞式 sleep
                if result:
                    return result
            except Exception as e:
                print(f"⚠️ 按钮点击尝试失败：{str(e)}")
                continue

        return None

    except Exception as e:
        print(f"❌ 页面处理异常：{str(e)}")
        return None
    finally:
        await page.close()

async def _find_join_buttons(page):
    """使用多种选择器策略查找 Join 按钮"""
    selectors = [
        # 通用按钮选择器（不区分大小写）
        "xpath=//*[contains(translate(text(), 'JOIN', 'join'), 'join')][self::button or self::a]",
        # 常见类名模式
        ".btn-join, .join-button, [class*='join'], [id*='join']",
        # 链接文本查找
        "a:has-text('Join'), a:has-text('Join Group')",
        # 按钮角色属性
        "[role='button']:has-text('Join')"
    ]
    found = set()
    for selector in selectors:
        elements = await page.query_selector_all(selector)
        for el in elements:
            if await el.is_visible():
                found.add(el)
    return list(found)

async def dismiss_modal(page):
    """
    检测页面中是否存在遮挡的弹窗（如 div.section__model），
    如果存在则尝试点击关闭按钮或者直接移除该元素
    """
    modal = await page.query_selector("div.section__model")
    if modal and await modal.is_visible():
        print("🔔 检测到弹窗，尝试关闭...")
        # 尝试查找关闭按钮（根据实际情况调整选择器）
        close_btn = await modal.query_selector("button.close, .close, [aria-label='Close']")
        if close_btn:
            try:
                await close_btn.click(timeout=2500)
                print("✅ 弹窗已关闭")
            except Exception as e:
                print(f"⚠️ 关闭弹窗失败：{e}")
        else:
            try:
                await page.evaluate("document.querySelector('div.section__model')?.remove()")
                print("✅ 弹窗已移除")
            except Exception as e:
                print(f"⚠️ 移除弹窗失败：{e}")

async def _click_and_track(context, origin_page, element, visited, depth):
    try:
        # 在点击前预先获取按钮信息（避免页面跳转后句柄失效）
        try:
            element_text = await element.text_content() or "<无文本>"
        except Exception:
            element_text = "<无法获取文本>"
        try:
            element_selector = await element.evaluate(
                "el => el.tagName + (el.id ? `#${el.id}` : '') + (el.className ? `.${el.className}` : '')"
            )
        except Exception:
            element_selector = "<无法获取选择器>"
        print(f"🖱️ 尝试点击按钮：{element_text} [{element_selector}]")

        # 在点击之前注册事件监听器以捕获真实的页面跳转
        target_future = asyncio.get_event_loop().create_future()

        async def handle_request(request):
            if request.resource_type == "document":
                new_url = request.url
                print(f"[方法1] 主框架跳转至: {new_url}")
                if "chat.whatsapp.com" in new_url and not target_future.done():
                    target_future.set_result(new_url)

        def on_frame_navigated(frame):
            if frame == origin_page.main_frame:
                new_url = frame.url
                print(f"[方法1] 主框架跳转至: {new_url}")
                if "chat.whatsapp.com" in new_url and not target_future.done():
                    target_future.set_result(new_url)

        def on_response(response):
            if response.request.resource_type == "document":
                new_url = response.url
                print(f"[方法2] 导航完成: {new_url}")
                if "chat.whatsapp.com" in new_url and not target_future.done():
                    target_future.set_result(new_url)

        context.on("framenavigated", on_frame_navigated)
        context.on("response", on_response)
        context.on("request", handle_request)

        try:
            # 点击动作（注意：此处必须在事件监听器已注册后执行点击）
            await element.click(timeout=10000)
        except Exception as click_err:
            err_message = str(click_err)
            if "intercepts pointer events" in err_message:
                print("⚠️ 点击被拦截，可能是弹窗覆盖。尝试关闭弹窗后重试...")
                await dismiss_modal(origin_page)
                await element.click(timeout=10000)
            else:
                print(f"⏰ 点击异常：{err_message}")
                raise click_err

        try:
            # 等待最多 10 秒捕获跳转事件
            new_url = await asyncio.wait_for(target_future, timeout=10)
            return new_url
        except asyncio.TimeoutError as te:
            print(f"⏰ 等待导航事件超时：{te}")
        finally:
            # 注销事件监听器
            context.remove_listener("framenavigated", on_frame_navigated)
            context.remove_listener("response", on_response)

        # Fallback：等待页面加载状态，然后检查当前 URL
        try:
            await origin_page.wait_for_load_state("networkidle", timeout=5000)
        except Exception as load_err:
            print(f"⏰ 等待页面加载超时：{load_err}")
        current_url = origin_page.url
        print(f"🔄 当前页跳转至：{current_url}")
        if "chat.whatsapp.com" in current_url:
            return current_url
        else:
            return await _process_page(context, current_url, visited, depth + 1)

    except Exception as e:
        print(f"🛑 点击操作失败：{str(e)}")
        return None



async def main():
    links = "https://financeee.site/us-f/stock/gen/"
    url = await handle_url(links)
    print(url)

if __name__ == "__main__":
    asyncio.run(main())
