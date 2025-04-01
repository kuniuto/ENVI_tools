import envi_tool

color_wavelengths = [650, 550, 450] # [R, G, B]
band_width = 40

envi_fname = 'F:/bridge/data/ENVI/20240523/UV/ref_uv6_rice_Img-d(s20,g50,49.97ms,350-1100)_20240523_104142'

envi_tool.color_enhancement(envi_fname,color_wavelengths,band_width)

