#include "Adaptor.h"

#include <iostream>

#include <vtkCPDataDescription.h>
#include <vtkCPInputDataDescription.h>
#include <vtkCPProcessor.h>
#include <vtkCPPythonScriptPipeline.h>
#include <vtkCellData.h>
#include <vtkCellType.h>
#include <vtkDoubleArray.h>
#include <vtkIntArray.h>
#include <vtkNew.h>
#include <vtkPointData.h>
#include <vtkPoints.h>
#include <vtkImageData.h>

namespace
{
vtkCPProcessor* Processor = nullptr;
vtkImageData* VTKGrid = nullptr;
const char* InputName = "particles";

int _start_x;
int _nx;
int _dx;
int _start_y;
int _ny;
int _dy;
int _start_z;
int _nz;
int _dz;


//----------------------------------------------------------------------------

//----------------------------------------------------------------------------
void UpdateVTKAttributes(vtkCPInputDataDescription* idd)
{
//  if (idd->IsFieldNeeded("velocity", vtkDataObject::POINT) == true)
//  {
//    if (VTKGrid->GetPointData()->GetNumberOfArrays() == 0)
//    {
//      // velocity array
//      vtkNew<vtkDoubleArray> velocityData;
//      velocityData->SetName("velocity");
//      velocityData->SetNumberOfComponents(3);
//      velocityData->SetNumberOfTuples(static_cast<vtkIdType>(velocity.size() / 3));
//      VTKGrid->GetPointData()->AddArray(velocityData);
//    }
//    vtkDoubleArray* velocityData =
//      vtkDoubleArray::SafeDownCast(VTKGrid->GetPointData()->GetArray("velocity"));
//
//    velocityData->SetArray(const_cast<double*>(velocity.data()), static_cast<vtkIdType>(velocity.size()), 1);
//  }
//  if (idd->IsFieldNeeded("collision", vtkDataObject::POINT) == true)
//  {
//    if (VTKGrid->GetPointData()->GetArray("collision") == nullptr)
//    {
//      // velocity array
//      vtkNew<vtkIntArray> collisionData;
//      collisionData->SetName("collision");
//      collisionData->SetNumberOfComponents(1);
//      collisionData->SetNumberOfTuples(static_cast<vtkIdType>(collisions.size()));
//      VTKGrid->GetPointData()->AddArray(collisionData);
//    }
//    vtkIntArray* collisionData =
//      vtkIntArray::SafeDownCast(VTKGrid->GetPointData()->GetArray("collision"));
//
//    collisionData->SetArray(const_cast<int*>(collisions.data()), static_cast<vtkIdType>(collisions.size()), 1);
//  }
}

//----------------------------------------------------------------------------
void BuildVTKDataStructures(vtkCPInputDataDescription *idd)
{
  // feed data to grid
  UpdateVTKAttributes(idd);
}
}

namespace Adaptor
{

//----------------------------------------------------------------------------
void Initialize(char* script, const int start_x, const int start_y, const int start_z, \
                          const int nx, const int ny, const int nz, \
                          const double dx, const double dy, const double dz)
{
  if (Processor == NULL)
  {
    Processor = vtkCPProcessor::New();
    Processor->Initialize();
  }
  else
  {
    Processor->RemoveAllPipelines();
  }
  vtkNew<vtkCPPythonScriptPipeline> pipeline;
  pipeline->Initialize(script);
  Processor->AddPipeline(pipeline);

  _start_x = start_x;
  _nx = nx;
  _dx = dx;
  _start_y = start_y;
  _ny = ny;
  _dy = dy;
  _start_z = start_z;
  _nz = nz;
  _dz = dz;

  if (VTKGrid == NULL)
  {
    // The grid structure isn't changing so we only build it
    // the first time it's needed. If we needed the memory
    // we could delete it and rebuild as necessary.
    VTKGrid = vtkImageData::New();
    printf("%d %d %d %d\n", start_x, start_z, nx, nz);
    VTKGrid->SetExtent(start_x, start_x+nx-1, start_y, start_y+ny-1, start_z, start_z+nz-1);
    VTKGrid->SetSpacing(dx, dy, dz);
  }


}

//----------------------------------------------------------------------------
void Finalize()
{
  if (Processor)
  {
    Processor->Delete();
    Processor = NULL;
  }
  if (VTKGrid)
  {
    VTKGrid->Delete();
    VTKGrid = NULL;
  }
}

//----------------------------------------------------------------------------
void CoProcess(double time, unsigned int timeStep)
{
  vtkNew<vtkCPDataDescription> dataDescription;
  dataDescription->AddInput(InputName);
  dataDescription->SetTimeData(time, timeStep);

  if (Processor->RequestDataDescription(dataDescription) != 0)
  {
    vtkCPInputDataDescription* idd = dataDescription->GetInputDescriptionByName(InputName);
    BuildVTKDataStructures(idd);
    idd->SetGrid(VTKGrid);
    Processor->CoProcess(dataDescription);
  }
}
} // end of Catalyst namespace

