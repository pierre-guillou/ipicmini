# state file generated using paraview version 5.6.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Load TTK plugin
paraview.simple.LoadPlugin(
    "/usr/local/lib/plugins/libTopologyToolKit.so", ns=globals()
)


def RequestDataDescription(_):
    pass

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1054, 1116]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [4.999995231628418, 4.999995231628418, 4.999995231628418]
renderView1.StereoType = 0
renderView1.CameraPosition = [-0.8483740451634203, 0.4682131099896808, -1.1367454385001476]
renderView1.CameraFocalPoint = [4.949923245169065, -0.6467021605253241, 3.7781458485226906]
renderView1.CameraViewUp = [-0.15876639053132546, 0.9058223267808129, 0.39278384073565076]
renderView1.CameraParallelScale = 9.169672001063862
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024
spreadSheetView1.FieldAssociation = 'Field Data'
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath='data/cinema.cdb')

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)
tTKCinemaProductReader1.FilepathColumn = [None, 'FILE']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKCinemaProductReader1
tTKCinemaProductReader1Display = Show(tTKCinemaProductReader1, renderView1)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]
vtkBlockColorsLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# trace defaults for the display properties.
tTKCinemaProductReader1Display.Representation = 'Surface'
tTKCinemaProductReader1Display.ColorArrayName = ['FIELD', 'vtkBlockColors']
tTKCinemaProductReader1Display.LookupTable = vtkBlockColorsLUT
tTKCinemaProductReader1Display.OSPRayScaleArray = 'Birth'
tTKCinemaProductReader1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKCinemaProductReader1Display.SelectOrientationVectors = 'Birth'
tTKCinemaProductReader1Display.ScaleFactor = 0.9999990463256836
tTKCinemaProductReader1Display.SelectScaleArray = 'Birth'
tTKCinemaProductReader1Display.GlyphType = 'Arrow'
tTKCinemaProductReader1Display.GlyphTableIndexArray = 'Birth'
tTKCinemaProductReader1Display.GaussianRadius = 0.04999995231628418
tTKCinemaProductReader1Display.SetScaleArray = ['POINTS', 'Birth']
tTKCinemaProductReader1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKCinemaProductReader1Display.OpacityArray = ['POINTS', 'Birth']
tTKCinemaProductReader1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKCinemaProductReader1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKCinemaProductReader1Display.SelectionCellLabelFontFile = ''
tTKCinemaProductReader1Display.SelectionPointLabelFontFile = ''
tTKCinemaProductReader1Display.PolarAxes = 'PolarAxesRepresentation'
tTKCinemaProductReader1Display.ScalarOpacityFunction = vtkBlockColorsPWF
tTKCinemaProductReader1Display.ScalarOpacityUnitDistance = 0.6543147533342097

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKCinemaProductReader1Display.DataAxesGrid.XTitleFontFile = ''
tTKCinemaProductReader1Display.DataAxesGrid.YTitleFontFile = ''
tTKCinemaProductReader1Display.DataAxesGrid.ZTitleFontFile = ''
tTKCinemaProductReader1Display.DataAxesGrid.XLabelFontFile = ''
tTKCinemaProductReader1Display.DataAxesGrid.YLabelFontFile = ''
tTKCinemaProductReader1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKCinemaProductReader1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKCinemaProductReader1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKCinemaProductReader1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKCinemaProductReader1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for vtkBlockColorsLUT in view renderView1
vtkBlockColorsLUTColorBar = GetScalarBar(vtkBlockColorsLUT, renderView1)
vtkBlockColorsLUTColorBar.Title = 'vtkBlockColors'
vtkBlockColorsLUTColorBar.ComponentTitle = ''
vtkBlockColorsLUTColorBar.TitleFontFile = ''
vtkBlockColorsLUTColorBar.LabelFontFile = ''

# set color bar visibility
vtkBlockColorsLUTColorBar.Visibility = 1

# show color legend
tTKCinemaProductReader1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'spreadSheetView1'
# ----------------------------------------------------------------

# show data from tTKCinemaProductReader1
tTKCinemaProductReader1Display_1 = Show(tTKCinemaProductReader1, spreadSheetView1)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(tTKCinemaProductReader1)
# ----------------------------------------------------------------
