#ifndef FEADAPTOR_HEADER
#define FEADAPTOR_HEADER

#include <vector>

namespace Adaptor
{
void Initialize(const char* script, const int start_x, const int start_y, const int start_z, \
                          const int nx, const int ny, const int nz, \
                          const double dx, const double dy, const double dz);

void Finalize();

void CoProcess(
  double time, unsigned int timeStep);
}

#endif
