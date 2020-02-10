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

import os
LoadPlugin(os.getenv("PV_PLUGIN_PATH") + "/TopologyToolKit.so", ns=globals())

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2063, 1116]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.155847419825348, -0.5139077104227479, 0.155847419825348]
renderView1.StereoType = 0
renderView1.CameraPosition = [0.155847419825348, -0.5139077104227479, 7.886675222379946]
renderView1.CameraFocalPoint = [0.155847419825348, -0.5139077104227479, 0.155847419825348]
renderView1.CameraParallelScale = 2.0008854697092
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath='data/pdiags.cdb')

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)

# create a new 'TTK PersistenceDiagramClustering'
tTKPersistenceDiagramClustering1 = TTKPersistenceDiagramClustering(Input=tTKCinemaProductReader1)
tTKPersistenceDiagramClustering1.Numberofclusters = 3
tTKPersistenceDiagramClustering1.OutputaDistanceMatrix = 1

# find source
tTKPersistenceDiagramClustering1_1 = FindSource('TTKPersistenceDiagramClustering1')

# create a new 'TTK DimensionReduction'
tTKDimensionReduction1 = TTKDimensionReduction(Input=OutputPort(tTKPersistenceDiagramClustering1_1,3),
    ModulePath='default')
tTKDimensionReduction1.SelectFieldswithaRegexp = 1
tTKDimensionReduction1.Regexp = 'Diagram.*'
tTKDimensionReduction1.InputIsaDistanceMatrix = 1

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=tTKDimensionReduction1)
tableToPoints1.XColumn = 'Component_0'
tableToPoints1.YColumn = 'Component_1'
tableToPoints1.ZColumn = 'Component_0'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tableToPoints1
tableToPoints1Display = Show(tableToPoints1, renderView1)

# get color transfer function/color map for 'ClusterId'
clusterIdLUT = GetColorTransferFunction('ClusterId')
clusterIdLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
clusterIdLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tableToPoints1Display.Representation = 'Surface'
tableToPoints1Display.ColorArrayName = ['POINTS', 'ClusterId']
tableToPoints1Display.LookupTable = clusterIdLUT
tableToPoints1Display.PointSize = 10.0
tableToPoints1Display.OSPRayScaleArray = 'CaseName'
tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tableToPoints1Display.SelectOrientationVectors = 'CaseName'
tableToPoints1Display.ScaleFactor = 0.2498018900574188
tableToPoints1Display.SelectScaleArray = 'CaseName'
tableToPoints1Display.GlyphType = 'Arrow'
tableToPoints1Display.GlyphTableIndexArray = 'CaseName'
tableToPoints1Display.GaussianRadius = 0.01249009450287094
tableToPoints1Display.SetScaleArray = ['POINTS', 'CaseName']
tableToPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.OpacityArray = ['POINTS', 'CaseName']
tableToPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
tableToPoints1Display.SelectionCellLabelFontFile = ''
tableToPoints1Display.SelectionPointLabelFontFile = ''
tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tableToPoints1Display.DataAxesGrid.XTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.YTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.ZTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.XLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.YLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tableToPoints1Display.PolarAxes.PolarAxisTitleFontFile = ''
tableToPoints1Display.PolarAxes.PolarAxisLabelFontFile = ''
tableToPoints1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for clusterIdLUT in view renderView1
clusterIdLUTColorBar = GetScalarBar(clusterIdLUT, renderView1)
clusterIdLUTColorBar.Title = 'ClusterId'
clusterIdLUTColorBar.ComponentTitle = ''
clusterIdLUTColorBar.TitleFontFile = ''
clusterIdLUTColorBar.LabelFontFile = ''

# set color bar visibility
clusterIdLUTColorBar.Visibility = 1

# show color legend
tableToPoints1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'ClusterId'
clusterIdPWF = GetOpacityTransferFunction('ClusterId')
clusterIdPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
clusterIdPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(tableToPoints1)
# ----------------------------------------------------------------

SaveData("data/clustering.vtu", CleantoGrid(Input=tableToPoints1))
